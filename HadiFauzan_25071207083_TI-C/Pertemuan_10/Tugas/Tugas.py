data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
#radix
def radixSort (arr):
    temp_data = arr.copy()
    radixArray = [[], [], [], [], [], [], [], [], [], []]

    if len(temp_data) == 0:
       return temp_data
    
    maxVal = max(temp_data)
    exp = 1

    while maxVal // exp > 0:

        while len(temp_data) > 0:
            val = temp_data.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                temp_data.append(val)

        exp *= 10
    return temp_data

#merge
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

radixsortedlist = radixSort(data)
mergesortedlist = mergeSort(data)

print("="*105)
print("Radix Sort")
print(f"Sebelum: {data}")
print("")
print(f"Sesudah: {radixsortedlist}")
print("="*105)

print('+-'*54) #pemisah biar rapi

print("="*105)
print("Merge Sort")
print(f"Sebelum di sort: {data}")
print("")
print(f"Sesudah di sort: {mergesortedlist}")
print("="*105)