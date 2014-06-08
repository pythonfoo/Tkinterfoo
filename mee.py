#!/usr/bin/python3
# -*- coding: utf-8 -*-
cr="""  mee.py
Michaels einfacher Editor - Version 0.1.2
  
Copyright 2014 Michael Stehmann <info@rechtsanwalt-stehmann.de>
  
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.\n  
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.\n
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA."""
  
from tkinter import * 
import os, tkinter.filedialog, tkinter.scrolledtext, tkinter.messagebox

class Editor(object):
	
	def __init__(self):
		self.content, self.endflag, self.newflag = "", False, False
		if not hasattr(self, 'fs'): self.fs=10
		self.master = Tk()
		self.master.title("Editor")
		self.master.geometry("+100+100")
		self.menu()
		self.st = tkinter.scrolledtext.ScrolledText(self.master, font="SansSerif, "+str(self.fs))
		self.st.pack(fill="both", expand="yes")
		self.master.mainloop()
		
	def menu(self):
		menu = Menu(self.master, font = "SansSerif, "+str(self.fs))
		self.master.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label= "Datei", menu=filemenu, font = "SansSerif, "+str(self.fs))
		filemenu.add_command(label="Neu", command=self.makenew, font = "SansSerif, "+str(self.fs))
		filemenu.add_command(label="Öffnen ...", command=self.opener, font = "SansSerif, "+str(self.fs))
		filemenu.add_command(label="Speichern ...", command=self.saver, font = "SansSerif, "+str(self.fs))
		filemenu.add_separator()
		filemenu.add_command(label="Beenden", command=self.ende, font = "SansSerif, "+str(self.fs))
		viewmenu = Menu(menu)
		menu.add_cascade(label= "Anzeige", menu=viewmenu, font = "SansSerif, "+str(self.fs))
		viewmenu.add_command(label="Schrift vergrößern", command=self.enlargefont, font = "SansSerif, "+str(self.fs))
		viewmenu.add_command(label="Schrift verkleinern", command=self.reducefont, font = "SansSerif, "+str(self.fs))
		menu.add_command(label="Informationen", command=self.minfo, font = "SansSerif, "+str(self.fs))

	def makenew(self):
		self.newflag = True
		self.ende()
		self.__init__()

	def enlargefont(self):
		self.fs = self.fs+1
		self.st["font"] = "SansSerif, "+str(self.fs)
		self.menu()

	def reducefont(self):
		if self.fs > 6:
			self.fs = self.fs-1
			self.st["font"] = "SansSerif, "+str(self.fs)
			self.menu()
		else: tkinter.messagebox.showwarning("Kleiner geht nicht!", "Noch kleiner ist nicht vorgesehen.", type="ok")

	def ende(self):
		if self.st.get("0.0", "end") != "\n" and self.st.get("0.0", "end") != self.content:
			if tkinter.messagebox.askyesno("Speichern?", "Vorher speichern?",icon="question"):
				if not self.newflag:
					self.endflag = True
				self.saver()
			else: self.master.destroy()
		else: self.master.destroy()

	def minfo(self):
		sb = tkinter.messagebox.showinfo("Informationen", cr, type="ok")

	def opener(self):
		try:
			fo = tkinter.filedialog.askopenfile(initialdir=os.getenv('HOME'))
			self.st.insert(INSERT,fo.read())
		except: return # Faengt Abbruch des Dateiladendialoges ab

	def saver(self):
		try:
			nfo = tkinter.filedialog.asksaveasfile(initialdir=os.getenv('HOME'))
			nfo.write(self.st.get("0.0", "end"))
			self.content = self.st.get("0.0", "end")
			if self.endflag == True: self.ende()
			if self.newflag == True: self.newdia()
		except: tkinter.messagebox.showwarning("Achtung!", "Es wurde nichts gespeichert!", type="ok")

if __name__ == '__main__':
	mee = Editor()
