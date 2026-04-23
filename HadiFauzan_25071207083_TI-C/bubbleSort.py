def bubble_sort (arr):
    n = len(arr)
    #loop sesuai dengan banyaknya elemen arr
    for i in range (n):
        #lalu loop untuk membandingkan elemen arr dengan elemen selanjutnya (sekitarnya juga bisa sih)
        for j in range (0, n-i-1):
            #untuk membandingkan elemen jika elemen lebih besar dari elemen di sebelahnya maka akan dipindahkan
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

NIM_saya = [2, 5, 0, 7, 1, 2, 0, 7, 0, 8, 3]
print ("hasil bubble sort dari NIM Hadi Fauzan: ", bubble_sort(NIM_saya.copy()))
