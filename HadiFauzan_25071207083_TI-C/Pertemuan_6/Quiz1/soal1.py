namaBuku = [
    ["Algoritma", 2000],
    ["Basisdata", 2500],
    ["Pemrograman", 3000],
    ["Bahasa", 3500],
    ["3769MDPL", 4000]
]
class buku:
    def listBukuDanDenda (self, namaBuku, denda):
        self.namaBuku = namaBuku
        self.denda = denda

    def tampilkanBuku(self):
        print (f"nama buku: {self.namaBuku} dengan denda {self.denda}")

    i = 0

    for i in range (5):
        print (int(input("masukkan nomor buku yang anda inginkan: ")))

        if input == listBukuDanDenda:
            print ("Ini buku yang anda inginkan: {self.namaBuku}, dan ini dendanya: {self.denda}")
        else:
            print ("nomor yang anda masukkan tidak valid!")
