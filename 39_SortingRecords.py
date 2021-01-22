# When you’re looking at results, you’ll want to be able to sort
# them so you can find what you’re looking for quickly or do
# some quick visual comparisons.
# Given the following data set
# First Name Last Name Position Separation date
# John Johnson Manager 2016-12-31
# Tou Xiong Software Engineer 2016-10-05
# Michaela Michaelson District Manager 2015-12-19
# Jake Jacobson Programmer
# Jacquelyn Jackson DBA
# Sally Weber Web Developer 2015-12-18
# create a program that sorts all employees by last name and
# prints them to the screen in a tabular format.
# 
# Example Output
# Name | Position | Separation Date
# --------------------|-------------------|----------------
# Jacquelyn Jackson | DBA |
# Jake Jacobson | Programmer |
# John Johnson | Manager | 2016-12-31
# Michaela Michaelson | District Manager | 2015-12-19
# Sally Weber | Web Developer | 2015-12-18
# Tou Xiong | Software Engineer | 2016-10-05
# 
# Constraint
# • Implement the data using a list of maps.


data = {'Johnson': ['John', 'Manager', '2016-12-31'],
'Xiong': ['Tou', 'Software Engineer', '2016-10-05'],
'Michaelson': ['Michaela', 'District Manager', '2015-12-19'],
'Jacobson': ['Jake', 'Programmer', ''],
'Jackson': ['Jacquelyn', 'DBA', ''],
'Weber': ['Sally', 'Web Developer', '2015-12-18']
}

data_sort = sorted(data.items())

print("Name                 |Position              |Separation Date")
print("---------------------|----------------------|--------------------")
for i in data_sort:
    name = i[1][0] + ' ' + i[0] 
    position = i[1][1]
    date = i[1][2]
    print('{name:20} | {position:20} | {date:20}'.format(name=name, position = position, date = date))
    # print (name + ' |' + i[1][1] + ' |' + i[1][2] ) 

