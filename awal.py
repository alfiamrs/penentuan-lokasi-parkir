from tkinter import *
from tkinter.ttk import *


class GuiMain:

    def __init__(self):
        # 1. INISIASI GUI UNTUK PROGRAM PARKIR

        # Insiasi window dari tkinter beserta ukurannya
        self.window = Tk()
        self.window.title('Sistem Penentuan Lokasi Parkir')
        w, h = 810, 575
        self.window.minsize(width=w, height=h)
        self.window.maxsize(width=w, height=h)

        # Style widget
        style = Style()
        style.configure('W.Tbutton')
        style.configure('TLabel', background='white', anchor='center')
        original_background = self.window.cget('background')
        style.configure('def.TLabel', background=original_background)
        style.configure('filled.TLabel', background='red')

        # Inisiasi list untuk menampung Plat Nomor yang terdeteksi
        self.nopol_list = ['AG 4710 YAT', 'S 3559 JAK',
                           'N 4136 CM', 'N 5263 BAR',
                           'P 3274 UJ', 'N 2775 AE',
                           'B 4365 KMG']
        self.counter_empty = 0

        # Inisiasi frame dasar untuk membagi dasar window
        title_frame = Frame(self.window,
                            height=45, width=810)
        main_frame = LabelFrame(self.window, text='Pemetaan Parkir',
                                height=420, width=700)
        bottom_frame = LabelFrame(self.window, text='Informasi',
                                  height=120, width=700)

        # Pengaturan letak dari frame dasar
        title_frame.grid(row=0, sticky='nsew', pady=10)
        main_frame.grid(row=1, sticky='ns', ipady=10)
        bottom_frame.grid(row=2, sticky='ns',
                          pady=20, ipadx=20)
        bottom_frame.grid_rowconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(0, weight=1)

        # Inisiasi Frame dalam Frame Pemetaan Parkir
        park_segment0 = Frame(main_frame, height=210,
                              width=700)
        park_segment1 = Frame(main_frame, height=210,
                              width=700)

        # Pengaturan letak dari frame park segment
        park_segment0.grid(row=0, sticky='ew', padx=20)
        park_segment1.grid(row=1, sticky='ew', padx=20)

        # Inisiasi widget pada frame dasar Pemetaan Parkir
        # Label untuk menampilkan title/judul
        title = Label(title_frame, text='SISTEM PEMETAAN PARKIR',
                      style='def.TLabel')
        title.config(font=('Arial', 14, 'bold'))  # Pengaturan font judul

        # Label untuk menampilkan blok parkir di Park segment0
        self.park1 = Label(park_segment0, width=15, text='1', style='TLabel',
                           borderwidth=2, relief='sunken')
        self.park2 = Label(park_segment0, text='2', width=15,
                           borderwidth=2, relief='sunken', style='TLabel')
        self.park3 = Label(park_segment0, text='3', width=15,
                           borderwidth=2, relief='sunken', style='TLabel')
        self.park4 = Label(park_segment0, text='4', width=15,
                           borderwidth=2, relief='sunken', style='TLabel')
        self.park5 = Label(park_segment0, text='5', width=15,
                           borderwidth=2, relief='sunken', style='TLabel')

        # Button keluar di bawah tiap label blok parkir di segment0
        self.park1_button = Button(park_segment0, text='keluar',
                                   command=None)
        self.park2_button = Button(park_segment0, text='keluar',
                                   command=None)
        self.park3_button = Button(park_segment0, text='keluar',
                                   command=None)
        self.park4_button = Button(park_segment0, text='keluar',
                                   command=None)
        self.park5_button = Button(park_segment0, text='keluar',
                                   command=None)

        # Label untuk menampilkan blok parkir di Park segment1
        self.park6 = Label(park_segment1, text='6', width=15,
                           borderwidth=2, relief='sunken')
        self.park7 = Label(park_segment1, text='7', width=15,
                           borderwidth=2, relief='sunken')
        self.park8 = Label(park_segment1, text='8', width=15,
                           borderwidth=2, relief='sunken', style='TLabel')
        self.park9 = Label(park_segment1, text='9', width=15,
                           borderwidth=2, relief='sunken', style='TLabel')
        self.park10 = Label(park_segment1, text='10', width=15,
                            borderwidth=2, relief='sunken', style='TLabel')

        # Button keluar di bawah tiap label blok parkir di segment1
        self.park6_button = Button(park_segment1, text='keluar',
                                   command=None)
        self.park7_button = Button(park_segment1, text='keluar',
                                   command=None)
        self.park8_button = Button(park_segment1, text='keluar',
                                   command=None)
        self.park9_button = Button(park_segment1, text='keluar',
                                   command=None)
        self.park10_button = Button(park_segment1, text='keluar',
                                    command=None)

        # Inisiasi widget pada frame dasar Informasi

        # Menampilkan widget pada frame dasar Informasi
        self.plat_label = Label(bottom_frame, text='Plat nomor yang terdeteksi',
                                style='def.TLabel')  # Label Plat nomor
        self.lokasi_parkir = Label(bottom_frame, text='Lokasi Kendaran',
                                   style='def.TLabel')  # Label judul lokasi parkir
        self.counter = Label(bottom_frame, text='Jumlah Tempat Kosong',
                             style='def.TLabel')  # Label jumlah tempat kosong
        self.plat_nomor = Combobox(bottom_frame, values=self.nopol_list,
                                   width=5, justify='center')  # Combobox berisi plat nomor
        self.plat_nomor.set('Pilih Plat Nomor')
        self.lokasi = Label(bottom_frame, text='Nomor parkir ', width=10,
                            borderwidth=2, relief='sunken')  # Label lokasi parkir
        self.counter_kosong = Label(bottom_frame, text='0', width=10,
                                    borderwidth=2, style='def.TLabel')  # Label counter
        self.show_log = Button(bottom_frame, text='Log', command=None)  # Button show log

        # Pengaturan letak dari setiap widget di window
        # Pengaturan letak title/judul
        title.grid(row=0, pady=(10, 40), sticky='ns')
        title.place(relx=.5, rely=.5, anchor='center')

        # Pengaturan letak baris dan kolom blok parkir pada Frame segment0
        self.park1.grid(row=0, column=0, sticky='ew', pady=20,
                        padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park2.grid(row=0, column=1, sticky='ew',
                        pady=20, padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park3.grid(row=0, column=2, sticky='ew',
                        pady=20, padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park4.grid(row=0, column=3, sticky='ew',
                        pady=20, padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park5.grid(row=0, column=4, sticky='ew',
                        pady=20, padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan

        # Pengaturan letak baris dan kolom blok parkir pada Frame segment1
        self.park6.grid(row=0, column=0, sticky='ew', pady=20, padx=20,
                        ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park7.grid(row=0, column=1, sticky='ew', pady=20, padx=20,
                        ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park8.grid(row=0, column=2, sticky='nsew', pady=20, padx=20,
                        ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park9.grid(row=0, column=3, sticky='nsew', pady=20, padx=20,
                        ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
        self.park10.grid(row=0, column=4, sticky='nsew', pady=20, padx=20,
                         ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan

        # Pengaturan letak baris dan kolom button keluar parkir pada Frame segment0
        self.park1_button.grid(row=1, column=0)
        self.park2_button.grid(row=1, column=1)
        self.park3_button.grid(row=1, column=2)
        self.park4_button.grid(row=1, column=3)
        self.park5_button.grid(row=1, column=4)

        # Pengaturan letak baris dan kolom button keluar parkir pada Frame segment1
        self.park6_button.grid(row=1, column=0)
        self.park7_button.grid(row=1, column=1)
        self.park8_button.grid(row=1, column=2)
        self.park9_button.grid(row=1, column=3)
        self.park10_button.grid(row=1, column=4)

        # Pengaturan letak baris dan kolom widget pada Frame Informasi
        self.plat_label.grid(row=0, column=0, sticky='ew', padx=10)
        self.lokasi_parkir.grid(row=0, column=1, sticky='ew', padx=20)
        self.counter.grid(row=0, column=2, sticky='ew', padx=10)
        self.plat_nomor.grid(row=1, column=0, sticky='ew', padx=20,
                             ipady=5, pady=5)
        self.lokasi.grid(row=1, column=1, sticky='ew',
                         ipady=5, pady=5, padx=10)
        self.counter_kosong.grid(row=1, column=2, sticky='ew',
                                 ipady=10, pady=10)
        self.show_log.grid(row=1, column=3, sticky='ew',
                           ipadx=5, padx=10)

        # 2. INISIASI DATA UNTUK PROSES PEMETAAN PARKIR

        # Inisiasi list untuk menampung Plat Nomor yang terdeteksi

        # def masuk_parkir(self):
        # current = self.plat_nomor.current()

        self.window.mainloop()


GuiMain()
