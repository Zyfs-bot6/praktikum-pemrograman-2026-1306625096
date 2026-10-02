print ("Pemprograman Konversi Suhu" )
print ("Muhammad Syalwan Fachrezy" )       
print ("1306625096" )
print()


x = int(input("suhu_awal"))
y = int(input("suhu_akhir"))
z = int(input("selang"))
print()

print("TABEL KONVERSI")
print('=' * 66)
print("|{0:^5}{1:^15}{2:^15}{3:^15}".format("No", "Celcius", "Reamur", "Fahrenheit"))
print('=' * 66)

n=1
while (x <= y):
    C =round(x,3)
    R = round (x*4/5,3)
    F = round (x*9/5+32,3)
    print("|{0:^5}{1:^15}{2:^15}{3:^15}".format(n, C, R, F))
    n=n+1
    x=x+z

print('=' * 66)

print()
print("selesai")

