import datetime

def registrasi_biodata():
    print("=" * 40)
    print("      FORMULIR REGISTRASI BIODATA")
    print("=" * 40)
    
    # 1. Mengambil Input dari Pengguna
    nama = input("Masukkan Nama Lengkap     : ").strip()
    panggilan = input("Masukkan Nama Panggilan   : ").strip()
    ttl = input("Tempat, Tanggal Lahir     : ").strip()
    jk = input("Jenis Kelamin (L/P)       : ").strip().upper()
    alamat = input("Masukkan Alamat           : ").strip()
    telepon = input("No. HP / WhatsApp         : ").strip()
    email = input("Alamat Email              : ").strip()
    hobi = input("Hobi Anda                 : ").strip()
    cita = input("Cita-cita                 : ").strip()

    # Menyesuaikan tampilan jenis kelamin
    jenis_kelamin = "Laki-laki" if jk == "L" else "Perempuan" if jk == "P" else "Tidak diisi"

    # Tanggal hari ini
    tgl_reg = datetime.date.today().strftime("%d-%m-%Y")

    # 2. Menyimpan data ke dalam Dictionary
    data_biodata = {
        "tgl_reg": tgl_reg,
        "nama": nama if nama else "-",
        "panggilan": panggilan if panggilan else "-",
        "ttl": ttl if ttl else "-",
        "jk": jenis_kelamin,
        "alamat": alamat if alamat else "-",
        "telepon": telepon if telepon else "-",
        "email": email if email else "-",
        "hobi": hobi if hobi else "-",
        "cita": cita if cita else "-"
    }
    
    return data_biodata


def tampilkan_biodata(data):
    """Fungsi untuk menampilkan biodata ke terminal"""
    print("\n" + "=" * 50)
    print("                HASIL BIODATA PENGGUNA")
    print("=" * 50)
    print(f" Tanggal Dibuat   : {data['tgl_reg']}")
    print("-" * 50)
    print(f" Nama Lengkap     : {data['nama']}")
    print(f" Nama Panggilan   : {data['panggilan']}")
    print(f" Tempat, Tgl Lahir: {data['ttl']}")
    print(f" Jenis Kelamin    : {data['jk']}")
    print(f" Alamat           : {data['alamat']}")
    print(f" No. HP / WA      : {data['telepon']}")
    print(f" Email            : {data['email']}")
    print(f" Hobi             : {data['hobi']}")
    print(f" Cita-cita        : {data['cita']}")
    print("=" * 50)
    print(" ✨ Terima kasih telah mengisi formulir biodata! ✨")
    print("=" * 50)


# --- Program Utama ---
if __name__ == "__main__":
    # Jalankan form registrasi di terminal
    hasil = registrasi_biodata()
    
    # Tampilkan hasilnya kembali ke terminal
    tampilkan_biodata(hasil)