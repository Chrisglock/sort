def get_pivot(array, i, j):
	pivot = array[j]
	item = i - 1

	for k in range(i, j):
		if array[k] <= pivot:
			item = item + 1
			(array[item], array[k]) = (array[k], array[item])

	array[item + 1], array[j] = array[j], array[item + 1]

	return item + 1


def quick_sort(array, i=None, j=None):
    if i == None:
        i = 0
    if j == None:
        j = len(array) - 1
        
    if i < j:
        pivot = get_pivot(array, i, j)
        quick_sort(array, i, pivot - 1)
        quick_sort(array, pivot + 1, j)

def bubbleSort(lista):
    n = len(lista)

    for i in xrange(1, n):
        for j in xrange(n-i):


            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]