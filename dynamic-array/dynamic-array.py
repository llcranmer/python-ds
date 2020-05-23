import ctypes 

class Array:

    def __init__(self):
        self._number_of_elements = 0
        self._capacity = 1
        self._resize_factor = 2
        self._array = self._make_array(self._capacity)
    
    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._number_of_elements

    def __getitem__(self, k):
        if not k <= k < self._number_of_elements:
            raise IndexError('Out of bounds')
        return self._array[k]

    def _append(self, obj):
        if self._number_of_elements == self._capacity: 
            self._resize(self_resize_factor * self._capacity)
        self._array[self._number_of_elements] = obj
        self._number_of_elements += 1

    def _resize(self, c):
        B = _make_array(c)
        for k in range(self._number_of_elements):
            B[k] = self._array[k]
        self._array = B 
        self._capacity = c

    def insert(self, obj):
        




def testInstantiate(a):
    assert a._number_of_elements == 0 
    assert a._capacity == 1

def testMake(a):
    assert a._array != None

def testAppend(a):
    a._append('hi')
    assert a[0] == 'hi'

if __name__ == "__main__":
    arr = Array()
    testInstantiate(arr)
    testMake(arr)
    testAppend(arr)

