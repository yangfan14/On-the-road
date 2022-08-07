"""Quick Sort"""

# quick sort with extra memory
def quick_sort(arr):
	if len(arr) <= 1:  # base case: sorted
		return arr

	# Time: O(3n) -> O(n), Space: O(n)
	pivot = arr[-1]
	left = [num for num in arr if num < pivot]
	middle = [num for num in arr if num == pivot]  # allow duplicate
	right = [num for num in arr if num > pivot]	

	return quick_sort(left) + middle + quick_sort(right)  # O(logN * O(n))


# helper function for in place sorting version
def partition(arr, l, r):
	pivot = arr[r]
	target_index = l
	for i in range(l, r):
		if arr[i] < pivot:
			arr[i], arr[target_index] = arr[target_index], arr[i]
			target_index += 1
	arr[r], arr[target_index] = arr[target_index], arr[r]
	return target_index

# helper function for in place sorting version
def quick_sort_in_place_helper(arr, l, r):
	if r - l <= 0:  # base case: sorted
		return l

	pivot = partition(arr, l, r)
	quick_sort_in_place_helper(arr, l, pivot - 1)
	quick_sort_in_place_helper(arr, pivot + 1, r)

def quick_sort_in_place(arr):
	quick_sort_in_place_helper(arr, 0, len(arr) - 1)
	return arr

test_cases = [
	[],
	[1],
	[2,1],
	[9,3,7,2],
	[12,32,89,23,44,64,74,39],
	[1,1],
	[45,23,45],
	[12,34,56,12,43,56,87,83,12]
]

for arr in test_cases:
	temp = arr[:]
	quick_sort_in_place(arr)
	print("before=", temp, "  after=", arr)
