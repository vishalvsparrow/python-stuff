#Trying data compression with the help of dictionary. It was my idea in the 5th sem to do so. Let us being writing a wonderful code.
#Input file: compression.txt
#file size: 4,373 bytes
#Output file: compression_output.txt
#file size: 4,317 bytes
#Compression achieved: 5.397%

import itertools
import re
fname = raw_input('Enter the name of the file')
if len(fname)<1: fname ='compress.txt'
fhand = open(fname,'r')
fout = open('compress_output.txt','w')
mydict = {}
mylist = []

for cheese in fhand:
	cheese.rstrip()
	word = cheese.split()
#	print word
#	print '--------don't forget to seek----------'
fhand.seek(0)
for w in word:
	mydict[w] = mydict.get(w,0) +1
#print (mydict)
for k,v in mydict.items():
	mylist.append((v,k))
	mylist.sort(reverse=True)

def wordLength3():
	sumOfKeys1 =0
	temp =[]
	count =0
#	Finding the top 4 words with most counts
#	print '\nfind words with length 3'
	for v,k in mylist:
		if len(k) ==3 and v!=1 and count<4:
			count +=1
			temp.append((k,v))
			sumOfKeys1 +=v
	return temp,sumOfKeys1	

def wordLength4():
	sumOfKeys2 = 0
	temp =[]
	count =0
#	print '\nfind words with length 4'
	for v,k in mylist:		
		if len(k) ==4 and v!=1 and count <8:
			count+=1
			temp.append((k,v))
			sumOfKeys2 +=v
	return temp,sumOfKeys2

top4 = wordLength3()[1]
top4List = wordLength3()[0]
top8 = wordLength4()[1]
top8List = wordLength4()[0]

def CalculateSize():
	mydict2 ={}
	count = 0
	temp =[]
#	determine which scheme to apply - 2 bits or 3 bits --> 2 bits for 3 words(top4), 3 bits for 4 words(top8)
#	comp2BitSize = wordLength3()[1]*2*3
#	traceback : 'function' object has no attribute '__getitem()__'
	comp2BitSize = top4*2*3
	comp3BitSize = top8*3*4
	if comp2BitSize > comp3BitSize:
		print 'Use 2 bit scheme'+'\nFollowing are the top 4 word-code pairs:\n'
		is2Bits = True
		repeatme = 2
#		Converting list of tuples to dictionary
		mydict2 = dict(top4List)
	else:
		print '\nUse 3 bit scheme'+'\nFollowing are the top 8 word-code pairs:\n'
		is3Bits = True
		repeatme = 3
		mydict2 = dict(top8List)
#	Creating a dynamic list of binary combinations. I love itertools library!
	binaryList = ["".join(bits) for bits in itertools.product('01',repeat =repeatme)]
	for key in mydict2:
#		print key,binaryList[count] #Keep it simple silly! (Direct manipulation of dictionary)
		mydict2[key] = binaryList[count]
#		temp.append((key,binaryList[count]))
		count +=1
#	mydict2 =dict(temp)
	return mydict2

#mydict = CalculateSize()
#print mydict

def replacer_factory(main_dict):
    def replacer(match):
        word = match.group()
        return main_dict.get(word, word)
    return replacer

def compress(text):
    pattern = r'\b\w+\b'  # this pattern matches whole words only   
    replacer = replacer_factory(CalculateSize())
    return re.sub(pattern, replacer, text)

def main():
  text = fhand.read()
	fout.write(compress(text))
	print '\nCheck the \'compress_output.txt\' file'

# Cannot decompress. Minor Bug fix needed.
'''def decompressor(text):
	pattern = r'\b\w+\b'
	revdict = dict([(v,k) for (k,v) in CalculateSize().items()])
	replacer = replacer_factory(revdict)
	return re.sub(pattern,replacer,text)
'''
# A good habit
if __name__ == '__main__':
    main()
