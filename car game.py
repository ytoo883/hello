command = ''
while command != "quit":
    command = input('>').lower()
    if command == 'start':
        print('car started')
    elif command == 'stop':
        print('car stopped')  
    elif command == 'help' :
            print('commands :satart, stop,help ')
    elif command == 'quit':
        break
print('By trixie core')
           

     
        