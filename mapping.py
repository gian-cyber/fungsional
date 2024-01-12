data_prima = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def tambah_info(n):
    return (n, n**2)

data_dengan_info = list(map(tambah_info, data_prima))

print(data_dengan_info)
