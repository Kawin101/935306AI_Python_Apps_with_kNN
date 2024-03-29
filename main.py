# tkinter GUI
from tkinter import *
from sklearn.datasets import clear_data_home ;

# import library for kNN Function
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

# Create a function to update the GUI with data from the CSV file
def update_gui():
    data = pd.read_csv('Dataset_01.csv')  # Load data from the CSV file

    # Loop through the data and update the GUI elements
    for index, row in data.iterrows():
        row_data = [index + 1] + list(row)  # Extract row data
        for col, value in enumerate(row_data):
            Label(frame, text=value, font=('arial', 20)).grid(row=index + 1, column=col)

root =Tk()
#ชื่อแอป
root.title("Project: HSW Gender App.")

Label(bg="black").pack()
Label(text="HSW Gender App",font=('Tahoma', 25, 'bold'),fg="white",bg="black").pack()
Label(text="เป็นแอปทำนายเพศของคุณ",font=('Tahoma', 20, 'bold'),fg="white",bg="black").pack()
Label(bg="black").pack()

frame = Frame(root,bd=3, height=10, width=10, relief=RIDGE, cursor="hand1" , highlightthickness=0)
frame.pack()

frame2 = Frame(root,bd=3, height=10, width=10, relief=RIDGE, cursor="hand1" , highlightthickness=1)
frame2.pack()

