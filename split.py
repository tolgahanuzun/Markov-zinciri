#-*- coding: utf-8 -*-
def datalist():

	with open("testdata.txt") as f:
		text = f.read()

	data = text.decode('utf-8')
	data= data.split(" ")

	files = open("testing.txt", "w")

	for item in data:

		item = item.encode('utf-8')
		files.write(item +'\n' )

	return "Yes"	

def datatransfer():
	text = open("testing.txt").read()
	datalist=[]
	loopdata = text.splitlines()
	count = 0

	for data in loopdata:
		try:
			dictionary = {}
			i = 0

			for fee in loopdata:
				if data == fee:
					i=i+1

			dictionary["name"]=data		
			dictionary["number"]=i
			dictionary["after"]=loopdata[count+1]
			datalist.append(dictionary)
			count=count+1
		except:
			print "no problem"

	return datalist

datalist()








