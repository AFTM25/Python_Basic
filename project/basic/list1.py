data_buah = ['jeruk', 'mangga', 'apel', 'nanas']
data_1    = data_buah.copy()
data_1[2] = 'stroberi'
print(f'Data buah = {data_buah}')
print(f'Data copy buah = {data_1}')

data_1.insert(2, 'nanas')
for x, y in enumerate(data_1):
    print(f'{x+1}.{y}')

