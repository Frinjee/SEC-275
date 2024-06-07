import tkinter as tk
import random, string, os
from tkinter import *
from tkinter import ttk
from tkinter import font
#from tk_funcs import HideScrollbar

root = tk.Tk()
root.title('SYS200-3 Converter')
root.geometry('385x385')
c_path = '@FF6CursorUp.cur'
ani_path = '@FFCursor-Pen.ani'
root.configure(background='#4a4d4f', cursor=c_path)

# initial styling
#cmc_sans = font.Font(family='Comic Sans MS', size=11, weight='bold')
stl = ttk.Style()
stl.configure('head_frame.TFrame', background='#81898f')
stl.configure('sb.Horizontal.TScrollbar', gripcount=0, troughcolor='#78858f', bordercolor='#81898f', 
		       relief='sunken', elementborderwidth=2, bd='2', highlightbackground='#636d75')

################################################################################################
#############		          		Head && LabelFrame						       #############
################################################################################################

head_frame = ttk.Frame(root, style='head_frame.TFrame')
head_frame.grid(row=0, column=0,sticky=W, padx=4, pady=4)
head_frame.columnconfigure(0, weight=1, pad=1)
head_frame.rowconfigure(0, weight=1)
head_frame.rowconfigure(1, weight=1)

opt_lblFrame = ttk.LabelFrame(head_frame, text='Select Conversion Option')
opt_lblFrame.grid(row=0, column=0, sticky=W, padx=2, pady=2)
opt_lblFrame.columnconfigure(0, weight=1, pad=1)
opt_lblFrame.rowconfigure(0, weight=1, pad=2)
opt_lblFrame.rowconfigure(1, weight=1, pad=2)

################################################################################################
#############		          		RADIOBUTTONS						           #############
################################################################################################
#r_path = '@FFCursor-Move.cur'
radio_rows = [['dec to bin', 'bin to dec'], ['dec to hex', 'hex to dec'], ['dec to oct', 'oct to dec']]
v = tk.IntVar()

for row_index, row in enumerate(radio_rows):
    for cell_index, cell in enumerate(row):
    	for x in range(5):
        	r_buttons = ttk.Radiobutton(opt_lblFrame, text=cell, value=cell, variable=v)
        	r_buttons.grid(row=row_index, column=cell_index)
        	

################################################################################################
#############			        ENTRY FRAME & CHILDREN 							   #############
################################################################################################
# begin style configuration for entry_frame
stl.configure('entry_frame.TFrame', background='#81898f')

# create entry LabelFrame and set its position w. grid()
entry_frame = ttk.LabelFrame(head_frame, text='Enter value to convert below', height=3)
entry_frame.grid(row=1, column=0, sticky=W)

entry_sb_frame = ttk.Frame(entry_frame)
entry_sb_frame.grid(row=0, column=0, columnspan=2, padx=2, pady=3, ipady=1)


val_entry = ttk.Entry(entry_sb_frame, width=45, cursor=ani_path)
val_entry.grid(row=0, column=0, columnspan=1, sticky=W, ipady=2, pady=1)

entry_sb = ttk.Scrollbar(entry_sb_frame, orient=HORIZONTAL, style='sb.Horizontal.TScrollbar')
entry_sb.grid(row=1, column=0, sticky=EW, ipadx=3, ipady=1)
val_entry.config(xscrollcommand=entry_sb.set)
entry_sb.config(command=val_entry.xview())


conv_button = ttk.Button(entry_sb_frame, text='🆗', width=3)
conv_button.grid(row=0, column=2, padx=2, pady=2, sticky=W)

result_text = Text(entry_frame, width=40, height=10, wrap='none', cursor=ani_path)
result_text.grid(row=2, column=0, padx=2, pady=1)

text_sb = Scrollbar(entry_frame, orient=HORIZONTAL)
text_sb.grid(row=3, column=0, sticky=EW)
result_text.config(yscrollcommand=text_sb.set)
text_sb.config(command=result_text.yview)
root.mainloop()



'''
free space ~195px/88px

entry_lbl = Label(opt_lblFrame, text='Enter value to convert: ')
val_entry = Entry(opt_lblFrame)
cnv_btn = Button(opt_lblFrame, text='Convert')

entry_lbl.grid(row=1, column=0, sticky=W, padx=1, pady=2)
val_entry.grid(row=1, column=1, sticky=W, padx=1, pady=2)
'''