from tkinter import *

class stock_tk:
    buff = ""
    value = []
    stock_list = []
    def __init__(self):
        self.root = Tk()
        self.root.title("win")
        self.root.geometry('800x600')
        self.root.resizable(width=True, height=True)
        self.root.aspect(minNumer=300, maxNumer=1000, minDenom=50, maxDenom=333)
        # 创建一个工具菜单
        self.menubar = Menu(self.root)
        self.menubar.add_command(label='打开', command=self.addNew)
        self.menubar.add_command(label='关闭', command=self.delSelect)
        self.root.config(menu=self.menubar)

        self.lf = LabelFrame(self.root,text="label frame",height= 400,width=300)
        self.lf.grid(row=0, column=0)
        self.putStockInfo()

        self.root.mainloop()


    def addNew(self):
        top = addStock(self.value)
        self.root.wait_window(top)
        print(self.value)
        self.label3 = Label(self.lf,text=self.value)
        self.label3.grid(row=1,column=0)

    def delSelect(self):
         pass

    def putStockInfo(self):
        '''展示股票信息'''
        self.getStockInfoFromBase()
        i = 0
        for each in self.stock_list:
            label = Label(self.lf,text=each)
            label.grid(row=i,column=0,textvariable=)

            label2 = Label(self.lf,text=each)
            label2.grid(row=i,column=1)
            i +=1

        pass

    def getStockInfoFromBase(self):
        '''从数据库中获得股票信息'''
        self.stock_list.append('sh601890')
        self.stock_list.append('sh601891')
        pass

class addStock(Toplevel):
    def __init__(self,value):
        Toplevel.__init__(self)
        self.val = StringVar()
        self.title = "请输入股票代码"
        self.geometry('300x200')
        self.ent = Entry(self)
        self.ent.pack()
        self.but = Button(self,text="确定",command=lambda:self.callback(value))
        self.but.pack()

    def callback(self,val):
        val.append(self.ent.get())
        print(self.ent.get())
        self.destroy()


st=stock_tk()