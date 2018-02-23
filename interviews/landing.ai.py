"""
Given lectures and their starting and ending times
0-------------10
   2----5
       4-----9
           8----------13
          	      11------15
                    12--------18
"""
examples = [[0,10], [2,5], [4,9], [11,15], [12,18]]


"""
Function 1 return the minimum number of students to cover all the lectures
"""
from heapq import heappop, heappush
def function1(arr):
	arr = sorted(arr, key=lambda x:x[0])
	heap = []
	for s,e in arr:
		if not heap:
			heap.append(e)
		else:
			prev_e = heap[0]
			if s >= prev_e:
				heappop(heap)
			heappush(heap, e)
	return len(heap)


"""
Imagine the student is lazy for attending the whole lecture
He wants to sign in the lecture and leave.
Function 2 returns the minumm number of trips for sign in the lectures
Notice: the lectures that have overlaps can be signed by a single trip

For the example above, return 2. Trip 1 is arriving at 4 and trip 2 at 12.
"""
def function2(arr):
	arr = sorted(arr, key=lambda x:x[0])
	count = 0
	interval = None
	for s, e in arr:
		if not interval:
			interval = (s, e)
			count += 1
			continue
		ps, pe = interval
		if not (e < ps or s > pe):
			interval = (max(s, ps), min(e, pe))
		else:
			interval = None
	return count 


print(function1(examples))
print(function2(examples))