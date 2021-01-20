command = ''
while command != "quit":
    command = input('>').lower()
    if command == 'start':
        print('car started')
    elif command == 'stop':
        print('car stopped')  
    elif command == 'help' :
            print('commands :satart, stop,help and quit ;)')
    elif command == 'quit':
        print('were sorry ;-(')
        break
print('goodbye,made By trixie core')
           

     
        