import tkinter
import tkinter.messagebox
import _sqlite3


def Insert(name, phone):
    c.execute('insert into people values(?,?)', (name, phone))


def Del(name):
    c.execute("delete from people where name = '%s'" % name)


def Update(name, phone):
    c.execute('update people set phone = (?) where  name = (?)', (phone, name))


def Serch():
    c.execute('select * from people')
    li = c.fetchall()
    return li


def Serchone(name):
    c.execute("select phone from people where people.name = '%s'" % name)
    return c.fetchall()


def add():
    def addDate():
        n = name.get()
        p = ph.get()
        if n == '' or p == '':
            tkinter.messagebox.showerror("错误", "信息有不能为空!")
            win1.destroy()
        else:
            Insert(n, p)
            tkinter.messagebox.showinfo("成功", "新增联系人成功")
            win1.destroy()

    # 设置窗口位置
    # 不能使用两次Tk（）去创建窗体，因为tkinter中只能有一个主线程，
    win1 = tkinter.Toplevel()
    win1.title('新增联系人')
    win1.geometry('500x300')
    sw = win1.winfo_screenwidth()
    sh = win1.winfo_screenheight()
    win1.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))
    # 欢迎语
    l = tkinter.Label(win1, text='欢迎进入新增页面', font=('华文行楷', 20), fg='purple')
    l.place(relx=0.5, rely=0.1, anchor='center')
    # 提示语
    l = tkinter.Label(win1, text='请输入联系人信息', font=('正楷', 15))
    l.place(relx=0.5, rely=0.3, anchor='center')
    # 姓名输入框
    Lname = tkinter.Label(win1, text='姓名:')
    Lname.place(relx=0.2, rely=0.5, anchor='center')
    nu = tkinter.StringVar()
    name = tkinter.Entry(win1, textvariable=nu)
    name.place(relx=0.25, rely=0.47, width=70)
    # 电话号输入框
    Lph = tkinter.Label(win1, text='电话:')
    Lph.place(relx=0.50, rely=0.5, anchor='center')
    nu = tkinter.StringVar()
    ph = tkinter.Entry(win1, textvariable=nu)
    ph.place(relx=0.55, rely=0.47, width=140)
    # 按钮
    b = tkinter.Button(win1, text='添加', width=10, height=3, bg='gray', command=addDate)
    b.place(relx=0, rely=1, anchor='sw')
    b2 = tkinter.Button(win1, text='退出', width=10, height=3, bg='gray', command=win1.destroy)
    b2.place(relx=1, rely=1, anchor='se')


def find():
    # 设置窗口位置
    # 不能使用两次Tk（）去创建窗体，因为tkinter中只能有一个主线程，
    win2 = tkinter.Toplevel()
    win2.title('查询联系人')
    win2.geometry('500x300')
    sw = win2.winfo_screenwidth()
    sh = win2.winfo_screenheight()
    win2.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))
    # 欢迎语
    l = tkinter.Label(win2, text='欢迎进入查询页面', font=('华文行楷', 20), fg='purple')
    l.place(relx=0.5, rely=0.1, anchor='center')

    ListB = tkinter.Listbox(win2)
    ListB.place(relx=0.3, rely=0.3, anchor='nw', width=200)
    li = Serch()
    for item in li:
        ListB.insert(0, item)

    # 按钮
    b2 = tkinter.Button(win2, text='退出', width=10, height=3, bg='gray', command=win2.destroy)
    b2.place(relx=1, rely=1, anchor='se')


def delete():
    def show():
        li = Serchone(name.get())
        if len(li) == 0:
            tkinter.messagebox.showerror("错误", "此人不存在")
            win3.destroy()
        pth = li[0]
        print(pth)
        ph = tkinter.Label(win3, text='%s' % pth)
        ph.place(relx=0.55, rely=0.5, anchor='center')

    def delDate():
        Del(name.get())
        tkinter.messagebox.showerror("成功", "删除成功")
        win3.destroy()

    # 设置窗口位置
    # 不能使用两次Tk（）去创建窗体，因为tkinter中只能有一个主线程，
    win3 = tkinter.Toplevel()
    win3.title('删除联系人')
    win3.geometry('500x300')
    sw = win3.winfo_screenwidth()
    sh = win3.winfo_screenheight()
    win3.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))
    # 欢迎语
    l = tkinter.Label(win3, text='欢迎进入删除页面', font=('华文行楷', 20), fg='purple')
    l.place(relx=0.5, rely=0.1, anchor='center')
    # 姓名输入框
    Lname = tkinter.Label(win3, text='姓名:')
    Lname.place(relx=0.2, rely=0.5, anchor='center')
    nu = tkinter.StringVar()
    name = tkinter.Entry(win3, textvariable=nu)
    name.place(relx=0.25, rely=0.47, width=70)
    # 电话号展示框
    Lph = tkinter.Label(win3, text='电话:')
    Lph.place(relx=0.50, rely=0.5, anchor='center')

    # 按钮
    b = tkinter.Button(win3, text='查询', width=10, height=3, bg='gray', command=show)
    b.place(relx=0, rely=1, anchor='sw')
    b = tkinter.Button(win3, text='确认删除', width=10, height=3, bg='gray', command=delDate)
    b.place(relx=0.15, rely=1, anchor='sw')
    b2 = tkinter.Button(win3, text='退出', width=10, height=3, bg='gray', command=win3.destroy)
    b2.place(relx=1, rely=1, anchor='se')


if __name__ == '__main__':
    def secondMain():
        op = v.get()
        if op == 1:
            add()
        elif op == 2:
            find()
        elif op == 3:
            """修改和添加的类似就不画了"""
            # change()
        elif op == 4:
            delete()


    # 数据库
    conn = _sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("create table people(name char(10),phone char(20))")

    # 设置窗口位置
    win = tkinter.Tk()
    win.title('我的通讯录')
    win.geometry('500x300')
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    win.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))
    # 欢迎语
    l = tkinter.Label(win, text='欢迎进入通讯录', font=('华文行楷', 20), fg='green')
    l.place(relx=0.5, rely=0.1, anchor='center')
    # 单选按钮
    choose = [('1.添加联系人', 1), ('2.查询联系人', 2), ('3.修改联系人', 3), ('4.删除联系人', 4)]
    v = tkinter.IntVar()
    v.set(1)
    x, y = 0.5, 0.2,
    for a, b in choose:
        cc = tkinter.Radiobutton(win, text=a, variable=v, value=b)
        cc.place(relx=x, rely=y, anchor='center')
        y += 0.1
    # 按钮
    b = tkinter.Button(win, text='确定', width=10, height=3, bg='gray', command=secondMain)
    b.place(relx=0, rely=1, anchor='sw')
    b2 = tkinter.Button(win, text='退出', width=10, height=3, bg='gray', command=win.quit)
    b2.place(relx=1, rely=1, anchor='se')

    win.mainloop()