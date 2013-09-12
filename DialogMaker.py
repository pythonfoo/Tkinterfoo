#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       dialogmaker.py
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
from tkinter import simpledialog
from tkinter import filedialog



class DialogMaker(object):
	"""Methoden zur Erzeugung und Gestaltung von Tkinter-Dialogen"""

	def __init__(self, title="Dialog"):
		"""Erzeugt Tkinter-Dialog und setzt Dialogtitel"""
		self.dia=Tk()
		self.dia.title(title)

	def mainloop(self):
		"""Erzeugt Dialog"""
		self.dia.mainloop()

	def auswahlbutton(self, befehl, r, c):
		"""Erzeugt den Auswahlbutton"""
		auswahlbutton = Button(self.dia, text = "Auswahl", bg="yellow", command = befehl)
		auswahlbutton.grid(row=r, column=c, padx=10)

	def aendernbutton(self, befehl, r, c):
		"""Erzeugt den Ändernbutton"""
		auswahlbutton = Button(self.dia, text = "Ändern", bg="yellow", command = befehl)
		auswahlbutton.grid(row=r, column=c, padx=10)

	def eingabebutton(self, befehl, r, c):
		"""Erzeugt den Eingabebutton"""
		eingabebutton = Button(self.dia, text = "Eingabe", bg="yellow", command = befehl)
		eingabebutton.grid(row=r, column=c, padx=10)

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
		e.grid(row=r, column=c, columnspan=cs)
		return e

	def eingabeFeldPasswd(self, w, r, c, cs=1):
		"""Erzeugt ein Eingabefeld mit * als Darstellung"""
		e = Entry(self.dia, width=w, show="*")
		e.grid(row=r, column=c, columnspan=cs)
		return e

	def listbox(self, liste, w, r, c):
		"""Erzeugt ein Listenfeld"""

		self.listbox = Listbox(self.dia, width=w)
		for i in range(0,len(liste)):
			self.listbox.insert("end", "  "+liste[i])
		self.listbox.grid(row=r, column=c, padx=5)
		return self.listbox

	def auswahl(self, listbox):
		"""Stellt die im Listenfeld des Dialoges gewaehlte Auswahl fest"""
		auswahl=listbox.get("active").strip()
		return auswahl

	# Vorgefertigtes

	def fileOpenDialog(self, diatitle="Dateiauswahldialog"):
		filename = filedialog.askopenfilename(filetypes = [('all files','*.*')],title = diatitle)
		return(filename)

	def questiondialog(self, diatitle, question, istring=""):
		answer = simpledialog.askstring(diatitle, question, initialvalue=istring)
		return answer

	def minfo(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showinfo(mbtitle, mbtext, type=btype)
		return sb

	def mwarning(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showwarning(mbtitle, mbtext, type=btype)
		return sb

	def merror(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showerror(mbtitle, mbtext, type=btype)
		return sb

	def yesorno(self, qbtitle, qbtext, qbicon="question"):
		a=messagebox.askyesno(qbtitle, qbtext, icon=qbicon)
		return a

	def okorcancel(self, qbtitle, qbtext, qbicon="question"):
		a=messagebox.askokcancel(qbtitle, qbtext, icon=qbicon)
		return a

	def retryorcancel(self, qbtitle, qbtext, qbicon="question"):
		a=messagebox.askretrycancel(qbtitle, qbtext, icon=qbicon)
		return a


def main():

	"""Erzeugt einen Dialog mit einem Listenfeld und zwei Buttons"""
	global md, lb

	md=DialogMaker("Beispieldialog")

	liste=["Dateiauswahl", "Passworteingabe", "Fragedialog"]

	lb = md.listbox(liste, 30, 0, 0)

	md.auswahlbutton(auswahlListenfeld, 0, 1)
	md.endebutton(1, 1)
	md.mainloop()

def auswahlListenfeld():
	auswahl = md.auswahl(lb)

	if auswahl == "Dateiauswahl":
		dateiname = md.fileOpenDialog()
		antwort1=md.minfo("Datei", dateiname)
		md.minfo("Rückgabe:", antwort1)
	elif auswahl == "Passworteingabe":
		pwdia()
	else:
		antwort2 = md.questiondialog("Eingabe", "Bitte Zeichenkette eingeben:")
		if antwort2:
			antwort3 = md.yesorno("Richtig?", antwort2)
			if antwort3 == 1:
				md.minfo("Rückgabe:", antwort3)

def pwdia():
	"""Dialog zur Eingabe des Passwortes"""
	global passd, passwort
	passd=DialogMaker("Passworteingabe")
	passd.label("Passwort", 30, 0, 0, "yellow", 2)
	passwort=passd.eingabeFeldPasswd(40, 1, 0, 2)

	passd.eingabebutton(passwdTest, 2, 1)
	passd.endebutton(2, 0)

	passd.mainloop()

def passwdTest():

	_passwort = passwort.get()

	if _passwort == "":
		messagebox.showerror('Achtung!', "Passwort muss eingegeben werden")
	else:
		antwort4=passd.retryorcancel("Richtig?", _passwort)

		if antwort4 == "retry":
			passd.ende()
			pwdia()
		else:
			passd.ende()

if __name__ == '__main__':
	main()