class  guiHeader(): 
    print("gui header is doing!")
    Label(frame,text=" K ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=0)
    Label(frame,text="").grid(row=0,column=1)
    Label(frame,text=" Height ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=2)
    Label(frame,text="").grid(row=0,column=3)
    Label(frame,text=" Weight ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=4)
    Label(frame,text="").grid(row=0,column=5)
    Label(frame,text=" Size ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=6)
    Label(frame,text="").grid(row=0,column=7)
    Label(frame,text=" Age ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=8)
    Label(frame,text="").grid(row=0,column=9)
    Label(frame,text=" Sex ",bg = "white",font=('arial', 20,'bold')).grid(row=0,column=10)
    Label(frame,text="").grid(row=0,column=11)
    print("gui header is done!")

class guiBodyDataTable():
    print("gui body data in table is doing!")
    #row=1
    Label(frame,text="1",font=('arial', 20)).grid(row=1,column=0)
    Label(frame,text="").grid(row=1,column=1)
    Label(frame,text="120",font=('arial', 20)).grid(row=1,column=2)
    Label(frame,text="").grid(row=1,column=3)
    Label(frame,text="40",font=('arial', 20)).grid(row=1,column=4)
    Label(frame,text="").grid(row=1,column=5)
    Label(frame,text="39",font=('arial', 20)).grid(row=1,column=6)
    Label(frame,text="").grid(row=1,column=7)
    Label(frame,text="25",font=('arial', 20)).grid(row=1,column=8)
    Label(frame,text="").grid(row=1,column=9)
    Label(frame,text="Women",font=('arial', 20)).grid(row=1,column=10)
    Label(frame,text="").grid(row=1,column=11)
    #row=2
    Label(frame,text="2",font=('arial', 20)).grid(row=2,column=0)
    Label(frame,text="").grid(row=2,column=1)
    Label(frame,text="130",font=('arial', 20)).grid(row=2,column=2)
    Label(frame,text="").grid(row=2,column=3)
    Label(frame,text="50",font=('arial', 20)).grid(row=2,column=4)
    Label(frame,text="").grid(row=2,column=5)
    Label(frame,text="40",font=('arial', 20)).grid(row=2,column=6)
    Label(frame,text="").grid(row=2,column=7)
    Label(frame,text="30",font=('arial', 20)).grid(row=2,column=8)
    Label(frame,text="").grid(row=2,column=9)
    Label(frame,text="Women",font=('arial', 20)).grid(row=2,column=10)
    Label(frame,text="").grid(row=2,column=11)
    #row=3
    Label(frame,text="3",font=('arial', 20)).grid(row=3,column=0)
    Label(frame,text="").grid(row=3,column=1)
    Label(frame,text="140",font=('arial', 20)).grid(row=3,column=2)
    Label(frame,text="").grid(row=3,column=3)
    Label(frame,text="60",font=('arial', 20)).grid(row=3,column=4)
    Label(frame,text="").grid(row=3,column=5)
    Label(frame,text="41",font=('arial', 20)).grid(row=3,column=6)
    Label(frame,text="").grid(row=3,column=7)
    Label(frame,text="35",font=('arial', 20)).grid(row=3,column=8)
    Label(frame,text="").grid(row=3,column=9)
    Label(frame,text="Women",font=('arial', 20)).grid(row=3,column=10)
    Label(frame,text="").grid(row=3,column=11)
    #row=4
    Label(frame,text="4",font=('arial', 20)).grid(row=4,column=0)
    Label(frame,text="").grid(row=4,column=1)
    Label(frame,text="150",font=('arial', 20)).grid(row=4,column=2)
    Label(frame,text="").grid(row=4,column=3)
    Label(frame,text="70",font=('arial', 20)).grid(row=4,column=4)
    Label(frame,text="").grid(row=4,column=5)
    Label(frame,text="42",font=('arial', 20)).grid(row=4,column=6)
    Label(frame,text="").grid(row=4,column=7)
    Label(frame,text="40",font=('arial', 20)).grid(row=4,column=8)
    Label(frame,text="").grid(row=4,column=9)
    Label(frame,text="Women",font=('arial', 20)).grid(row=4,column=10)
    Label(frame,text="").grid(row=4,column=11)
    #row=5
    Label(frame,text="5",font=('arial', 20)).grid(row=5,column=0)
    Label(frame,text="").grid(row=5,column=1)
    Label(frame,text="160",font=('arial', 20)).grid(row=5,column=2)
    Label(frame,text="").grid(row=5,column=3)
    Label(frame,text="80",font=('arial', 20)).grid(row=5,column=4)
    Label(frame,text="").grid(row=5,column=5)
    Label(frame,text="43",font=('arial', 20)).grid(row=5,column=6)
    Label(frame,text="").grid(row=5,column=7)
    Label(frame,text="45",font=('arial', 20)).grid(row=5,column=8)
    Label(frame,text="").grid(row=5,column=9)
    Label(frame,text="Women",font=('arial', 20)).grid(row=5,column=10)
    Label(frame,text="").grid(row=5,column=11)
    #row=6
    Label(frame,text="6",font=('arial', 20)).grid(row=6,column=0)
    Label(frame,text="").grid(row=6,column=1)
    Label(frame,text="170",font=('arial', 20)).grid(row=6,column=2)
    Label(frame,text="").grid(row=6,column=3)
    Label(frame,text="90",font=('arial', 20)).grid(row=6,column=4)
    Label(frame,text="").grid(row=6,column=5)
    Label(frame,text="44",font=('arial', 20)).grid(row=6,column=6)
    Label(frame,text="").grid(row=6,column=7)
    Label(frame,text="50",font=('arial', 20)).grid(row=6,column=8)
    Label(frame,text="").grid(row=6,column=9)
    Label(frame,text="Man",font=('arial', 20)).grid(row=6,column=10)
    Label(frame,text="").grid(row=6,column=11)
    #row=7
    Label(frame,text="7",font=('arial', 20)).grid(row=7,column=0)
    Label(frame,text="").grid(row=7,column=1)
    Label(frame,text="180",font=('arial', 20)).grid(row=7,column=2)
    Label(frame,text="").grid(row=7,column=3)
    Label(frame,text="100",font=('arial', 20)).grid(row=7,column=4)
    Label(frame,text="").grid(row=7,column=5)
    Label(frame,text="45",font=('arial', 20)).grid(row=7,column=6)
    Label(frame,text="").grid(row=7,column=7)
    Label(frame,text="55",font=('arial', 20)).grid(row=7,column=8)
    Label(frame,text="").grid(row=7,column=9)
    Label(frame,text="Man",font=('arial', 20)).grid(row=7,column=10)
    Label(frame,text="").grid(row=7,column=11)
    #row=8
    Label(frame,text="8",font=('arial', 20)).grid(row=8,column=0)
    Label(frame,text="").grid(row=8,column=1)
    Label(frame,text="190",font=('arial', 20)).grid(row=8,column=2)
    Label(frame,text="").grid(row=8,column=3)
    Label(frame,text="110",font=('arial', 20)).grid(row=8,column=4)
    Label(frame,text="").grid(row=8,column=5)
    Label(frame,text="46",font=('arial', 20)).grid(row=8,column=6)
    Label(frame,text="").grid(row=8,column=7)
    Label(frame,text="60",font=('arial', 20)).grid(row=8,column=8)
    Label(frame,text="").grid(row=8,column=9)
    Label(frame,text="Man",font=('arial', 20)).grid(row=8,column=10)
    Label(frame,text="").grid(row=8,column=11)
    #row=9
    Label(frame,text="9",font=('arial', 20)).grid(row=9,column=0)
    Label(frame,text="").grid(row=9,column=1)
    Label(frame,text="200",font=('arial', 20)).grid(row=9,column=2)
    Label(frame,text="").grid(row=9,column=3)
    Label(frame,text="120",font=('arial', 20)).grid(row=9,column=4)
    Label(frame,text="").grid(row=9,column=5)
    Label(frame,text="47",font=('arial', 20)).grid(row=9,column=6)
    Label(frame,text="").grid(row=9,column=7)
    Label(frame,text="65",font=('arial', 20)).grid(row=9,column=8)
    Label(frame,text="").grid(row=9,column=9)
    Label(frame,text="Man",font=('arial', 20)).grid(row=9,column=10)
    Label(frame,text="").grid(row=9,column=11)
    #row=10
    Label(frame,text="10",font=('arial', 20)).grid(row=10,column=0)
    Label(frame,text="").grid(row=10,column=1)
    Label(frame,text="210",font=('arial', 20)).grid(row=10,column=2)
    Label(frame,text="").grid(row=10,column=3)
    Label(frame,text="130",font=('arial', 20)).grid(row=10,column=4)
    Label(frame,text="").grid(row=10,column=5)
    Label(frame,text="48",font=('arial', 20)).grid(row=10,column=6)
    Label(frame,text="").grid(row=10,column=7)
    Label(frame,text="70",font=('arial', 20)).grid(row=10,column=8)
    Label(frame,text="").grid(row=10,column=9)
    Label(frame,text="Man",font=('arial', 20)).grid(row=10,column=10)
    Label(frame,text="").grid(row=10,column=11)
    print("gui body data in table is done!")

class guiFootHeader():
    print("gui foot header is doing!")
    #row=0
    Label(frame2,text=" K ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=0)
    Label(frame2,text=" Height ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=1)

    Label(frame2,text="").grid(row=0,column=2)
    Label(frame2,text=" Weight ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=3)

    Label(frame2,text="").grid(row=0,column=4)
    Label(frame2,text=" Size ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=5)

    Label(frame2,text="").grid(row=0,column=6)
    Label(frame2,text=" Age ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=7)

    Label(frame2,text="").grid(row=0,column=8)
    Label(frame2,text=" Sex ",bg = "white",font=('arial', 20, 'bold')).grid(row=0,column=9)

    #row=1
    Neighbors_input = IntVar(value=5)
    #txt = StringVar()
    Neighbors_Entry = Entry(frame2,textvariable=Neighbors_input,font=('arial', 15))
    Neighbors_Entry.grid(row=1,column=0)

    Height_input = IntVar(value=175)
    #txt01 = StringVar()
    Height_Entry = Entry(frame2,textvariable=Height_input,font=('arial', 15))
    Height_Entry.grid(row=1,column=1)

    Weight_input = IntVar(value=75)
    #txt02 = StringVar()
    Weight_Entry = Entry(frame2,textvariable=Weight_input,font=('arial', 15))
    Weight_Entry.grid(row=1,column=3)

    Size_input = IntVar(value=44)
    Size_Entry = Entry(frame2,textvariable=Size_input,font=('arial', 15))
    Size_Entry.grid(row=1,column=5)

    Age_input = IntVar(value=28)
    Age_Entry = Entry(frame2,textvariable=Age_input,font=('arial', 15))
    Age_Entry.grid(row=1,column=7)

    Label(frame2,text="").grid(row=1,column=2)
    Label(frame2,text="").grid(row=1,column=4)
    Label(frame2,text="").grid(row=1,column=6)
    Label(frame2,text="").grid(row=1,column=8)
    print("gui foot header is done!")
    #row=3 , showtxet

class mainFunction():
    def listToString(s):
        print("main fuction listToString method is working!")
        # Credit: https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
        # initialize an empty string
        str1 = ""
    
        # traverse in the string
        for ele in s:
            str1 += ele

        print("main fuction listToString method is work done!")
        # return string
        return str1
        
    def showText():
        print("main fuction showText method is working!")

        # Reset gui button display to default(null)!
        guiFootHeader.Label03 = Label(frame2,text='               ',font=('arial', 20))
        guiFootHeader.Label03.grid(row=1,column=9)

        # k-Nearest Neighbors Fuction
        Neighbors = guiFootHeader.Neighbors_input.get()
        Weight = guiFootHeader.Weight_input.get()
        Height = guiFootHeader.Height_input.get()
        Size = guiFootHeader.Size_input.get()
        Age = guiFootHeader.Age_input.get()

        fileDataset = 'Dataset_01.csv'
        data = pd.read_csv(fileDataset)

        # แปลงข้อมูลจากไฟล์ตัวอักษร เป็น ตัวเลข (0 = หญิง, 1 = ชาย)
        # data['Gender'] = data.Gender.replace(['Women','Men'],[0,1])

        # How to fix error? Let's do follows this https://stackoverflow.com/questions/69326639/sklearn-warning-valid-feature-names-in-version-1-0
        x = data[['Height', 'Weight', 'Size', 'Age']].values # conversion of X into array
        y = data['Gender']
        
        # Set data between train and test
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=10)
    
        # K max = 7 becase train_size = 0.7 in 1.0 (70% in 100%)

        # print(x_test.count())
        # Define K value, Set model between train and test
        kNN_model = KNeighborsClassifier(n_neighbors=Neighbors)
        kNN_model = kNN_model.fit(x_train, y_train)
        kNNScore = kNN_model.score(x_test, y_test)
        # print(kNNScore)

        # Input data and Show Output
        StartkNN = [ [Height,Weight,Size,Age]]
        Sex = kNN_model.predict(StartkNN)
        # Covert data format text list to string, ['A','B','C', ...] to A, B, C, ...
        ShowSex = (mainFunction.listToString(Sex))
        # Move data in Showsex to ShowSextoGui, ShowSex = Women -> ShowSextoGui's Women too!
        ShowSextoGui = ShowSex
        # Get display data on Gui
        Label03 = Label(frame2,text=ShowSextoGui,font=('arial', 20))
        Label03.grid(row=1,column=9)
        print("main fuction showText method is work done!")
        # print(ShowSex)
        return ShowSextoGui
        # print(kNN_model.predict(StartkNN))
        # Label03 = Label(frame2,text="M/W",font=('arial', 20))
        # Label03.grid(row=1,column=7)

    def Del_txt():
        print("main fuction Del_txt method is working!")
        guiFootHeader.Neighbors_Entry.delete(0,END)
        guiFootHeader.Height_Entry.delete(0,END)
        guiFootHeader.Weight_Entry.delete(0,END)
        guiFootHeader.Size_Entry.delete(0,END)
        guiFootHeader.Age_Entry.delete(0,END)
        guiFootHeader.Label03 = Label(frame2,text='               ',font=('arial', 20))
        guiFootHeader.Label03.grid(row=1,column=9)
        print("main fuction Del_txt method is work done!")

class guiFootButton():
    print("gui foot button is doing!")
    #row=4
    showText = Button(frame2,text=' ทำนาย ', command=mainFunction.showText, bg="black",font=('arial', 15),fg="white").grid(row=3,column=3)
    Del_txt = Button(frame2,text=' ลบ ', command=mainFunction.Del_txt, bg="black",font=('arial', 15),fg="white").grid(row=3,column=5)
    print("gui foot button is done!")

# Add a button to trigger the update
update_button = Button(root, text="Update Data", command=update_gui)
update_button.pack()

# Configure the GUI and start the main loop
# กำหนดขนาดหน้าต่าง พื้นหลังสีดำ
root.configure(background='black')
root.geometry("1400x700")
root.mainloop()