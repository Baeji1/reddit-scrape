import json

file = open("reddit.json","r")
data = json.load(file)
file.close()

pages = {}
c = "1"

for i in data:
	pages[c] = i
	d = int(c)+1
	c = str(d)

a = []

#print pages["1"][str(''.join(pages["1"].keys()))]
#print len(pages)
for i in range(1,len(pages)+1):
	a.append(pages[str(i)][str(''.join(pages[str(i)].keys()))])

for i in range(len(pages)):
	print "PAGE " + str(int(i)+int(1)) + ":"
	for j in range(len(a[0]["votes"])):
		print ""
		
		b = a[i]["title"][j]
		b.encode("utf-8")
		print "   Title: " + b
		
		b = a[i]["votes"][j]
		b.encode("utf-8")
		print "   Votes: " + b
		
		b = a[i]["user"][j]
		b.encode("utf-8")
		print "   User:  "  + b 
		
		b = a[i]["subreddit"][j]
		b.encode("utf-8")
		print "   Subreddit: " + b
	
	print ""

