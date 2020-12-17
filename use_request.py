import requests

#Kalau berhasil
url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success!, Response = {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Whoops, ada kesalahan requests {response.status_code}')
    #print(f'Success!', {response}) --> bisa menggunakan cara ini
except Exception as e:
    print('There is an error', e)
print('Program Ended')

#kalau gagal
url = 'https://deti k.com'
try:
    response = requests.get(url)
    print('Success!', response)
except Exception as e:
    print('\nThere is an error', e)
print('Program Ended')