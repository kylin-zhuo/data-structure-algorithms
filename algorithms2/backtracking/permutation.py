# Permutations

def permutation(arr):
	temp, result = [], []
	backtrack(temp, result, arr, set())
	return result

def backtrack(temp, result, arr, visited):
	if len(temp) == len(arr):
		result.append(temp[:])
		return
	for i in range(len(arr)):
		if i not in visited:
			temp.append(arr[i])
			visited.add(i)
			backtrack(temp, result, arr, visited)
			visited.remove(i)
			temp.pop()

arr = [1,2,3]
result = permutation(arr)

print(result)
