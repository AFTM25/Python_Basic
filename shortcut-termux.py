print('Hello World')
print('Shortcut pada apk termux')

sesi_Baru = 'CTRL + ALT + C'
set_Nama_Sesi = 'CTRL + ALT + R'
pindah_Sesi_Sebelumnya = 'CTRL + ALT + Panah Atas'
pindah_Sesi_Awal_Setelahnya = 'CTRL + ALT + Panah Bawah'
open_Side_Bar = 'CTRL + ALT + Panah Kanan'
close_Side_Bar = 'CTRL + ALT + Panah Kiri'
open_Menu_Apk = 'CTRL + ALT + M'
open_Link = 'CTRL + ALT + U'
catatan_open_Link = '''
Sebelum menjalankan shortcut Ctrl + Alt + U, pada tampilan termux ketik terlebih dahulu situs apa atau website apa yang akan dibuka. Misalkan saya akan buka web google. Maka pada tampilan termux ketik xdg-open 'https://google.com' . Kemudian enter.
Sebetulnya perintah ini hanya menampilkan situs atau website yang sudah diketik secara manual pada halaman layar termux sesi tersebut.
'''

paste_Text = 'CTRL + ALT + V'
size_Font = 'CTRL + ALT + +/-'
pilih_Sesi_Aktif = 'CTRL + ALT + 1-9'
hapus_Sesi_Ini = 'CTRL + SHIFT + D'

def tampilkan():
    shortcut = {
            'Menambahkan sesion baru' : sesi_Baru,
            
    }
