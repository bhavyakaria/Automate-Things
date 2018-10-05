import sys
import bs4

print('No of arguments:',len(sys.argv))
print('Arg:', str(sys.argv))

args = sys.argv
fileName = sys.argv[1]
x=1
for i in range(len(sys.argv)): 

	if i == 0:
		continue

	fileName = sys.argv[i]
	print(fileName)

	# loads the file and closes it without fail 
	with open(fileName) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt)

	# replce title with provided text in argument
	soup.title.string.replace_with("Wonder Man")
	 
	# save the file again
	with open(fileName,"w") as outf:
		outf.write(str(soup))

	