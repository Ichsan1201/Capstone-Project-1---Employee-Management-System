#Data Karyawan PT PWD

data = [
    {'NIP': 101, 'Nama': 'Ichsan', 'Gender': 'Laki-laki', 'Cabang': 'Jakarta', 'Performance': 'A', 'Absensi': 0},
    {'NIP': 102, 'Nama': 'Vina', 'Gender': 'Perempuan', 'Cabang': 'Bandung', 'Performance': 'A', 'Absensi': 2},
    {'NIP': 103, 'Nama': 'Kadir', 'Gender': 'Laki-laki', 'Cabang': 'Semarang', 'Performance': 'B', 'Absensi': 6},
    {'NIP': 104, 'Nama': 'Bimo', 'Gender': 'Laki-laki', 'Cabang': 'Yogyakarta', 'Performance': 'C', 'Absensi': 0},
    {'NIP': 105, 'Nama': 'Nisa', 'Gender': 'Perempuan', 'Cabang': 'Surabaya', 'Performance': 'B', 'Absensi': 1}
]

#Fungsi Keyakinan
def yakin(message):
    sure = input(f"Apakah Anda Yakin untuk {message.capitalize()} (Y/N)? ").lower()
    if sure== 'y' or sure == 'yes':
        return True
    elif sure == 'n' or sure == 'no':
        return False
    else:
        return yakin(message)
    
#Fungsi Cek NIP
def checknip():
    nip = input('Masukkan NIP : ')
    banyakdata = len(data)
    index = 0
    for i in range(banyakdata):
        if(int(nip) == int(data[i]['NIP'])):
            index += i+1
        else:
            index +=0
    return index

#Fungsi READ
def allReport():
    banyakData = len(data) 
    if(banyakData != 0):
        print('------------------------------------------------------------------------------------')
        print(f'| {'No':^3} | {'NIP':^5} | {'NAMA':^12} | {'GENDER':^12} | {'CABANG':^12} | {'PERFORMANCE':^12} | {'ABSENSI':^7} |')
        print('------------------------------------------------------------------------------------')
        for i, d in enumerate(data, start=1):
            print(f"| {i:^3} | {d['NIP']:^5} | {d['Nama']:<12} | {d['Gender']:<12} | {d['Cabang']:<12} | {d['Performance']:^12} | {d['Absensi']:^7} |")
        print('------------------------------------------------------------------------------------')
    else:
        print('Belum ada data pegawai dalam database')
        show()
def singleReport():
    index = checknip()
    if(index!= None):
        print('NIP    :', data[index-1]['NIP'])
        print('Nama   :', data[index-1]['Nama'])
        print('Gender :', data[index-1]['Gender'])
        print('Cabang   :', data[index-1]['Cabang'])
        print('Performance   :', data[index-1]['Performance'])
        print('Absensi  :',data[index-1]['Absensi'])
        print('')
    else:
        print('Tidak ada data dengan NIP tersebut')
        singleReport()              
def show():
    print('''======= Report Data Pegawai =======

    1. Report Seluruh Data
    2. Report Data Tertentu
    3. Kembali Ke Menu Utama

    ''')

    code = input('Silahkan Pilih Sub Menu Report Data Pegawai [1 - 3] : ')
    if code == '1':
        allReport()
    elif code == '2':
        singleReport()
    elif code == '3':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        show()

#Fungsi DELETE
def deletedata():
    index = checknip()
    if(index!= None):
        jawaban = yakin('Hapus Data')
        if(jawaban == True):
            del data[index-1]
            print('Data telah terhapus')
        else:
            delete()        
    else:
        print("Tidak ada data dengan NIP tersebut")
        delete() 
def delete():
    print('''======= Menghapus Data Pegawai =======

    1. Hapus Data Pegawai
    2. Kembali Ke Menu Utama

    ''')

    code = input('Silahkan Pilih Sub Menu Delete Data [1 - 2]')
    if code == '1':
        deletedata()
    elif code == '2':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        delete()

#Fungsi CREATE/ADD
def adding():
    banyakdata = len(data)
    print('Menambah Data Baru')
    nipbaru = int(input('Masukkan NIP : '))
    namabaru = input('Masukkan Nama : ').capitalize()
    genderbaru = input('Masukkan Gender : ').capitalize()
    cabangbaru = input('Masukkan Cabang : ').capitalize()
    performancebaru = input('Masukkan Performance : ').capitalize()
    absensibaru = input('Masukan Absensi Pegawai : ').capitalize()
    jawaban = yakin('Menambah Data')
    if(jawaban==True):
        data.append({'NIP':nipbaru, 'Nama':namabaru, 'Gender':genderbaru, 'Cabang':cabangbaru, 'Performance':performancebaru, 'Absensi':absensibaru})
        print('Data berhasil ditambah')
    else:
        add()
