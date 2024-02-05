def get_user_input():
    user_input = input(">> ")
    return user_input

def parse_query(user_input):
    parsed_input = user_input.split(" ")
    print(parsed_input)
    dictionary_query = {}
    for x in range(0, len(parsed_input)-1, 2):
        dictionary_query.update({parsed_input[x]:parsed_input[x+1]})
        print(dictionary_query)
    return "dictionary"

def execute_query():
    return "results of the query execution"

looper = True
while looper == True:
    user_input = get_user_input()
    if user_input.lower() == "help":
        print('help notes')
    elif user_input.lower() == "quit":
        print('Quitting...')
        looper = False
    else:
        parse = parse_query(user_input)
        print(parse)