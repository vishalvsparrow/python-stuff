#Saved the source code for the HTML page at admin panel as a txt file.
#Time to calculate the number of users who haven't taken the test.
import re
count = 0
text = []
mydict={}
fname = raw_input('Enter the file name: \n')
if len(fname)<1: fname = 'utonexus_users.txt'
fhand = open(fname,'r')
#Bug with file operations. Need to clear it out.
'''
for line in fhand:
	line = line.lower()
	line = line.rstrip()
#	text = line.split()
#	if not '<td>test' in text: continue 
#	print text
#	print line
	if line.startswith('<td>test'):
		count = count+1
#	if line.startswith('<td>')
print count
'''
#Now calculate the total number of people for each personality type
#Also calculate the total number of people who took the test
for line in fhand:
	strings = re.search(r'[IE][SN][TF][PJ]',line)
	if strings:
		string = strings.group()
#		print string
		text.append(string)
		count = count+1
		mydict[string] = mydict.get(string,0) +1
for k,v in mydict.items():
	print k,v
#print str(mydict)+'\n'
print '\nTotal number of people who took the test out of 222 users: '+str(count)	
fhand.close()
