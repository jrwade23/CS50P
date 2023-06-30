# I essentially had to destroy the original code fuel.py so that I could successfuly run a Unit Test on it without the 
# interference of user inputs. I don't think it was worth the cost. I would have rather debugged manualy to keep the more user
# friendly user interaction intact. Only use modified_fuel.py to run  test_fuel.py successfully.

def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fract):
   
    #fract = input(prompt)
    n, d = fract.split("/")
    
    
    n = int(n)
    
    
    d = int(d)
    
    #if d >= n:
            
    return round(n/d*100)
            

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"percent = {p}%"


if __name__ == "__main__":
    main()