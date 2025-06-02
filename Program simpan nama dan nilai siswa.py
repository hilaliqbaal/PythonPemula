
print("Program List Nilai Kelas 10-1")

#untuk menyimpan data final
list_final = [] 
#untuk memulai while
MulaiProgram = True

#fungsi untuk melakukan penambahan data
def MenambahDataNilai():
    Xmulai = True
    while(Xmulai):
        Keluar = int(input("Apakah anda ingin keluar? 1. Ya, 2. Tidak, masukkan angka saja : "))
        if Keluar == 2:
            NamaSiswa = input("Masukkan Nama Siswa : ")
            NilaiSiswa= float(input("Masukkan Nilai Siswa : "))
            databaru = [NamaSiswa,NilaiSiswa]
            list_final.append(databaru)
            return databaru
        elif Keluar == 1:
            ucapan = "Terima Kasih"
            print(ucapan)
            Xmulai = False
        else:
            print("Mohon Masukkan Format Yang Benar, 1/2")
    return None



while(MulaiProgram):
    print("""
         -----Menu-----
        1. Menambah Data Nilai
        2. Menghapus Data Nilai
        3. Menampilkan Data Nilai 
        4. Keluar Program
          """)
    
    InputPilihan = int(input("Masukkan Pilihan Menu, contoh = 1 : "))

    if InputPilihan == 1:
        print("Masukkan Data dengan format nama,nilai")
        MenambahDataNilai()
        
    elif InputPilihan == 2:
        if len(list_final) == 0:
            print("Belum ada data yang bisa dihapus.")
        else:
             print("Data saat ini:")
        for peserta in list_final:
            print(f"Nama Siswa: {peserta[0]}  Nilai Siswa: {peserta[1]}")

        NamaygDihapus = input("Masukkan Nama yang ingin Anda hapus: ")

        # Cek apakah ada data yang cocok
        ditemukan = False
        for data in list_final:
            if data[0].lower() == NamaygDihapus.lower():
                list_final.remove(data)
                print(f"Data untuk {NamaygDihapus} berhasil dihapus.")
                ditemukan = True
                break  # Keluar dari loop setelah menghapus
        if not ditemukan:
            print("Nama tidak ditemukan dalam daftar.")

    elif InputPilihan == 3:
        for peserta in list_final:
            print(f"Nama Siswa {peserta[0]}  Nilai Siswa {peserta[1]}")       
     
    else:
        print("Halo")