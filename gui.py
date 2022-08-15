from tkinter import *
from tkinter.ttk import *
from utils import *
from custom_csv import Csv


class gui:
    def __init__(self):
        # creates a Tk() object
        self.master = Tk()
        self.csv = None

        # sets the geometry of main
        # root window
        self.master.geometry("400x400")

        self.lbl1 = Label(self.master, text='Path CSV File')

        self.lbl2 = Label(self.master, text='Src')
        self.lbl3 = Label(self.master, text='dest')
        self.lbl4 = Label(self.master, text='weight')
        self.t1String = StringVar()
        self.t1 = Entry(width=23, textvariable=self.t1String)

        self.b1 = Button(self.master,
                         text='Load CSV File',
                         command=lambda: self.loadCsv(self.t1String.get()),
                         width=15)
        self.b1.place(x=162, y=100)

        # self.n = StringVar()
        # self.n2 = StringVar()
        # self.t2 = Combobox(self.master, width=20, textvariable=self.n)
        # self.t2['values'] = (self.csv.get_columns())
        # self.t3 = Combobox(self.master, width=20, textvariable=self.n2)
        # self.t3['values'] = (self.csv.get_columns())

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        # self.lbl2.place(x=100, y=150)
        # self.t2.place(x=200, y=150)
        # self.lbl3.place(x=100, y=200)
        # self.t3.place(x=200, y=200)

        self.b1 = Button(self.master,
                         text='Select Aggregation configuration',
                         command=self.openNewWindow,
                         width=30)
        self.b1.place(x=110, y=320)

        # mainloop, runs infinitely
        mainloop()

    def openNewWindow(self):
        newWindow = Toplevel(self.master)
        newWindow.title("New Window")
        newWindow.geometry("300x320")
        # Label(newWindow,
        #       text="This is a new window").pack()

        nLbl1 = Label(newWindow, text='select agg')
        nLbl1.place(x=120, y=60)
        listAggr = Listbox(newWindow, selectmode="multiple")
        listAggr.pack(padx=10, pady=10,
                      expand=YES)
        for item in agg_function_list():
            listAggr.insert(END, item)
        listAggr.place(x=90, y=80)
        b1 = Button(newWindow,
                    text='connection',
                    command=self.openConnWindow,
                    width=30)
        b1.place(x=60, y=280)

        algoLbl = Label(newWindow, text='select algorithm')
        algoLbl.place(x=110, y=10)

        stringAlgo = StringVar()
        comboAlgo = Combobox(newWindow, width=20, textvariable=stringAlgo)
        comboAlgo['values'] = ('dbscan', 'isolation_forest')
        comboAlgo.place(x=82,y=35)

    def openConnWindow(self):
        newWindow2 = Toplevel(self.master)
        newWindow2.title("New Window")
        newWindow2.geometry("400x380")
        lbl1 = Label(newWindow2, text='Neo4j connection')

        lbl2 = Label(newWindow2, text='Url')
        lbl3 = Label(newWindow2, text='User')
        lbl4 = Label(newWindow2, text='Password')

        self.urlString = StringVar()
        self.urlEn = Entry(newWindow2, width=23, textvariable=self.urlString)
        self.userString = StringVar()
        self.userEn = Entry(newWindow2, width=23, textvariable=self.userString)
        self.passString = StringVar()
        self.passEn = Entry(newWindow2, width=23, textvariable=self.passString)
        lbl1.place(x=150, y=90)
        lbl2.place(x=100, y=150)
        lbl3.place(x=100, y=200)
        lbl4.place(x=100, y=250)
        self.urlEn.place(x=200, y=150)
        self.userEn.place(x=200, y=200)
        self.passEn.place(x=200, y=250)

        b1 = Button(newWindow2,
                    text='Create Graph',
                    command=self.openConnWindow,
                    width=30)
        b1.place(x=110, y=330)

    def loadCsv(self, csvFile):
        self.csv = Csv(csvFile)
        self.n = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.t2 = Combobox(self.master, width=20, textvariable=self.n)
        self.t2['values'] = (self.csv.get_columns())
        self.t3 = Combobox(self.master, width=20, textvariable=self.n2)
        self.t3['values'] = (self.csv.get_columns())
        self.t4 = Combobox(self.master, width=20, textvariable=self.n3)
        self.t4['values'] = (self.csv.get_columns())
        self.lbl2.place(x=100, y=150)
        self.t2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)
