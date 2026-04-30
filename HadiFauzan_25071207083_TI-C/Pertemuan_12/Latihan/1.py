struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
    "README.txt": 8
    }
}

def total_ukuran(folder : dict) -> int:
    total = 0
    for nama, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        elif isinstance(value, int):
            total += value
    return total

def hitung_file(folder : dict) -> int:
    total = 0
    for nama, value in folder.items():
        if isinstance(value, dict):
            total += hitung_file(value)
        elif isinstance(value, int):
            total += 1
    return total

def cari_terbesar(folder : dict) -> tuple:
    max_nama = ""
    max_size = 0
    for nama, value in folder.items():
        if isinstance(value, dict):
            file, size = cari_terbesar(value)            
            if size > max_size:
                max_nama = file
                max_size = size
            elif isinstance (value, int):
                if value > max_size:
                    max_nama = nama
                    max_size = value
        return (max_nama, max_size)
    
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    for key, value in folder.items():
        indentasi = "  " * level 
        
        if isinstance(value, int):
            print(f"{indentasi}📄{key} ({value} KB)")
        
        elif isinstance(value, dict):
            print(f"{indentasi}📁{key}")
            tampilkan_tree(value, nama=key, level=level + 1)

tampilkan_tree(struktur)