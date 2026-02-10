#1
def Penjumlahan(b):
  return lambda a : a + b

hasilJumlahan = Penjumlahan(2)

print(hasilJumlahan(3))

#2
def pengurangan(b):
  return lambda a : a + b

hasilKurangan = pengurangan(5)

print (hasilKurangan(4))

#3
def perkalian(b):
  return lambda a : a * b

hasilKalian = perkalian(2)

print (hasilKalian(10))

#4
def pembagian(b):
  return lambda a : a / b

hasilBagian = pembagian(8)

print (hasilBagian(80))

#5
def modulus(b):
  return lambda a : a % b

hasilOlus = modulus(8)

print (hasilOlus(10))

#6
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

gen = fibonacci()
for _ in range(5):
  print(next(gen))


#BANGGG, TURUNKAN TUTORIAL FIBONACCIII