def get_user_input():
    user_input = input(">> ")
    return user_input

def parse_query(user_input):
    return "dictionary"

def execute_query():
    return "results of the query execution"

looper = True
while looper == True:
    user_input = get_user_input()
    if user_input.lower() == "help":
        print('help notes')
    if user_input.lower() == "quit":
        print('Quitting...')
        looper = False