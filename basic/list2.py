nama1 = input('Masukkan Nama : ')
usia1 = int(input('Masukkan Usia : '))
gender1 = input('Masukkan Gender : ')
p1 = [nama1, usia1, gender1]

nama2 = input('Masukkan Nama : ')
usia2 = int(input('Masukkan Usia : '))
gender2 = input('Masukkan Gender : ')
p2 = [nama2, usia2, gender2]

gabung = [p1, p2]
for profile in gabung:
  print(f'Nama \t: {profile[0]}')
  print(f'Usia \t: {profile[1]}')
  print(f'Gender \t: {profile[2]}')