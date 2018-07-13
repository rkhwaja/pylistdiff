from listdiff import _DiffLists, DiffListsByKey, DiffUnsortedLists

def test_diff_unsorted_lists():
	listA = [3, 2, 1]
	listB = [5, 4, 3]
	inA, inBoth, inB = DiffUnsortedLists(listA=listA, listB=listB, keyA=lambda x: x, keyB=lambda x: x)
	assert inA == [1, 2]
	assert inBoth == [(3, 3)]
	assert inB == [4, 5]

def test_diff_lists_by_key():
	listA = [1, 2, 3]
	listB = [3, 4, 5]
	inA, inBoth, inB = DiffListsByKey(iterA=iter(listA), iterB=iter(listB), keyA=lambda x: x, keyB=lambda x: x)
	assert inA == [1, 2]
	assert inBoth == [(3, 3)]
	assert inB == [4, 5]

def RunDiffLists(listA, listB, expected=None):
	resultA = _DiffLists(iterA=iter(listA), iterB=iter(listB), compare=lambda x, y: (x > y) - (y > x))
	resultB = DiffListsByKey(iterA=iter(listA), iterB=iter(listB), keyA=lambda x: x, keyB=lambda x: x)
	assert expected == resultA
	assert resultA == resultB

def test():
	RunDiffLists([1, 2, 3, 5], [2, 3, 4], ([1, 5], [(2, 2), (3, 3)], [4]))
	RunDiffLists([], [2, 3, 4], ([], [], [2, 3, 4]))
	RunDiffLists([1, 2, 3, 5], [], ([1, 2, 3, 5], [], []))
	RunDiffLists([], [], ([], [], []))
	RunDiffLists([1, 2, 3], [4, 5, 6], ([1, 2, 3], [], [4, 5, 6]))
