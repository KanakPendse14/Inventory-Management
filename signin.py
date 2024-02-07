from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginClass:
    
    def __init__(self,root):
        
        self.root = root
        self.root.title('Login')
        self.root.geometry('1350x700')
        self.root.state('zoomed')
        self.root.configure(bg='#fff')


        self.bg_frame = Image.open("bg-image.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')
        
        
        self.lgn_frame = Frame(self.root,width=400, height=500, bg='#1F2544')
        self.lgn_frame.place(x=445, y=150)  
        
        self.heading = Label(self.lgn_frame, text='Login', bg='#1F2544', fg='white', font=('Microsoft YaHei UI Bold', 30, 'bold'))  
        self.heading.place(x=135, y=40)
        
        
        #Username input
        self.user_lbl = Label(self.lgn_frame, text='Username', bg='#1F2544', fg='white', font=('Microsoft YaHei UI Light', 20))
        self.user_lbl.place(x=30, y = 130)
        self.user_entry = Entry(self.lgn_frame, highlightthickness=0, relief= FLAT, width=30, fg='white',bg='#1F2544', font=('Microsoft YaHei UI Light', 15))
        self.user_entry.place(x=30, y = 170)
        self.user_entry.configure(insertbackground='white')
        Frame(self.lgn_frame, width=300, height=2,bg='white').place(x=30, y = 205)
        

    # #Password input
        self.pass_lbl = Label(self.lgn_frame, text='Password', bg='#1F2544', fg='white', font=('Microsoft YaHei UI Light', 20))
        self.pass_lbl.place(x=30, y=250)
        self.pass_entry = Entry(self.lgn_frame, highlightthickness=0, relief= FLAT, width=30, fg='white',bg='#1F2544', font=('Microsoft YaHei UI Light', 15), show='*')
        self.pass_entry.place(x=30, y=300)
        self.pass_entry.configure(insertbackground='white')
        Frame(self.lgn_frame, width=300, height=2,bg='white').place(x=30, y = 330)

    # #Button

        self.login_btn = Button(self.lgn_frame, width=15, pady=3,text='Login', cursor='hand2', bg='#6C22A6',fg='white',border=0, font=('Microsoft YaHei UI Bold', 13, 'bold'))
        self.login_btn.place(x=115, y=370)
        self.dont_have_an_acc = Label(self.lgn_frame,text="Don't have an account?",fg='white',bg='#1F2544',font=('Microsoft YaHei UI Light', 12))
        self.dont_have_an_acc.place(x=60, y=432)

        self.sign_up_btn = Button(self.lgn_frame,pady=0,text='Sign up', cursor='hand2',bg='#1F2544',fg='#9F70FD',border=0,font=('Microsoft YaHei UI Light', 12))
        self.sign_up_btn.place(x=248,y=430)
    
if __name__ == "__main__":
        root = Tk()
        obj = LoginClass(root)
        root.mainloop()
        
