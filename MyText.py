import re
import fasttext
import fasttext.util
from pymystem3 import Mystem

class Text:

	def __init__(self,text,model):
		reg = re.compile('[^а-яА-Я ]')
		modifiedtext = reg.sub(' ', text)
		self.wordlist = modifiedtext.split(" ")

		while "" in self.wordlist:
			self.wordlist.remove("")

		self.text = " ".join(self.wordlist).lower()
		self.wordlist.clear()
		self.vector = model.get_sentence_vector(self.text)

	def GetVector(self):
		return self.vector

	def PrintInfo(self):
		print(self.text)
		print(self.vector)


#text =Text("По&nbsp;его словам, главы Бразилии, Уругвая, Эквадора, Колумбии, Панамы и&nbsp;Венесуэлы с&nbsp;удовлетворением наблюдают за&nbsp;тем, как Турция выполняет роль посредника в&nbsp;переговорах России и&nbsp;Украины.«Мы&nbsp;хотели&nbsp;бы внести свой вклад»,&nbsp;— процитировал Чавушоглу президента Бразилии, отметив, что&nbsp;Анкара обязательно изучит это предложение.Ранее представитель турецкого президента Ибрагим Калын заявил, что&nbsp;Анкара продолжит предпринимать усилия для&nbsp;прекращения боевых действий на&nbsp;Украине и&nbsp;завершения конфликта Москвы и&nbsp;Киева. Он&nbsp;также отметил, что&nbsp;есть вероятность достижения решения на&nbsp;основе суверенитета и&nbsp;территориальной целостности Украины."
#)
#text.PrintText()




