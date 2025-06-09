#Program Cek Angka


datalist = []

JumlahElemenInput = int(input("Masukkan Jumlah Elemen : "))

for i in range(JumlahElemenInput):
    data = int(input(f"input elemen ke {i+1}: "))
    datalist.append(data)

print(f"List yang kamu buat : {datalist}")

Mulai = True

while(Mulai):
    print("""
            Menu Aplikasi
        1. Panjang List
        2. Nilai Terkecil List
        3. Nilai Terbesar List
        4. Penjumlahan Isi List
        5. Urutan Naik
        6. Urutan Turun
        7. Balik Urutan List
        8. Keluar
          
          """)
    pilihan = int(input("Masukkan Pilihan Anda (dalam angka) : "))

    if pilihan == 1:
        x = len(datalist)
        print(f"Data Awal = {datalist}, Panjang List = {x}")

    elif pilihan == 2:
        x = min(datalist)
        print(f"Data Awal = {datalist}, List Terkecil = {x}")

    elif pilihan ==3:
        x = max(datalist)
        print(f"Data Awal = {datalist}, List Terbesar = {x}")

    elif pilihan ==4:
        x = max(datalist)
        print(f"Data Awal = {datalist}, Penjumlahan Total Isi List = {x}")

    elif pilihan ==5:
        x = datalist.sort()
        print(f"Data Awal = {datalist}, Urutan List Naik = {x}")

    elif pilihan ==6:
        x = datalist.sort(reverse=True)
        print(f"Data Awal = {datalist}, Urutan List Turun = {x}")

    elif pilihan ==7:
        x = datalist.reverse()
        print(f"Data Awal = {datalist}, Data Awal Dibalik = {x}")

    elif pilihan == 8:
        print("Bye")
        mulai = False

    else:
        print("Masukkan Angka dgn Benar Woiiii")