from elasticsearch import Elasticsearch
import json


def GetAllNews(index="posts",size=1000,ip="192.168.1.77",port="9200"):
	client = Elasticsearch(
    str("http://"+str(ip)+":"+str(port))
	) 
	doc = {'size': size,
		'query': {
		'match_all' : {}
		}
	}
	resp = client.search(index="posts", body= doc)
	textlist = list() 
	for i in resp["hits"]["hits"]:
		textlist.append(i["_source"]["Content"])
	return textlist
	







