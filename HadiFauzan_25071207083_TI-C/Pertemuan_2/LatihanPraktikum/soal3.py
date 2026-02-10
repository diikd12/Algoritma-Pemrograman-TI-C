def JumlahDigit(n):
    if n < 10:
        return n
    else:
        return (n % 10) + JumlahDigit (n//10)
    
nilai = 1234
hasil = JumlahDigit(nilai)

print (f'Input:', nilai)
print (f'Output', hasil)