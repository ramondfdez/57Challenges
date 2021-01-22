# Alphabetizing the contents of a file, or sorting its contents,
# is a great way to get comfortable manipulating a file in your
# program.
# Create a program that reads in the following list of names:
# Ling, Mai
# Johnson, Jim
# Zarnecki, Sabrina
# Jones, Chris
# Jones, Aaron
# Swift, Geoffrey
# Xiong, Fong
# Read this program and sort the list alphabetically. Then print
# the sorted list to a file that looks like the following example
# output.
# 
# Example Output
# Total of 7 names
# -----------------
# Ling, Mai
# Johnson, Jim
# Jones, Aaron
# Jones, Chris
# Swift, Geoffrey
# Xiong, Fong
# Zarnecki, Sabrina
# 
# Constraint
# • Don’t hard-code the number of names.

f_in = open("Files/41_file.txt", "r")

data = f_in.readlines()

data.sort()

size = len(data)

f_out = open("Files/41_file_out.txt", "w")

f_out.write("Total of " + str(size) + " names\n")
f_out.write('------------------\n')
f_out.writelines(data)