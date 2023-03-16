from tkinter import * ;

root =Tk()
#ชื่อแอป
root.title("Name Project: HSW Gender.")

Label(bg="black").pack()
Label(text="App HSW Gender.",font=('Tahoma', 25, 'bold'),fg="white",bg="black").pack()
Label(text="เป็นแอปทำนายเพศของคุณ",font=('Tahoma', 20, 'bold'),fg="white",bg="black").pack()
Label(bg="black").pack()

frame = Frame(root,bd=3, height=10, width=10, relief=RIDGE, cursor="hand1" , highlightthickness=0)
frame.pack()

#row=0
Label(frame,text=" K ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=0)
Label(frame,text="").grid(row=0,column=1)
Label(frame,text=" Height ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=2)
Label(frame,text="").grid(row=0,column=3)
Label(frame,text=" Weight ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=4)
Label(frame,text="").grid(row=0,column=5)
Label(frame,text=" Size ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=6)
Label(frame,text="").grid(row=0,column=7)
Label(frame,text=" Sex ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=8)
Label(frame,text="").grid(row=0,column=9)


#row=1
Label(frame,text="1",font=('arial', 20)).grid(row=1,column=0)
Label(frame,text="").grid(row=1,column=1)
Label(frame,text="120",font=('arial', 20)).grid(row=1,column=2)
Label(frame,text="").grid(row=1,column=3)
Label(frame,text="40",font=('arial', 20)).grid(row=1,column=4)
Label(frame,text="").grid(row=1,column=8)
Label(frame,text="39",font=('arial', 20)).grid(row=1,column=6)
Label(frame,text="").grid(row=1,column=7)
Label(frame,text="Women",font=('arial', 20)).grid(row=1,column=8)
Label(frame,text="").grid(row=1,column=9)


#row=2
Label(frame,text="2",font=('arial', 20)).grid(row=2,column=0)
Label(frame,text="").grid(row=2,column=1)
Label(frame,text="130",font=('arial', 20)).grid(row=2,column=2)
Label(frame,text="").grid(row=2,column=3)
Label(frame,text="50",font=('arial', 20)).grid(row=2,column=4)
Label(frame,text="").grid(row=2,column=5)
Label(frame,text="40",font=('arial', 20)).grid(row=2,column=6)
Label(frame,text="").grid(row=2,column=7)
Label(frame,text="Women",font=('arial', 20)).grid(row=2,column=8)
Label(frame,text="").grid(row=2,column=9)


#row=3
Label(frame,text="3",font=('arial', 20)).grid(row=3,column=0)
Label(frame,text="").grid(row=3,column=1)
Label(frame,text="140",font=('arial', 20)).grid(row=3,column=2)
Label(frame,text="").grid(row=3,column=3)
Label(frame,text="60",font=('arial', 20)).grid(row=3,column=4)
Label(frame,text="").grid(row=3,column=5)
Label(frame,text="41",font=('arial', 20)).grid(row=3,column=6)
Label(frame,text="").grid(row=3,column=7)
Label(frame,text="Women",font=('arial', 20)).grid(row=3,column=8)
Label(frame,text="").grid(row=3,column=9)


#row=4
Label(frame,text="4",font=('arial', 20)).grid(row=4,column=0)
Label(frame,text="").grid(row=4,column=1)
Label(frame,text="150",font=('arial', 20)).grid(row=4,column=2)
Label(frame,text="").grid(row=4,column=3)
Label(frame,text="70",font=('arial', 20)).grid(row=4,column=4)
Label(frame,text="").grid(row=4,column=5)
Label(frame,text="42",font=('arial', 20)).grid(row=4,column=6)
Label(frame,text="").grid(row=4,column=7)
Label(frame,text="Women",font=('arial', 20)).grid(row=4,column=8)
Label(frame,text="").grid(row=4,column=9)


#row=5
Label(frame,text="5",font=('arial', 20)).grid(row=5,column=0)
Label(frame,text="").grid(row=5,column=1)
Label(frame,text="160",font=('arial', 20)).grid(row=5,column=2)
Label(frame,text="").grid(row=5,column=3)
Label(frame,text="80",font=('arial', 20)).grid(row=5,column=4)
Label(frame,text="").grid(row=5,column=5)
Label(frame,text="43",font=('arial', 20)).grid(row=5,column=6)
Label(frame,text="").grid(row=5,column=7)
Label(frame,text="Women",font=('arial', 20)).grid(row=5,column=8)
Label(frame,text="").grid(row=5,column=9)


#row=6
Label(frame,text="6",font=('arial', 20)).grid(row=6,column=0)
Label(frame,text="").grid(row=6,column=1)
Label(frame,text="170",font=('arial', 20)).grid(row=6,column=2)
Label(frame,text="").grid(row=6,column=3)
Label(frame,text="90",font=('arial', 20)).grid(row=6,column=4)
Label(frame,text="").grid(row=6,column=5)
Label(frame,text="44",font=('arial', 20)).grid(row=6,column=6)
Label(frame,text="").grid(row=6,column=7)
Label(frame,text="Man",font=('arial', 20)).grid(row=6,column=8)
Label(frame,text="").grid(row=6,column=9)


#row=7
Label(frame,text="7",font=('arial', 20)).grid(row=7,column=0)
Label(frame,text="").grid(row=7,column=1)
Label(frame,text="180",font=('arial', 20)).grid(row=7,column=2)
Label(frame,text="").grid(row=7,column=3)
Label(frame,text="100",font=('arial', 20)).grid(row=7,column=4)
Label(frame,text="").grid(row=7,column=5)
Label(frame,text="45",font=('arial', 20)).grid(row=7,column=6)
Label(frame,text="").grid(row=7,column=7)
Label(frame,text="Man",font=('arial', 20)).grid(row=7,column=8)
Label(frame,text="").grid(row=7,column=9)

#row=8
Label(frame,text="8",font=('arial', 20)).grid(row=8,column=0)
Label(frame,text="").grid(row=8,column=1)
Label(frame,text="190",font=('arial', 20)).grid(row=8,column=2)
Label(frame,text="").grid(row=8,column=3)
Label(frame,text="110",font=('arial', 20)).grid(row=8,column=4)
Label(frame,text="").grid(row=8,column=5)
Label(frame,text="46",font=('arial', 20)).grid(row=8,column=6)
Label(frame,text="").grid(row=8,column=7)
Label(frame,text="Man",font=('arial', 20)).grid(row=8,column=8)
Label(frame,text="").grid(row=8,column=9)

#row=9
Label(frame,text="9",font=('arial', 20)).grid(row=9,column=0)
Label(frame,text="").grid(row=9,column=1)
Label(frame,text="200",font=('arial', 20)).grid(row=9,column=2)
Label(frame,text="").grid(row=9,column=3)
Label(frame,text="120",font=('arial', 20)).grid(row=9,column=4)
Label(frame,text="").grid(row=9,column=5)
Label(frame,text="47",font=('arial', 20)).grid(row=9,column=6)
Label(frame,text="").grid(row=9,column=7)
Label(frame,text="Man",font=('arial', 20)).grid(row=9,column=8)
Label(frame,text="").grid(row=9,column=9)


#row=10
Label(frame,text="10",font=('arial', 20)).grid(row=10,column=0)
Label(frame,text="").grid(row=10,column=1)
Label(frame,text="210",font=('arial', 20)).grid(row=10,column=2)
Label(frame,text="").grid(row=10,column=3)
Label(frame,text="130",font=('arial', 20)).grid(row=10,column=4)
Label(frame,text="").grid(row=10,column=5)
Label(frame,text="48",font=('arial', 20)).grid(row=10,column=6)
Label(frame,text="").grid(row=10,column=7)
Label(frame,text="Man",font=('arial', 20)).grid(row=10,column=8)
Label(frame,text="").grid(row=6,column=10)



frame2 = Frame(root,bd=3, height=10, width=10, relief=RIDGE, cursor="hand1" , highlightthickness=1)
frame2.pack()

#row=0
Label(frame2,text=" K ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=0)
Label(frame2,text=" Height ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=1)

Label(frame2,text="").grid(row=0,column=2)
Label(frame2,text=" Weight ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=3)

Label(frame2,text="").grid(row=0,column=4)
Label(frame2,text=" Size ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=5)

Label(frame2,text="").grid(row=0,column=6)
Label(frame2,text=" Sex ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=7)


#row=1
txt = IntVar()
#txt = StringVar()
mytxt = Entry(frame2,textvariable=txt,font=('arial', 20))
mytxt.grid(row=1,column=0)

txt01 = IntVar()
#txt01 = StringVar()
mytxt01 = Entry(frame2,textvariable=txt01,font=('arial', 20))
mytxt01.grid(row=1,column=1)

txt02 = IntVar()
#txt02 = StringVar()
mytxt02 = Entry(frame2,textvariable=txt02,font=('arial', 20))
mytxt02.grid(row=1,column=3)

txt03 = IntVar()
mytxt03 = Entry(frame2,textvariable=txt03,font=('arial', 20))
mytxt03.grid(row=1,column=5)

Label(frame2,text="").grid(row=1,column=2)
Label(frame2,text="").grid(row=1,column=4)
Label(frame2,text="").grid(row=1,column=6)


#row=3 , showtxt
def showText():
    # Main Fuction
    Label03 = Label(frame2,text="M/W",font=('arial', 20))
    Label03.grid(row=1,column=7)



def Del_txt():
    mytxt.delete(0,END)
    mytxt01.delete(0,END)
    mytxt02.delete(0,END)
    mytxt03.delete(0,END)



#row=4
showText = Button(frame2,text=' ทำนาย ', command=showText, bg="black",font=('arial', 15),fg="white").grid(row=3,column=3)
Del_txt = Button(frame2,text=' ลบ ', command=Del_txt, bg="black",font=('arial', 15),fg="white").grid(row=3,column=5)

#กำหนดขนาดหน้าต่าง พื้นหลังสีดำ
root.configure(background='black')
root.geometry("1400x700")
root.mainloop()