import bs4
import sys
 
# load the file
with open("index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)

# replce title with provided text in argument
soup.title.string.replace_with(sys.argv[1])
 
# save the file again
with open("index.html", "w") as outf:
    outf.write(str(soup))