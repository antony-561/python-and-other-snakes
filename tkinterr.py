from tkinter import *

root = Tk()
root.geometry("800x600")

genV = IntVar()


label1 = Label(root,text = "Student Registration Form")
label1.pack()
label2 = Label(root,text = "Name:")
label2.pack()
nameIn = Entry(root,width = 50)
nameIn.pack()
label3 = Label(root,text = "Course:")
label3.pack()
courseIn = Entry(root,width = 50)
courseIn.pack()
label4 = Label(root,text = "Sem:")
label4.pack()
semIn = Entry(root,width = 50)
semIn.pack()
genLabel = Label(root,text = "Gender:")
genLabel.pack()
maleRadio = Radiobutton(root,variable = genV,value = "Male", text = "Male")
maleRadio.pack()
femaleRadio = Radiobutton(root,variable = genV,value = "Female",text = "Female")
femaleRadio.pack()

subBtn = Button(root,text = "Submit", pady = 8)
subBtn.pack()


mainloop()
