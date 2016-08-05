import urllib
import re
import winsound
import time

match = list()

# Define the time interval to check the result, in seconds
time_to_check = 5
string_to_check = 'BE SEM 4 - Regular'

# I like my computer making a 432 hertz sound lasting for 1 second
freq = 432
dur = 1000

while 1:
	data = urllib.urlopen('http://result1.gtu.ac.in/')

	for line in data:
		match += re.findall(string_to_check,line)
	
	if len(match) == 0:
		print ('No result yet')
		time.sleep(time_to_check)

	else:
		flag = 1
		print 'result declared!'
		break

if flag == 1:
	print 'Check your result on the GTU website. Press ctrl+C or ctrl+D to exit'
	while 1:
		winsound.Beep(freq,dur)
		time.sleep(4)

