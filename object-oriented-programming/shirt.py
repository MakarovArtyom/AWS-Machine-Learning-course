"""Define class 'Shirt'"""
class Shirt: # good practice - capitalize the first letter in class
    # proceed with class constructor
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        # define class attributes
        # self will store your attributes, like color, size, style and price
        # self - a dictionary that holds all of your attributes and values of these attributes
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    # define the method
    # self already has the price inside it, as well the other attributes
    # it's always the first argument
    def price_change(self, new_price):
        # change the value of price, we do not need to return anything
        self.price = new_price
    def discount(self, discount):
        return self.price * (1-discount)
