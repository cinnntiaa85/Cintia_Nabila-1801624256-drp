from datetime import datetime

print('=== Aplikasi Manajemen Aktivitas ===')

aktivitas = input('Masukkan aktivitas: ')
aktivitas = aktivitas.lower()

if aktivitas == 'sarapan':

    print('Menu tersedia: sushi, pizza, burger, sosis')

    menu = input('Masukkan menu sarapan: ')
    menu = menu.lower()

    if menu == 'sushi' or menu == 'pizza' or menu == 'burger':
        print('Bahan tersedia, silakan dimasak terlebih dahulu')
        print('Selamat menikmati sarapanmu!')

    elif menu == 'sosis':
        print('Menu dapat langsung dipanaskan dan disajikan')

    else:
        print('Bahan tidak tersedia, silakan membeli terlebih dahulu')

elif aktivitas == 'kerja':

    waktu_sekarang = datetime.now()

    jam = waktu_sekarang.hour
    menit = waktu_sekarang.minute

    print('Waktu sekarang:', jam, ':', menit)

    if jam > 8 or (jam == 8 and menit > 0):
        print('Anda terlambat masuk kerja')

    else:
        print('Anda belum terlambat masuk kerja')
        print('Semangat bekerja hari ini!')

else:
    print('Aktivitas tidak tersedia')