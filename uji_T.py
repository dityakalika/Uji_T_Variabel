
nama_variabel = input('nama variabel? ')
sig_1 = input('Sig pertama : ')
sig_2_Vassumed = input('Sig kedua atas (assumed): ')
sig_2_Vnotassumed = input('Sig kedua bawah (not assumed):')
sig_1_bool = int(sig_1)
sig_2_atas = int(sig_2_Vassumed)
sig_2_bawah = int(sig_2_Vnotassumed)

if sig_1_bool >= 0.05:
    if sig_2_atas <= 0.05:
        print('Hasil Signifikan')
        print('Kesimpulan : ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')
    elif sig_2_atas >= 0.05:
        print('Hasil tidak Signifikan')
        print('Kesimpulan : tidak ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')

elif sig_1_bool <= 0.05:
    if sig_2_bawah <= 0.05:
        print('Hasil Signifikan')
        print('Kesimpulan : ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')
    elif sig_2_bawah >= 0.05:
        print('Hasil tidak Signifikan')
        print('Kesimpulan : tidak ada perbedaan rata-rata provinsi', (nama_variabel),'tinggi dengan',(nama_variabel),'rendah.')

else:
    print('something wrong')





