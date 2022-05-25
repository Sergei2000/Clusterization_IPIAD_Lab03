import fasttext
import fasttext.util
from MyText import Text
import ElasticConnector
from ElasticConnector import *
import Cluster 
from Cluster import *




#fasttext.util.download_model('ru')
news = GetAllNews(ip="192.168.1.10")
ft = fasttext.load_model('cc.ru.300.bin')
print("model loaded")

texts = list()
for New in news:
	texts.append(Text(New,ft))

dispatcher = ClusterDispatcher()
cluster = Cluster(ft,texts[0])
dispatcher.AppendCluster("1",cluster)



cluster = Cluster(ft,Text("к сожалению нередки случаи когда злоумышленники представляясь сотрудниками коммунальных служб проникают в квартиры москвичей чаще всего пожилых людей пенсионеров и предлагают услуги по замене счетчиков проверке газовых плит перед праздничными днями еще раз напоминаем сотрудники коммунальных служб если не возникла аварийная ситуация никогда не приходят без предупреждения отметил бирюков заместитель мэра подчеркнул что выезды специалистов осуществляются только по заявке граждан время приезда заранее согласовывается все внезапные проверки незаконны если к вам пришли с такой проверкой то сто процентов это мошенники при этом они часто пытаются продать дорогостоящее оборудование которое может представлять реальную опасность при эксплуатации хотел бы еще раз напомнить москвичам о необходимости быть внимательнее и не попадаться на такие уловки констатировал бирюков глава комплекса городского хозяйства сообщил что информация о проверках заранее размещается на информационном стенде в подъезде и на сайте организации которая ее проводит уточнить сведения о выезде сотрудников аварийных служб можно по телефонам компаний которые есть на официальном сайте правительства москвы",ft))
dispatcher.AppendCluster("3",cluster)



#
#print(dispatcher.GetClustersnum())
for i in texts:
	dispatcher.Distribute(i)
	print(dispatcher.CountDistance(texts[0].GetVector(),i.GetVector()))

for i in dispatcher.clusters.keys():
	print("\n")
	print(dispatcher.clusters[i].textlist[0].text)
	print("\n")
	print(dispatcher.clusters[i].textlist[-1].text)


#for i in dispatcher.clusters.keys():
#	if int(dispatcher.clusters[i].GetSize()) > 1 and int(dispatcher.clusters[i].GetSize()) < 5:
#		for i in dispatcher.clusters[i].textlist:
#			print (i.text)


