'''
nama_variabel = input('nama variabel? ')
sig_1 = float(input('Sig pertama : '))
sig_2_Vassumed = float(input('Sig kedua atas (assumed): '))
sig_2_Vnotassumed = float(input('Sig kedua bawah (not assumed):'))
'''

while True:
    nama_variabel = input('nama variabel? ')
    sig_1 = float(input('Sig pertama : '))
    sig_2_Vassumed = float(input('Sig kedua atas (assumed): '))
    sig_2_Vnotassumed = float(input('Sig kedua bawah (not assumed):'))

    print(nama_variabel)
    if sig_1 > 0.05:
        if sig_2_Vassumed < 0.05:
            print('Hasil Signifikan')
            print('Kesimpulan : ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')
        elif sig_2_Vassumed > 0.05:
            print('Hasil tidak Signifikan')
            print('Kesimpulan : tidak ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')
    elif sig_1 < 0.05:
        if sig_2_Vnotassumed < 0.05:
            print('Hasil Signifikan')
            print('Kesimpulan : ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')
        elif sig_2_Vnotassumed > 0.05:
            print('Hasil tidak Signifikan')
            print('Kesimpulan : tidak ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')
    else:
        print('something wrong')





