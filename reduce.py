from functools import reduce

data_angka = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] #saya menggunakan angka soal 8.2

def jumlahkan(x, y):
    return x + y

hasil_jumlah = reduce(jumlahkan, data_angka)

print(hasil_jumlah)
