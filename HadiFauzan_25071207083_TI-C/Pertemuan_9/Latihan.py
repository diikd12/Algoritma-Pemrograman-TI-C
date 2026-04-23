
elemenN = []

for i in range (5):
    while True:
        angka1 = int(input(f"Masukkan elemen non negatif ke-{i+1}: "))

        if angka1 < 0:
            print ("Input tidak valid, harus non negatif!")
        else:
            elemenN.append(angka1)
        break   
print (f"elemen non-negatif yang anda masukkan: {elemenN}")

#insertion sort
n= len(elemenN)
for a in range(1, n):
    insert_indexN = a
    C_valueN = elemenN.pop(a)

    for b in range(a-1, -1, -1):
        if elemenN[b] > C_valueN:
            insert_indexN = b
    elemenN.insert(insert_indexN, C_valueN)

print (f"Hasil pengurutan negatif insertion: {elemenN}")

#quicksort
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

quicksort(elemenN)
print("quicksort", elemenN)

def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

mysortedlist = countingSort(elemenN)
print("countingsort", mysortedlist)