print ('Welcome to atm')
restart=('Y')
chances=3
balance=500.50
while chances >=0:
    pin = int(input('Please enter your 4 digit pin: '))
    if pin == (1234):
        print('You entered your pin correctly')
        print('Press 1 for check balance')
        print('Press 2 for withdrawl')
        print('Press 3 for deposite')
        print('Press 4 for transfer\n ')
        while restart not in ('n','No','no','N'):
            option = int(input('Select option to start'))
            if option == 1:
                print('Your balance is ',balance)
                restart = input('Would you like to go back: ')
               # if restart in ('n','No','no','N'):
                print('Thank you')
                break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input('Enter amount to withdrawl 100,500,2000 for other enter 1: '))
                if withdrawl in [100,500,2000]:
                    balance = balance - withdrawl
                    print ('\n Your balance is ',balance)
                    restart = input('Would you like to go back: ')
                    #if restart in ('n','No','no','N'):
                    print('Thank you')
                    break
                elif withdrawl != [100,500,2000]:
                    print('Invalid amount \n')
                    restart = ('Y')
                elif withdrawl == 1:
                     withdrawl = float(input('Enter a desired amount: '))
            elif option == 3:
                deposite = float(input('Enter amount you want to deposite'))
                balance = balance + deposite
                print('\n Your current balance is ',balance)
                restart = input('Would you like to go back: ')
               # if restart in ('n','No','no','N'):
                print('Thank you')
                break
            elif option == 4:
                print('Enter amount number')
                print('Enter amount you want to transfer')
                print('Transaction sucessfull ')
                break 
            else :
                print('Sorry enter a correct number \n')
                restart = ('Y')
    elif pin != (1234):
          print('Incorrect Pin')
          chances = chances-1
          if chances == 0:
              print('You reached your limit')
              break
              
          
           
             
                     
        