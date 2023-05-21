def main():
    due = 50
    
    while due > 0:
        # States the amount the user still owes and prompts user to enter a coin value
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            due = due - coin
        else:
            # 'None' indicates to do nothing and return to loop, while break would have exited the loop entirely
            None

    if due < 0:
        change = 0 - due
        print(f"Change Owed: {change}")
    else:
        # If code runs properly this should always print 0!
        print(f"Change Owed: {due}")
 

main()