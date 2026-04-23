#A
def pemenang (pemain, lawan):
    """menentukan pemenang""" #Docstring
    if pemain == lawan:
        return "Seri"
    elif (pemain == "gunting" and lawan == "kertas") or (pemain == "kertas" and lawan == "batu") or (pemain == "batu" and lawan == "gunting"):
        return "pemain menang"
    else:
        return "lawan menang"
    
def input_pemain():
    """meminta input pilihan pemain yang valid (sengaja menggunakan lower agar komputer tidak salah baca)"""
    opsi = ["batu", "gunting", "kertas"]

    while True:
        pemain = input ("Masukkan pilihan (batu, gunting, kertas): ").lower()
        if pemain in opsi:
            return pemain
        else:
            print ("Pilihan tidak valid. Silahkan dicoba lagi!")

def ronde (nama_pemain, nomor_ronde):
    """melakukan 1 ronde permainan serta menentukan pemenang, kalah, atau seri"""
    pilihan_pemain = input_pemain()
    opsi_lawan = ["batu", "gunting", "kertas"]
    tks_unik = pilihan_pemain + str (len(nomor_ronde))
    indeks_acak = abs(hash(tks_unik)) % 3
    pilihan_lawan = opsi_lawan[indeks_acak] 
    hasil = pemenang(pilihan_pemain, pilihan_lawan)
    print (f"Pilihan pemain: {pilihan_pemain}")
    print (f"pilihan lawan: {pilihan_lawan}")
    print (f"hasil: {hasil}")

    point = 0
    if hasil == "pemain menang":
        point = 10
    elif hasil == "Seri":
        point = 5
    return [pilihan_pemain, pilihan_lawan, hasil, point]

#B
def tampilkan_riwayat (matrix):
    """menampilkan riwayat permainan dalam bentuk tabel"""
    print ("Riwayat Permainan: ")

    if len (matrix) == 0:
        print ("masih belum ada riwayat permainan")
        return
    
    print (f"No. | {'pemain':<10} | {'lawan':<10} | {'hasil':<15} | {'point':<5}")
    print ("-" *30)

    nomor = 1
    for baris in matrix:
        print (f"{nomor:<4} | {baris[0]:<10} | {baris[1]:<10} | {baris[2]:<15} | {baris[3]:<5}")
        nomor += 1
#C
def bubble_score (leaderboard):
    """mengurutkan leaderboard berdasarkan skor menggunakan fungsi bubble sort"""
    DataSort = leaderboard.copy()
    n = len (DataSort)

    for i in range (n):
        for j in range (0, n-i-1):
            if DataSort[j][1] < DataSort[j+1][1]:
                DataSort[j], DataSort[j+1] = DataSort[j+1], DataSort[j]

    return DataSort

def score_leaderboard (leaderboard):
    """Menampilkan Leaderboard berdasarkan skor"""
    print ("+++=== LEADERBOARD ===+++")
    urutan = bubble_score(leaderboard)
    print (f"{'Rank':<3} | {'Nama':<15} | {'score':<10}")
    print ("-" *30)

    rank = 1
    for baris in urutan:
        nama = baris[0]
        score = baris[1]
        print (f"{rank:<3} | {nama:<15} | {score:<10}")
        rank += 1

#Utama
def clear_screen():
    """membersihkan layar terminal (biar rapi aja)"""
    print ("\n" *50)


def main ():
    """Program utama untuk menjalankan permainan"""
    riwayat_ronde = []

    score_pemain = [
        ["Alice", 100],
        ["Bob", 85],
        ["Charlie", 50]
    ]

    nama = input ("Masukkan nama pemain: ")

    score_pemain.append ([nama, 0])

    while True:
        
        print ("\n=== MAIN MENU ===")
        print ("1. Main 1 Ronde")
        print ("2. Lihat Riwayat Ronde")
        print ("3. Lihat Leaderboard")
        print ("4. Keluar")

        pilihan = input ("pilih menu 1-4: ")

        if pilihan == "1":
            clear_screen()
            hasil_ronde = ronde(nama_pemain=nama, nomor_ronde = riwayat_ronde)
            riwayat_ronde.append (hasil_ronde)
            point = hasil_ronde[3]

            for baris in score_pemain:
                if baris[0] == nama:
                    baris[1] += point
        
        elif pilihan == "2":
            clear_screen()
            tampilkan_riwayat(riwayat_ronde)

        elif pilihan == "3":
            clear_screen()
            score_leaderboard(score_pemain)
        
        elif pilihan == "4":
            clear_screen()
            print ("Terima kasih sudah bermain!")
            break
        else:
            print ("pilihan tidak valid. Silahkan coba lagi!")
main()