from statistics import mean

list_data = [11, 67, 55, 34, 90, 23, 83, 45]
print('Data sekarang: ', list_data)

# operasi statistik
nilai_terkecil = min(list_data)
print('Data terkecil: ', nilai_terkecil)

nilai_terbesar = max(list_data)
print('Data terbesar: ', nilai_terbesar)

nilai_rata_rata = mean(list_data)
print('Rata-rata: ', nilai_rata_rata)


# Pencarian Data
cari = int(input("Masukkan Angka Yang Anda Cari : "))

#fungsi
def searchNumber(List, search):
    counter = 0
    result = 0
    while counter != len(list_data):
        if list_data[counter] == search:
            result = counter
        counter += 1
    return result

#pemangilan Fungsi
hasil = searchNumber(list_data, cari)

if cari not in list_data:
    print("Angka tidak ditemukan !!!")
else:
    print('Angka %s berada di index %s'% (cari, hasil))

#edit list data
print('---------------------------------')
print('            EDIT DATA            ')
print(list_data)
print('---------------------------------')

x = int(input('Masukan no index yang mau diedit : '))

list_data[x] = int(input('Masukan nilai pengubah : '))

print(list_data)
