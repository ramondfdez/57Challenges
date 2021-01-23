# Programming languages can create files and folders too.
# Create a program that generates a website skeleton with the
# following specifications:
# • Prompt for the name of the site.
# • Prompt for the author of the site.
# • Ask if the user wants a folder for JavaScript files.
# • Ask if the user wants a folder for CSS files.
# • Generate an index.html file that contains the name of the
# site inside the <title> tag and the author in a <meta> tag.
# 
# Example Output
# Site name: awesomeco
# Author: Max Power
# Do you want a folder for JavaScript? y
# Do you want a folder for CSS? y
# Created ./awesomeco
# Created ./awesomeco/index.html
# Created ./awesomeco/js/
# Created ./awesomeco/css/

import os 

name = input("Site name: ")
author = input("Author: ")
js = input("Do you want a folder for Javascript? ")
css = input("Do you want a folder for CSS? ")

directory = os.path.join("Files/", name)
os.mkdir(directory)

html = os.path.join(directory, "index.html")
f_out = open(html, "w")

f_out.write("<!DOCTYPE  html>\n")
f_out.write("<html>\n")
f_out.write("<head>\n")
f_out.write("<meta name=\"author\" content=" + author + ">\n")
f_out.write("<title> " + name + " </title>\n")
f_out.write("</head>\n")
f_out.write("<body>\n")
f_out.write("</body>\n")
f_out.write("</html>\n")

if (js.upper() == 'Y' or js.upper() == 'YES'):
    path_js = os.path.join(directory,"js")
    os.mkdir(path_js)

if (css.upper() == 'Y' or css.upper() == 'YES'):
    path_css = os.path.join(directory,"css")
    os.mkdir(path_css)

