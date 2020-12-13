import sys
from random import randint

def Quit():
    sys.exit()

def main():
    global bonus
    print('Login')
    username = input('Username : ')
    password = int(input('Password : '))
    try:
        file_name = 'users/' + username + str(password) + '.txt'
        with open(file_name) as file:
            bonus = int(file.read())
        print('\n\tWelcome ' + username.title())
    except:
        print('Account not found!')
        Home()
            
    print('\t\t Emmy\'s Guess Game ')
    print("\n Enter any number 0 - 9, You've 3 trials \n to get a number correctly.")
    print(" A win at first trial for a round is a $50 win \n at second win is a $30 and third $15. ")
    print(" But a lose at a loss of $20. Note: if your balance falls below $20, \n your sccount crashes, then you create a new one.")
    flag = True

    while flag:
        correct_number = randint(0, 10)
        print('\n Balance = $' + str(bonus))
        print('\t\t Guess the number!')
        try:
            first_trial = int(input('Your First Trial : '))
            if first_trial == correct_number:
                bonus += 50
                print('You got it right!')
                
            elif first_trial != correct_number:
                print('Wrong!, Two More Trial')
                second_trial = int(input('\nYour Second Trial: '))
                if second_trial == correct_number:
                    bonus +=30
                    print('You got the number on your second trial')
                elif second_trial != correct_number:
                    print('Wrong!, Last Trial')
                    third_trial = int(input('\nYour Third Trial: '))
                    if second_trial == correct_number:
                        bonus+=15
                        print('You got the number on your Third trial')
                    else:
                        bonus -=20
                        print('You didn\'t get it correct')
                        print('The correct number is ' + str(correct_number))

            choice = input('Do you still want to  continue, y/n? : ')
            if choice.title == 'Y':
                pass
            elif choice.title() == 'N':
                file_name = 'users/' + username + str(password) + '.txt'
                with open(file_name, 'w') as file:
                    file.truncate()
                    file.write(str(bonus))
                flag = False
            else:
                pass
                           
        except:
            print('Wrong Input')
        if bonus < 20:
            flag = False
            Home()
            
def Home():
    print("\n'R' to Register New Account")
    print("'Q' to Quit on any Request")
    print("'L' to Login")
    operation = input('Enter your operation : ')
    if operation.title() == 'R':
        Register()
    elif operation.title() == 'L':
        main()
    elif operation.title() == 'Q':
        Quit()
    else:
        Home()


def  Register():
    print('Dear User, Fill in the following')
    username = input('Enter Username : ')
    password = int(input('Enter 4 digit numbers as Password : '))
    file_name = 'users/' + username + str(password) + '.txt'
    with open(file_name, 'a') as file:
        file.write(str(100))
    main()
        
Home()

