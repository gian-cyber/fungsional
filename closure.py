def hitung_pangkat(basis):
    def pangkatkan(pangkat):
        return basis ** pangkat
    return pangkatkan

pangkat_dua = hitung_pangkat(2)
pangkat_tiga = hitung_pangkat(3)

print(pangkat_dua(5))  
print(pangkat_tiga(4)) 
