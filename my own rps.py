import random
human_turn=input(print('whawill you pick: ','Rock? Scissors? Paper?'))
print('Human chose: ',human_turn,'.')

choices=('Rock','Scissors','Paper')

computer_turn=random.randint(0,2)
computer_turn=choices[computer_turn]
print('Computer chose: ',computer_turn,'.')

if human_turn == 'Rock' and computer_turn =='Scissors':
    print('Human wins!')
elif computer_turn == 'Rock' and human_turn =='Scissors':
    print('Computer wins!')

    
elif human_turn == 'Paper' and computer_turn =='Rock':
    print('Human wins!')
elif computer_turn == 'Paper' and human_turn =='Rock':
    print('Computer wins!')

elif human_turn == 'Scissors' and computer_turn =='Paper':
    print('Human wins!')
elif computer_turn == 'Scissors' and human_turn =='Paper':
    print('Computer wins!')

else:
    print('Draw')

def rps_function():
    import random
    human_turn=input(print('whawill you pick: ','Rock? Scissors? Paper?'))
    print('Human chose: ',human_turn,'.')

    choices=('Rock','Scissors','Paper')

    computer_turn=random.randint(0,2)
    computer_turn=choices[computer_turn]
    print('Computer chose: ',computer_turn,'.')

    if human_turn == 'Rock' and computer_turn =='Scissors':
        print('Human wins!')
    elif computer_turn == 'Rock' and human_turn =='Scissors':
        print('Computer wins!')


    elif human_turn == 'Paper' and computer_turn =='Rock':
        print('Human wins!')
    elif computer_turn == 'Paper' and human_turn =='Rock':
        print('Computer wins!')

    elif human_turn == 'Scissors' and computer_turn =='Paper':
        print('Human wins!')
    elif computer_turn == 'Scissors' and human_turn =='Paper':
        print('Computer wins!')

    else:
        print('Draw')
    Continue=input("Do you want to continue - yes or no")
    if continue="yes":
        rps_function()
rps_function()

