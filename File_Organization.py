# file handling amd file organization : navigate, rename, move , copy , remove

# automate all these::

import os
# print(os.getcwd())   # Current directory

os.chdir('/Users/khatiwadaprajwal22icloud.com/Desktop/random')  # change the directory 
# print(os.getcwd()) 
# now our current directory is changed
# Now i want to work in this directory and play with these files.


# Get the list of all the files in this directory
# for files in os.listdir():
#     # print(files)

# for files in os.listdir():
#     if(files == '.DS_Store'):   # to avoid the DS file
#         continue
#     print(files)

# Now
# split the base name from the extension and modify the name and put back together:
for files in os.listdir():
    name,ext= os.path.splitext(files)
    splitted = name.split("-")      #RETURNS list
    print(splitted)
    for s in splitted:
        splitted = [s.strip()]

    print(splitted)

# now i want number in beginning , python and title and get rid of spaces
# split this string to each and get different elements
