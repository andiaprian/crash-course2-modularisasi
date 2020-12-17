from geometry.persegipanjang import hitung_luas_persegi_panjang, info as info_persegi_panjang, info
from geometry.segitiga import hitung_luas_segitiga, info as info_segitiga

#memanggil package alt + enter
print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(10, 30)}')

print(info_persegi_panjang())
print(f'hitung_luas_segitiga {hitung_luas_persegi_panjang(10, 30)}') #cara copy paste cmd + D

#cara kedua
import geometry.segitiga as gs
print(f'\nCara kedua menghitung_luas_segitiga {gs.hitung_luas_segitiga(10, 30)}')