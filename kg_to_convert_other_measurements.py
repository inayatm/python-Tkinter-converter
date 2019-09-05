from tkinter import *


frame=Tk()
frame.title("Converter")
def kgTo():
    grams_text.delete(1.0,END)
    pounds_text.delete(1.0,END)
    ounces_text.delete(1.0,END)
    grams=int(en_value.get())*1000
    grams_text.insert(END,str(grams)+" grams")
    pounds=int(en_value.get())*2.20462
    pounds_text.insert(END,str(pounds)+" pounds")
    ounce=int(en_value.get())*35.274
    ounces_text.insert(END,str(ounce)+" ounces")

def clearFields():
    entry_filed.delete(0,'end')
    grams_text.delete(1.0,END)
    pounds_text.delete(1.0,END)
    ounces_text.delete(1.0,END)

KG_lable=Label(frame,text="KG")
en_value=StringVar()
entry_filed=Entry(frame,textvariable=en_value)
#entry_filed.config(height=0,width=15)
convert_button=Button(frame,text="convert",command=kgTo)
clear_button=Button(frame,text="clear",command=clearFields)
grams_text=Text(frame,height=0,width=15)
pounds_text=Text(frame,height=0,width=15)
ounces_text=Text(frame,height=0,width=15)


KG_lable.grid(row=0,column=1)
entry_filed.grid(row=0,column=2)
clear_button.grid(row=0,column=3)
grams_text.grid(row=2,column=1)
pounds_text.grid(row=2,column=2)
ounces_text.grid(row=2,column=3)
convert_button.grid(row=3,column=2)


frame.mainloop()
