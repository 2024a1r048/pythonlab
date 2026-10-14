 #Create a Product class with the product name,price and quantity.Add an instance method to calculate the toatal cost.;Take thesevalues from the user and display the product name and total cost

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

p = Product(name, price, quantity)

print("Product Name:", p.name)
print("Total Cost:", p.total_cost())