class pinjaman:
    def peminjaman (self, buku):
        self.buku = buku
        self.lamaHari = False

    def hitung_hari (self):
        self.lamaHari = True
        print (int(input(f"Masukkan berapa hari untuk pinjaman buku ini: ", self.lamaHari)))
        while (self.lamaHari):
            self.lamaHari = 0
            break