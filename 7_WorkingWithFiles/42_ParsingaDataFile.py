# Sometimes data comes in as a structured format that you
# have to break down and turn into records so you can process
# them. CSV, or comma-separated values, is a common standard for doing this.
# Construct a program that reads in the following data file:
# Ling,Mai,55900
# Johnson,Jim,56500
# Jones,Aaron,46000
# Jones,Chris,34500
# Swift,Geoffrey,14200
# Xiong,Fong,65000
# Zarnecki,Sabrina,51500
# Process the records and display the results formatted as a
# table, evenly spaced, as shown in the example output.
# 
# Example Output
# Last First Salary
# -------------------------
# Ling Mai 55900
# Johnson Jim 56500
# Jones Aaron 46000
# Jones Chris 34500
# Swift Geoffrey 14200
# Xiong Fong 65000
# Zarnecki Sabrina 51500
# 
# Constraints
# • Write your own code to parse the data. Don’t use a CSV
# parser.
# • Use spaces to align the columns.
# • Make each column one space longer than the longest
# value in the column.



f_in = open("Files/42_file.csv", "r")

data = f_in.readlines()

print("Last       First       Salary")
print("-----------------------------\n")

for i in data:
    x = i.split(",")
    print('{last:12}{first:12}{salary:12}'.format(last=x[0], first = x[1], salary = x[2]) )