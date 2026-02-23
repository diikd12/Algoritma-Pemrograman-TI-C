def hitung_patungan():
    print ("Program Bagi Tagihan")
    try:
        total_belanja = float(input("masukkan total belanja (Rp): "))
        jumlah_orang = int(input("masukkan jumlah orang: "))
        tagihan_perorang = total_belanja / jumlah_orang
    
    except ValueError:
        print("ERROR: Mohon masukkan angka yang valid!")
    except ZeroDivisionError:
        print ("ERROR: Jumlah orang tidak boleh 0!")
    except Exception as e:
        print (f"Terjadi kesalahan tidak terduga: {e}")
    else:
        print (f"Setiap orang harus membayar: RP {tagihan_perorang:,.2f}")
    finally:
        print("Terima kasih telah mencoba untuk menggunakan program ini")
hitung_patungan()