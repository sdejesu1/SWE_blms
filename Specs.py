# This function gets the users input and returns it
def get_user_input():
    user_input = input(">> ")
    return user_input


# This function splits the users input by spaces and adds it to a dictionary
# such that the first input is the key and the second is the element and it
# alternates in that pattern
# this function returns the dictionary
def parse_query(user_input):
    parsed_input = user_input.split(" ")
    print(parsed_input)
    dictionary_query = {}
    for x in range(0, len(parsed_input)-1, 2):
        dictionary_query.update({parsed_input[x]:parsed_input[x+1]})
        print(dictionary_query)
    print(query_validater(dictionary_query))
    return dictionary_query


# This function takes in the dictionary and validates all the key values and elements
# It returns a boolean value if it is valid or not
def query_validater(dictionary_query):
    isvalid = False
    for key in dictionary_query.keys():
        if (key.lower() == 'get') or (key.lower() == 'if') or (key.lower() == '==') or (key.lower() == '&&') or \
                (key.lower() == '>>') or (key.lower() == '<<') or (key.lower() == '<=') or (key.lower() == '>=') or \
                (key.lower() == 'all') or (key.lower() == 'help') or (key.lower() == 'quit'):
            isvalid = True
        else:
            isvalid = False
    return isvalid


# This function will be used to execute the query made in the parser
def execute_query():
    return "results of the query execution"


# the following code runs the code above
looper = True
while looper:
    user_input = get_user_input()
    if user_input.lower() == "help":
        print('help notes')
    elif user_input.lower() == "quit":
        print('Quitting...')
        looper = False
    else:
        parse = parse_query(user_input)
        print(parse)
