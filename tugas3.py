#1
#membuat dictionary orang
orang = [
    {'nama': 'Arsene Lupin', 'nik': 1234, 'jenis_kelamin': 'male', 'tanggal_lahir': '1902-03-23'},
    {'nama': 'Sherlock Holmes', 'nik': 4321, 'jenis_kelamin': 'male', 'tanggal_lahir': '1876-08-16'},
    {'nama': 'Irene Adler', 'nik': 6789, 'jenis_kelamin': 'female', 'tanggal_lahir': '1884-10-07'}
]

#2
# menerima input dari user
nama_dicari = input("Masukkan nama yang ingin dicari: ")

#3
# melakukan pencarian berdasarkan nama
for data in orang:
    if data['nama'].lower() == nama_dicari.lower():
        print(f"Data ditemukan:")
        print(f"Nama: {data['nama']}")
        print(f"NIK: {data['nik']}")
        print(f"Jenis kelamin: {data['jenis_kelamin']}")
        print(f"Tanggal lahir: {data['tanggal_lahir']}")
        break
else:
    print("Data tidak ada")
