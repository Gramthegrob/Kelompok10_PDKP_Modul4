from method import *

print("Selamat datang di Tugas program Kelompok 10")

def listBaju(): #fungsi list baju no return
    print("""
     -------------------------------------
    Simulasi harga total modal pakaian
    Persiapkan uang modal!
    Daftar list pakaian dan harga-nya :
    1 : Kaos Polo - Rp. 50.000
    2 : Kemeja - Rp. 80.000
    3 : Baju Batik - Rp. 65.000
    4 : Celana - Rp. 70.000
    5 : Rok - Rp. 55.000
    0 : Batal
    ------------------------------------
    """)


def opsiBaju(opsi): #fungsi opsi baju dengan return berparameter
    switcher={
        1: "Kaos polo - Rp. 50.000",
        2: "Kemeja - Rp. 80.000",
        3: "Baju Batik - Rp. 65.000",
        4: "Celana - Rp. 70.000",
        5: "Rok - Rp. 55.000",
        0: "Batal",
        }
    return switcher.get(opsi, "Kode tersebut salah")


def hargaBaju(opsi): #fungsi harga baju dengan return berparameter
    if opsi == int(1):
        harga = int(50000)
        return harga
    elif opsi == 2:
        harga = int(80000)
        return harga
    elif opsi == 3:
        harga = int(65000)
        return harga
    elif opsi == 4:
        harga = int(70000)
        return harga
    elif opsi == 5:
        harga = int(55000)
        return harga
    else:
        print("Opsi anda salah! ")


def totalModal():
    global total 
    total = 0
    while True:
        listBaju()
        a = int(input("Masukkan kode baju : "))
        if a == 0:
            print("Anda membatalkan program.")
            break
        print(opsiBaju(a))
        list = [opsiBaju(a)]
        q = int(input("Masukkan kuantitas baju : "))
        totalAwal = hargaBaju(a) * q
        total = total + totalAwal
        print("Total harga modal baju : ", total)
        while True:
            lanjut = input("Apakah anda masih ingin menambahkan baju lagi? : (1. Iya/ 0. Tidak) : ")
            if lanjut == '1':
                break
            elif lanjut == '0':
                print("Total harga modal baju : " , total)
                print("Program selesai.")
                break
            else:
                print("Pilihan anda salah, silahkan masukkan angka 1 atau 0.")
                continue

        if lanjut == '0':
            break

    return total
