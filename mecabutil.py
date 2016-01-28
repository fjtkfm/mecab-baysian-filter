# coding: utf-8

import MeCab

mode = '-Ochasen'

word_classes = ['名詞', '動詞', '形容詞']


def getwords(sentence):
	tagger = MeCab.Tagger(mode)
	tagger.parse('')
	node = tagger.parseToNode(sentence)
	words = []
	while node:
		if node.feature.split(',')[0] in word_classes:
			words.append(node.surface)
		node = node.next

	return words

if __name__ == '__main__':
	sentence1 = 'Python（パイソン）は、広く使用されている汎用のプログラミング言語である。'
	print(sentence1, ' => ', getwords(sentence1))
