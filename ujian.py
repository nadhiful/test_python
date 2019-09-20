#!/bin/bash

stop = False
i = 0


while (not stop):
	q = input("Ketikkan perintah Anda : " )
	if q == 'init':
		a = input("Masukkan angka : ")
		if a.isdigit():
			z = int(a)
			if z <= 0:
				print("Angka anda tidak valid")
				pass
			else:
				row = z
				column = 3 
				matrix = []
				w = input("Masukkan entry")
				for i in range(row):
					e = []
					for j in range(column):
						e.append(w)
						pass
					matrix.append(e)	
					pass
				for i in range(row):
					for j in range(column):
						print(matrix[i][j], end = " ")
						print()
						pass
					pass

				
				#print("Ini baris ", row)
				
			
		else:
			print("Angka anda tidak valid")
			pass
		
			pass
		pass

	pass

	tanya = input("Sudah selesai mengunakan program ? y/t : ")
	if (tanya == "y"):
		stop = True
		pass
