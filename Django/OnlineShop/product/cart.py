from decimal import Decimal
from django.contrib.sessions.models import Session
from product.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity):
        print(quantity, '----------------')
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}

        self.session.modified = True


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def quantity(self):
        li = []
        for item in self.cart.values():
            li.append(int(item["quantity"]))
        return sum(li)


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

