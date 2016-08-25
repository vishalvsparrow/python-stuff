import urllib
import re
from bs4 import BeautifulSoup

destination_url = raw_input('Enter the url from which you wish to download the files: ') 
# link1 = 'http://ebook.nscpolteksby.ac.id/files/Ebook/Accounting/Statistics%20for%20Business%20and%20Economics%20(2011)/'
extension = (raw_input('Enter the file extension: ')).strip()
fhand = urllib.urlopen(destination_url).read()
# link2 = 'http://hcmaslov.d-real.sci-nnov.ru/public/mp3/Beatles/01%20Please,%20Please%20Me/'

testfile = urllib.URLopener()

soup = BeautifulSoup(fhand,'html.parser')

tags = soup('a')

count = 0

for tag in tags: 
	file_name = tag.get('href',None)
	valid = re.findall('[.]'+extension,file_name)
	if not len(valid)==0:
		save_name = re.sub("%20",' ',file_name)
		testfile.retrieve(destination_url+file_name,save_name+"."+extension)
		print save_name+"<--------------Downloaded"
		count +=1


if count == 0:
	print 'Nothing found here! Try another extension or check the url'
