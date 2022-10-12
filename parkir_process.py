from datetime import datetime

class Parkir:
    '''
    Class parkir berisi fungsi dalam pemrosesan parkir.
    Terdiri atas fungsi parkir_masuk, lihat_parkir, dan parkir_keluar

    '''

    def parkir_masuk(self):
        '''
        Fungsi parkir masuk secara otomatis

        '''

        for blok, button in zip(self.blok_list, self.blok_button):
            for nopol in self.nopol_aktif:
                if nopol not in self.blok_label and blok.cget('text').isdigit():
                    log_dict = dict()
                    log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    log_dict[self.log_keys[1]] = nopol
                    log_dict[self.log_keys[2]] = 'Sukses Parkir'
                    log_dict[self.log_keys[3]] = 'Parkir masuk ke Blok ' + blok.cget('text')
                    self.log.append(log_dict)

                    blok.configure(text=nopol, style='filled.TLabel')
                    button.configure(state='normal')
                    self.blok_label = [i.cget('text') for i in self.blok_list]
                    break


        # Update nilai counter
        counter = len([i for i in self.blok_list if i.cget('text').isdigit()])
        self.counter_kosong.configure(text=str(counter))

    def lihat_parkir(self, event):

        current = self.plat_nomor.current()
        if current != -1:
            value = self.nopol_aktif[current]
            for idx, val in enumerate(self.blok_label):
                if value == val:
                    self.lokasi.configure(text='Blok {}'.format(idx+1))
                    break
    @staticmethod
    def parkir_keluar(self, idx, *args, **kwargs):
        for index, (label, button) in enumerate(zip(self.blok_list, self.blok_button)):
            if index == idx:
                button.configure(state='disable')
                for i in range(10):
                    if self.nopol_list[i] == label.cget('text'):
                        self.nopol_list[i] = ''
                        for j in range(len(self.nopol_aktif)):
                            if self.nopol_aktif[j] == label.cget('text'):
                                log_dict = dict()
                                log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                log_dict[self.log_keys[1]] = self.nopol_aktif[j]
                                log_dict[self.log_keys[2]] = 'Sukses Keluar'
                                log_dict[self.log_keys[3]] = 'Parkir keluar dari Blok ' + str(idx+1)
                                self.log.append(log_dict)

                                del self.nopol_aktif[j]
                                label.configure(text=str(index+1), style='avail.TLabel')
                                self.plat_nomor.configure(values=self.nopol_aktif)
                                counter = int(self.counter_kosong.cget('text'))
                                self.counter_kosong.configure(text=str(counter + 1))
                                break
                        break