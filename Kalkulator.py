A = float(input("A = "))
B = float(input("B = "))
C = int(input("(1=Tambah 2=Kurang 3=kali 4=bagi) Operasi = "))

if C == 1 :
    print(A+B)
elif C == 2 :
    print(A-B)
elif C == 3 :
    print(A*B)
elif C == 4 :
    if B == 0 :
        print("Tidak bisa dibagi 0")
        exit(1)
    print(A/B)
else :
    print("salah input") 

