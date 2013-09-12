#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       tk-bewegt.py
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

def bewege_dreieck(ereignis):

	if ereignis.keysym == 'Up':
		leinwand.move(1, 0, -3)
	elif ereignis.keysym == 'Down':
		leinwand.move(1, 0, 3)
	elif ereignis.keysym == 'Left':
		leinwand.move(1, -3, 0)
	else:
		leinwand.move(1, 3, 0)


if __name__ == '__main__':
	tk = Tk()
	leinwand = Canvas(tk, width=400, height=400)
	leinwand.pack()
	leinwand.create_polygon(10, 10, 10, 60, 50, 35)

	leinwand.bind_all('<KeyPress-Up>', bewege_dreieck)
	leinwand.bind_all('<KeyPress-Down>', bewege_dreieck)
	leinwand.bind_all('<KeyPress-Left>', bewege_dreieck)
	leinwand.bind_all('<KeyPress-Right>', bewege_dreieck)

	tk.mainloop()
