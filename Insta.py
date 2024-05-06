from tkinter import *
import instaloader
from tkinter import messagebox
insta=instaloader.Instaloader()

def download():
    username=ilink.get()
    insta.download_profile(username,profile_pic_only=True)
    messagebox.showinfo('Success','Profile Image is successfully download')

root=Tk()
root.title('Instagram Profile Pic downloader')

logoImage=PhotoImage(file='instagram.png')
logoLabel=Label(root,image=logoImage)
logoLabel.grid(pady=10)

titleLabel=Label(root,text='Instagram Profile Image downloader',font=('Times New Roman',30,'bold'))
titleLabel.grid(row=1,column=0,pady=10,padx=30)

ilink=Label(root,text='Enter Username:',font=('arial',20,'bold'))
ilink.grid(row=2,column=0,pady=10)
ilink=Entry(root,width=40,font=('arial',15,'bold'),bd=5)
ilink.grid(row=3,column=0,pady=10)

downloadButton=Button(root,text='Download',font=('arial',15,'bold'),bg='#E1306C',command=download)
downloadButton.grid(row=4,column=0,pady=10)
root.mainloop()