barang_harga = ("Pensil", 1500, "Buku", 5000, "Penggaris", 2000)

def pisahkan_data(tuple_data):
    nama_barang = list(filter(lambda x: isinstance(x, str), tuple_data))
    harga_barang = list(filter(lambda x: isinstance(x, int), tuple_data))
    return nama_barang, harga_barang

def gabungkan_ke_dictionary(nama_barang, harga_barang):
    return dict(zip(nama_barang, harga_barang))

nama_barang, harga_barang = pisahkan_data(barang_harga)
barang_dict = gabungkan_ke_dictionary(nama_barang, harga_barang)

print(barang_harga)
print(nama_barang)
print(harga_barang)
print(barang_dict)
