print("\nGenerator Expression")
def generate_angka_ganjil():
    for angka in range(51):
        if angka % 2 != 0:
            yield angka

for angka in generate_angka_ganjil():
    
    print(angka, end=' ')

