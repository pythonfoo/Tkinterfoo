#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  TkinterGUI.py
#  
#  Copyright 2013 Mechtilde Stehmann <mechtilde@stephan>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from tkinter import *
#import tkinter.filedialog
#import tkinter.messagebox
#import tkinter.simpledialog


def _(String):
	"""solange keine gettext Integration erfolgt ist, ist dies ein dummy"""
	return String

class createWindow(tkinter.Frame):

	def __init__(self, master):
		self.master = master
		self.menuBar = tkinter.Menu(master)
		self.master.config(menu = self.menuBar)
		self.fillMenuBar()

	def fillMenuBar(self):
		self.menuFile=tkinter.Menu(self.menuBar, tearoff=False)
		self.menuBar.add_cascade(label = "Kalender", menu=self.menuFile)
		self.menuFile.add_command(label = "Fenster", command = self.handler)
		self.menuFile.add_command(label = "Einfach", command = self.einfacheAnzeige)
		self.menuFile.add_command(label = "Erweitert", command = self.handler)
		self.menuFile.add_separator()
		self.menuFile.add_command(label = "Beenden", command = self.quit)

		self.menuFile1=tkinter.Menu(self.menuBar, tearoff=False)
		self.menuBar.add_cascade(label = "Datei", menu=self.menuFile1)
		self.menuFile1.add_command(label = "Neu", command = self.handler)
		self.menuFile1.add_command(label = "Öffnen", command = self.handler)
		self.menuFile1.add_command(label = "Speichern", command = self.handler)
		self.menuFile1.add_command(label = "Speichern unter", command = self.handler)
		self.menuFile1.add_separator()
		self.menuFile1.add_command(label = "Beenden", command = self.quit)

		self.menuFile2=tkinter.Menu(self.menuBar, tearoff=False)
		self.menuBar.add_cascade(label = "Bearbeiten", menu=self.menuFile2)
		self.menuFile2.add_command(label = "Suchen", command = self.handler)
		self.menuFile2.add_command(label = "Ersetzen", command = self.handler)
		self.menuFile2.add_separator()
		self.menuFile2.add_command(label = "Ausschneiden", command = self.handler)
		self.menuFile2.add_command(label = "Kopieren", command = self.handler)
		self.menuFile2.add_command(label = "Einfügen", command = self.handler)

	def einfacheAnzeige(self):
		# Label für die Anzeige der Daten
		labelMonat = Label(master=tkFenster, text='Januar', fg='white', bg='gray', font=('Arial', 16))
		labelMonat.place(x=5, y=5, width=170, height=20)
		labelTag = Label(master=tkFenster, text='21', fg='red', bg='#FFCFC9', font=('Arial', 72))
		labelTag.place(x=5, y=30, width=170, height=80)
		labelWochentag = Label(master=tkFenster, text='Montag')
		labelWochentag.place(x=35, y=115, width=90, height=30)

	def calendar(self):
		pass


	def handler(self):
		pass

def main():
	# Erzeugung eines Fensters
	tkFenster =Tk()
	tkFenster.title("Kalender")
	# Erzeugung einer Variablen Größe
	tkFenster.geometry("180x145")

	cal = createWindow(tkFenster)

	# Aktivieren des Fensters
	tkFenster.mainloop()
	return 0

if __name__ == '__main__':
	main()

