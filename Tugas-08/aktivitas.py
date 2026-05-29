
user = input("Siapa nama Anda? ")

print(f"\n1. PAPAN CATUR INPUT AKTIVITAS {user}")

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n2. DAFTAR AKTIVITAS {user}")

daftar_aktivitas = []

jumlah_aktivitas = int(input("Berapa banyak aktivitas yang ingin Anda tambahkan? "))

for i in range(jumlah_aktivitas):

    print(f"\n🌸 Aktivitas ke-{i+1} 🌸")

    nama_aktivitas = input("Nama aktivitas: ")
    waktu_aktivitas = input("Waktu aktivitas: ")
    tempat_aktivitas = input("Tempat aktivitas: ")

    # PILIH KATEGORI
    print("\nPilih kategori aktivitas:")
    print("1. Kuliah 📚")
    print("2. Me Time 💕")
    print("3. Game 🎮")
    print("4. Organisasi 🫂")

    pilihan = input("Masukkan pilihan kategori (1-4): ")

    if pilihan == "1":
        kategori = "Kuliah 📚"

    elif pilihan == "2":
        kategori = "Me Time 💕"

    elif pilihan == "3":
        kategori = "Game 🎮"

    elif pilihan == "4":
        kategori = "Organisasi 🫂"

    else:
        kategori = "Lainnya ✨"

    # IMPROVISASI PRIORITAS
    print("\nSeberapa penting aktivitas ini?")
    print("1. Penting banget 😵‍💫")
    print("2. Biasa aja 😌")
    print("3. Santai dulu 💤")

    prioritas_pilihan = input("Masukkan pilihan (1-3): ")

    if prioritas_pilihan == "1":
        prioritas = "Penting banget 😵‍💫"

    elif prioritas_pilihan == "2":
        prioritas = "Biasa aja 😌"

    elif prioritas_pilihan == "3":
        prioritas = "Santai dulu 💤"

    else:
        prioritas = "Tidak diketahui"

    # STATUS AKTIVITAS
    status_input = input("Status (Selesai/Belum Selesai): ")

    if status_input.lower() == "selesai":
        status = "Selesai ✅"

    else:
        status = "Belum selesai ⏳"

    # MENYIMPAN DATA
    aktivitas = {
        "aktivitas": nama_aktivitas,
        "waktu": waktu_aktivitas,
        "tempat": tempat_aktivitas,
        "kategori": kategori,
        "prioritas": prioritas,
        "status": status
    }

    daftar_aktivitas.append(aktivitas)

# OUTPUT HASIL
print("\n" + "=" * 50)
print(f"🌸 DAFTAR AKTIVITAS {user} 🌸")
print("=" * 50)

for i in range(len(daftar_aktivitas)):

    print(f"\n✨ AKTIVITAS {i+1} ✨")
    print(f"Nama Aktivitas : {daftar_aktivitas[i]['aktivitas']}")
    print(f"Waktu          : {daftar_aktivitas[i]['waktu']}")
    print(f"Tempat         : {daftar_aktivitas[i]['tempat']}")
    print(f"Kategori       : {daftar_aktivitas[i]['kategori']}")
    print(f"Prioritas      : {daftar_aktivitas[i]['prioritas']}")
    print(f"Status         : {daftar_aktivitas[i]['status']}")

# PENUTUP
print("\n" + "=" * 50)
print("🌙 AKTIVITAS HARI INI TELAH TERSIMPAN 🌙")
print("=" * 50)

print(f"📖 Semua aktivitas milik {user} sudah berhasil disimpan.")
print("🌸 Tetap semangat menjalani hari-harimu 🌸")
print("💗 See you on your next activity! 💗")