from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


def main():
  win=Tk()
  app = login_window(win)
  win.mainloop()



class login_window: 
  def __init__(self,root):
      self.root= root
      self.root.title("Login")
      # self.root.geometry("1550x800+0+0")
        
      screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        
      self.root.geometry("{}x{}".format(screen_width, screen_height))
      root.state('zoomed')

      self.bg=ImageTk.PhotoImage(file=r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\bg1.jpg")
      
    #  resize_image = self.bg.resize((1536, 864))
        

      lbl_bg=Label(self.root,image=self.bg)
      lbl_bg.place(x=0,y=0, relwidth=1, relheight=1)  

      frame= Frame(self.root, bg="gray66")
      frame.place(x=610,y=170,width=340,height=450)

      img1=Image.open(r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\acc.png")
      img1=img1.resize((100,100),Image.ANTIALIAS)
      self.photoimage1=ImageTk.PhotoImage(img1)
      lblimage1=Label(image=self.photoimage1,bg="gray66",borderwidth=0)
      lblimage1.place(x=730,y=175,width=100,height=100)


      get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="Black",bg="gray66")
      get_str.place(x=95,y=100)

      #label for username block
      username=lbl=Label(frame,text="Username",font=("times new roman", 15, "bold"),fg="black",bg="grey66")
      username.place(x=70, y=155)

      self.txtuser= ttk.Entry(frame,font=("Times new roman", 15, "bold"))
      self.txtuser.place(x=40,y=180,width=270)

      #label for the password block
      password=lbl=Label(frame,text="Password",font=("times new roman", 15, "bold"),fg="black",bg="grey66")
      password.place(x=70, y=225)

      self.txtpass= ttk.Entry(frame,font=("Times new roman", 15, "bold"))
      self.txtpass.place(x=40,y=250,width=270)
        

      #icon images
      img2=Image.open(r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\acc.png")
      img2=img2.resize((25,25),Image.ANTIALIAS)
      self.photoimage2=ImageTk.PhotoImage(img2)
      lblimage1=Label(image=self.photoimage2,bg="gray66",borderwidth=0)
      lblimage1.place(x=650,y=326,width=25,height=25)   

      img3=Image.open(r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\lock-512.png")
      img3=img3.resize((25,25),Image.ANTIALIAS)
      self.photoimage3=ImageTk.PhotoImage(img3)
      lblimage1=Label(image=self.photoimage3,bg="gray66",borderwidth=0)
      lblimage1.place(x=650,y=395,width=25,height=25)  

      #creating login button
      loginbtn= Button(frame,command=self.login ,text="Login",font=("new times roman",15, "bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      loginbtn.place(x=110,y=300,width=120,height=35)
      
      #creating register button
      registerbtn= Button(frame,text="Register",command=self.register_window,font=("new times roman",10, "bold"),borderwidth=0,fg="black",bg="gray66",activeforeground="black",activebackground="gray66")
      registerbtn.place(x=90,y=350,width=160)

      #creating forget Password Button
      forgot_pass_btn= Button(frame,text="Password Forgotten",command=self.Forgotten_password,font=("new times roman",10, "bold"),borderwidth=0,fg="black",bg="gray66",activeforeground="black",activebackground="gray66")
      forgot_pass_btn.place(x=90,y=373,width=160)


  def register_window(self):
    self.new_window=Toplevel(self.root)
    self.app=register(self.new_window)    


  #creating a function for the working of login button
  def login(self):
    if self.txtuser.get()=="" or self.txtpass.get()=="":
      messagebox.showerror("Error","All feild required")              
    elif self.txtuser.get()=="Ali" and self.txtpass.get()=="1234":
      messagebox.showinfo("info", "Access Gained.")
    else:
      # messagebox.showerror("Error","Invalid Username & Password.")
      conn=mysql.connector.connect(host="localhost",user="root",password="rootpassword",database="face_recogizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                  self.txtuser.get(),
                                                                                  self.txtpass.get()
                                                                                ))

      row=my_cursor.fetchone()

      if row==None:
        messagebox.showerror("Error","Invalid username & password", parent = self.root)
      else:
        open_main=messagebox.askyesno("Yes/No","Access only Admin", parent = self.root)
        if open_main>0:
          self.new_window=Toplevel(self.root)
          # self.app=Face_Recognition_System(self.new_window) 
        else:
          if not open_main:
            return
      conn.commit()
      conn.close()


  #reset password window
  def reset_pass(self):
    if self.combo_security_Q.get()=="":
      messagebox.showerror("Error","Select the security question",parent=self.root2)
    elif self.txt_security.get()=="":
      messagebox.showerror("Error","Please enter the answer",parent=self.root2)
    elif self.txt_newpass.get()=="":
      messagebox.showerror("Error","Please enter the new password",parent=self.root2)
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="rootpassword",database="face_recogizer")
      my_cursor=conn.cursor()
      query=("select * from  register where email= %s and securityQ=%s and securityA=%s")
      value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
      my_cursor.execute(query,value)
      row=my_cursor.fetchone()
    
      if row==None:
        messagebox.showerror("Error","Please Enter the correct answer",parent=self.root2)
      else:
        query=("update register set password=%s where email=%s")
        value=(self.txt_newpass.get(),self.txtuser.get())
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        messagebox.showinfo("info","Your password has been reset, please login new password",parent=self.root2)
        self.root2.destroy()

  #creating forget password window  

  def Forgotten_password(self):
    if self.txtuser.get()=="":
      messagebox.showerror("Error","Please enter the Email address to reset password")
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="rootpassword",database="face_recogizer")
      my_cursor=conn.cursor()
      query= ("select * from register where email =%s")
      value= (self.txtuser.get(),)
      my_cursor.execute(query,value)
      row=my_cursor.fetchone()
     # print(row)
     
      if row==None:
        messagebox.showerror("Error","Please enter the valid username", parent = self.root)
      else:
        conn.close()
        self.root2=Toplevel()
        self.root2.title("Forget Password")
        self.root2.geometry("340x450+610+170")

        l=Label(self.root2,text="Forget Password",font=("new times roman",20, "bold"),fg="red",bg="white")
        l.place(x=0,y=10,relwidth=1)
        security_Q=Label(self.root2,text="Secutiry Question",font=("times new roman",15,"bold"), bg="white")
        security_Q.place(x=50,y=80)

        self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("","Your Birth Place","Your Favorite Teacher","Your Pet Name")
        self.combo_security_Q.place(x=50,y=110,width=250)
        self.combo_security_Q.current(0)

        #creating the security answer lable and frame
        security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"), bg="white")
        security_A.place(x=50,y=150)
        self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
        self.txt_security.place(x=50,y=180,width=250)

        new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"), bg="white")
        new_password.place(x=50,y=220)
        self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
        self.txt_newpass.place(x=50,y=250,width=250)

        btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"), fg="white",foreground="green")
        btn.place(x=100,y=290)



class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_secorityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #creating Background Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\wallpaperflare.com_wallpaper (2).jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #creating image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\bg.jpeg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #main Frame 
        frame =Frame(self.root,bg="White",)
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here", font=("times new roman",20,"bold"),fg="black", bg="white")
        register_lbl.place(x=20,y=20)


        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"), bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        last_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"), bg="white")
        last_name.place(x=370,y=100)
        self.lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Conatct Number",font=("times new roman",15,"bold"), bg="white")
        contact.place(x=50,y=170)
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Address",font=("times new roman",15,"bold"), bg="white")
        email.place(x=370,y=170)
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)


        #creating the security question lable and frame
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"), bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("","Your Birth Place","Your Favorite Teacher","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        #creating the security answer lable and frame
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"), bg="white")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_secorityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #creating password label and frame
        password=Label(frame,text="Enter Password", font=("times new roman",15,"bold"), bg="white")
        password.place(x=50,y=310)
        pass_entry=ttk.Entry(frame, textvariable=self.var_pass,font=("times new roman",15,"bold"))
        pass_entry.place(x=50,y=340,width=250)

        #creating Confirm password label and frame
        confirm_pass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"), bg="white")
        confirm_pass.place(x=370,y=310)
        confirm_pass_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        confirm_pass_entry.place(x=370,y=340,width=250)

        #creating check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #creating register button
        img=Image.open(r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\reg1.png")
        img=img.resize((200,90),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=50,y=420,width=200)

        #creating login button
        img1=Image.open(r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\DSA_project_Ali\log2.png")
        img1=img1.resize((200,110),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=370,y=420,width=200)

        

    def register_data(self):

      if self.var_fname.get()==""or self.var_email.get==""or self.var_securityQ.get=="":
          messagebox.showerror("Error", "All feilds are required")
      elif self.var_pass.get()!=self.var_confpass.get():
          messagebox.showerror("Error","Password Dosent match", parent = self.root)
      elif self.var_check.get()==0:
          messagebox.showerror("Error","Please agree our Terms and Conditions", parent = self.root)
      else:
          try:

              conn=mysql.connector.connect(host="localhost",user="root",password="rootpassword",database="face_recogizer")
              my_cursor=conn.cursor()
              query=("select*from register where email=%s")
              value=(self.var_email.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              if row!=None:
                  messagebox.showerror("Error","User already exist, try another email")
              else:
                  my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_contact.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_securityQ.get(),
                                                                                      self.var_secorityA.get(),
                                                                                      self.var_pass.get()

                                                                                  ))

              conn.commit()
              messagebox.showinfo("info","Registered Successfully")

      
          except Error as e:
              print("Error while connecting to MySQL", e)
          finally:
              if conn.is_connected():
                  my_cursor.close()
                  conn.close()
                  print("MySQL connection is closed")
 
if __name__=="__main__":
  main()
  
