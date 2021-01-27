# Given an input file, read the file and look for all occurrences
# of the word utilize. Replace each occurrence with use. Write
# the modified file to a new file.
# 
# Example Output
# Given the input file of
# One should never utilize the word "utilize" in
# writing. Use "use" instead.
# The program should generate
# One should never use the word "use" in
# writing. Use "use" instead.
# 
# Constraints
# • Prompt for the name of the output file.
# • Write the output to a new file.


file_in = open('Files/45_file.txt', 'r')
text_in = file_in.read()
print (text_in)

text_out = text_in.replace('utilize', 'use')

file_out = open('Files/45_file_out.txt', 'w')
file_out.write(text_out)
print (text_out)