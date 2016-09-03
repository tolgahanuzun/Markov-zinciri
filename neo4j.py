from neo4jrestclient.client import  GraphDatabase
import split

gdb = GraphDatabase("http://localhost:7474/db/data/",username="neo4j", password="tolga123")
keyword = gdb.labels.create("Keyword")

datalist = split.datatransfer()

for data in datalist:
	try:
		if data["number"]== 1:
			fee =datalist[datalist.index(data)+1]
			name = gdb.nodes.create(name=data["name"], again=data["number"])
			name2 = gdb.nodes.create(name=fee["name"], agein=fee["number"])			
			keyword.add(name,name2)
			name.relationships.create("once", name2)
	except:
	print "Ups" 	
	