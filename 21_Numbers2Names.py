# Many programs display information to the end user in one
# form but use a different form inside the program. For
# example, you may show the word Blue on the screen, but
# behind the scenes you’ll have a numerical value for that
# color or an internal value because you may need to represent
# the textual description in another language for Spanishspeaking visitors.
# Write a program that converts a number from 1 to 12 to the
# corresponding month. Prompt for a number and display the
# corresponding calendar month, with 1 being January and
# 12 being December. For any value outside thatrange, display
# an appropriate error message.
#
# Example Output
# Please enter the number of the month: 3
# The name of the month is March.
#
# Constraints
# • Use a switch or case statement for this program.
# • Use a single output statement for this program.

month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

number = input("Please enter the number of the month: ")

try:
    print("The name of the month is " + month[int(number)])
except:
    print("The month doesn't exist")