
mydict = {'brand': 'My Brand', 'model': '1992'}

print(mydict.keys())

print(mydict.values())

"""Chain Map"""
#Collates dictionaries into a single collection. An example is shown below.

from collections import ChainMap
d ={1:1}
d_1 ={2,2}
d_2 = {3,3}
print(ChainMap(d, d_1, d_2))
#maps function shows the content of the chainmap directories
print(ChainMap(d, d_1, d_2).maps)
