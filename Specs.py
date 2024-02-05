# This function gets the users input and returns it
def get_user_input():
    user_input = input(">> ")
    return user_input


# This function splits the users input by spaces and adds it to a dictionary
# such that the first input is the key and the second is the element, and it
# alternates in that pattern
# this function returns the dictionary
def parse_query(user_input):
    parsed_input = user_input.split(" ")
    print(parsed_input)
    dictionary_query = {}
    for x in range(0, len(parsed_input)-1, 2):
        dictionary_query.update({parsed_input[x]: parsed_input[x+1]})
        print(dictionary_query)
    print(query_validater(dictionary_query))
    return dictionary_query


# This function takes in the dictionary and validates all the key values and elements It returns a boolean value if
# it is valid or not
# NOTE every odd number key after 4 must be a comparison key for when validating comparison operators
# WARNING!!!  the dictionary does not allow for multiple of the same keys so a statement like
# "get name if start_date == 1999 && end_date == 2010" the the last == will not be added
def query_validater(dictionary_query):
    isvalid = False
    key_num = 0
    print(len(dictionary_query))
    for key in dictionary_query.keys():
        if len(dictionary_query) == 2:
            isvalid = False
        elif (key.lower() == 'get') or (key.lower() == 'if') or (key.lower() == '==') or (key.lower() == '&&') or \
                (key.lower() == '>>') or (key.lower() == '<<') or (key.lower() == '<=') or (key.lower() == '>=') or \
                (key.lower() == 'all') or (key.lower() == 'help') or (key.lower() == 'quit'):
            if key_num == 0 and key == "get":
                isvalid = True
            if key_num == 1 and key != "if":
                isvalid = False
            if key_num == 2 and key != ">>" and key != "<<" and key != "<=" and key != ">=" and key != "==":
                isvalid = False
            if key == "&&" and (key_num+1) % 2 != 0 and key_num > 3:
                isvalid = False
        else:
            isvalid = False
        key_num = key_num + 1

    return isvalid


# This function will be used to execute the query made in the parser
def execute_query():
    return "results of the query execution"


# the following code runs the code above
looper = True
while looper:
    user_input = get_user_input()
    if user_input.lower() == "help":
        print('The following are they key words you can use to query with')
        print('Entering "get" followed by the name of the column you wish to search through')
        print('Entering "if" after a get statements will return all data that meets the condition you have defined')
        print('Entering "==" checks to see if something is equal to another, this should only be used after an if '
              'statement')
        print('Entering "&&" allows you to add another if condition to an existing one')
        print('Entering "<<", ">>", "<=", or ">=" comparing operators allows you to get items that are less than, '
              'greater than, less than or equal to, or greater than or equal to')
        print('Entering "all" allows the user to get all fo the data')
        print('Entering "help" gives the current menu')
        print('Entering "quit" ends the program')
        print('here are some example queries')
        print('get artist if name == "aerosmith"')
        print('get artist if end_date >> 2000 && start_date << 1990')
    elif user_input.lower() == "quit":
        print('Quitting...')
        looper = False
    else:
        parse = parse_query(user_input)
        print(parse)
