import matplotlib.pyplot as plt

data = [
    ('bus', 5, 200),
    ('trem', 8, 150),
    ('kereta', 12, 300),
    ('minibus', 6, 180),
    ('tram', 9, 220),
]

jenis_kendaraan = [item[0] for item in data]
penggunaan_energi = [item[1] for item in data]
biaya_operasional = [item[2] for item in data]

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.bar(jenis_kendaraan, penggunaan_energi, color='blue')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Penggunaan Energi')
plt.title('Penggunaan Energi per Kendaraan')

plt.subplot(1, 3, 2)
plt.bar(jenis_kendaraan, biaya_operasional, color='green')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Biaya Operasional')
plt.title('Biaya Operasional per Kendaraan')

plt.subplot(1, 3, 3)
for i, label in enumerate(jenis_kendaraan):
    plt.scatter(penggunaan_energi[i], biaya_operasional[i], label=label)
    plt.text(penggunaan_energi[i], biaya_operasional[i], label)
plt.xlabel('Penggunaan Energi')
plt.ylabel('Biaya Operasional')
plt.title('Hubungan Energi dan Biaya Operasional')
plt.legend()

plt.tight_layout()
plt.show()
