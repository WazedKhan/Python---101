class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return "Dog class"

    def say_hi(self):
        print(f'{self.name} said Hi!')

    def roll(self):
        print(f'{self.name} rolled')

    def details(self):
        print(f'Name: {self.name}, Age: {self.age}, Color: {self.color}')



a = Dog('Snowy', 3, 'White')

b = Dog('Pakku', 4, 'Black')

c = Dog('Danny', 5, 'Red')

a.say_hi()
b.say_hi()
c.say_hi()
c.roll()
a.roll()
a.details()

print(a)

nums = [1,2,3,4,5]

# avg

def do_sum(nums):
    return sum(nums)

def avg(nums):
    sum_ = do_sum(nums)
    av = sum_ // len(nums)
    print(av)

avg(nums)