from tkinter import *
from itertools import cycle

alp = 'abcçdeəfgğhxıijkqlmnoöprsştuüvyz '
root = Tk()

root.geometry('500x300')
root.resizable(0,0)
root.title("Atyən") # Atyən   \U0001F49C

Label(root, text ='Şifrələmə və Deşifrələmə', font = 'arial 20 bold').pack()

Label(root, text ='Vijner ', font = 'arial 20 bold').pack(side =BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(text:str, keytext:str):
    f = lambda arg: alp[(alp.index(arg[0])+alp.index(arg[1]) %33) %33]
    return ''.join(map(f, zip(text.lower(), cycle(keytext.lower()))))

def Decode(coded_text, keytext):
    f = lambda arg: alp[alp.index(arg[0])-alp.index(arg[1])%33]
    return ''.join(map(f, zip(coded_text.lower(), cycle(keytext.lower()))))


def Mode():
    if(mode.get() == 's'):
        Result.set(Encode(Text.get(),private_key.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(Text.get(),private_key.get()))
    else:
        Result.set('Mod Təyin Edilməyib')


def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(root, font= 'arial 12 bold', text='Mətin').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 12 bold', text ='Açar').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MOD(s-Şifrələmə, d-Deşifrələmə)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

Button(root, font = 'arial 10 bold', text = 'Nəticə'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(root, font = 'arial 10 bold' ,text ='Təmizləmək' ,width =10, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(root, font = 'arial 10 bold',text= 'Çıxış' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()
