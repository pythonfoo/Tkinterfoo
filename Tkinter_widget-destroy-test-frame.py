#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       Tkinter_widget-destroy-test.py
#       
#       Copyright 2014 Michael Stehmann <info@rechtsanwalt-stehmann.de>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from tkinter import *
from tkinter import messagebox

class DialogMaker(object):
	"""Methoden zur Erzeugung und Gestaltung von Tkinter-Dialogen"""

	def __init__(self, title):
		"""Erzeugt Tkinter-Dialog und setzt Dialogtitel"""
		self.dia=Tk()
		self.dia.geometry("+100+100") 
		self.diatitle(title)

	def diatitle (self, title):
		"""Setzt den Titel des Dialogs"""
		self.dia.title(title)

	def mainloop(self):
		"""Erzeugt Dialog"""
		self.dia.mainloop()

	def makeframe(self):
		self.frame = Frame(self.dia, borderwidth=2, bg = "green")
		self.frame.pack(fill="both",expand=1)
		return self.frame

	def button(self, btext, befehl, r, c):
		"""Erzeugt den Button"""
		button = Button(self.frame, text = btext, command = befehl)
		button.grid(row=r, column=c, padx=10)
		return button

	def endebutton(self, r, c):
		"""Erzeugt den Button zum Beenden"""
		eb = Button(self.frame, text = "Ende", fg="red", command = self.ende)
		eb.grid(row=r, column=c)
		return eb

	def ende(self):
		"""Beendet den Dialog"""
		#self.dia.destroy()
		"""Das geht auch:"""
		self.dia.quit()   # gibt nichts zurueck
		# quit()          # gibt None zurueck

	def label(self, ausgabetext, w, r, c, bgc, cs=1, rs=1):
		"""Erzeugt ein Anzeigefeld"""
		lb = Label(self.frame, text = ausgabetext, width=w, bg=bgc)
		lb.grid(row=r, column=c, columnspan=cs, rowspan=rs)
		return lb

class TestDialog(object):

	def __init__(self):
		self.md = DialogMaker("Destroy-Test")
		self.poorframe = self.md.makeframe()
		self.poorlabel = self.md.label("Hilfe!\nIch soll verschwinden!", 30, 0, 0, "yellow", 1, 2)
		self.md.button("Label entfernen", self.labelEntfernen, 0, 1)
		self.md.endebutton(1, 1)
		self.md.mainloop()

	def labelEntfernen(self):
		"""Label verschwinden lassen"""
		self.poorlabel.grid_remove()
		messagebox.showinfo("Überraschung", "Noch sind wir nicht am Ende!")
		"""Fenster wird verschoben"""
		self.md.dia.geometry("+200+200")
		self.poorlabel.grid()
		mb = messagebox.askyesno("Ich bin wieder da!", "Doch noch zerstören?",icon="question")
		if mb:
			self.frameEntfernen()

	def frameEntfernen(self):
		"""Frame zerstoeren"""
		self.poorframe.destroy()
		"""Einen neuen ins Fenster setzen"""
		self.md.makeframe()
		self.md.label("Das hast Du nun davon!", 40, 0, 0, "green")
		eb = self.md.endebutton(1, 0)
		eb["fg"] = "black"

def main():
	td = TestDialog()
	return 0

if __name__ == '__main__':
	main()

