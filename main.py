#data structure
#range function return a list tant starter from zero to a number before that the put it in the brack 
print(range(4))
#[0, 1, 2, 3]
stuff = list()
#make a empty list and assignt to the variable stuff
#x=x.append() is a error that make a mistake just use x.append()
#.slipt divides a string in a list of multiple strings
#split is intelligent and detect all the spaces in the original string
#when the string have other think different of a space like a com we put that in the parenthesis
abc = 'with three words'
stuff = abc.split()
print(stuff)
#['with', 'three', 'words']
#join is the inverse and we usa the variable delimiter to put the space between ther words
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)
#'pining for the fjords'
#exercise
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)
#exercise 2
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): 
        continue
    words = line.split()
    count += 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
# In this case we would say that the two lists are equivalent, because they have the 
# same elements, but not identical, because they are not the same object. If two objects 
# are identical, they are also equivalent, but if they are equivalent, they are not necessarily
#  identical.
#OTHER WAY TO FIND A LINE IN A TEXT BUT ADDING A guardian statement
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    #this si a guardian statememnt that jump the empty spaces and continue with the code, the erro was IndexError: list index out of range
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    #this other way to put a guardian, you must look the order of the statements
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])

#exercise 3 
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    mail = words[1]
    count[mail] = count.get(mail,0) + 1
bigcount = None
bigmail = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigmail = word
print(mail, bigcount)