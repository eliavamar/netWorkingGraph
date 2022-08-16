from tkinter import *
from tkinter.ttk import *

from graph import Graph
from utils import *
from custom_csv import Csv


class gui:
    def __init__(self):
        self.master = Tk()
        self.master.title("Create Graph")
        self.csv = None
        self.master.geometry("400x300")

        lblWel = Label(self.master, text='Welcome To Project')
        lblWel.place(x=150, y=40)

        self.lblLoad = Label(self.master, text='Path CSV File')
        self.lblLoad.place(x=100, y=80)
        self.pathString = StringVar()
        self.pathEn = Entry(width=23, textvariable=self.pathString)
        self.pathEn.place(x=180, y=80)
        self.loadBut = Button(self.master,
                              text='Load CSV File',
                              command=lambda: self.loadCsv(self.pathString.get()),
                              width=15)
        self.loadBut.place(x=154, y=120)

        self.buildBut = Button(self.master,
                               text='Build Graph',
                               command=self.buildGraphWindow,
                               width=20)
        self.buildBut.place(x=140, y=170)

        self.mlBut = Button(self.master,
                            text='ML Algorithm',
                            command=self.mlAlgorithemWindow,
                            width=20)
        self.mlBut.place(x=140, y=200)

        mainloop()

    def mlAlgorithemWindow(self):
        buildAlgo = Toplevel(self.master)
        buildAlgo.title("ML Graph")
        buildAlgo.geometry("400x380")
        lbCcol = Label(buildAlgo, text='col')
        lbAlgo = Label(buildAlgo, text='algorithm')
        lbOut = Label(buildAlgo, text='out file')

        lbCcol.place(x=100, y=60)
        lbAlgo.place(x=100, y=170)
        lbOut.place(x=100, y=200)

        listCol = Listbox(buildAlgo, selectmode="multiple", height=5, width=20)
        listCol.pack(padx=5, pady=5, expand=YES)
        for item in self.csv.get_columns():
            listCol.insert(END, item)
        listCol.place(x=200, y=60)

        algoStr = StringVar()
        comboAlgo = Combobox(buildAlgo, width=20, textvariable=algoStr)
        comboAlgo['values'] = ('dbscan', 'isolation_forest')
        comboAlgo.place(x=200, y=170)

        outPathString = StringVar()
        outPathEn = Entry(buildAlgo, width=23, textvariable=outPathString)
        outPathEn.place(x=200, y=200)

        runAlgo = Button(buildAlgo,
                         text='Run',
                         command=lambda : self.playAlgorithems([listCol.get(i) for i in listCol.curselection()], algoStr.get(),outPathString.get()),
                         width=20)
        runAlgo.place(x=140, y=250)

    def buildGraphWindow(self):
        self.loadCsv(self.pathString.get())
        buidGraphWin = Toplevel(self.master)
        buidGraphWin.title("Build Graph")
        buidGraphWin.geometry("400x450")

        lbNeo = Label(buidGraphWin, text='Neo4j Configuration')
        lbNeo.place(x=140, y=25)

        lbUrl = Label(buidGraphWin, text='Url')
        lbUser = Label(buidGraphWin, text='User')
        lblPass = Label(buidGraphWin, text='Password')

        urlString = StringVar()
        urlEn = Entry(buidGraphWin, width=23, textvariable=urlString)
        userString = StringVar()
        userEn = Entry(buidGraphWin, width=23, textvariable=userString)
        passString = StringVar()
        passEn = Entry(buidGraphWin, width=23, textvariable=passString)

        lbUrl.place(x=100, y=60)
        lbUser.place(x=100, y=90)
        lblPass.place(x=100, y=120)

        urlEn.place(x=200, y=60)
        userEn.place(x=200, y=90)
        passEn.place(x=200, y=120)

        lbGrapg = Label(buidGraphWin, text='Graph Configuration')
        lbGrapg.place(x=140, y=150)

        lbSrc = Label(buidGraphWin, text='Src')
        lbDest = Label(buidGraphWin, text='Dest')
        lblWei = Label(buidGraphWin, text='Weight')
        lblGro = Label(buidGraphWin, text='Group By')
        lblAgg = Label(buidGraphWin, text='Select Agg')

        lbSrc.place(x=100, y=180)
        lbDest.place(x=100, y=210)
        lblWei.place(x=100, y=240)
        lblGro.place(x=100, y=270)
        lblAgg.place(x=100, y=340)

        srcStr = StringVar()
        destStr = StringVar()
        weiStr = StringVar()
        comboSrc = Combobox(buidGraphWin, width=20, textvariable=srcStr)
        comboSrc['values'] = (self.csv.get_columns())
        comboDest = Combobox(buidGraphWin, width=20, textvariable=destStr)
        comboDest['values'] = (self.csv.get_columns())
        comboWei = Combobox(buidGraphWin, width=20, textvariable=weiStr)
        comboWei['values'] = (self.csv.get_columns())

        comboSrc.place(x=200, y=180)
        comboDest.place(x=200, y=210)
        comboWei.place(x=200, y=240)

        listGroup = Listbox(buidGraphWin, selectmode="multiple", height=3, width=20, exportselection=False)
        listGroup.pack(padx=5, pady=5,
                       expand=YES)
        listGroup.place(x=200, y=270)

        update = Button(buidGraphWin,
                        text='update',
                        command=lambda: (listGroup.delete(0, END), listGroup.insert(END, srcStr.get()),
                                         listGroup.insert(END, destStr.get()), listGroup.insert(END, weiStr.get())),
                        width=7)
        update.place(x=30, y=280)

        listAggr = Listbox(buidGraphWin, selectmode="multiple", height=3, width=20, exportselection=False)
        listAggr.curselection()
        listAggr.pack(padx=5, pady=5,
                      expand=YES)
        for item in agg_function_list():
            listAggr.insert(END, item)
        listAggr.place(x=200, y=340)
        runGraph = Button(buidGraphWin,
                          text='Run',
                          command=lambda: self.createGraph(urlString.get(), userString.get(), passString.get(),
                                                           srcStr.get(),
                                                           destStr.get(), weiStr.get(),
                                                           [listGroup.get(i) for i in listGroup.curselection()],
                                                           [listAggr.get(i) for i in listAggr.curselection()]),
                          width=20)
        runGraph.place(x=140, y=420)

    def createGraph(self, url, user, password, src, dest, w, groupList=None, aggList=None):
        if w == '': w=None
        if len(groupList) == 0: groupList = None
        if len(aggList) == 0: aggList = None
        print(groupList)
        print(aggList)
        if groupList:
            if aggList:
                self.drawHtmlGraph(self.csv.group_by(groupList, aggList), url, user, password, src, dest, w)
            else:
                self.drawHtmlGraph(self.csv.group_by(groupList), url, user, password, src, dest, w)
        else:
            self.drawHtmlGraph(self.csv, url, user, password, src, dest, w)

    def drawHtmlGraph(self, df, url, user, password, src, dest, w):
        G = Graph(df, url, user, password, src, dest, w)
        # G.draw_graph(len(df))

    def playAlgorithems(self):
        print('temp')

    def loadCsv(self, csvFile):
        self.csv = Csv(csvFile)
    #
    #     buildBut = Button(newWindow,
    #                       text='Create Graph',
    #                       command=self.openConnWindow,
    #                       width=30)
    #     b1.place(x=110, y=330)
    #
    #     self.n = StringVar()
    #     self.n2 = StringVar()
    #     self.n3 = StringVar()
    #     self.t2 = Combobox(self.master, width=20, textvariable=self.n)
    #     self.t2['values'] = (self.csv.get_columns())
    #     self.t3 = Combobox(self.master, width=20, textvariable=self.n2)
    #     self.t3['values'] = (self.csv.get_columns())
    #     self.t4 = Combobox(self.master, width=20, textvariable=self.n3)
    #     self.t4['values'] = (self.csv.get_columns())
    #     self.lbl2.place(x=100, y=150)
    #     self.t2.place(x=200, y=150)
    #     self.lbl3.place(x=100, y=200)
    #     self.t3.place(x=200, y=200)
    #     self.lbl4.place(x=100, y=250)
    #     self.t4.place(x=200, y=250)
