#
def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    
    TotalNilai = sum(nilai)
    JumlahData = len(nilai)
    hasil = TotalNilai/JumlahData

    return hasil

dataNilai = [80, 75, 90, 60, 85]
output = rata_rata(dataNilai)

print (f'Rata-rata nilai mahasiswa adalah =', {output})
