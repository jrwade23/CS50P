def main():
    fraction = input("Fraction: ")
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    print(f"x = {x} and y = {y}")
    percent = find_percent(x, y)

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"percent = {percent}%")

def find_percent(n, d):
    return round(n/d*100)

main()