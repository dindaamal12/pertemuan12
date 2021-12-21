print('program menambah data dengan class')
data ={}
class nilai():
    def tambah(self):
        print('\nmenambah data')
        nama=input('masukan nama\t\t: ')
        nim=input('masukan NIM\t\t: ')
        tugas=int(input('masukan nilai tugas\t: '))
        uts=int(input('masukan nilai Uts\t: '))
        uas=int(input('masukan nilai UAS\t: '))
        akhir=(0.30*tugas)+(0.35*uts)+(0.35*uas)
        data[nama]=nim,tugas,uts,uas,akhir
    def ubah(self):
        print('\nmengubah data')
        nama = input('masukan nama\t\t: ')
        if  nama in data.keys():
            nim=input('masukan NIM\t\t: ')
            tugas=int(input('masukan nilai tugas\t: '))
            uts=int(input('masukan nilai Uts\t: '))
            uas=int(input('masukan nilai UAS\t: '))
            akhir=(0.30*tugas)+(0.35*uts)+(0.35*uas)
            data[nama]=nim,tugas,uts,uas,akhir
            print('\ndata berhasil diubah')
        else:
            print('\ndata tidak ditemukan !')
    def hapus(self):
        print('\nmenghapus data')
        nama=input('masukan nama\t\t: ')
        if nama in data.keys():
            del data[nama]
            print('\ndata berhasil dihapus')
        else:
            print('\ndata tidak ditemukan !')

    def lihat(self):
        print('\nmelihat data')
        if data.items():
            print('===============================================================================')
            print("| no |     nama     |     nim     |  tugas  |   uts   |    uas   |    akhir   |")
            print('===============================================================================')
            i=0
            for x in data.items():
                i+=1
                print("|{6:4}|{0:14s}|{1:13s}|{2:9}|{3:9}|{4:10}|{5:12}|".format (x[0] ,x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],i))
            print('===============================================================================')
        else:
            print('\ndata tidak ditemukan !')
    def keluar(self):
        print('\nterimakasih\n')
while True:
    d=nilai()
    print('\nmenambah data\t\t(1)\nmengubah data\t\t(2)\nmenghapus data\t\t(3)\nmenampilkan data\t(4)')
    a=input("masukan pilihan : ")
    if (a=="1"):
        d.tambah()
    elif (a=="2"):
        d.ubah()
    elif (a=="3"):
        d.hapus()
    elif (a=="4"): 
        d.lihat()
    else:
        d.keluar()
        break