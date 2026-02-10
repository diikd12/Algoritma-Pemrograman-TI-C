def PangkatRekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * PangkatRekursif(a, b - 1)
    
a = 2
b = 5

hasil = PangkatRekursif(a, b)
print (f'Input a =', a, 'dan b =', b )
print (f'Hasil', a, 'Pangkat', b, 'adalah =', hasil)