'''
total = 6

for i in range (1,total+1):
	if i ==1: temp = 'st'
	elif i ==2: temp ='nd'
	elif i ==3: temp = 'rd'
	else: temp = 'th'

	marks = raw_input('Enter your %d %s semester CPI ' %(i,temp,))
'''

from Tkinter import *
import ttk

def takein(value1):
	return ((value1-0.5)*10);


def calculate(*args):
    try:
        value1 = float(sem2.get())
#        value2 = float(sem4.get())
        firstYear.set(takein(value1))
#        print firstYear
        value2 = float(sem4.get())
        secondYear.set(takein(value2))
        value3 = float(sem6.get())
        thirdYear.set(takein(value3))


    except ValueError:
        pass

    
root = Tk()
root.title("   CPI to Percentage")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

firstYear = StringVar()
secondYear = StringVar()
thirdYear = StringVar()
#sem1 = StringVar()
sem2 = StringVar()
#sem3 = StringVar()
sem4 = StringVar()
#sem5 = StringVar()
sem6 = StringVar()


ttk.Label(mainframe, text="2nd Sem CPI").grid(column=1, row=1, sticky=W)
Sem2_entry = ttk.Entry(mainframe, width=7, textvariable=sem2)
Sem2_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="4th Sem CPI").grid(column=1, row=2, sticky=W)
Sem4_entry = ttk.Entry(mainframe, width=7, textvariable=sem4)
Sem4_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="6th Sem CPI").grid(column=1, row=3, sticky=W)
Sem6_entry = ttk.Entry(mainframe, width=7, textvariable=sem6)
Sem6_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="\n ").grid(column=1, row=4, sticky=W)

ttk.Label(mainframe, text="First Year % ").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, textvariable=firstYear).grid(column=2, row=7, sticky=(W, E))
ttk.Label(mainframe, text="Second Year % ").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, textvariable=secondYear).grid(column=2, row=8, sticky=(W, E))
ttk.Label(mainframe, text="Third Year % ").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, textvariable=thirdYear).grid(column=2, row=9, sticky=(W, E))
ttk.Label(mainframe, text="\n ").grid(column=1, row=10, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=11, sticky=W)

'''

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
'''
#img = PhotoImage(file='ico.ico')
#root.tk.call('wm', 'iconphoto', root._w, img)
root.iconbitmap(r'ico.ico')
root.bind('<Return>', calculate)

root.mainloop()