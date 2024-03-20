import sys

LIST = [1, 3, 2]
TUPLE = (1, 2, 8)
LIST.insert(2, 9)
print(sys.getsizeof(LIST))
print(sys.getsizeof(TUPLE))

#leng(object)
print(len(LIST))
#>>> 2

print(len(TUPLE))
#>>> 2

#max(object)
print(max(TUPLE))
#retrieves the largest value

#min(object)
print(min(TUPLE))
#retrieves the smalles value
import collections
from collections import namedtuple

Employee = namedtuple('Record', ['first_name', 'last_name'])
emp1_Record = Employee('yasar', 'halim')
emp2_Record = Employee('sinan', 'bilir')
print(emp1_Record, emp2_Record)

#because TUPLE is immutable, a special function is needed to use functional operators
from collections import deque
d = deque([1, 2, 3])
d.appendleft(4)
d.pop()
print(d)