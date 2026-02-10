for x in range (10, 90, 2):
    print(x)

print ('done om ini akhirnya =', x)

def sapa(name="hadi"):
    print ('Halo mamang', name)

sapa()
#ini namanya void function^^

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#recursion
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

#function itu adalah sebuah blok kode yang dapat digunakan kembali
#secara bahasa mudahnya function itu adalah sebuah prosedur
#fungsi adalah sebuah blok kode yang hanya akan berjalan ketika dipanggil
