def main():

    import inflect
    p = inflect.engine()

    names = create_list("Name: ")
    names = p.join(names, final_sep="")  # uses inflect package to seperate items in list by commas with last element seperated by 'and' (no comma)
    print(f"Adieu, adieu, to {names}")
    

def create_list(n):
    n = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break

        n.append(name)

    return n
    
if __name__ == "__main__":
    main()