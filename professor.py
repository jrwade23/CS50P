# “calculator” that would generate ten different math problems for David to solve. 
# For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. 
# If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. 
# If David were to answer incorrectly, the toy would display EEE. 
# And after three incorrect answers for the same problem, the toy would simply display the 
# correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5)

def main():
    
    score = 0
    num_questions = 10
    chances = 3
    level = get_level("Level: ")

    # generate 10 questions using random ints with digits equal to level [1-3]
    for _ in range(num_questions):
        x = generate_integer(level)
        y = generate_integer(level)
        
        # three opportunities to answer correctly
        for i in range(chances):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                answer = None

            if answer == x + y:
                score = score + 1
                break
            else:
                print("EEE")
                # after 3 incorrect attempts, print the solution
                if i == 2:
                    print(f"{x} + {y} = {x+y}")

    # Show how many problems were answered correctly out of num_questions
    print(f"Score: {score}")

def get_level(l):   
    l = 0
    # only levels 1-3 are accepted
    while l < 1 or l > 3:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
    return l


def generate_integer(digits):
    # the number of digits in each integer is determined by level chosen
    # i.e. level 2 generates positive integers between 10 and 99
    import random
    n = random.randint(10**(digits-1), (10**digits)-1)
    return n


if __name__ == "__main__":
    main()