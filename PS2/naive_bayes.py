import numpy as np
import matplotlib.pyplot as plt
import operator
import math

def generate_dict(file,dictionary):
 f = open(file)
 text = f.read()
 text = text.split(' ')
 for word in text:
  if word in dictionary:
   dictionary[word] += 1
  else:
   dictionary[word] = 1
 return dictionary

def extract_words(path,name):
 f = open(path + name)
 files = f.readlines() 
 d = {}
 for file in  files :
  d = generate_dict( path + file[:-1],d) 
 return d 

def total_words(dictionary):
	total = 0
	for keys in dictionary:
		if keys in list_all:
		 total += dictionary[keys]
	return total

def test(file):
 dt = {}
 dt = generate_dict(file,dt)
 sum1 = 0.0
 sum0 = 0.0
 for word in dt:
 	if word in list_all:
 	 i = list_all.index(word)
 	 sum1 += prob_array[i][1]*dt[word]
 	 sum0 += prob_array[i][0]*dt[word]
 if sum1 >= sum0:
 	return 1
 else :
 	return 0
 
all_d = extract_words('ex6DataEmails/ALL/','all.txt')
spam_d = extract_words('ex6DataEmails/spam-train/','spam.txt')
notspam_d = extract_words('ex6DataEmails/nonspam-train/','notspam.txt')

list_all = []
sorted_d = sorted(all_d.items(), key=operator.itemgetter(1))
for words in sorted_d[-2500:]:
	list_all.append(words[0])

total_spam = total_words(spam_d)
total_notspam = total_words(notspam_d)

prob_array = np.zeros((2500,2))
for i in range(0,2500):
	prob_array[i][0] = math.log10((1.0)/(total_notspam + 2500))
	prob_array[i][1] = math.log10((1.0)/(total_spam + 2500))
for words in spam_d:
	if words in list_all:
		i = list_all.index(words)
		prob_array[i][1] = math.log10((spam_d[words]+1.0)/(total_spam + 2500))
for words in notspam_d:
	if words in list_all:
		i = list_all.index(words)
		prob_array[i][0] = math.log10((notspam_d[words]+1.0)/(total_notspam + 2500))

spam_wrong = 0
notspam_wrong = 0
spam_test = open('ex6DataEmails/spam-test/spam.txt').readlines()
nonspam_test = open('ex6DataEmails/nonspam-test/notspam.txt').readlines()

for files in spam_test:
 if test('ex6DataEmails/spam-test/' + files[:-1]) == 0:
 	spam_wrong += 1
for files in nonspam_test:
 if test('ex6DataEmails/nonspam-test/' + files[:-1]) == 1:
 	notspam_wrong += 1

print spam_wrong
print notspam_wrong