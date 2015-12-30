#Python for Informatics with Dr. Chuck Severance. Assignment 10.2 from coursera's Python for Everybody [part 2]

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#mylist = [] #I was going to do the redundant job of appending dict to a temp list. Just a reminder that I didn't do it.
mydict = {}
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    word = line.split()
    word = word[5]
    pos = word.find(':')
    word = word[:pos]
    mydict[word] = mydict.get(word,0)+1
#print mydict
for key,value in sorted(mydict.items()): #Converting the dictionary to a list of tuples	
	print key,value

#List comprehenstion : A dynamic list of tuples	
#print sorted( (k,v) for (k,v) in mydict.items()) 
