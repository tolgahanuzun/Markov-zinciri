from neo4jrestclient.client import  GraphDatabase
import split

gdb = GraphDatabase("http://localhost:7474/db/data/",username="neo4j", password="tolga123")
keyword = gdb.labels.create("Keyword")

datalist = split.datatransfer()

fee = {}


for data in datalist:
	try:
		fee[data["name"]]= gdb.nodes.create(name=data["name"], again=data["number"])	
		keyword.add(fee[data["name"]])	
	except:
		print "Ups" 


for data in datalist:	
	try:
		fee[data["name"]].relationships.create("sonra",fee[data["after"]] )
	except:
		print "Ups" 
		

'''	
name.relationships.create("once", name2)

try:
		
		
except:
	

'''