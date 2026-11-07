# Dina Shafa Laura 2601098
# Latihan 1 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("pass")
    elif i % 3 == 0:
        print("kelipatan 3")
    elif i % 5 == 0:
        print("kelipatan 5")
    else:
        print(i)


#Latihan 2
n = int(input("Masukkan jumlah hewan yang akan diinput: "))
hewan = []

for i in range(n):
    nama = input(f"Masukkan nama hewan ke-{i + 1}: ")
    hewan.append(nama)

print("\nDaftar nama hewan:")

for i in range(n):
    print(f"{i + 1}. {hewan[i]}")

print("Jumlah hewan yang diinput:", len(hewan))

# Dina Shafa Laura 2601098
#Latihan 3 
n = int(input("masukkan jumlah bilangan yang akan diinput : "))
bilangan = []
for i in range(n):
    angka = int(input(f"Bilangan ke-{i + 1} : "))
    bilangan.append(angka)

for i in range(n):
    if bilangan[i] % 2 == 0:
        print(f"Bilangan {bilangan[i]} adalah genap")
    else:
        print(f"Bilangan {bilangan[i]} adalah ganjil")

# Dina Shafa Laura 2601098
#Latihan 4 
for i in range(1, 81):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

# Dina Shafa Laura 2601098
#Latihan 5 
while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == "dasproRPL" and password == "RPLfire!123":
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah!")