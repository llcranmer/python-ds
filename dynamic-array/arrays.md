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

**Why use enumerate?**

First of all, the alternative way can be costly: 
You either need a separate variable assignment to get the element or use a[i] all the time which could theoretically be an expensive operation. 

Imagine a being a database cursor: When you iterate it (a.__iter__ being called) the object can safely assume that you are going to iterate over all its items. 

So all or at least multiple rows could be retrieved at once. When getting the length such an optimization would be stupid though since you surely don't want to retrieve data just because you want the number of items. 

Also, when retrieving a specific item you cannot assume that other items will be retrieved, too.

Additionally, using enumerate() works with any iterable while range(len()) only works with countable, indexable objects.
