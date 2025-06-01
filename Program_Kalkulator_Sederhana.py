
VariabelMulai = True

def FungsiPertambahan(Angka1,Angka2):
    return Angka1 + Angka2

def FungsiPengurangan(Angka1,Angka2):
    return Angka1 - Angka2

def FungsiPerkalian(Angka1,Angka2):
    return Angka1 * Angka2

def FungsiPembagian(Angka1,Angka2):
    return Angka1 / Angka2

def FungsiKuadrat(Angka3):
    return Angka3**2

while(VariabelMulai):
    print("Kalkulator Sederhana")
    print("--------------------")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Kuadrat")
    print("6. Keluar ")

    pilihanmenu = int(input("Masukkan Menu Pilihan (dalam angka, contoh : 1) : "))
    

    if pilihanmenu == 1 :
        Angka1 = float(input("Masukkan Angka Pertama : "))
        Angka2 = float(input("Masukkan Angka Kedua : "))
        print(Angka1, " + ",Angka2, " = ", FungsiPertambahan(Angka1,Angka2))
    elif pilihanmenu == 2 :
        Angka1 = float(input("Masukkan Angka Pertama : "))
        Angka2 = float(input("Masukkan Angka Kedua : "))
        print(Angka1, " - ",Angka2, " = ", FungsiPengurangan(Angka1,Angka2))
    elif pilihanmenu == 3 :
        Angka1 = float(input("Masukkan Angka Pertama : "))
        Angka2 = float(input("Masukkan Angka Kedua : "))
        print(Angka1, " x ",Angka2, " = ", FungsiPerkalian(Angka1,Angka2))
    elif pilihanmenu == 4 :
        Angka1 = float(input("Masukkan Angka Pertama : "))
        Angka2 = float(input("Masukkan Angka Kedua : "))
        print(Angka1, " : ",Angka2, " = ", FungsiPembagian(Angka1,Angka2))
    elif pilihanmenu == 5 :
        Angka3 = float(input("Masukkan Angka Yang ingin Dikuadratkan : "))
        print(Angka3, " ^2 ", " = ", FungsiKuadrat(Angka3))
    elif pilihanmenu == 6 :
        print("Terima Kasih")
        VariabelMulai = False
    else : 
        print("Mohon Masukkan Pilihan Sesuai Format")
