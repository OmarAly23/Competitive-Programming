# algorithm
# sort A then find i and j
# i and j will be the first two elements that their sum adds up to the target value

# MergeSort in Python
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# algorithm
# sort A then find i and j
# i and j will be the first two elements that their sum adds up to the target value
def twoSums(A, target):
    mergeSort(A)
    sum = 0
    for ele in A:
        sum += ele
        if sum >= target:
            x = A.index(ele)
            y = A.index(ele-1)
            return (y, x)

    return -1


A = [6,3,4,9]
target = 7

L = twoSums(A, target)
print(L)


# Anagrams
string = "kuwait"
str2 = "wuaitk"
res = ''.join(sorted(string))
res2 = ''.join(sorted(str2))
if res==res2:
    print('Anagrams')
else:
    print('Not anagrams')
