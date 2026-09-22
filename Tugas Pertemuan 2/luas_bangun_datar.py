print("=== PROGRAM MENGHITUNG LUAS BANGUN DATAR ===")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")
print("5. Jajar Genjang")
print("6. Trapesium")
print("7. Belah Ketupat")
print("8. Layang-Layang")

pilihan = int(input("Pilih bangun datar (1-8): "))

if pilihan == 1:
    sisi = float(input("Masukkan sisi: "))
    luas = sisi * sisi
    print("Luas persegi =", luas)

elif pilihan == 2:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print("Luas persegi panjang =", luas)

elif pilihan == 3:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga =", luas)

elif pilihan == 4:
    jari_jari = float(input("Masukkan jari-jari: "))
    luas = 3.14 * jari_jari * jari_jari
    print("Luas lingkaran =", luas)

elif pilihan == 5:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = alas * tinggi
    print("Luas jajar genjang =", luas)

elif pilihan == 6:
    sisi1 = float(input("Masukkan sisi sejajar 1: "))
    sisi2 = float(input("Masukkan sisi sejajar 2: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * (sisi1 + sisi2) * tinggi
    print("Luas trapesium =", luas)

elif pilihan == 7:
    diagonal1 = float(input("Masukkan diagonal 1: "))
    diagonal2 = float(input("Masukkan diagonal 2: "))
    luas = 0.5 * diagonal1 * diagonal2
    print("Luas belah ketupat =", luas)

elif pilihan == 8:
    diagonal1 = float(input("Masukkan diagonal 1: "))
    diagonal2 = float(input("Masukkan diagonal 2: "))
    luas = 0.5 * diagonal1 * diagonal2
    print("Luas layang-layang =", luas)

else:
    print("Pilihan tidak tersedia")