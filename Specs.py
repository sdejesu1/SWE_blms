# This function gets the users input and returns it
def get_user_input():
    user_input = input(">> ")
    return user_input


# This function parses the users input into a list of lists of two. The first element in the sub list is the key and the
# second element in the sublist is the item in question this way validation is easier
# This function takes in a user input and returns the parsed query
# params string user input
# returns list of lists of two
def parse_query_double_list(user_input):
    parsed_input = user_input.split(" ")
    query_list = []
    for x in range(0, len(parsed_input) - 1, 2):
        query_list.append([parsed_input[x], parsed_input[x + 1]])
    return query_list


# This function validates the query by making sure that all keywords are correct, the query starts with the word get,
# that the word "if" is only used as the third word in the query (meaning it is the first element in the second
# list), that comparison operators are used as the forth word in the query (meaning it is the first element in the
# third list), that "&&" operators are only used after the third key in the list and if they are used than they are
# used in an odd number index of the whole query, and it validates that all queries have an even number of words and any
# comparison operator after an and statement happens at odd numbered index of the entire query
# params a list of lists of length 2
# returns a boolean value telling if the query is valid or not
def double_list_validator(query_list):
    isvalid = False
    key_num = 0
    for x in query_list:
        if (x[0] == 'get') or (x[0] == 'if') or (x[0] == '==') or (x[0] == '&&') or \
                (x[0] == '>>') or (x[0] == '<<') or (x[0] == '<=') or (x[0] == '>=') or \
                (x[0] == 'all') or (x[0] == 'help') or (x[0] == 'quit'):
            if key_num == 0 and x[0] == "get":
                isvalid = True
            if key_num == 1 and x[0] != "if":
                isvalid = False
                print('ERROR')
                print('Please make sure your query has an "if" statement for the third word in the query')
                print('EX: get artist_name if start_date == 1999')
                print('Alternatively you can just limit your query to a get statement only')
                print('EX: get artist_name')
                print('This will give you all the artists names')
            if key_num == 2 and x[0] != ">>" and x[0] != "<<" and x[0] != "<=" and x[0] != ">=" and x[0] != "==":
                isvalid = False
                print('ERROR')
                print("Query has its comparison operator in the wrong place or is missing")
                print('comparison operators are considered any of the following: ')
                print('"<<", ">>", "<=", ">=", "=="')
                print('Please put your comparison operators following an if statement or an and statement')
                print('Make sure comparison operators are between two values')
                print('EX: get artist_name if start_date <= 1990 && end_date >= 2010')
            if x[0] == "&&" and (key_num + 1) % 2 != 0 and key_num > 3:
                isvalid = False
                print("ERROR")
                print("Query has its && operators missing or in the wrong place")
                print('&& operators should be used to tie two comparison operations together following an "if" '
                      'statement')
                print("EX: get artist_name if start_date <= 1990 && end_date >= 2000")
            if x[0] != ">>" and x[0] != "<<" and x[0] != "<=" and x[0] != ">=" and x[0] != "==" and (
                    key_num + 1) % 2 != 0 and key_num > 4:
                isvalid = False
                print("An unexpected error has occurred")
        else:
            isvalid = False
            print("An unexpected error has occurred")
        key_num = key_num + 1
    if (key_num + 1) % 2 != 0:
        isvalid = False
        print("ERROR")
        print("All queries should have an even number of words")
        print('Check to make sure that all comparison operators are between two items of interest and tied together '
              'with an "&&" operator')
    return isvalid


# This function will be used to execute the query made in the parser
def execute_query():
    return "results of the query execution"


# This function takes in the parsed query and returns a reformatted list of comparison operators and items of interest
# to be used to get information from firebase
# params list of lists of two elements
# returns a list of one element and several lists of three elements showing the comparisons in place
def pass_query(parse):
    mod_parse = []
    for x in parse:
        if x[0] == "get":
            mod_parse.append(x[1])
        if x[0] == "if":
            mod_parse.append(x[1])
        if x[0] == "&&":
            mod_parse.append(x[1])
        if x[0] == "==" or x[0] == "<<" or x[0] == ">>" or x[0] == "<=" or x[0] == ">=":
            mod_parse.append(x[0])
            mod_parse.append(x[1])
    conditional_statements = 0
    for x in mod_parse:
        FinalList = [mod_parse[0]]
    for x in parse:
        if x[0] == "if" or x[0] == "&&":
            FinalList.append([])
            conditional_statements = conditional_statements + 1
    x = 0
    for y in range(conditional_statements):
        x_counter = 0
        while x_counter < 3:
            adder = mod_parse[1:][x]
            FinalList[1:][y].append(adder)
            x_counter = x_counter + 1
            x = x + 1
    return FinalList


# the following code runs the code above
def main():
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
            parse = parse_query_double_list(user_input)
            if not double_list_validator(parse):
                print("Query is invalid")
            if double_list_validator(parse):
                print("Query is valid")
                passer = pass_query(parse)
                print(passer)


if __name__ == '__main__':
    main()
