def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if y != 0:
        return a / b
    else:
        return "Tidak bisa dibagi dengan nol"

def menu_tampilan():
    print("Pilih operasi yang diinginkan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")

while True:
    menu_tampilan()

    pilihan = input("Masukkan pilihan ([1] [2] [3] [4] [5]): ")

    if pilihan == '5':
        print("See you later!!")
        break

    x = int(input("Masukkan angka pertama: "))
    y = int(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print("Hasil pertambahan =", penjumlahan(x, y))
    elif pilihan == '2':
        print("Hasil Pengurangan =", pengurangan(x, y))
    elif pilihan == '3':
        print("Hasil Perkalian =", perkalian(x, y))
    elif pilihan == '4':
        if y != 0:
            print("Hasil pembagian =", pembagian(x, y))
        else:
            print("Tidak bisa dibagi dengan nol!")
    else:
        print("Invalid")
