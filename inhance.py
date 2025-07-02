from tkinter import *
from tkinter import ttk
import requests
from PIL import ImageTk ,Image

def data_get():
    city = city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3376aac7db2ad0116c9888d7a4ba6926").json()
    w_label1.config(text=data["weather"][0]["main"])
 
    tempmin_label1.config(text=str(f"{(data["main"]["temp"]-273.15):,.1f}c"))
  




win =Tk()
win.title("Weather forcast ")
win.config(bg="#ADD8E6")
win.geometry("650x300")

name_label=Label(win,text="Weather Forcasting",font=("Time New Roman",26),fg="#ADD8E6",bg="black")
name_label.place(x=105,y=10,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather Forcasting",font=("Time New Roman",16),values=list_name,textvariable=city_name)
com.place(x=210,y=80,height=30,width=200)



done_button= Button(win,text="Done",font=("Time New Roman",12),command=data_get)
done_button.place(x=280,y=125,height=30,width=60)

w_label1=Label(win,text="",font=("Time New Roman",24,),bg="#ADD8E6")
w_label1.place(x=25,y=240,height=50,width=210)


original_image = Image.open("w3.png")
resized_image = original_image.resize((200, 180))
img = ImageTk.PhotoImage(resized_image)


imgl = Label(win, image=img, bg="#ADD8E6")
imgl.place(x=430, y=95)
win.img = img

tempmin_label1=Label(win,text="",font=("Time New Roman",78),bg="#ADD8E6")
tempmin_label1.place(x=30,y=135,height=110,width=250)




win.mainloop()