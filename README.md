# Overview

Diff 2 python lists using a given key

![image](https://github.com/rkhwaja/pylistdiff/workflows/ci/badge.svg) [![image](https://codecov.io/gh/rkhwaja/pylistdiff/branch/master/graph/badge.svg)](https://codecov.io/gh/rkhwaja/pylistdiff)

# Usage

``` python
listA = [3, 2, 1]
listB = [5, 4, 3]
inA, inBoth, inB = DiffUnsortedLists(listA=listA, listB=listB, keyA=lambda x: x, keyB=lambda x: x)
assert inA == [1, 2]
assert inBoth == [(3, 3)]
assert inB == [4, 5]

listA = [1, 2, 3]
listB = [3, 4, 5]
resultB = DiffListsByKey(iterA=iter(listA), iterB=iter(listB), keyA=lambda x: x, keyB=lambda x: x)
assert inA == [1, 2]
assert inBoth == [(3, 3)]
assert inB == [4, 5]
```
