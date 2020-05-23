# Arrays 

## Dynamic Array

Copy and rebuild a static array at a new location, with new memory size. 

**Operation**|**Cost**
:-----:|:-----:
Lookup| O(1)
Append | O(1) can be O(n) <=> triggers an expansion
Insert| O(n) 
Delete| O(n) 

## Static Array

Fixed in size. It cannot grow.

### Performance

**Operation**|**Cost**
:-----:|:-----:
Lookup| O(1)
Push| O(1)
Insert| O(n) b/c Traversal
Delete| O(n) b/c Traversal 
Pop | O(1)

**Traversal :=** Go through a list and access each item exactly once

**Searching :=** Find the index of an item if it exists

### Example Problem
**Problem statement:** Given two arrays, create a function that let's a user know whether these two arrays contain any common items. 

```python 
# Edge Case 
# i. arrays of different length?
# ii. alwas the same input type, input 1 is of the same type of input 2 and vice versa

#### START ####
arr_1 = ['a', 'b', 'c', 'x']
arr_2 = ['z', 'y', 'i']
arr_3 = ['a', 'b', 'c', 'x']
def hasCommonItem(arr1, arr2):
  for _, val in enumerate(arr1):
    if val in arr2:
      return True
  return False

test1 = hasCommonItem(arr_1, arr_2)
assert test1 == False
test2 = hasCommonItem(arr_1, arr_3)
assert test2 == True
```

**Solution:** 17

>First of all, the first way is ugly: You either need a separate variable assignment to get the element or use a[i] all the time which could theoretically be an expensive operation. Imagine a being a database cursor: When you iterate it (a.__iter__ being called) the object can safely assume that you are going to iterate over all its items. So all or at least multiple rows could be retrieved at once. When getting the length such an optimization would be stupid though since you surely don't want to retrieve data just because you want the number of items. Also, when retrieving a specific item you cannot assume that other items will be retrieved, too.
Additionally, using enumerate() works with any iterable while range(len()) only works with countable, indexable objects.

## Implementing an Array in Python 

```python 
import ctypes 

class DynamicArray: 
"""A Dynamic Array """"
    def __init__(self):
        self._n = 0;
        self._capacity = 1;
        self._resize = 2;
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
    """ return a new array with the capacity c  """
        return (c * ctypes.py_object)()

    def __len__(self):
       return self._n

    def __getitem__(self, k):
        if not k <= k < self._n:
            raise IndexError('Out of bounds')
        return self._A[k]

    def _resize(self, c):
      B = _make_array(c)
      for k in range(self._n):
        B[k] = self._A[k]
      self._A = B
      self._capacity = c 

    def append(self, obj):
        if self._n == self._capacity:
            self._resize( 2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
        
```