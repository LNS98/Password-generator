""" password generator"""
import random

def passwd_generator():
    """
    Main funciton which generates a password. User can choose betweeen 3 options:
    weak, medium, strong.
    """
    #ask for user what type of stregnth they want and store the answer in answer
    print( "What type of password would you like to have: weak, medium, secure?")
    answer = input("Type w/m/h:")

    while True:
        #make sure user has typed either w, m or h
        if answer == 'w' or  answer == 'm' or  answer == 'h':
            #if so break out of loop
            break
        else:
            #else make him retype until he hass done it correctly
            answer = input("Type w/m/h:")



    # define an empty lsit which will contain password
    password = []

    #for weak password generate a password between 5 - 10 alphabetical lowercase characteres
    if answer == 'w':

        #choose a random number between 5 and 10 to be the length of password
        length = random.randint(5, 10)

        # begining and endiong chars will be 'a' and 'z'
        beg_ind = 'a'
        end_ind = 'z'

        # run function to create list containing all chars to make passwd from
        char_list = char_list_gen(beg_ind, end_ind)

        #run function to generate passwd list
        pass_list = pass_list_gen(length, char_list)

    #for medium password generate a password between 10 - 15 alphabetical characteres
    elif answer == 'm':

        #choose a random number between 10 and 15 to be the length of password
        length = random.randint(10, 15)

        # begining and ending chars will be 'a' and 'z'
        beg_ind1 = 'a'
        end_ind1 = 'z'

        # and uppercase letters
        beg_ind2 = 'A'
        end_ind2 = 'Z'

        # run function to create list containing all chars to make passwd from
        char_list1 = char_list_gen(beg_ind1, end_ind1)
        char_list2 = char_list_gen(beg_ind2, end_ind2)

        #concatante indivudual lsits
        char_list = char_list1 + char_list2

        #run function to generate passwd list
        pass_list = pass_list_gen(length, char_list)

    #for strong password generate a password between 15- 20 alphabetical characteres
    #and numbers
    elif answer == 'h':

        #choose a random number between 15 and 20 to be the length of password
        length = random.randint(15,20)

        # begining and ending chars will be 'a' and 'z'
        beg_ind1 = 'a'
        end_ind1 = 'z'

        # and uppercase letters
        beg_ind2 = 'A'
        end_ind2 = 'Z'

        #and numbers
        beg_ind3 = '0'
        end_ind3 = '9'

        # run function to create list containing all chars to make passwd from
        char_list1 = char_list_gen(beg_ind1, end_ind1)
        char_list2 = char_list_gen(beg_ind2, end_ind2)
        char_list3 = char_list_gen(beg_ind3, end_ind3)

        #concatante aindividual lists
        char_list = char_list1 + char_list2 + char_list3

        #run function to generate passwd list
        pass_list = pass_list_gen(length, char_list)

    #join psssword list together so thats it is a word and return it
    password = "".join(pass_list)
    print("Password is '{}'".format(password))

    return password

def pass_list_gen(length, char_list):
    """
    Creates a list of length 'length' containg a random set of characters from
    the char_list. Basically creates a list containg the password characters.
    """
    #empty variable containg list which will be populated
    pass_list = []

    #repeat as many times as length of password
    for i in range(length):

        #create random index in range of chars and then append that char to the lis
        ind = random.randint(0,len(char_list) - 1)
        pass_list.append(char_list[ind])

    return pass_list

def char_list_gen(beg_index, last_index):
    """
    Creates a list containg all characters set betweeen index 'beg_index' and
    'last_index' as per UNICODE valuse of these indicies.
    """
    #create list containing all avaible characters
    char_list = [chr(i) for i in range(ord(beg_index), ord(last_index) + 1)]

    return char_list

#passwd_generator()
