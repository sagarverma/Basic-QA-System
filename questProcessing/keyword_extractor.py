from nltk.corpus import conll2000
import nltk
from nltk.chunk.util import conlltags2tree
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])

class ChunkParser(nltk.ChunkParserI):
	def __init__ (self, train_sents):
		train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
		self.tagger = nltk.TrigramTagger(train_data)

	def parse(self, question):
		pos_tags = [pos for (word,pos) in question]
		tagged_pos_tags = self.tagger.tag(pos_tags)
		chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
		conlltags = [(word,pos,chunktag) for ((word, pos), chunktag) in zip(question, chunktags)]
		print conlltags
		return conlltags2tree(conlltags)

def key_extract(question):
	NPChunker = ChunkParser(train_sents)
	words = nltk.word_tokenize(question)
	tokens = nltk.pos_tag(words)
	print NPChunker.parse(tokens)
