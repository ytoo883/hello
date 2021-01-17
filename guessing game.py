import random
computers_number = random.randint(1,100)
prompt = 'What is your guess?  '
while True:
    players__guess = input(prompt)
    if computers_number == int(players__guess):#
        print('Correct!')
        break
    elif computers_number > int(players__guess):
        print('To low')
    else:
        print('To high')