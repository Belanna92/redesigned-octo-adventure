# This program will assess the data gathered from the Codetown Public Transport Data Collection System to determine
# which bus routes require additional busses.
# This will be determined by the user inputting how many additional busses are available
import os

print("Welcome to the Codetown Public Transport Data Analysis System")


# The read_route_data function takes a single parameter that is the name of a text file
# and will read the data from the text file entered, then return a list of dictionaries from that data.
#
# The data must be in the format 'positive integer, positive float' e.g. 123, 5.4
# and there must not be duplicate routes.
# The data will then be organised into a list of dictionaries each containing two keys:
# 'route_number' and 'happy_ratio'
#
def read_route_data(file_name):
    l_of_dictionaries = []
    check_no_duplicate_stops = []
    with open(file_name) as routes:
        if os.path.getsize(file_name) == 0:
            print("Please ensure the data is in the format 'positive integer, positive float' e.g. 123, "
                  "5.4 before trying again.")
            exit()
        for line in routes:
            line = line.strip()
            each_item = line.split(",")
            if line == 0:
                exit()
            if len(each_item) != 2:
                print("Please ensure the data is in the format 'positive integer, positive float' e.g. 123, "
                      "5.4 before trying again.")
                exit()
            zero = int(each_item[0])
            check_no_duplicate_stops.append(zero)
            one = float(each_item[1])
            in_dictionary = {"route_number": zero, "happy_ratio": one}
            l_of_dictionaries.append(in_dictionary)
    check_no_duplicate_stops_set = set(check_no_duplicate_stops)
    if len(check_no_duplicate_stops_set) != len(check_no_duplicate_stops):
        print("Please ensure that there are no duplicate route numbers in the file before trying again.")
        exit()
    return l_of_dictionaries


# The sort_route_data function takes a single parameter that is the name of a list of dictionaries.
# The list of dictionaries is returned sorted in the order of routes with the most need for extra busses to
# the routes with the least need for extra buses.
#
# The list of dictionaries is coming directly from the read_route_data function.
# The dictionaries are first sorted into numerical order.
# Then the dictionaries with happy_ratios of 0 are removed from the list, and added to the end.
#
def sort_route_data(data):
    sorted_l_of_dictionaries = []
    zero_happy_ratio = []
    sorted_route_data = sorted(data, key=lambda d: d["happy_ratio"])
    for i in sorted_route_data:
        if i["happy_ratio"] < 1:
            zero_happy_ratio.append(i)
        else:
            sorted_l_of_dictionaries.append(i)
    for i in zero_happy_ratio:
        sorted_l_of_dictionaries.append(i)
    return sorted_l_of_dictionaries


# The is_valid_input function checks if the number of routes entered is non-negative integer and a valid input for
# the context. The user will be given the chance to re-enter the number if they make a mistake.
# If the number the user enters in greater than the number of routes, they will be prompted to to re-enter the number.
#
def is_valid_input(user_input):
    while True:
        try:
            number = int(input(user_input))
        except ValueError:
            print("Please enter a non-negative integer.")
            continue

        if number < 0:
            print("Please enter a non-negative integer.")
            continue

        if len(sort_route_data(read_route_data('routes.txt'))) < number:
            print("You must enter a number equal to or less than the number of routes.")
            continue

        else:
            break
    return number


# Try to run the read_route_data and sort_route_data functions. If there are any issues the user will be
# prompted to correct them and the program will exit.
try:
    more_busses = sort_route_data(read_route_data('routes.txt'))
except (FileNotFoundError, PermissionError, FileExistsError, IsADirectoryError):
    print("Please ensure the file exist and we have permission to view it before trying again")
    exit()
except ValueError:
    print("Please ensure each line of routes.txt contains a route number, followed by a comma, followed by a happy "
          "ratio")
    exit()


# Call the is_valid_input function to determine how many extra busses are available
n = is_valid_input("How many routes can have an extra bus? ")
# Save the user input in an additional variable to refer to later
extra_busses = n

# Take the bus routes that have already been put in order with the sort_route_data function and create a list of the
# bus routes that will be presented to the user based on how many buses are available
bus_routes = []
for i in more_busses:
    if n <= 0:
        break
    bus_routes.append(i['route_number'])
    n = n - 1

# Present the final information to the user
if extra_busses == 0:
    print("Please try again later when you have additional busses available.")
else:
    print("You should add busses to the following routes: ")
    index = 0
    for i in bus_routes:
        print(bus_routes[index])
        index += 1