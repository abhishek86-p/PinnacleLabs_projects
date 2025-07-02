from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3376aac7db2ad0116c9888d7a4ba6926").json()
    w_label1.config(text=data["weather"][0]["main"])
    wB_label1.config(text=data["weather"][0]["description"])
    tempmin_label1.config(text=str(data["main"]["temp_min"]-273.15))
    tempmax_label1.config(text=str(data["main"]["temp_max"]-273.15))




win =Tk()
win.title("Weather forcast ")
win.config(bg="skyblue")
win.geometry("500x540")

name_label=Label(win,text="Weather Forcasting",font=("Time New Roman",36,"bold"),bg="sky blue")
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather Forcasting",font=("Time New Roman",36),values=list_name,textvariable=city_name)
com.place(x=28,y=120,height=50,width=450)



done_button= Button(win,text="Done",font=("Time New Roman",28),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


w_label=Label(win,text="Weather Climate",font=("Time New Roman",14))
w_label.place(x=25,y=260,height=50,width=210)

w_label1=Label(win,text="--",font=("Time New Roman",14))
w_label1.place(x=260,y=260,height=50,width=210)



wB_label=Label(win,text="Weather Description",font=("Time New Roman",14))
wB_label.place(x=25,y=330,height=50,width=210)
wB_label1=Label(win,text="--",font=("Time New Roman",14))
wB_label1.place(x=260,y=330,height=50,width=210)


tempmin_label=Label(win,text="Min Temperature",font=("Time New Roman",14))
tempmin_label.place(x=25,y=400,height=50,width=210)
tempmin_label1=Label(win,text="--",font=("Time New Roman",14))
tempmin_label1.place(x=260,y=400,height=50,width=210)

tempmax_label=Label(win,text="max Temperature",font=("Time New Roman",14))
tempmax_label.place(x=25,y=470,height=50,width=210)
tempmax_label1=Label(win,text="--",font=("Time New Roman",14))
tempmax_label1.place(x=260,y=470,height=50,width=210)



win.mainloop()