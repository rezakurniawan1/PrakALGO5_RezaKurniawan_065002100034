print("- - - D E R E T  F I B O N A C C I - - -")

jumlah = int(input("Masukkan jumlah bilangan\t: "))
angka1 = int(input("Masukkan bilangan pertama\t: "))
angka2 = int(input("Masukkan bilangan kedua\t\t: "))

count = 2

print(f"{angka1}\n{angka2}")

while count < jumlah:
	fibo = angka1 + angka2
	print(fibo)
	
	angka1 = angka2
	angka2 = fibo

	count += 1