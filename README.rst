Overview
========
Diff 2 python lists using a given key

Usage
=====

.. code:: python

listA = [3, 2, 1]
listB = [5, 4, 3]
inA, inBoth, inB = DiffUnsortedLists(iterA=iter(listA), iterB=iter(listB), keyA=lamba x: x, keyB=lambda x: x)
assert inA == [1, 2]
assert inBoth == [(3, 3)]
assert inB == [4, 5]

listA = [1, 2, 3]
listB = [3, 4, 5]
resultB = DiffListsByKey(iterA=iter(listA), iterB=iter(listB), keyA=lambda x: x, keyB=lambda x: x)
assert inA == [1, 2]
assert inBoth == [(3, 3)]
assert inB == [4, 5]
