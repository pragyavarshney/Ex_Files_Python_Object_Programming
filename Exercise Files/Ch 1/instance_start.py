# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title,author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret="This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price -(self.price*self._discount)
        else:
            return self.price

    # TODO: try setting the discount
    def setdiscount(self, amount):
        self._discount = amount  # this attribute is internal to class not to be used outside


# TODO: create some book instances
b1 = Book("War and Peace","Leo Tolstoy",1220,30)
b2 = Book("The Catcher in the Rye","JD Salinger",300,45 )

# TODO: print the price of book1
print(b1.getprice())
print(b2.getprice())
b2.setdiscount(0.15)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
#print(b2.__secret) #AttributeError: 'Book' object has no attribute '__secret'
print(b2._Book__secret)
