import operator

dict = dict()

dict['test']=1
dict['test999']=2
dict['test3']=3
dict['test64']=11

print sorted(dict.items(), key=operator.itemgetter(1))


