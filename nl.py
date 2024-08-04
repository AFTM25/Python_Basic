# Tipe Data Sequence Biner

b1 = bytes('Hello World', 'utf-8')
print('Nilai dari b1 = ', b1)

ba = bytearray(b1)
mv = memoryview(ba)
print('Lokasi memori dalam memoryview = ', mv)

