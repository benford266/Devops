def unique_sort(lst):
	sorted = lst
	sorted.sort()
	sorted = list(dict.fromkeys(sorted))
	return sorted


unique_sort([1,2,3,4,3,4,9,6])