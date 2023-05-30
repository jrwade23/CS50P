def main():
    percent = find_percent("Fraction: ")
    
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"percent = {percent}%")

def find_percent(prompt):
    while True:
        fraction = input(prompt)
        n, d = fraction.split("/")
        
        try:
            n = int(n)
        except ValueError:
            pass
        try:
            d = int(d)
        except ValueError:
            pass
        try:
            if d >= n:
                try:
                    return round(n/d*100)
                except (ZeroDivisionError, TypeError):
                    pass
            else:
                None
        except TypeError:
            pass


main()