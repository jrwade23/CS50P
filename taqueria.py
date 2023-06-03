def main():
    cost = 0
    while True:
        price = get_price("Item: ")
        try:
            cost = cost + price
        except TypeError:
             break
        print(f"Total: ${cost:0,.2f}")
        
    #print(f"Total: ${cost:0,.2f}")

def get_price(prompt):
    while True:
        try:
            order = input(prompt).lower().title()
        except EOFError:
            return

        items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

        # The use of get() defaults to None to avoid KeyError,
        # therefore no need to deal with exception but conditional required
        if items.get(order) == None:
            None
        else:
            return items.get(order)

main()