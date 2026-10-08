#identitas
print("Pemprograman Faktorisasi Bilangan" )
print("Nama : Muhammad Syalwan Fachrezy")
print("NIM : 1306625096")
print()

#program
while True:
    hasil =[]
    n = int(input("Masukkan Bilangan <100 (selesai = 0)"))
    if n == 0:
        break
    for i in range(1, n+1):
        if n % i == 0:
            hasil.append(i)
    print("Bilangan" , n, "Faktornya = ", hasil)
print("Selesai")
