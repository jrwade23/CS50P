# - Expects the user to specify as a command-line argument the number of Bitcoins,
# that they would like to buy. If that argument cannot be converted to a float, 
# the program should exit via sys.exit with an error message.
# - Queries the API for the CoinDesk Bitcoin Price Index at 
# https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
# among whose nested keys is the current price of Bitcoin as a float.
# - Outputs the current cost of Bitcoins in USD to four decimal places, using , 
# as a thousands separator.

def main():
    import sys
    import requests
    #import json

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    
    # print(json.dumps(response.json(), indent=2))

    # print(response.json()["bpi"]["USD"]["rate_float"])

# Alternative:
    # obj = response.json()
    # rate = obj["bpi"]["USD"]["rate_float"]

    rate = response.json()["bpi"]["USD"]["rate_float"]

    try:
        cost = rate * float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    print(f"$ {cost:,.4f}" )

if __name__ == "__main__":
    main()