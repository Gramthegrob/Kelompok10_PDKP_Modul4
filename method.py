class metode: #print modal
    #init method
    def _init_(self, harga):
        self.harga = harga

    #self parameter
    def trims(self):
        print("Terimakasih sudah menggunakan program kelompok 10")

    #method dengan parameter
    def selesai(self, waktu):
        print("Program akan selesai dalam :")
        while waktu > 0:
            print(waktu)
            waktu -= 1