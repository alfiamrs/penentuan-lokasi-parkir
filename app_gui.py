from tkinter import *
from tkinter.ttk import *
from .parkir_process import Parkir
from .deteksi import Deteksi
from .logging import Logging
from .logging_alt import NonPandasLogging


class AppGUI(Deteksi, Parkir, Logging, NonPandasLogging):
    '''
    Class untuk menampilkan aplikasi pemetaan parkir

    '''

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
        style.configure('start.TLabel', background='white', anchor='center')
        original_background = self.window.cget('background')
        style.configure('def.TLabel', background=original_background, anchor='center')
        style.configure('avail.TLabel', background='darkolivegreen2', anchor='center')
        style.configure('filled.TLabel', background='tan1', anchor='center')

        # Inisiasi list untuk menampung Plat Nomor yang terdeteksi
        self.nopol_list = []
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
        title = Label(title_frame, text='SISTEM PENENTUAN LOKASI PARKIR',
                      style='def.TLabel')
        title.config(font=('Arial', 14, 'bold'))  # Pengaturan font judul

        # Label untuk menampilkan blok parkir
        self.blok_list = []
        for i in range(10):
            if i < 5:
                self.park = Label(park_segment0, width=15, text=str(i+1), style='avail.TLabel',
                                  borderwidth=2, relief='sunken')
                self.park.grid(row=0, column=i, sticky='ew', pady=20,
                                padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan
            else:
                self.park = Label(park_segment1, width=15, text=str(i+1), style='avail.TLabel',
                                  borderwidth=2, relief='sunken')
                self.park.grid(row=0, column=i-5, sticky='ew', pady=20,
                                padx=20, ipady=10, ipadx=5)  # Posisi gambar yang ditampilkan

            self.blok_list.append(self.park)

        # Button keluar di bawah tiap label blok parkir di segment0
        self.blok_button = []
        for i in range(10):
            if i < 5:
                self.park_button = Button(park_segment0, text='Keluar',
                                          command=lambda idx=i: Parkir.parkir_keluar(self, idx),
                                          state='disabled')
                self.park_button.grid(row=1, column=i)
            else:
                self.park_button = Button(park_segment1, text='Keluar',
                                          command=lambda idx=i: Parkir.parkir_keluar(self, idx),
                                          state='disabled')
                self.park_button.grid(row=1, column=i-5)

            self.blok_button.append(self.park_button)


        # Inisiasi widget pada frame dasar Informasi

        # Menampilkan widget pada frame dasar Informasi
        self.plat_label = Label(bottom_frame, text='Plat nomor yang terdeteksi',
                                style='def.TLabel')  # Label Plat nomor
        self.lokasi_parkir = Label(bottom_frame, text='Lokasi Kendaran',
                                   style='def.TLabel')  # Label judul lokasi parkir
        self.counter = Label(bottom_frame, text='Jumlah Tempat Kosong',
                             style='def.TLabel')  # Label jumlah tempat kosong

        self.upload_button = Button(bottom_frame, text='Start Upload',
                                   command= super().start_opencv)
        self.plat_nomor = Combobox(bottom_frame, values=self.nopol_list,
                                   width=5, justify='center')  # Combobox berisi plat nomor
        self.plat_nomor.set('Pilih Plat Nomor')
        self.lokasi = Label(bottom_frame, text='Nomor parkir ', width=10,
                            borderwidth=2, relief='sunken', style='start.TLabel')  # Label lokasi parkir
        self.counter_kosong = Label(bottom_frame, text='0', width=10,
                                    borderwidth=2, style='def.TLabel')  # Label counter
        self.log_button = Button(bottom_frame, text='Log', command=super().show_non_pandas_log)  # Button show log

        # Pengaturan letak dari setiap widget di window
        # Pengaturan letak title/judul
        title.grid(row=0, pady=(10, 40), sticky='ns')
        title.place(relx=.5, rely=.5, anchor='center')

        # Pengaturan letak baris dan kolom widget pada Frame Informasi
        self.plat_label.grid(row=0, column=1, sticky='ew', padx=10)
        self.lokasi_parkir.grid(row=0, column=2, sticky='ew', padx=20)
        self.counter.grid(row=0, column=3, sticky='ew', padx=10)
        self.upload_button.grid(row=1, column=0, sticky='ew',
                                ipadx=5, padx=10)
        self.plat_nomor.grid(row=1, column=1, sticky='ew', padx=20,
                             ipady=5, pady=5)
        self.lokasi.grid(row=1, column=2, sticky='ew',
                         ipady=5, pady=5, padx=10)
        self.counter_kosong.grid(row=1, column=3, sticky='ew',
                                 ipady=10, pady=10)
        self.log_button.grid(row=1, column=4, sticky='ew',
                             ipadx=5, padx=10)


        # 2. INISIASI DATA UNTUK PROSES PEMETAAN PARKIR
        self.blok_label = [i.cget('text') for i in self.blok_list]
        self.nopol_aktif = [i for i in self.nopol_list if not i.isdigit() and i != '']

        # dictionary log
        self.log = list()
        self.log_keys = ['Waktu', 'Plat Nomor', 'Status', 'Keterangan']

        # Update Lokasi Parkir ketika memilih Plat Nomor di Combobox
        self.plat_nomor.bind('<<ComboboxSelected>>', super().lihat_parkir)


        # Inisiasi list untuk menampung Plat Nomor yang terdeteksi
        self.window.mainloop()

