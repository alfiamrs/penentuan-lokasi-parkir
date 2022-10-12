import os
import subprocess
import re
from tkinter import filedialog, messagebox
from datetime import datetime
#from .parkir_process import Parkir

class Deteksi:
    '''
    Class Deteksi berisi fungsi untuk memanggil program pendeteksi plat nomor
    yang outputnya digunakan sebagai input dari aplikasi pemetaan parkir

    '''
    #def __init__(self):
    #    super().__init__()

    def start_opencv(self):

        os.chdir('E:\ALPR FIA')
        # Untuk regex
        pat = r"^.*\= (.*[A-Z])\\r.*$"
        sub_pat = r"(\d+(\.\d+)?)"
        counts = 0

        if len(self.nopol_list) <= 10:
            counter = 10 - len(self.nopol_list)
            avail_park = len([i for i in self.nopol_list if i == ''])
            if (counter != 0) | (avail_park != 0):
                imgs = filedialog.askopenfilenames(title='Choose images')
                img_counter = 0
                for i in range(len(imgs)):
                    log_dict = dict()

                    try:
                        proc = subprocess.Popen(['python', 'Main1.py', '--image', imgs[i]],
                                                 stdout=subprocess.PIPE)
                        try:
                            plat = re.search(pat, str(proc.communicate()[0]))
                            fixed_plat = re.sub(sub_pat, r" \1 ", plat.group(1))

                            if len(fixed_plat.strip().split(sep=' ')) < 3:
                                messagebox.showinfo('Perhatian',
                                                    'Plat nomor {} tidak terdeteksi dengan baik. '
                                                    'Lanjut ke kendaraan lain.'.format(fixed_plat))

                                log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                log_dict[self.log_keys[1]] = fixed_plat
                                log_dict[self.log_keys[2]] = 'Gagal Deteksi'
                                log_dict[self.log_keys[3]] = 'Tidak terdeteksi dengan baik'
                                self.log.append(log_dict)
                                continue

                            if fixed_plat in self.nopol_aktif:
                                messagebox.showinfo('Perhatian',
                                                    'Plat nomor {} telah parkir. '
                                                    'Lanjut ke kendaraan lain.'.format(fixed_plat))

                                log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                log_dict[self.log_keys[1]] = fixed_plat
                                log_dict[self.log_keys[2]] = 'Gagal Parkir'
                                log_dict[self.log_keys[3]] = 'Plat nomor duplikat'
                                self.log.append(log_dict)
                                continue

                            if (counter > 0) | (avail_park == 0):
                                self.nopol_list.append(fixed_plat)
                                counter -= 1

                                log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                log_dict[self.log_keys[1]] = fixed_plat
                                log_dict[self.log_keys[2]] = 'Sukses Deteksi'
                                log_dict[self.log_keys[3]] = 'Plat nomor terdeteksi'
                                self.log.append(log_dict)

                            elif avail_park > 0:
                                for j in range(len(self.nopol_list)):
                                    if self.nopol_list[j] == '':
                                        self.nopol_list[j] = fixed_plat
                                        avail_park -= 1

                                        log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                        log_dict[self.log_keys[1]] = fixed_plat
                                        log_dict[self.log_keys[2]] = 'Sukses Deteksi'
                                        log_dict[self.log_keys[3]] = 'Plat nomor terdeteksi'
                                        self.log.append(log_dict)
                                        break
                            img_counter += 1

                        except:
                            counts += 1

                            log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                            log_dict[self.log_keys[1]] = ''
                            log_dict[self.log_keys[2]] = 'Gagal Deteksi'
                            log_dict[self.log_keys[3]] = 'Plat nomor tidak terdeteksi'
                            self.log.append(log_dict)
                            continue

                    except KeyboardInterrupt:
                        proc.terminate()

                    finally:
                        if (avail_park == 0) & (counter == 0) & ((len(imgs) - img_counter) > 0):
                            n = len(imgs) - img_counter
                            messagebox.showinfo('Perhatian',
                                                '{} gambar terakhir tidak terscan '
                                                'karena parkir telah penuh'.format(n))

                            log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                            log_dict[self.log_keys[1]] = str(n) + ' plat nomor'
                            log_dict[self.log_keys[2]] = 'Gagal Parkir'
                            log_dict[self.log_keys[3]] = 'Parkir penuh'
                            self.log.append(log_dict)
                            break

                self.nopol_aktif = [i for i in self.nopol_list if not i.isdigit() and i != '']
                self.blok_label = [i.cget('text') for i in self.blok_list]
                # Update combobox
                self.plat_nomor.configure(values=self.nopol_aktif)
                self.parkir_masuk()


            else:
                messagebox.showinfo('Perhatian',
                                    'Parkir sudah penuh!')
                log_dict = dict()

                log_dict[self.log_keys[0]] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                log_dict[self.log_keys[1]] = ''
                log_dict[self.log_keys[2]] = 'Gagal Parkir'
                log_dict[self.log_keys[3]] = 'Parkir penuh'
                self.log.append(log_dict)

                return None
