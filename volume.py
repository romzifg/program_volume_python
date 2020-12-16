import math

print("Program Menghitung Volume")

def vbalok():
    print("Menghitung Volume Balok")
    p = float(input("Panjang = "))
    l = float(input("Lebar = "))
    t = float(input("Tinggi = "))

    v = p*l*t
    print ("volume Balok = %0.2f" %v)


def vkubus():
    print("Menghitung Volume Kubus")
    s = float(input("Sisi = "))
    
    v = s*s*s
    print ("volume Kubus = %0.2f" %v)

def vtabung():
    print("Menghitung Volume Tabung")
    r = float(input("Jari-Jari = "))
    t = float(input("Tinggi = "))

    v = math.pi * (r**2) * t

    print ("volume Tabung = %0.2f" %v)

def vkerucut():
    print("Menghitung Volume Kerucut")
    r = float(input("Jari-Jari = "))
    t = float(input("Tinggi = "))

    v = 0.33 * math.pi * (r**2) * t

    print ("volume Kerucut = %0.2f" %v)

def pengulangan():
    a = input("Apakah anda ingin mencoba lagi ? (y/n) ")
    if a == 'y':
        menu()
    elif a == 'n':
        print("Program Selesai")

def menu():
    print("1 untuk menghitung Volume Balok")
    print("2 untuk menghitung Volume Kubus")
    print("3 untuk menghitung Volume Tabung")
    print("4 untuk menghitung Volume Kerucut")

    n = int(input("Masukan Nilai = "))
   
    if n == 1:
        vbalok()
        pengulangan()
    elif n == 2:
        vkubus()
        pengulangan()
    elif n == 3:
        vtabung()
        pengulangan()
    elif n == 4:
        vkerucut()
        pengulangan()
    else:
        print("nilai yang anda masukan salah")
        pengulangan()
        
menu()