from decimal import Decimal
from django.contrib.sessions.models import Session
from product.models import Product

class Cart:
    # creating a session for product
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    # adding or updating product session with quantity
    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}

        self.session.modified = True


    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['sub_total'] = Decimal(item['price']) * Decimal(item['quantity'])
            yield item


    def total_price(self):
        # li = []
        # for item in self.cart.values():
        #     li.append(Decimal(item['price']) * Decimal(item['quantity']))
        # return sum(li)
        return sum(Decimal(item['price']) * Decimal(item['quantity'] ) for item in self.cart.values())

    def final_price(self):
        price = self.total_price()
        shipping = 20
        taxes = 10
        final = price + shipping + taxes
        return final

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True


    def clear(self):
        del self.session["cart"]
        self.session.modified = True
