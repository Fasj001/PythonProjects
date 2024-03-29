a = {}
import sys
def login_page():
    while True:
        print("Please create a new user")
        
        usrname = input("Please enter a username: ")
        psword = input("\nPlease enter a password: ")
        
        a[usrname] = psword
        
        login_usrname = input("\nPlease enter your username: ")
        login_psword  = input("\nPlease enter your password: ")
        
        if login_usrname not in a or a[login_usrname] != login_psword:
            print("\n.....")
            print("\nWrong username or password")
        else:
            print("\n.....")
            print("\nYou have logged inn!")
            break
        
login_page()

def quiz():
    while True:
        
        print("\nWelcome to this quiz!!")
    
        questions = [
            ["\nHow many league champs are there in league?", "a", "123", ["a.123", "b.342", "c122", "d.12"]], 
            ["\nHow many league champs are there in league?", "c", "122", ["a.123", "b.342", "c.122", "d.12"]],
            ["\nHow many league champs are there in league?", "b", "342", ["a.123", "b.342", "c.122", "d.12"]],
            ["\nHow many league champs are there in league?", "d", "12", ["a.123", "b.342", "c.122", "d.12"]]
        ]
        correct = 0
        wrong = 0
        wrong_answer = []
    
    
        for question, correct_letter, correct_word, options in questions:
            print(question)
        
            for option in options:
                print(option)
            answer = input("Answer: ")

            if answer == correct_letter or answer == correct_word:
                correct += 1
            else:
                wrong += 1
            wrong_answer.append((question, correct_letter, correct_word, answer))
            
            print(f"\nYou got {correct} correct answers and {wrong} incorrect answers.\n")
        
            for question, correct_letter, correct_word, answer in wrong_answer:
                print("%s \tThe correct anser is %s.%-1s, you answered %s." %(question, correct_letter, correct_word, answer))
        break

##This is supposed to be a python calculator but i cba idk how to make it work 
##def calculator_program():
        print("Welcome to the calculator")
        choice = menu()
        while choice !=5:
            if choice  < 1 or choice > 5:
                print("Invalid choice")
            else:
                num1 = int(input("Enter first number : "))
                num2 = int(input("Enter second number : "))
                if choice == 1:
                    result = addition(num1, num2)
                elif choice == 2:
                    result = subtraction(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == 3:
                    result = multiplication(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == 4:
                    result = division(num1, num2)
                    if result != False:
                        print(f"{num1} + {num2} = {result}")
                    else:
                        print("Divion by ZERO is not defined.")
                else:
                    logout()
                    
            choice = menu()
            
            print("Bye Bye!")
                    
            def addition(num1, num2):
                return num1 + num2
            def subtraction(num1, num2):
                return num1 - num2
            def multiplication(num1, num2):
                return num1 * num2
            def divistion(num1, num2):
                if num2 == 0:
                    return False
                else:
                    return num1/num2
            
            def menu():
                print("\n1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. QUIT")
                choice = int(input("Enter the operation you want to perform: "))
                return choice
        calculator_program()


def main_menu():
    while True:
        choice = input("""
        -A: Quiz
        -B: Logout
        -C: Link to ?

        Please enter your choice: """)
        
        if choice  == "A" or choice == "a":
            quiz()
            break
        elif choice == "B" or choice == "b":
            print("You have choicen to logout")
            break
        elif choice == "C" or choice == "c":
            calculator_program()
        else:
            print("You need to choice a option, either A or B")
            
main_menu()

def logout():
    print("\nLogging out...")
    sys.exit
logout()
