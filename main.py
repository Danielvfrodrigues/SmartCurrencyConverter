from tkinter import *
import requests
from datetime import datetime

root = Tk()
root.title('SmartCurrency')
root.iconbitmap('logo.ico')
root.geometry("500x350")
root.resizable(False, False)


def convert():
    moeda1 = var_from.get()
    moeda2 = var_to.get()

    if moeda1 == moeda2:
        display.delete(0, 'end')
        display.insert(0, 'Take different currencies')
        display.config(fg='#d40a00', justify='center')
    else:
        url = "https://economia.awesomeapi.com.br/last/" + moeda1 + '-' + moeda2

        req = requests.get(url)
        req_dic = req.json()

        combination = moeda1+moeda2

        cotacao = float(req_dic[combination]['bid'])
        now = datetime.now()

        display.delete(0, 'end')
        display.config(fg='#000000', justify='right')
        display.insert(0, var_to.get()+' '+'%.2f' % round(cotacao, 2))
        print(now)


# Label
title = Label(root, text='SmartCurrency Converter', font=('Helvetica', 16))
title.pack(pady=20)


# Radio Frame
radio_frame = Frame(root)
radio_frame.pack()

# Label Frame
lf_from = LabelFrame(radio_frame, text="FROM")
lf_from.pack(side="left", anchor='n', padx=(5, 20))

lf_to = LabelFrame(radio_frame, text="TO")
lf_to.pack(side="left", anchor='n')

var_from = StringVar()
var_to = StringVar()
var_from.set('USD')
var_to.set('BRL')  # need to use v.set and v.get to
# set and get the value of this variable
radiobutton_from1 = Radiobutton(lf_from,
                                text="USD",
                                variable=var_from, value='USD', padx=25)
radiobutton_from2 = Radiobutton(lf_from,
                                text="BRL",
                                variable=var_from, value='BRL')
radiobutton_from3 = Radiobutton(lf_from,
                                text="EUR",
                                variable=var_from, value='EUR')
radiobutton_from4 = Radiobutton(lf_from,
                                text="GBP",
                                variable=var_from, value='GBP')

radiobutton_to1 = Radiobutton(lf_to,
                              text="USD",
                              variable=var_to, value='USD', padx=25)
radiobutton_to2 = Radiobutton(lf_to,
                              text="BRL",
                              variable=var_to, value='BRL')
radiobutton_to3 = Radiobutton(lf_to,
                              text="EUR",
                              variable=var_to, value='EUR')
radiobutton_to4 = Radiobutton(lf_to,
                              text="GBP",
                              variable=var_to, value='GBP')

radiobutton_from1.grid(row=0)
radiobutton_from2.grid(row=1)
radiobutton_from3.grid(row=2)
radiobutton_from4.grid(row=3)

radiobutton_to1.grid(row=0)
radiobutton_to2.grid(row=1)
radiobutton_to3.grid(row=2)
radiobutton_to4.grid(row=3)


display_frame = Frame(root)
display_frame.pack(anchor='n', pady=(45, 20), padx=0)
display = Entry(display_frame, text='', font=(
    "Helvetica", 24), justify='right')
display.pack()

btn_frame = Frame(root)
btn_frame.pack()
start_btn = Button(btn_frame, text="Go!",
                   command=convert, pady=5, padx=25)
start_btn.grid(row=5)

if var_from == var_to:
    pass
else:
    pass

root.mainloop()
