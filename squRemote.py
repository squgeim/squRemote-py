#!/usr/bin/python

from squR import *
from threading import Thread
import Tkinter
import tkMessageBox

class TksquRemote(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent=parent
    self.init()
    self.proc = Thread(target=self.start)
    self.proc.daemon = True
    self.proc.start()
    
  def init(self):
    self.grid()
    
    self.txt = Tkinter.StringVar()
    self.txt.set("squRemote is running on \n IP: "+HOST+" PORT: "+str(PORT))
    text = Tkinter.Label(self,textvariable=self.txt,anchor="w")
    text.grid(column=0,row=1,sticky="EW")
    
    self.grid_columnconfigure(0,weight=1)
    self.resizable(False,False)
    self.update()
    self.geometry(self.geometry())
    #self.protocol('WM_DELETE_WINDOW', self.stop)
    
  def stop(self):
    tkMessageBox.showerror("Some Error","There has been some error.")
    self.destroy()
  
  def start(self):
    if(HOST==""):
      tkMessageBox.showerror("No Wifi","Seems your wi-fi is off. Try again after connecting to a wifi")
      self.destroy()
    SocketServer.TCPServer.allow_reuse_address = True
    self.server = SocketServer.TCPServer((HOST,PORT), MyTCPHandler)
    try:
      self.server.serve_forever()
    except KeyboardInterrupt:
      print "got it!"
      self.server.shutdown()
    except squRemote.socerr:
      tkMessageBox.showerror("Error","There has been some error. Please try again after a minute.")
  
if __name__=="__main__":
  app=TksquRemote(None)
  app.title("squRemote")
  if not getuid():
    app.mainloop()
  else:
    tkMessageBox.showerror("squRemote","Not enough permissions, are you root?")
    
