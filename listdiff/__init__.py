# another method might be to start with inA and inB and remove the ones that are shared

# another method would be to make a separate function that carries on with the iterator until it reaches x>=y and then return
# with this you're only working with one iterator at a time?
# if the items are equal, we need to increment both iterators until they are unequal

# another method is to use yield to make an iterator?

def DiffUnsortedLists(listA, listB, keyA, keyB):
	"""iterators point to unsorted lists but the given keys represent their identities for comparison"""
	return DiffListsByKey(iter(sorted(listA, key=keyA)), iter(sorted(listB, key=keyB)), keyA, keyB)

def DiffListsByKey(iterA, iterB, keyA, keyB):
	"""iterators point to lists sorted by the given keys, which also represent their identities for comparison"""
	return _DiffLists(iterA, iterB, lambda a, b: -1 if keyA(a) < keyB(b) else 1 if keyA(a) > keyB(b) else 0)

#assumes iterA and iterB are ordered
def _DiffLists(iterA, iterB, compare):
	"""
	iterA and iterB are iterators to sorted collections
	compare takes an A item and a B item and returns <0, 0 or >0
	returns a triple of inA, inBoth, inB
	"""
	inA, inBoth, inB = [], [], []
	incA, incB = True, True
	while True:
		if incA:
			a = next(iterA, None)
		if incB:
			b = next(iterB, None)
		if b is None:
			if a is None:
				break
			inA.append(a)
			incA, incB = True, False
		elif a is None:
			inB.append(b)
			incA, incB = False, True
		elif compare(a, b) < 0:
			inA.append(a)
			incA, incB = True, False
		elif compare(a, b) > 0:
			inB.append(b)
			incA, incB = False, True
		else:
			assert compare(a, b) == 0
			inBoth.append((a, b))
			incA, incB = True, True
	return inA, inBoth, inB

def TestRunDiffLists(listA, listB, expected=None):
	print('------')
	print(listA)
	print(listB)
	resultA = _DiffLists(iterA=iter(listA), iterB=iter(listB), compare=lambda x, y: (x > y) - (y > x))
	resultB = DiffListsByKey(iterA=iter(listA), iterB=iter(listB), keyA=lambda x: x, keyB=lambda x: x)
	assert expected == resultA
	assert resultA == resultB

def Test():
	RunDiffLists([1, 2, 3, 5], [2, 3, 4], ([1, 5], [(2, 2), (3, 3)], [4]))
	RunDiffLists([], [2, 3, 4], ([], [], [2, 3, 4]))
	RunDiffLists([1, 2, 3, 5], [], ([1, 2, 3, 5], [], []))
	RunDiffLists([], [], ([], [], []))
	RunDiffLists([1, 2, 3], [4, 5, 6], ([1, 2, 3], [], [4, 5, 6]))
