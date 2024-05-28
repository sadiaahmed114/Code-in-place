import random

def generate_problem():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2

def main():
    correct_in_row = 0
    
    print("Khansole Academy")
    
    while correct_in_row < 3:
        num1, num2 = generate_problem()
        correct_answer = num1 + num2
        
        user_answer = int(input(f"What is {num1} + {num2}? Your answer: "))
        
        if user_answer == correct_answer:
            correct_in_row += 1
            print("Correct!")
            print(f"You've gotten {correct_in_row} correct in a row.\n")
        else:
            correct_in_row = 0
            print("Incorrect.")
            print(f"The expected answer is {correct_answer}\n")
    
    print("Congratulations! You mastered addition.")

if __name__ == "__main__":
    main()