def add():
    print('''======= Menambah Data Pegawai =======

    1. Tambah Data Pegawai
    2. Kembali Ke Menu Utama

    ''')
    code = input('Silahkan Pilih Sub Menu Menambah Data Pegawai [1 - 2] : ')
    if code == '1':
        adding()
    elif code == '2':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        add()

#Fungsi UPDATE/EDIT
def editdata():
    index = checknip()

    if(index == -1):
        print("Tidak ada data dengan NIP tersebut")
        return
    
    print ("Kolom yang bisa diedit: Nama, Gender, Cabang, Performance dan Absensi")
    kolom = input("Masukan kolom yang ingin diedit:").capitalize()

    if kolom not in data[index-1]:
        print("Tidak ada nama kolom tersebut")
        return
    
    inputBaru = input(f"Masukan {kolom} baru :")

    if yakin ("Edit Data"):
        data[index-1][kolom]=inputBaru
        print("Data telah terupdate")

       
def edit():
    print('''======= Mengubah Data Pegawai =======

    1. Ubah Data Pegawai
    2. Kembali Ke Menu Utama

    ''')

    code = input('Silahkan Pilih Sub Menu Mengubah Data Pegawai [1 - 2] : ')
    if code == '1':
        editdata()
    elif code == '2':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        edit()

#Fungsi EXIT
def close():
    jawaban = yakin('Keluar dari Aplikasi')
    if(jawaban==True):
        print('Terima Kasih')
        exit()
    else:
        menu()

#Fungsi BONUS
def bonus ():
    index = checknip()

    if index == 0:
        print("Tidak ada data dengan NIP tersebut")
        return
    
    pegawai = data[index-1]
    nilaiKinerja = pegawai ['Performance'].upper()
    absensi = int(pegawai['Absensi'])

    gajiDasar = 10000000
    bonusDasar = 1000000

    print(f"\nNama      : {pegawai['Nama']}")
    print(f"Performance : {nilaiKinerja}")
    print(f"Absensi     : {absensi} hari")

    if nilaiKinerja == "A":
        bonusTambahan = gajiDasar * 0.20
    elif nilaiKinerja == "B":
        bonusTambahan = gajiDasar * 0.10
    elif nilaiKinerja == "C":
        bonusTambahan = 0
    else:
        print("Nilai performance tidak valid")
        return
    
    totalBonus = bonusDasar + bonusTambahan

    if absensi <= 4:
        denda = 0
    else :
        if nilaiKinerja in ["A","B"]:
            denda = gajiDasar * 0.05
        elif nilaiKinerja == "C":
            denda = gajiDasar * 0.10

    gajiTotal = gajiDasar + totalBonus - denda

    print ("\n======== RINCIAN GAJI ========")
    print (f"Gaji Dasar     : Rp {gajiDasar}")
    print (f"Bonus Kinerja  : Rp {int(totalBonus)}")
    print (f"Denda          : Rp {int(denda)}")
    print ('----------------------------------')
    print (f"Total Gaji     : Rp {int(gajiTotal)}")


#Default MENU
def menu():
    print('''======= Data Record Pegawai PT PWD =======

        1. Report Data Pegawai
        2. Menambahkan Data Pegawai
        3. Mengubah Data Pegawai
        4. Menghapus Data Pegawai
        5. Gaji Dan Bonus Yang Diterima Pegawai
        6. Exit
        ''')

    code = input('Silahkan Pilih Main Menu [1-6] : ')
    if code == '1':
        show()
    elif code == '2':
        add()
    elif code == '3':
        edit()
    elif code == '4':
        delete()
    elif code == '5':
        bonus()
    elif code == '6':
        close()
    else :
        print('  *** Pilihan yang anda masukkan salah ***')

data = [
    {
        'NIP': 101,
        'Nama':'Ichsan',
        'Gender': 'Laki-laki',
        'Cabang': 'Jakarta',
        'Performance': 'A',
        'Absensi': 0
    },
    {
        'NIP': 102,
        'Nama':'Vina',
        'Gender': 'Perempuan',
        'Cabang': 'Bandung',
        'Performance': 'A',
        'Absensi': 2
    },
    {
        'NIP': 103,
        'Nama':'Kadir',
        'Gender': 'Laki-laki',
        'Cabang': 'Semarang',
        'Performance': 'B',
        'Absensi': 6
    },
    {
        'NIP': 104,
        'Nama':'Bimo',
        'Gender': 'Laki-laki',
        'Cabang': 'Yogyakarta',
        'Performance': 'C',
        'Absensi': 0
    },
    {
        'NIP': 105,
        'Nama':'Nisa',
        'Gender': 'Perempuan',
        'Cabang': 'Surabaya',
        'Performance': 'B',
        'Absensi': 1
    }    
]

while(True):
    menu()
