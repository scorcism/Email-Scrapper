from tkinter import *
import requests
from bs4 import BeautifulSoup
import html5lib
import re
from copy import copy


window = Tk()
window.geometry('450x450')
window.title('Emails from the Link')

entry1 = StringVar()


def fetch():
    try: 
        url = entry1.get()
        r = requests.get(url)
        content = r.text
        soup = BeautifulSoup(content, 'html5lib')
        soup_text = (soup.get_text())
        reg_exp = re.findall(r"[a-zA-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]+", soup_text)
        ins = ""
        for value in reg_exp:
            ins += value+'\n'
        ins2 = copy(ins)
        text.config(state= "normal")
        text.insert(INSERT,ins2)

    except Exception:
        print("No Email Available")
    
    return fetch




Label(window,text= "Provide Specific URL").grid(row= 0, column =0)

Label(window, text= "URL: ").grid(row=2 , column =0)
Entry(window,textvariable = entry1).grid(row=2, column =1)

btn = Button(window,text= "Fetch!!", command = fetch)
btn.grid(row =3, column =1,pady = 12)

text =Text(window,width = 29, height = 13)
text.grid(row= 5 , column= 1, pady= 3, padx= 2)


window.mainloop()