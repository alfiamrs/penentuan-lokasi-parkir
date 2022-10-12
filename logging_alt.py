from tkinter import *
from tkinter.ttk import *
import pandas as pd
from tkinter import messagebox, filedialog

class NonPandasLogging:

    def show_non_pandas_log(self):
        if len(self.log) == 0:
            messagebox.showinfo('Perhatian',
                                'Tidak ada log aktivitas')
            return None

        df = pd.DataFrame.from_records(self.log)
        def to_csv():
            file = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
            if file is None:
                return
            df.to_csv(file.name, index=False)
            file.close()

        log_window = Toplevel(self.window)
        log_window.title('Log Aktivitas')
        w, h = 700, 575
        log_window.minsize(width=w, height=h)
        log_window.maxsize(width=w, height=h)

        style = Style()
        style.configure('title.TLabel', anchor='center')
        style.configure('W.Tbutton')

        title_frame = Frame(log_window, height=75, width=700)
        tableframe = Frame(log_window, height=420, width=700)
        title_frame.grid(row=0, sticky='nsew')
        tableframe.grid(row=1, sticky='nsew')

        title = Label(title_frame, text='LOG AKTIVITAS PARKIR',
                      style='title.TLabel')
        title.config(font=('Arial', 14, 'bold'))
        title.grid(row=0)
        title.place(relx=.5, rely=.5, anchor='center')

        table = Treeview(tableframe, columns=(0, 1, 2, 3),
                         show='headings', height=15)

        for idx, val in enumerate(self.log[0].keys()):
            if idx == 3:
                table.column(idx, stretch=FALSE, width=200)
            else:
                table.column(idx, stretch=FALSE, width=150)

            table.heading(idx, text=val)

        for idx, val in enumerate(self.log):
            table.insert(parent='', index=idx, iid=idx,
                         values=tuple(val.values()))
        table.grid(row=0, column=0, sticky='ns', pady=20, padx=(20, 2))

        scrollbar = Scrollbar(tableframe,
                              orient=VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='nsw', pady=20)

        export_csv = Button(tableframe, text='Export CSV', command=to_csv)
        export_csv.grid(row=1, column=0, ipadx=5, padx=(20, 2), sticky='w')

        def handle_click(event):
            if table.identify_region(event.x, event.y) == "separator":
                return "break"


        table.bind('<Button-1>', handle_click)