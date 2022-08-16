from tkinter import *
from tkinter.ttk import *

import utils
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

        lblLoad = Label(self.master, text='File Loaded!')
        self.lblPath = Label(self.master, text='Path CSV File')
        self.lblPath.place(x=100, y=80)
        self.pathString = StringVar()

        self.pathEn = Entry(width=23, textvariable=self.pathString)
        self.pathEn.place(x=180, y=80)
        self.loadBut = Button(self.master,
                              text='Load CSV File',
                              command=lambda: (self.loadCsv(self.pathString.get()), lblLoad.place(x=165, y=148)),
                              width=15)
        self.loadBut.place(x=154, y=120)

        self.buildBut = Button(self.master,
                               text='Build Graph',
                               command=self.buildGraphWindow,
                               width=20)
        self.buildBut.place(x=140, y=200)

        self.mlBut = Button(self.master,
                            text='ML Algorithm',
                            command=self.mlAlgorithemWindow,
                            width=20)
        self.mlBut.place(x=140, y=230)

        mainloop()

    def mlAlgorithemWindow(self):
        buildAlgo = Toplevel(self.master)
        buildAlgo.title("ML Graph")
        buildAlgo.geometry("400x470")
        lbAlgo = Label(buildAlgo, text='algorithm')

        lbAlgo.place(x=100, y=50)

        algoStr = StringVar()
        comboAlgo = Combobox(buildAlgo, width=20, textvariable=algoStr)
        comboAlgo['values'] = ('dbscan', 'isolation_forest')
        comboAlgo.place(x=200, y=50)

        selConf = Button(buildAlgo,
                         text='Select Configuration',
                         command=lambda: self.createAlgoConfig(buildAlgo, algoStr.get()),
                         width=20)
        selConf.place(x=140, y=80)



    def createAlgoConfig(self, win, algo):
        if algo == "dbscan":
            self.lb1 = Label(win, text=list(utils.get_default_dbscan_params())[0])
            self.lb1.place(x=100, y=110)
            self.lb1String = StringVar()
            self.lb1En = Entry(win,width=23, textvariable=self.lb1String)
            self.lb1En.place(x=200, y=110)
            self.lb2 = Label(win, text=list(utils.get_default_dbscan_params())[1])
            self.lb2.place(x=100, y=130)
            self.lb2String = StringVar()
            self.lb2En = Entry(win,width=23, textvariable=self.lb2String)
            self.lb2En.place(x=200, y=130)
            self.lb3 = Label(win, text=list(utils.get_default_dbscan_params())[2])
            self.lb3.place(x=100, y=150)
            self.lb3String = StringVar()
            self.lb3En = Entry(win,width=23, textvariable=self.lb3String)
            self.lb3En.place(x=200, y=150)
            self.lb4 = Label(win, text=list(utils.get_default_dbscan_params())[3])
            self.lb4.place(x=100, y=170)
            self.lb4String = StringVar()
            self.lb4En = Entry(win,width=23, textvariable=self.lb4String)
            self.lb4En.place(x=200, y=170)
            self.lb5 = Label(win, text=list(utils.get_default_dbscan_params())[4])
            self.lb5.place(x=100, y=190)
            self.lb5String = StringVar()
            self.lb5En = Entry(win,width=23, textvariable=self.lb5String)
            self.lb5En.place(x=200, y=190)
            self.lb6 = Label(win, text=list(utils.get_default_dbscan_params())[5])
            self.lb6.place(x=100, y=210)
            self.lb6String = StringVar()
            self.lb6En = Entry(win,width=23, textvariable=self.lb6String)
            self.lb6En.place(x=200, y=210)
            self.lb7 = Label(win, text=list(utils.get_default_dbscan_params())[6])
            self.lb7.place(x=100, y=230)
            self.lb7String = StringVar()
            self.lb7En = Entry(win,width=23, textvariable=self.lb7String)
            self.lb7En.place(x=200, y=230)
            self.lb8 = Label(win, text=list(utils.get_default_dbscan_params())[7])
            self.lb8.place(x=100, y=250)
            self.lb8String = StringVar()
            self.lb8En = Entry(win,width=23, textvariable=self.lb8String)
            self.lb8En.place(x=200, y=250)

            lbCcol = Label(win, text='col')
            lbCcol.place(x=100, y=280)
            listCol = Listbox(win, selectmode="multiple", height=5, width=20)
            listCol.pack(padx=5, pady=5, expand=YES)
            for item in self.csv.get_columns():
                listCol.insert(END, item)
            listCol.place(x=200, y=280)

            lbOut = Label(win, text='out file')
            lbOut.place(x=100, y=380)

            outPathString = StringVar()
            outPathEn = Entry(win, width=23, textvariable=outPathString)
            outPathEn.place(x=200, y=380)

            runAlgo = Button(win,
                             text='Run',
                             command=lambda: self.playAlgorithems([listCol.get(i) for i in listCol.curselection()],
                                                                  algo, outPathString.get()),
                             width=20)
            runAlgo.place(x=140, y=410)

        if algo == "isolation_forest":
            lb1 = Label(win, text=list(utils.get_default_isolation_forest_params())[0])
            lb1.place(x=100, y=110)
            lb1String = StringVar()
            lb1En = Entry(win,width=23, textvariable=lb1String)
            lb1En.pack()
            lb1En.place(x=200, y=110)
            lb2 = Label(win, text=list(utils.get_default_isolation_forest_params())[1])
            lb2.place(x=100, y=130)
            lb2String = StringVar()
            lb2En = Entry(win,width=23, textvariable=lb2String)
            lb2En.place(x=200, y=130)
            lb3 = Label(win, text=list(utils.get_default_isolation_forest_params())[2])
            lb3.place(x=100, y=150)
            lb3String = StringVar()
            lb3En = Entry(win,width=23, textvariable=lb3String)
            lb3En.place(x=200, y=150)
            lb4 = Label(win, text=list(utils.get_default_isolation_forest_params())[3])
            lb4.place(x=100, y=170)
            lb4String = StringVar()
            lb4En = Entry(win,width=23, textvariable=lb4String)
            lb4En.place(x=200, y=170)
            lb5 = Label(win, text=list(utils.get_default_isolation_forest_params())[4])
            lb5.place(x=100, y=190)
            lb5String = StringVar()
            lb5En = Entry(win,width=23, textvariable=lb5String)
            lb5En.place(x=200, y=190)
            lb6 = Label(win, text=list(utils.get_default_isolation_forest_params())[5])
            lb6.place(x=100, y=210)
            lb6String = StringVar()
            lb6En = Entry(win,width=23, textvariable=lb6String)
            lb6En.place(x=200, y=210)
            lb7 = Label(win, text=list(utils.get_default_isolation_forest_params())[6])
            lb7.place(x=100, y=230)
            lb7String = StringVar()
            lb7En = Entry(win,width=23, textvariable=lb7String)
            lb7En.place(x=200, y=230)
            lb8 = Label(win, text=list(utils.get_default_isolation_forest_params())[7])
            lb8.place(x=100, y=250)
            lb8String = StringVar()
            lb8En = Entry(win,width=23, textvariable=lb8String)
            lb8En.place(x=200, y=250)
            lb9 = Label(win, text=list(utils.get_default_isolation_forest_params())[8])
            lb9.place(x=100, y=270)
            lb9String = StringVar()
            lb9En = Entry(win,width=23, textvariable=lb9String)
            lb9En.place(x=200, y=270)

            lbCcol = Label(win, text='col')
            lbCcol.place(x=100, y=300)
            listCol = Listbox(win, selectmode="multiple", height=5, width=20)
            listCol.pack(padx=5, pady=5, expand=YES)
            for item in self.csv.get_columns():
                listCol.insert(END, item)
            listCol.place(x=200, y=300)

            lbOut = Label(win, text='out file')
            lbOut.place(x=100, y=400)

            outPathString = StringVar()
            outPathEn = Entry(win, width=23, textvariable=outPathString)
            outPathEn.place(x=200, y=400)

            runAlgo = Button(win,
                             text='Run',
                             command=lambda: self.playAlgorithems([listCol.get(i) for i in listCol.curselection()],
                                                                  algo, outPathString.get()),
                             width=20)
            runAlgo.place(x=140, y=430)


    def buildGraphWindow(self):
        self.loadCsv(self.pathString.get())
        buidGraphWin = Toplevel(self.master)
        buidGraphWin.title("Build Graph")
        buidGraphWin.geometry("400x340")

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
        # lblGro = Label(buidGraphWin, text='Group By')
        # lblAgg = Label(buidGraphWin, text='Select Agg')

        lbSrc.place(x=100, y=180)
        lbDest.place(x=100, y=210)
        lblWei.place(x=100, y=240)
        # lblGro.place(x=100, y=270)
        # lblAgg.place(x=100, y=340)

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

        # listGroup = Listbox(buidGraphWin, selectmode="multiple", height=3, width=20, exportselection=False)
        # listGroup.pack(padx=5, pady=5,
        #                expand=YES)
        # listGroup.place(x=200, y=270)
        #
        # update = Button(buidGraphWin,
        #                 text='update',
        #                 command=lambda: (listGroup.delete(0, END), listGroup.insert(END, srcStr.get()),
        #                                  listGroup.insert(END, destStr.get()), listGroup.insert(END, weiStr.get())),
        #                 width=7)
        # update.place(x=30, y=280)
        #
        # listAggr = Listbox(buidGraphWin, selectmode="multiple", height=3, width=20, exportselection=False)
        # listAggr.curselection()
        # listAggr.pack(padx=5, pady=5,
        #               expand=YES)
        # for item in agg_function_list():
        #     listAggr.insert(END, item)
        # listAggr.place(x=200, y=340)
        # runGraph = Button(buidGraphWin,
        #                   text='Run',
        #                   command=lambda: self.createGraph(urlString.get(), userString.get(), passString.get(),
        #                                                    srcStr.get(),
        #                                                    destStr.get(), weiStr.get(),
        #                                                    [listGroup.get(i) for i in listGroup.curselection()],
        #                                                    [listAggr.get(i) for i in listAggr.curselection()]),
        #                   width=20)
        runGraph = Button(buidGraphWin,
                          text='Run',
                          command=lambda: self.createGraph(urlString.get(), userString.get(), passString.get(),
                                                           srcStr.get(),
                                                           destStr.get(), weiStr.get()), width=20)
        runGraph.place(x=140, y=300)

    def createGraph(self, url, user, password, src, dest, w, groupList=None, aggList=None):
        if w == '': w = None
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
        G = Graph(self.csv.get_df(), url, user, password, src, dest, w)
        # G.draw_graph(len(df))

    def playAlgorithems(self, listCol, algoType, outPath):
        print('temp')

    def loadCsv(self, csvFile):
        self.csv = Csv(csvFile)
