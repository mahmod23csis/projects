from modRoom import Room
from datetime import *

r1 = Room("BR160",50,100)
print("Room 1:", r1)
print("Testing getters for Room 1")
idNum = r1.getRmID(); print("ID Number: ", idNum)
rmLength = r1.getRmLength(); print("Length ", rmLength)
rmWidth = r1.getRmWidth(); print("Width ", rmWidth)
rmArea = r1.calcRmArea(); print("Area: ", rmArea)

r2 = Room("LI 300",20,40)
print("\n\nRoom 2: ", r2)
print("\n\nTesting setters for Room 2")
r2.setRmID("Hagen123")
r2.setRmLength(300); r2.setRmWidth(150)
print("Changing r2's info to Hagen 123, Length 300, Width 150")
print(r2)
