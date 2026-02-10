def BilanganPrima(n):
    ListPrima = []

    for u in range (2, n + 1):
        Prima = True
        for i in range (2, u):
            if (u % i) == 0:
                Prima = False
                break
        if Prima:
            ListPrima.append(u)
    return ListPrima

n = 50
Hasil = BilanganPrima(n)

print (f'Hasil bilangan prima antara 1 sampai {n} adalah =', Hasil)