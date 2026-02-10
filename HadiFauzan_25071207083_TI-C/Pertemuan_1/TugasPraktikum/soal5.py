#input fungsi hitung
def hitung (a, b):

    #tambahkan operasi sederhana
    tambah = a + b
    kurang = a - b

    #mengembalikan nilai ke pemanggil fungsi
    return tambah, kurang

#memanggil fungsi hitung
hasilTambah, hasilKurang = hitung (5, 3)

#output hasil operasi
print ('Hasil Penjumlahan: ', hasilTambah)
print ('Hasil Pengurangan: ', hasilKurang)