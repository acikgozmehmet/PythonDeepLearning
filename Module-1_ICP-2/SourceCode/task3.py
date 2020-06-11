filename = "input.txt"

# first approach to read a file and storing the content into a list
infile = open(filename, 'r')
line = infile.readline()
mylist = []
while line != "":
    lst = line.split()
    mylist.extend(lst)
    line = infile.readline()

infile.close()

# alternative for reading a file and storing the content in a list
# with open(filename, 'r') as infile:
#     all_lines = infile.readlines()
#
# mylist = []
# for line in all_lines:
#     mylist.extend(line.split())


# alternative 1
# from collections import Counter
# mydict = dict(Counter(mylist))


# alternative 2
mydict = {}
for item in mylist:
    if item not in mydict.keys():
        mydict[item] = 1
    else:
        mydict[item] += 1

# diplay
for key, values in mydict.items():
    print(f"{key}: {values}")

# to save in a a new file
with open("result.txt", 'w') as outfile:
    for key, values in mydict.items():
        outfile.write(f"{key}: {values}\n")
