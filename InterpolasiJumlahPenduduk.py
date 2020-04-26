# fungsi validasi
def inputNumber(inputUser):
    while True:
        try:
            userInput = float(input(inputUser))
        except ValueError:
            print("Inputan Harus Angka")
            continue
        else:
            return userInput
            break
 
print("===================================================")
print("              Prediksi Jumlah Penduduk             ")
print("         menggunakan interpolasi kuadratik         ")
print("===================================================")
print("")
print("")
thn = []
jml = []
pers = []
for i in range(3):
     thn.append(inputNumber("Masukkan Tahun ("+str(i+1)+") : "))
     jml.append(inputNumber("Masukkan Jumlah Penduduk ("+str(i+1)+") : "))
thnCari = inputNumber("Masukan tahun yang dicari : ")
# sort by year
for i in range(3):
    for j in range(3-i):
        if(thn[j] > thn[j-1]) :
            tempThn = thn[j]
            tempJml = jml[j]
            thn[j] = thn[j+1]
            jml[j] = jml[j+1]
            thn[j+1] = tempThn
            jml[j+1] = tempJml

pers1 = ((thnCari-thn[1])*(thnCari-thn[2]))/((thn[0]-thn[1])*(thn[0]-thn[2]))
pers2 = ((thnCari-thn[0])*(thnCari-thn[2]))/((thn[1]-thn[0])*(thn[1]-thn[2]))
pers3 = ((thnCari-thn[0])*(thnCari-thn[1]))/((thn[2]-thn[0])*(thn[2]-thn[1]))
    
hasil = (jml[0]*pers1)+(jml[1]*pers2)+(jml[2]*pers3)

for i in range(3):
    print("Tahun "+str(int(thn[i]))+" Jumlah Penduduk "+str(int(jml[i])))
print("===================================================")
print("Jumlah penduduk pada tahun "+str(int(thnCari))+" Adalah "+str(round(hasil,1)))
