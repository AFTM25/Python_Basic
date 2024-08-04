list_A = []
while True:
    user = int(input('Masukkan Angka Berupa Bilangan Bulat : '))
    list_A.extend([user])

    if input('Lanjut ? ') == 'n':
        print('Data Angka = ', list_A)
        total = 0
        for bilangan in list_A:
            total += bilangan

        print('Panjang Item = ', len(list_A), 'item')
        print('Jumlah Item = ', total)
        break
