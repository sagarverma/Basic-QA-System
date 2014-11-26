import nltk
from nltk.corpus import stopwords
from spotlight import annotate
import spotlight
from functools import partial
import requests
api = partial(annotate, 'http://spotlight.dbpedia.org/rest/annotate')
stop = stopwords.words('english')
def spotter(question):
	words = nltk.word_tokenize(question)
	inp = ""
	for word in words:
		if word not in stop:
			inp += word
			inp += " "
	out = None
	try:
		out = api(inp)
	except requests.exceptions.HTTPError:
		out = "netErr"
	except spotlight.SpotlightException:
		out = "noSpotRes"
	except ValueError:
		out = "JSONErr"
	return out

