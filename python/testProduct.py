__author__="Mahmod Ahmad"
__date__="10/28/2020"

"""In the test file we test our getters, setters, string converter, date,
and user input for the products."""

from modVerifyDate import *
from modProduct import *
from datetime import *

def main():
    p1 = Product("222", "Cement", 430, 12.99, datetime(2018,10,20))
    print("Product 1: ",p1, "\n")
    print("Testing getters for Product 1","\n")
    id = p1.getProdID(); print("ID: ", id)
    name = p1.getProdName(); print("Name: ", name)
    quantity = p1.getProdQuantity(); print("Quantity: ", quantity)
    price = p1.getProdPrice(); print("Price: $%s" %(price))
    production = p1.getProdDate(); print("Production Date: ", production)
    age = p1.ProdAge(); print("Product Age: %s years" %(age))

    p2 = Product("333", "Iron", 320, 7.99, datetime(2014,10,20))
    print("\n\Product 2: ", p2,)
    print("\n\nTesting setters for Product 2""\n")
    p2.setProdID("232")
    p2.setProdName("Steel"); p2.setProdQuantity(250); p2.setProdPrice(9.99);
    p2.setProdDate(datetime(2015,4,18))
    print("Changing p2's info to ID 232, Steel, Quantity 250, Price 9.99,\
 Date 04-18-2015")
    print(p2)
    
    id = input("Enter product ID: ")
    name = input("Enter product name: ")
    quantity = input("Enter product quantity: ")
    price = float(input("Enter product price: "))
    
    yr = input("Enter year of production: ")
    while isValidYear(yr) == False:
        print("Error! Try again.")
        yr = input("Enter year of production: ")
    yr = int(yr)

    mn = input("Enter month of production: ")
    while isValidMonth(mn) == False:
        print("Error! Try again.")
        mn = input("Enter month of production: ")
    mn = int(mn)

    dy = input("Enter day of production: ")
    while isValidDate(yr, mn, dy) == False:
        print("Error! Try again.")
        dy = input("Enter year of production: ")
    dy = int(dy)
    prodDate = date(yr, mn, dy)

    p3 = Product(id, name, quantity, price, prodDate)
    print(p3)

main()
