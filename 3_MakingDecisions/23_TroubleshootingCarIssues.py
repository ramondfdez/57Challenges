# An expert system is a type of artificial intelligence program
# that uses a knowledge base and a set of rules to perform a
# task that a human expert might do. Many websites are
# available that will help you self-diagnose a medical issue by
# answering a series of questions. And many hardware and
# software companies offer online troubleshooting tools to
# help people solve simple technical issues before calling a
# human.
# Create a program that walks the user through troubleshooting issues with a car. Use the following decision tree to build
# the system:
#
# Example Output
# Is the car silent when you turn the key? y
# Are the battery terminals corroded? n
# The battery cables may be damaged.
# Replace cables and try again.
#
# Constraint
# • Ask only questions that are relevant to the situation and
# to the previous answers. Don’t ask for all inputs at once.

level1 = input("Is the car silent when you turn the key? ")

if level1.upper() == 'Y' or level1.upper() == "YES":
    level2 = input("Are the battery terminals corroded? ")
    if level2.upper() == 'Y' or level2.upper() == "YES":
        print("Clean terminals and try starting again.")
    elif level2.upper() == 'N' or level2.upper() == "NO":
        print("Replace cables and try again.")
    else:
        print("Please enter Y or N to answer the questions.")
elif level1.upper() == 'N' or level1.upper() == "NO":
    level2 = input("Does the car make a clicking noise? ")

    if level2.upper() == 'Y' or level2.upper() == "YES":
        print("Replace the battery.")

    elif level2.upper() == 'N' or level2.upper() == "NO":
        level3 = input("Does the car crank up but fail to start? ")
        if level3.upper() == 'Y' or level3.upper() == "YES":
            print("Check spark plug connections.")
        elif level3.upper() == 'N' or level3.upper() == "NO":
            level4 = input("Does the engine start and then die? ")
            if level4.upper() == 'Y' or level4.upper() == "YES":
                level5 = input("Does your car have fuel injection? ")
                if level5.upper() == 'Y' or level5.upper() == "YES":
                    print("Get it in for service")

                elif level5.upper() == 'N' or level5.upper() == "NO":
                    print("Check to ensure the chocke is opening and closing ")

                else:
                    print("Please enter Y or N to answer the questions.")

            elif level4.upper() == 'N' or level4.upper() == "NO":
                print("We don't know what is happening to your car ")

            else:
                print("Please enter Y or N to answer the questions.")

        else:
            print("Please enter Y or N to answer the questions.")

    else:
        print("Please enter Y or N to answer the questions.")
else:
    print("Please enter Y or N to answer the questions.")
