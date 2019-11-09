
# Quick Sort
def partition(A, p, r):
  x = A[r]
  i = p - 1
  for j in range(p, r):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i+1

def quickSort(A, p, r):
  if p < r:
    q = partition(A, p, r)
    quickSort(A, p, q-1)
    quickSort(A, q+1, r)
      


# Merge Sort
def merge(A, p, q, r):
  i = k = p
  j = q + 1
  B = A[:]
  while i <= q and j <= r:
    if A[i] <= A[j]:
      B[k] = A[i]
      k += 1
      i += 1
    else:
      B[k] = A[j]
      j += 1
      k += 1
  while i <= q:
      B[k] = A[i]
      k += 1
      i += 1
  while j <= r:
      B[k] = A[j]
      k += 1
      j += 1
  for i in range(p, r+1):
      A[i] = B[i]


def mergeSort(A, p, r):
  if p < r:
    q = (p+r) >> 1
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)


# Heap Sort
def leftChild(start):
  return (start+1)*2-1

def rightChild(start):
  return (start+1)*2

def maxHeapify(A, start, size):
  left = leftChild(start)
  right = rightChild(start)
  if left < size and A[left] > A[start]:
    largest = left
  else:
    largest = start
    if right < size and A[right] > A[largest]:
      largest = right
    if largest != start:
      A[start], A[largest] = A[largest], A[start]
      maxHeapify(A, largest, size)

def buildMaxheap(A):
  size = len(A)
  for i in range(size/2)[::-1]:
    maxHeapify(A, i, size)

def heapSort(A):
  buildMaxheap(A)
  size = len(A)
  for i in range(1, len(A))[::-1]:
    A[0], A[i] = A[i], A[0]
    size -= 1
    maxHeapify(A, 0, size)


import random
import time

for size in range(1,8):
  A = range(10 ** size)
  random.shuffle(A)


  t =time.time()
  # quickSort(A, 0, len(A)-1)
  heapSort(A)
  print str(size) + ": " + str(time.time() - t)
