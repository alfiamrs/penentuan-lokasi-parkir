from tkinter import messagebox
import pandas as pd
from pandastable import Table
from tkinter import *
from tkinter import _tkinter


class Logging:

    def show_log(self):

        if len(self.log) == 0:
            messagebox.showinfo('Perhatian',
                                'Tidak ada log aktivitas')
            return None

        df = pd.DataFrame.from_records(self.log)

        log_window = Toplevel(self.window)
        log_window.title('Log Aktivitas')
        w, h = 810, 575
        log_window.minsize(width=w, height=h)
        log_window.maxsize(width=w, height=h)

        table_frame = Frame(log_window)
        table_frame.pack(fill=BOTH, expand=1)

        table = Table(table_frame, dataframe=df,
                      showtoolbar=True, showstatusbar=True)
        table.show()

        def on_close():
            response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
            if response:
                table.destroy()
                table_frame.destroy()
                log_window.withdraw()
                return None

        log_window.protocol('WM_DELETE_WINDOW', on_close)
