from Tkinter import *
import socket 
import threading
import time
from os import system



root = Tk()

global text_field
text_field = Label(root, text="")
text_field.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S, rowspan=2)


ip_entry = Entry(root)

ip_entry.insert(0, '10.0.10.164')

ip_entry.grid(row=9, column=0, rowspan=2, columnspan=3, sticky=W+E+N+S)

global hostname
hostname = ip_entry.get()

global big_text
big_text = Label(root, text="")
big_text.grid_remove()
big_text.grid(row=13, column=0, columnspan=4, sticky=W+E+N+S, rowspan=4)
   

def send_packet(data):
   try:
      global hostname
      TCP_IP = hostname
      TCP_PORT = 2431
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TCP_IP, TCP_PORT))
      s.send(data)
      s.close()
   except Exception as e:
      global big_text
      big_text = Label(root, text=e)
      big_text.grid_remove()
      big_text.grid(row=13, column=0, columnspan=4, sticky=W+E+N+S, rowspan=4)

def connect_to_ip():
   if system("ping -c 1 " + ip_entry.get() + " -t 2") is 0:
      t2.start()
      ip_entry.grid_remove()
      connect_button.grid_remove()
      global hostname
      hostname = ip_entry.get()
      Button(root, text="< PREV", command= lambda: send_packet("Stick_3Ae\07\01\00\00\00\00\00\00\00\00\00\00")).grid(row=0, column=0, rowspan=2, sticky=W+E+N+S)
      Button(root, text="NEXT >", command= lambda: send_packet("Stick_3Ae\02\01\00\00\00\00\00\00\00\00\00\00")).grid(row=0, column=3, rowspan=2, sticky=W+E+N+S)

      Button(root, text="Scene 1", command= lambda: send_packet("Stick_3Am\00\01\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=3, column=0, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 2", command= lambda: send_packet("Stick_3Am\00\02\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=3, column=1, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 3", command= lambda: send_packet("Stick_3Am\00\03\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=3, column=2, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 4", command= lambda: send_packet("Stick_3Am\00\04\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=3, column=3, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 5", command= lambda: send_packet("Stick_3Am\00\05\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=6, column=0, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 6", command= lambda: send_packet("Stick_3Am\00\06\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=6, column=1, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 7", command= lambda: send_packet("Stick_3Am\00\07\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=6, column=2, rowspan=2, sticky=W+E+N+S)
      Button(root, text="Scene 8", command= lambda: send_packet("Stick_3Am\00\10\00\00\01\00\00\00\00\00\00\00\00\00\00")).grid(row=6, column=3, rowspan=2, sticky=W+E+N+S)
      global big_text
      big_text = Label(root, text="")
      big_text.grid_remove()
      big_text.grid(row=13, column=0, columnspan=4, sticky=W+E+N+S, rowspan=4)
   else:
      global big_text
      big_text = Label(root, text="Device not found")
      big_text.grid_remove()
      big_text.grid(row=13, column=0, columnspan=4, sticky=W+E+N+S, rowspan=4)
      
connect_button = Button(root, text="Connect", command= connect_to_ip)
connect_button.grid(row=9, column=3, rowspan=2, sticky=W+E+N+S)

def status():
   try:
      while True:
         global text_field
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         global hostname
         s.connect((hostname, 2431))
         message = s.recvfrom(2431)
         message = str(message)
         message = message.replace("\\","")
         message = message.replace("x00","")
         message = message.replace("dd","")
         message = message.replace("Stick_3A#","")
         message = message.replace("x0","")
         message = message.replace("', None","")
         message = message.replace("'2","")
         message = message.replace("21","")
         message = message.replace("(","")
         message = message.replace(")","")
         text_field = Label(root, text=message[:1] + " " + message[1:])
         text_field.grid_remove()
         text_field.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S, rowspan=2)
         time.sleep(0.333)
   except Exception as e:
      global big_text
      big_text = Label(root, text=e)
      big_text.grid_remove()
      big_text.grid(row=13, column=0, columnspan=4, sticky=W+E+N+S, rowspan=4)

t1 = threading.Thread(target=Tk, args=())
t2 = threading.Thread(target=status, args=())

t1.start()

root.geometry('{}x{}'.format(310, 450))
root.minsize(320, 450)

root.title("Nicolaudie Scene Launcher")

root.mainloop()
