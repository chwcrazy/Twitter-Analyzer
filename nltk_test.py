__author__ = 'chenghaowei'


from nltk.corpus import gutenberg
from nltk import FreqDist
print gutenberg.fileids()
fd = FreqDist()
for word in gutenberg.words('austen-persuasion.txt'):
    fd[word] += 1
print fd.N()
print fd.B()
for word in fd.keys()[:10]:
    print word, fd[word]
