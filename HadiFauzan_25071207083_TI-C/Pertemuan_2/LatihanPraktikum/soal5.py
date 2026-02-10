import math

def jarak(x1, x2, y1, y2):
    selisihX = x2 - x1
    selisihY = y2 - y1
    d = math.sqrt(selisihX**2 + selisihY**2)
    return d

x1, y1 = 1, 1
x2, y2 = 4, 5

hasil = jarak(x1, x2, y1, y2)
print (f'jarak =', hasil)