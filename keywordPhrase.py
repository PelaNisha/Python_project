from collections import Counter
from nltk.corpus import stopwords 	

stop_words = set(stopwords.words('english'))

def keyRead():								#function to convert the string to a list of items
	li = []
	with open("myfile.txt", "r+") as file1:
		for line in file1:       
			for word in line.split():
				if word not in stop_words:
				# displaying the words           
					li.append(word)
	return li
	
def splt1(a):
	li2 = []
	for i in range(0, len(a)-1):
		# if a[i] not in stop_words:
		s = (a[i]+" "+a[i+1])
		li2.append(s)
	return str(li2)

def splt2(w):							#function to create the dict of words and their count
	my_dict = {}
	words = w.split(',')
	word_counts = Counter(words)
	for word, count in sorted(word_counts.items()):
			my_dict[word] = [count]
	return my_dict
	
def sortD(d):								#function to sort dict by value in descending order
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders:
		print(i[0], i[1])	

x = keyRead()
y = splt1(x)
z =splt2(y)
sortD(z)