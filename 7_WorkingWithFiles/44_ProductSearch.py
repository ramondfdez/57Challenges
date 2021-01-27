# Create a program that takes a product name as input and
# retrieves the current price and quantity forthat product. The
# product data is in a data file in the JSON format and looks
# like this:
# {
# "products" : [
# {"name": "Widget", "price": 25.00, "quantity": 5 },
# {"name": "Thing", "price": 15.00, "quantity": 5 },
# {"name": "Doodad", "price": 5.00, "quantity": 10 }
# ]
# }
# Print out the product name, price, and quantity if the product
# is found. If no product matches the search, state that no
# product was found and start over.
# 
# Example Output
# What is the product name? iPad
# Sorry, that product was not found in our inventory.
# What is the product name? Widget
# Name: Widget
# Price: $25.00
# Quantity on hand: 5
# 
# Constraints
# • The file is in the JSON format. Use a JSON parserto pull
# the values out of the file.
# • If no record is found, prompt again.

import json

path = "Files/44_json.json"

def buscarJson(producto, path):
    encontrado = False
    file = open(path, "r")
    text = json.load(file)
    for p in text["products"]:
        if p["name"].upper() == producto.upper():
            print("Name: " + p["name"])
            print("Price: " + str(p["price"]))
            print("Quantity on hand: " + str(p["quantity"]))
            encontrado = True
    return encontrado

while True:

    producto = input("What is the product name? ")
    if (buscarJson(producto, path)):
        break
    else:
        print("Sorry, that product was not found in our inventory.")