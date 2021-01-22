# Sorting records is helpful, but sometimes you need to filter
# down the results to find or display only what you’re looking
# for.
# Given the following data set
# First Name Last Name Position Separation date
# John Johnson Manager 2016-12-31
# Tou Xiong Software Engineer 2016-10-05
# Michaela Michaelson District Manager 2015-12-19
# Jake Jacobson Programmer
# Jacquelyn Jackson DBA
# Sally Weber Web Developer 2015-12-18
# create a program that lets a userlocate allrecords that match
# the search string by comparing the search string to the first
# or last name field.
# 
# Example Output
# Enter a search string: Jac
# Results:
# Name | Position | Separation Date
# --------------------|-------------------|----------------
# Jacquelyn Jackson | DBA |
# Jake Jacobson | Programmer |
# 
# Constraint
# • Implement the data using an array of maps or an associative array


data = {'Johnson': ['John', 'Manager', '2016-12-31'],
'Xiong': ['Tou', 'Software Engineer', '2016-10-05'],
'Michaelson': ['Michaela', 'District Manager', '2015-12-19'],
'Jacobson': ['Jake', 'Programmer', ''],
'Jackson': ['Jacquelyn', 'DBA', ''],
'Weber': ['Sally', 'Web Developer', '2015-12-18']
}

last_name = input("Enter a search string: ")

data_sort = sorted(data.items())

print("Name                 |Position              |Separation Date")
print("---------------------|----------------------|--------------------")
for i in data_sort:
    if last_name in i[0]:
        name = i[1][0] + ' ' + i[0] 
        position = i[1][1]
        date = i[1][2]
        print('{name:20} | {position:20} | {date:20}'.format(name=name, position = position, date = date))
        # print (name + ' |' + i[1][1] + ' |' + i[1][2] ) 

