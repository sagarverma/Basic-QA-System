from questProcessing import resource_extractor as rex
from classifier.classifier import *
import re
from os import path

REL_WORDS_DIR = path.join(path.dirname(__file__), "classifier/rel_words/")

mapp = {'HUM' : ['group','peop','prof','title'], 'gr': ['group'], 'ind':['peop','prof'], 'title':['title'], 'LOC':['loca','univ','city','country','mount','state'], 'city':['city','loca'], 'country':['country','loca'], 'mount':['mount','loca'], 'state':['state','loca'], 'NUM':['num', 'popu', 'unit', 'weight', 'code', 'date', 'dimension', 'perc', 'speed'], 'weight' :['weight'], 'code':['code'], 'volsize':['dimension'], 'count':['num'], 'date':['date'], 'dist':['unit','dimension'], 'money':['num'], 'perc':['prec'], 'speed':['speed'], 'ABBR':['abb'], 'abb':['abb'], 'exp':['abb'], 'ENTY':['anim','body','color','currency','dise','event','food','instrument','lang','letter','plant','product','religion','sport' ,'substance','tech', 'symbol','vessel','word'], 'animal':['anim'], 'body':['body'], 'color':['color'], 'currency':['currency'], 'dismed':['disme'], 'event':['event'], 'food':['food'], 'instru':['instrument'], 'lang':['lang'], 'letter':['letter'],'plant':['plant'], 'product':['product'], 'religion':['religion'], 'sport':['sport'], 'substance':['substance'], 'techmeth':['tech'], 'symbol':['symbol'], 'termeq':['tech'], 'veh':['vessel'], 'word':['word'], 'DESC':['def','desc'], 'def':['def','desc'], 'desc':['def','desc'], 'manner':['def','desc'], 'reason':['def','desc']}

clf = Classifier()
clf.load_model()

def form_query(question):
	coarse,fine = clf.classify(question)
	re_out = rex.spotter(question)
	#print re_out
	resource_keyword = ""
	resource_uri = ""
	if re_out != 'netErr' and re_out != 'noSpotRes' and re_out != 'JSONErr':
		resource_keyword = re_out[0]['surfaceForm']
		resource_uri = re_out[0]['URI']
		"""
		types = re.sub('[/:,]', ' ', re_out[0]['types'])
		types = types.split()
		types = list(set(types))
		print types
		print coarse,fine
		rel_words_files = None
		if fine == 'other':
			rel_words_files = mapp[coarse[0]]
		else:
			rel_words_files = mapp[fine[0]]

		print rel_words_files

		rel_words = []
		for item in rel_words_files:
			f = open(REL_WORDS_DIR + item,'r')
			for line in f:
				rel_words.append(line[:-1])
			f.close()

		print rel_words
		"""
	return resource_keyword,resource_uri
