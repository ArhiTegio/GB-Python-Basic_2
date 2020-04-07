from collections import deque
from queue import Queue
from collections import OrderedDict
from collections import namedtuple
point = namedtuple('Point', ['x', 'y'])
list_all_e = [float(1.3), int(30), oct(30), hex(30), True, False, "Hello World!", chr(125), complex(1.2), bytes(2),
        bytearray(b'hello world!'), [1, 2, 3, 4, 5], (1, 2, 3, 4, 5), set('hello'), frozenset('hello'),
        dict([(1, 'hello'), (2, 'world')]), OrderedDict([(1, 'hello'), (2, 'world')]), deque(['eat', 'sleep', 'code']),
        Queue(['eat', 'sleep', 'code']), point]

print('В листе содержится:')
for e in list_all_e:
    print('Элемент (' + str(e) + ') является типом - ' + str(type(e)))
