#program untuk melakukan print dengan for 
jumlah_perulangan = 3 
for index in range (jumlah_perulangan):
    print (f"Print ke- {index}")

for i in range (1,6):
    print(i)

for i in "Python":
    print(f"Huruf : {i}")

for i in range(10):
    print(f"Nilai ke-{1}")

for i in range(2, 11, 2):
    print(f"Nilai ke-{1}")

#Program untuk melakukan print dengan while 
angka = 0
while(angka < 8):
    print(f"Angka Sekarang: {angka}")
    angka += 1

#Fungsi Break (untuk menghentikan suatu looping)
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)
    if i == 3:
        break

#Fungsi Continue (untuk menghentikan sementara)
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)
    if i == 3:
       continue
    print(i) 

#Range 

#Nested



