#TERDAPAT BUG PADA BAGIAN LIHAT RIWAYAT BERMAIN🙏``
#===BAGIAN A===
def tentukan_pemenang (pilihan_pemain, pilihan_komputer):
    """menentukan pemenang"""
    if pilihan_pemain == pilihan_komputer:
        return "Seri 0 point"
    elif (pilihan_pemain == "gunting" and pilihan_komputer == "kertas" or pilihan_pemain == "kertas" and pilihan_komputer == "batu" or pilihan_pemain == "batu" and pilihan_komputer == "gunting"):
        return "Pemain menang +10 point, Komputer kalah 0 point"
    else:
        return "Pemain kalah 0 point, Komputer menang +10 point"
    
def input_pemain ():
    """meminta pemain untuk input suit (gunting/batu/kertas)"""
    opsi = ["gunting", "batu", "kertas"]

    while True:
        pemain = input ("Masukkan pilihan (gunting/batu/kertas): ").lower()
        if pemain in opsi:
            return pemain
        else:
            print("Input yang anda masukkan salah. Harap coba lagi!")

def ronde (nama_pemain, nomor_ronde):
    """melakukan 1 ronde permainan serta menentukan siapa pemenang di dalam permainan"""
    pilihan_pemain = input_pemain()
    opsi_komputer = ["gunting", "batu", "kertas"]
    pilihan_unik = pilihan_pemain + str (len(nomor_ronde))
    indeks_acak = abs(hash(pilihan_unik)) % 3
    pilihan_komputer = opsi_komputer[indeks_acak]
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print(f"Pilihan pemain: {pilihan_pemain}")
    print(f"Pilihan Komputer: {pilihan_komputer}")
    print(f"hasil: {hasil}")

    point = 0
    if hasil == "Pemain menang +10 point, Komputer kalah 0 point":
        point = 10
    return [pilihan_pemain, pilihan_komputer, hasil, point]

#=== BAGIAN B ===
def tampilkan_riwayat(riwayat):
    """menampilkan riwayat permainan dalam bentuk tabel (matriks 2D)"""
    print ("=== RIWAYAT PERMAINAN ===") 

    if len (riwayat) == 0:
        print ("Masih belum ada riwayat permainan")
        return
    
    print (f"No. | {'PilihanPemain':<10} | {'PilihanKomputer':<10} | {'Hasil':<15} | {'point':<5}")
    print ("-" *50)

    nomor = 1
    for baris in riwayat:
        print (f"{nomor:<4} | {baris[0]:<10} | {baris[1]:<10} | {baris[2]:<15} | {baris[3]:<5}")
        nomor += 1

#=== BAGIAN C ===
def bubble_sort_riwayat(riwayat):
    """mengurutkan leaderboard berdasarkan score tertinggi menggunakan fungsi bubble sort"""
    DataSort = riwayat.copy()
    n = len (DataSort)

    for i in range(n):
        for j in range (0, n-i-1):
            if DataSort[j][1] < DataSort[j+1][1]:
                DataSort[j], DataSort[j+1] = DataSort[j+1], DataSort[j]
                
    return DataSort

def tampilkan_leaderboard(riwayat):
    """Menampilkan leaderboard"""
    print ("===== LEADERBOARD ======")
    urutan = bubble_sort_riwayat(riwayat)
    print (f"{'Rank':<3} | {'Nama':<15} | {'score':<10}")
    print ("=" *50)

    rank = 1
    for baris in urutan:
        nama = baris[0]
        score = baris[1]
        print (f"{rank:<3} | {nama:<15} | {score:<10}")
        rank += 1

#=== BAGIAN C ===
def main():
    """program utama untuk menjalankan kode program"""
    riwayat_ronde = []

    score_pemain = [
        ["Raziq", 90],
        ["Mufid", 100],
        ["Ayam", 20],
    ]

    nama = input ("Masukkan nama pemain: ")
    score_pemain.append ([nama, 0])

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Main")
        print("2. Lihat Riwayat Bermain")
        print("3. Lihat LeaderBoard")
        print("4. Keluar")

        pilihan = input ("Silahkan Memilih (1/2/3/4): ")

        if pilihan == "1":
            hasil = ronde(nama_pemain = nama, nomor_ronde = riwayat_ronde)
            riwayat_ronde.append (hasil)
            point = hasil[3]

            for baris in score_pemain:
                if baris[0] == nama:
                    baris[1] += point

        elif pilihan == "2":
            tampilkan_riwayat(riwayat_ronde)

        elif pilihan == "3":
            tampilkan_leaderboard(score_pemain)

        elif pilihan == "4":
            print ("Terimakasih telah bermain!👋")
            break
        else:
            print ("Pilihan tidak valid. Silahkan coba lagi!")
main()