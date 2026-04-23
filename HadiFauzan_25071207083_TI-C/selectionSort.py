def selection_sort(arr):
    n = len(arr)
    #loop banyak elemen arr
    for i in range (n):
        #nyari nilai min dari elemen arr
        min = i
        for j in range (i+1, n):
            if arr[j] < arr[min]:
                min = j
        #menukar nilai min dengan elemen pertama
        arr[i], arr[min] = arr[min], arr[i]
    return arr
def selection_sort_max(arr1):
    n = len(arr1)
    for i in range (n):
        max = i
        for j in range (i+1, n):
            if arr1[j] > arr1[max]:
                max = j
        arr1[i], arr1[max] = arr1[max], arr1[i]
    return arr1

NIM_saya = [2, 5, 0, 7, 1, 2, 0, 7, 0, 8, 3]
print ("hasil selection sort dari NIM Hadi Fauzan: ", selection_sort(NIM_saya.copy()))
print ("hasil dari minimum NIM saya adalah: ", min(NIM_saya.copy()))
print ("max: ", max (NIM_saya.copy()))