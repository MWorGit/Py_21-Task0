import http.client
import json
from tkinter import *
import sys
import os

#Dada input
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
json = json.loads(data.decode("utf-8"))


#Window init 
root = Tk()
root.title("Сovid stats - Asia")
root.geometry("350x400")
text = Text(width=20, height=35, fg='Black', font=("Comic Sans", 12))
text.pack(side=LEFT)
message = StringVar(value = "Input asian country")
Entry(textvariable=message).place(x = 200, y = 120)


#Countrys arr 
countR = ["Turkey","Iran","Indonesia","Philippines","Iraq"]

def outF(text, json, i):
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[14])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[12])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[10])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[2])

def clic():
    inp_dat = message.get()
    if inp_dat == countR[0]:
        outF(text, json, 1)
    elif inp_dat == countR[1]:
        outF(text, json, 2)
    elif inp_dat == countR[2]:
        outF(text, json, 3)
    elif inp_dat == countR[3]:
        outF(text, json, 4)
    elif inp_dat == countR[4]:
        outF(text, json, 5)
    else:
        text.insert('1.0', "Error \n")

def restart():
    os.execl(sys.executable, os.path.abspath('civid.py'), *sys.argv)  

#Buttons init
Button(root, text="Enter", font=("Comic Sans", 12), command=clic, fg='Green',width=15, height=2,).place(x = 200, y = 1)
Button(root, text="Restart", font=("Comic Sans", 12), command=restart, fg='Green', width=15, height=2,).place(x = 200, y = 51)
root.mainloop()
