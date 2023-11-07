from tkinter import *
from customtkinter import*
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class Tenant():
   def __init__(self, root):
      self.root = root
      self.root.geometry("1000x500+180+60")
      self.root.title("Tenant Management System")
      main_f = CTkFrame(self.root, width=1400, height=700, fg_color="#0beba1", corner_radius=0)
      main_f.place(x=0, y=0)

      CTkLabel(main_f, text="TENANT MANAGEMENT SYSTEM",width=1000, bg_color="red", font=("Bookman Old style", 30),).place(x=0, y=0)

      admin_btn = CTkButton(main_f, text="Tenant Panel", font=("Bookman Old style", 30), width=230, height=200, corner_radius=50, bg_color="#0beba1")
      admin_btn.place(x=200, y=180)

      admin_btn = CTkButton(main_f, text="Admin Panel", font=("Bookman Old style", 30), width=230, height=200, corner_radius=50, bg_color="#0beba1")
      admin_btn.place(x=550, y=180)

      self.video_capture = cv2.VideoCapture(2)
      self.current_image = None

      self.update_webcam()

   def update_webcam(self):
      ret, frame = self.video_capture.read()
      if ret:
         self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR))

         self.photo = ImageTk.PhotoImage(image=self.current_image)

         self.root.after(15, self.update_webcam)

      # create webcam feedd display








if __name__ == "__main__":
   root = Tk()
   app = Tenant(root)
   root.mainloop()
