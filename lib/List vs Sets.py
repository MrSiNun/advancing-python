#sets contain larger space than lists becaose they are stored on blocks, lists are small peaces
import sys
list = [1,2]
set = {1,2}
print(sys.getsizeof(list))
print(sys.getsizeof(set))




