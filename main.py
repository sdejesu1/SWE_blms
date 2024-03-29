import re
import admin
import firebase_query as fq

# This function gets the users input and returns it
def get_user_input():
    user_input = input(">> ")
    user_input = user_input.lower()
    return user_input

# This function parses the users input into a list of lists of two. The first element in the sub list is the key and the
# second element in the sublist is the item in question this way validation is easier
# This function takes in a user input and returns the parsed query
# params string user input
# returns list of lists of two
def parse_query_double_list(user_input):
    pattern = re.compile(r'("[^"]+"|\S+)')
    parsed_input = pattern.findall(user_input)
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
    columnNames = ["artist name", "location", "songs", "genre", "start of career", "end of career"]
    columnNamesAndALL = ["artist name", "location", "songs", "genre", "start of career", "end of career", "all"]
    isvalid = False
    key_num = 0
    ifValidation = True
    comparisonValidation = True
    andValidation = True
    columnNameValid = True
    for x in query_list:
        # checks to make sure that all the first elements in the sublist are a keyword
        if (x[0] == 'get') or (x[0] == 'if') or (x[0] == '==') or (x[0] == '&&') or \
                (x[0] == '>') or (x[0] == '<') or (x[0] == '<=') or (x[0] == '>=') or \
                (x[0] == 'all') or (x[0] == 'help') or (x[0] == 'quit'):
            # Checks to make sure that the keyword "get" is in the right location
            if key_num == 0 and x[0] == "get":
                isvalid = True
                # if the element following the keyword is not one of the column names set false values
                if x[1] not in columnNamesAndALL:
                    isvalid = False
                    columnNameValid = False
            # Checks to see that any key in the second location of the list of lists is the value "if" if not it sets
            # values to false
            if key_num == 1 and x[0] != "if":
                isvalid = False
                ifValidation = False
            # Checks to make sure that any key in the third location of the list of lists is one of the comparison
            # operators
            if key_num == 2 and x[0] != ">" and x[0] != "<" and x[0] != "<=" and x[0] != ">=" and x[0] != "==":
                isvalid = False
                comparisonValidation = False
            # Checks to make sure that any "&&" key is in an even number location greater than 3 and sets validators
            if x[0] == "&&" and (key_num + 1) % 2 != 0 and key_num > 3:
                isvalid = False
                andValidation = False
            # Checks to make sure that any comparison operator is in an even number location greater than 4 and sets the
            # validators
            if x[0] != ">" and x[0] != "<" and x[0] != "<=" and x[0] != ">=" and x[0] != "==" and (
                    key_num + 1) % 2 != 0 and key_num > 4:
                isvalid = False
                print("An unexpected error has occurred")
            # Checks to make sure that any non key value is one that is in our column names list
            if key_num <= 1:
                if x[1] not in columnNamesAndALL:
                    isvalid = False
                    columnNameValid = False
            if key_num > 1 and (key_num+1) % 2 == 0:
                if x[1] not in columnNames:
                    isvalid = False
                    columnNameValid = False

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
    if columnNameValid != True:
        print('ERROR')
        print('Please make sure your query has valid column names')
        print('Column names are as follows:')
        print('"artist name", "location", "songs", "genre", "start of career", "end of career"')
        print('Make sure each column name is surrounded by double quotation marks ""')
    if ifValidation != True:
        print('ERROR')
        print('Please make sure your query has an "if" statement for the third word in the query')
        print('EX: get artist_name if start_date == 1999')
        print('Alternatively you can just limit your query to a get statement only')
        print('EX: get artist_name')
        print('This will give you all the artists names')
    if andValidation != True:
        print("ERROR")
        print("Query has its && operators missing or in the wrong place")
        print('&& operators should be used to tie two comparison operations together following an "if" '
              'statement')
        print("EX: get artist_name if start_date <= 1990 && end_date >= 2000")
    if comparisonValidation != True:
        print('ERROR')
        print("Query has its comparison operator in the wrong place or is missing")
        print('comparison operators are considered any of the following: ')
        print('"<", ">", "<=", ">=", "=="')
        print('Please put your comparison operators following an if statement or an and statement')
        print('Make sure comparison operators are between two values')
        print('EX: get artist_name if start_date <= 1990 && end_date >= 2010')
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
        if x[0] == "==" or x[0] == "<" or x[0] == ">" or x[0] == "<=" or x[0] == ">=":
            mod_parse.append(x[0])
            mod_parse.append(x[1])
    conditional_statements = 0
    for x in mod_parse:
        finalList = [mod_parse[0]]
    for x in parse:
        if x[0] == "if" or x[0] == "&&":
            finalList.append([])
            conditional_statements = conditional_statements + 1
    x = 0
    for y in range(conditional_statements):
        x_counter = 0
        while x_counter < 3:
            adder = mod_parse[1:][x]
            finalList[1:][y].append(adder)
            x_counter = x_counter + 1
            x = x + 1
    return finalList


# A function that takes in a list and searches through it to remove all quotes so that it is better formatted
# params list
# returns a list
def quote_remover(mylist):
    finalQuery = []
    for x in mylist:
        if isinstance(x, list):
            finalQuery.append(quote_remover(x))
        elif isinstance(x, int):
            print("hey listen")
            finalQuery.append(x)
        elif isinstance(x, str) and x.isdigit():
            finalQuery.append(int(x))
        else:
            finalQuery.append(x.replace("'", "").replace('"', ''))
    return finalQuery


# the following code runs the code above
def main():
    #introduction to program
    print("\nHello All! Welcome to our collection of information about some of spotify's top artists:")
    #categories and keys
    print('\nThe Categories are: "Artist Name", "Location", "Songs", "Genre", "Start of Career", and "End of Career"')
    print('The Keys are: get, if, ==, &&, <, >, <=, >=, all')
    print('------------------------------')
    print('Please enter your query now, type "help" to see your options, or "quit" to close the program:')

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
            print('Entering "<", ">", "<=", or ">=" comparing operators allows you to get items that are less than, '
                  'greater than, less than or equal to, or greater than or equal to')
            print('Entering "all" allows the user to get all of the data')
            print('Entering "help" gives the current menu')
            print('Entering "quit" ends the program')
            print('------------------------------')
            print('here are some example queries')
            print('get songs if "artist name" == "halsey"')
            print('get "artist name" if "end of career" > 2000 && "start of career" < 1990')
        elif user_input.lower() == "quit":
            print('Quitting...')
            looper = False
        else:
            parse = parse_query_double_list(user_input)
            parse = quote_remover(parse)
            if double_list_validator(parse):
                print("Query is valid")
                passer = pass_query(parse)
                print(passer)
                fq.querying_user_data(passer)
            else:
                print("Query is invalid")

if __name__ == '__main__':
    main()
