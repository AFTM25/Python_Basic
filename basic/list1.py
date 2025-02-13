data_buah = ['jeruk', 'mangga', 'apel', 'nanas']
data_1    = data_buah.copy()
data_1[2] = 'stroberi'
print(f'Data buah = {data_buah}')
print(f'Data copy buah = {data_1}')

data_1.insert(2, 'nanas')
print(f'Data buah copy = {data_1}')

data_buah.append('delima')
data_buah.append('manggis')
print(f'Data buah = {data_buah}')

data_buah.remove('delima')
print(f'Data buah = {data_buah}')

data_buah.sort()
print(f'\nData buah setelah di sort = {data_buah}')
