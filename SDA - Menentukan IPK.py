nilai_angka = {'A' : 4, 'B' : 3.5, 'B' : 3, 'C+' : 2.5, 'C' : 2, 'D+' : 1.5, 'D' : 1, 'E':0}
nilai_angka_list = []

while True :
  huruf_mutu = input("Masukan Huruf mutu = ")
  if huruf_mutu.lower() == 'selesai' :
    break
  elif huruf_mutu not in niali_angka :
    print ("Tidak Valid")
  else : 
    nilai_angka_list.append(nilai_angka[huruf_mutu])

if len(nilai_angka_list) > 0 :
  ipk = sum(nilai_angka_list) / len(nilai_angka_list)
  print("IPK anda adalah : ", round(ipk, 2))
  
else :
  print("Anda belum memasukan nilai untuk dihitung IPK.")
