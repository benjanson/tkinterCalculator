from tkinter import *
from tkinter.messagebox import *
import math as m

import threading

# some fonts
font1= ('Linux Biolinum Keyboard O', 20, 'bold')
font = ('FreeMono', 20)



# important functions
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0, END)


def click_btn_function(event):
    global p
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)



    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            anser = eval(ex)
            textField.delete(0, END)
            textField.insert(0, anser)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)


# creating a window
window = Tk()
window.title('NORMAL CALCULATOR')
window.geometry('447x310')
# label

headingLabel = Label(window, text='CALCULATOR', font=font1,bg="gray36",fg='cornflower blue')
headingLabel.pack(side=TOP, pady=3,fill=X)
team = Label(window,text='''Green Team Members\n\nBENJOHNSON HEMBRAM,  AKASH ROUT,\n  SOMYA RANJAN SAHOO,  SAGAR MALLICk,\n  SESASMITA DAS,  SUBRAJEET GIRI, SIDDHART KISSAN''',font='P052')
headinLabel = Label(window, text="\n\n       To Calculate POWER use '+' sign \n \nExample: x power y = x+y \n\nThen press the '^' symbol",font='P052')

# textfiled
textField = Entry(window, font=font, bg="PaleGreen3",
      justify="right",fg='black')
textField.pack(side=TOP, pady=10, fill=X, padx=10)
# buttons

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='powder blue',
                     activeforeground='DarkOrange2',bg='gray13')
divideBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='<--', font=font, width=11, relief='ridge', activebackground='powder blue',
                  activeforeground='black',bg='cornflower blue', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='powder blue',
                     activeforeground='black',bg='cornflower blue', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all btns
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)


def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)


textField.bind('<Return>', enterClick)
#####################################################################################################
# Sc buttons......
scFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='powder blue',
                 activeforeground='black',bg='silver',fg='black')
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='powder blue',
                activeforeground='black',bg='silver',fg='black')
powBtn.grid(row=0, column=1)


factBtn = Button(scFrame, text='x!', font=font, width=5, relief='ridge', activebackground='powder blue',
                 activeforeground='black',bg='silver',fg='black')
factBtn.grid(row=0, column=2)

radBtn = Button(scFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='powder blue',
                activeforeground='black',bg='silver',fg='black')
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='powder blue',
                activeforeground='black',bg='silver',fg='black')
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='powder blue',
                activeforeground='black',bg='silver',fg='black')
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='powder blue',
                activeforeground='black',bg='silver',fg='black')
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='powder blue',
                activeforeground='black',bg='silver',fg='black')
tanBtn.grid(row=1, column=3)

normalcalc = True


def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))


    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))

    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split('+')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))

    textField.delete(0, END)
    textField.insert(0, answer)


def sc_click():
    global normalcalc
    team.pack_forget()
    buttonFrame.pack()
    headinLabel.pack_forget()
    textField.pack(side=TOP, pady=10, fill=X, padx=10)
    if normalcalc:
        # sc...
        buttonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side=TOP, pady=20)
        buttonFrame.pack(side=TOP)
        window.geometry('443x431')
        window.title('SCIENTIFIC CALCULATOR')

        print("show sc")
        normalcalc = False
    else:
        team.pack_forget()
        print('show normal')
        scFrame.pack_forget()
        window.geometry('447x310')
        window.title('NORMAL CALCULATOR')

        normalcalc = True
normalcalc = False
Details = True
def AboutUs():
    textField.pack_forget()
    global Details

    global normalcalc
    if Details:
        scFrame.pack_forget()
        buttonFrame.pack_forget()
        
        team.pack(side=TOP)
        headinLabel.pack_forget()
        Details=False
        normalcalc = True
    else:

        team.pack_forget()
        scFrame.pack_forget()
        buttonFrame.pack_forget()
        headinLabel.pack(side=TOP, pady=3, fill=X)
        Details=True
# end functions
# binding sc buttons
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

fontMenu = ('', 15,)
menubar = Menu(window, font=fontMenu)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)
mode.add_checkbutton(label="About Us", command=AboutUs)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()