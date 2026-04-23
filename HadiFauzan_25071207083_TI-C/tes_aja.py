#contoh kisi-kisi nomor 1

data_mahasiswa = [
    {'nama' : 'Hadi', 'nilai' : 95, 'status' : 'Aktif'},
    {'nama' : 'Nadin', 'nilai' : 100, 'status' : 'My Bini'},
    {'nama' : 'J ORGIL', 'nilai' : 50, 'status' : 'Aktif (beliau hanya NPC)'},
    {'nama' : 'Budak Stress', 'nilai' : 45, 'status' : 'Tidur'},
]

#cara untuk mengurutkan nama dengan rapi
data_mahasiswa.sort(key=lambda x: x['nama'])
print ('data mahasiswa yang sudah diurutkan berdasarkan nama:')
for mhs in data_mahasiswa:
    print (mhs['nama'])

mhs_lulus = [mhs for mhs in data_mahasiswa if mhs ['nilai'] > 70]

#kalau ingin tahu berapa banyak yang lulus aja, bisa kek gini: 
print ('\nmahasiswa yang lulus :', len(mhs_lulus))

#kalau ingin spesifik, misal kaya hanya print namanya saja, begini contohnya: 
print ("nama mahasiswa yang lulus:")
for mhs in mhs_lulus:
    print (mhs['nama'])

#kalau ingin print semua datanya dengan rapi, bisa kek gini!
print ('\nnama dan keterangan mahasiswa yang lulus: ')
for mhs in mhs_lulus:
    print (f"{mhs['nama']} nilai: {mhs['nilai']} status: {mhs['status']}")


#contoh kisi-kisi nomor 2
mobil = ("BMW M4 Competition", "TOYOTA Supra MKIV", "Nissan Skyline R34 GT-R", "Porsche 911 GT3 RS", "BMW M4 Competition")

print ("\nmobil Brian O'Conner: \n", mobil[1]+'\n', mobil[2])
#tuple tidak bisa di ubah, jadi kita tidak bisa menambahkan atau menghapus data di dalamnya.

aku_nak_mobil_ni = set(mobil)
print ("\nmobil unik: ", aku_nak_mobil_ni)