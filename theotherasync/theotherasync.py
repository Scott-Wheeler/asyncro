from collections import deque

class Q:
    def __init__(self):
        self._q = deque()

    def get(self):
        return self._q.popleft()

    def put(self, something):
        self._q.append(something)


class BoundQ:
    def __init__(self, length=None):
        self.length = length

        if length is None:
            self._q = deque()
        else:
            self._q = deque((), length)


    def get(self):
        return self._q.popleft()


    def put(self, something):
        if len(self._q) < self.length:
            self._q.append(something)
        else:
            print("no")
    


def producer(q, num):
    for i in range(num):
        q.put(i)
    q.put(None)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("Got: ", item)


def test_Q():
    q = Q()
    
    q.put(42)
    assert q.get() == 42
test_Q()

def test_BoundQ():
    q = BoundQ(5)
    
    q.put(42)
    assert q.get() == 42
test_BoundQ()
    
def test_producer_consumer():
#     print('test_producer_consumer start')
    q = Q()
    producer(q, 50)
#     print('test_producer_consumer producer done')
    consumer(q)
#     print('test_producer_consumer done')
test_producer_consumer()

    