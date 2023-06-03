def main():

    # Create a dictionary 'groceries' from user input
    # 'Key' is name of item, 'value' is number of the item listed
    groceries = create_dictionary("Item: ")

    # Alphabetize grocery list
    alpha_groceries = alpha_dictionary(groceries)    

    # Print list of items w/quantity
    for items in alpha_groceries:
        print(f"{alpha_groceries[items]} {items}")


def create_dictionary(groc):
    groc = {}
    while True:
        try:
            item = input("Item: ").upper()
        except EOFError:
            break

        if item not in groc:
            groc.update({item : 1})
        else:
            groc[item] = groc[item] + 1

    return groc

def alpha_dictionary(groc):
    groceries_keys = list(groc)
    groceries_keys.sort()
    return {items : groc[items] for items in groceries_keys}

main()