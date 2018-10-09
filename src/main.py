import sys


options = {'1': 'START',
           '2': 'ADD',
           '3': 'REMOVE',
           '4': 'EDIT',
           '5': 'EXIT',}

routines = '' #file path for routines (defined on installation)

def get_option():
    option = input()
    return option


'''
Exibits routines to user and waits for choice
'''
def choose_routine():
    pass


def print_menu():
    print("""
        ================= TASK SPRINTER  =================
        1 - Start routine
        2 - Add routine
        3 - Remove routine
        4 - Edit routine
        5 - Exit
        ==================================================
    """)


if __name__ == "__main__":
    while True:
        print_menu()
        option = get_option() # lacks input validation
        if options[option] == 'START':
            routine = choose_routine()
            print('Starting')
            routine.start()

        elif options[option] == 'ADD':
            routine.add()
            print('Adding')

        elif options[option] == 'REMOVE':
            routine = choose_routine()
            print('Removing')
            routine.remove()

        elif options[option] == 'EDIT':
            routine = choose_routine()
            print('Editing')
            routine.edit()

        else: # EXIT
            print('Exiting')
            sys.exit()

