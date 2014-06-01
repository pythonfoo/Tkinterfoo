#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       DiaTestIteration1.py
#       
#       Copyright 2013 Michael Stehmann <info@rechtsanwalt-stehmann.de>
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
		self.diatitle(title)

	def diatitle (self, title):
		"""Setzt den Titel des Dialogs"""
		self.dia.title(title)

	def mainloop(self):
		"""Erzeugt Dialog"""
		self.dia.mainloop()

	def button(self, btext, befehl, r, c):
		"""Erzeugt den Auswahlbutton"""
		auswahlbutton = Button(self.dia, text = btext, command = befehl)
		auswahlbutton.grid(row=r, column=c, padx=10)

	def endebutton(self, r, c):
		"""Erzeugt den Button zum Beenden"""
		eb = Button(self.dia, text = "Ende", fg="red", command = self.ende)
		eb.grid(row=r, column=c)

	def ende(self):
		"""Beendet den Dialog"""
		self.dia.destroy()

	# Allgemeine Elemente

	def label(self, ausgabetext, w, r, c, bgc, cs=1):
		"""Erzeugt ein Anzeigefeld"""
		lb = Label(self.dia, text = ausgabetext, width=w, bg=bgc)
		lb.grid(row=r, column=c, columnspan=cs)

	def eingabeFeld(self, w, r, c, cs=1):
		"""Erzeugt ein Eingabefeld"""
		e = Entry(self.dia, width=w)
		e.grid(row=r, column=c, columnspan=cs, padx=20)
		return e

	def minfo(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showinfo(mbtitle, mbtext, type=btype)
		return sb

class TestDialog(object):

	def __init__(self, Topicliste):
		self.tpliste = Topicliste

	def generateDialog(self):

		self.md = DialogMaker("Testdialog 1")

		r = 0
		self.entrydict = {}
		for element in self.tpliste:
			self.md.label(element, 30, r, 0, "yellow")
			self.entrydict.update({element : self.md.eingabeFeld(30, r, 1)})
			r = r + 1

		self.md.button("Felder auslesen", self.eingabeauslesen, r, 1)
		self.md.endebutton(r, 0)
		self.md.mainloop()
		return 0

	def eingabeauslesen(self):

		getdict = {}
		zkausgabe =""

		for element in self.tpliste:
			getdict.update({element : self.entrydict[element].get()})
		for element in self.tpliste:
			zkausgabe += element + " = " + getdict[element] + "\n"

		self.md.minfo("Ausgabe:", zkausgabe)
		self.md.ende()

if __name__ == '__main__':

	td = TestDialog(["Erster Punkt", "Zweiter Punkt", "Dritter Punkt"])
	td.generateDialog()

