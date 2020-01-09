# my first tkinter project 

import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox

main_application=tk.Tk()
main_application.geometry('1000x500')
main_application.title("MG Text Editor")
main_application.wm_iconbitmap("icon.ico")

# ........................................%%%%%%%%%%%%%%%%%%5.menu.%%%%%%%%%%%%%%%%%%%%%%%%%%%..........................................

menubar=tk.Menu(main_application)

# ...........................in menu file ,edit,view, theme...........................

file=tk.Menu(menubar,tearoff=0)
edit=tk.Menu(menubar,tearoff=0)
view=tk.Menu(menubar,tearoff=0)
theme=tk.Menu(menubar,tearoff=0)

# for uploading logo Photoimage   this full file

new_icon=tk.PhotoImage(file=r"icons2\new.png")
open_icon=tk.PhotoImage(file=r"icons2\open.png")
save_icon=tk.PhotoImage(file=r"icons2\save.png")
save_as_icon=tk.PhotoImage(file=r"icons2\save_as.png")
exit_icon=tk.PhotoImage(file=r"icons2\exit.png")
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&.........MAIN MENU FUNCTIONALITY&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# ))))))))))))))))))))))))))))))))))))))))))))))) file ((((((((((((((((((((((((((((()))))))))))))))))))))))))))))
# ....................new......for new just delete the item
file_strr=""

def new_caller():
    # m_box=messagebox.askyesno("Do you want to save the file")  #return 1===yes,0====no
    # if m_box==1
    text_writer.delete(1.0,tk.END)
# ....................open......s1=use filelog s2=file write insert
# https://pythonspot.com/tk-file-dialogs/
def open_caller():
    global file_strr
    file_strr=filedialog.askopenfilename(title="Select",filetypes=(("Text File",".txt"),("All Files","*.*")))
    # since error are coming when user does not select file so error handling
    try:
        with open(file_strr,'r') as sf :
            text_writer.delete(1.0,tk.END)
            text_writer.insert(1.0,sf.read())
    except:
        return 

# ....................save......s1=filedialod asksavefile1. save opened file,,2.save new file...for open no need msg but for new require msg
# since we have declare file_strr as global in open so we will get to know that whether file is open or not lets see
#  direct save ===== copy all current data open file and write no appenn save again
def save_caller():
    global file_strr
    if file_strr:
        curr_data=text_writer.get(1.0,tk.END) 
        with open(file_strr,"w",encoding='utf-8') as sa:
            sa.write(curr_data)
            sa.close()
    else:
        filedialog.asksaveasfile(title="Save File",defaultextension=".txt",filetypes=(("Text File",".txt"),("All Files","*.*")))
# ....................saveas......saveas...1.open filelog get all text editor data and write
def saveas_caller():
    try:   # erro when user open savas but doesn't save
        file_strr=text_writer.get(1.0,tk.END)
        saveas_file=filedialog.asksaveasfile(mode='w',title="Save File",defaultextension=".txt",filetypes=(("Text File",".txt"),("All Files","*.*")))
        saveas_file.write(file_strr)   # since we are doing anything becoz asksavasfile doing
        saveas_file.close()
    except:
        return
# ....................exit......before exit we will ask for save file use messagebox
def exit_caller():
    m_box=messagebox.askyesnocancel('Warning',"Do you want to save your file ")# title,write  mbox==1,yes...mbox=0,no
    if m_box:
        saveas_caller()
    elif m_box==0:
        main_application.destroy()
    else:
        return    
    

# +++++++++++++++++++++++++++++++++++++++++++ commond ++++++++++++++++++++++++++++++++++++=
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator='Crlt+N',command=new_caller)
file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator='Crlt+O',command=open_caller)
file.add_separator()
file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator='Crlt+S',command=save_caller)
file.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator='Crlt+Alt+S',command=saveas_caller)
file.add_separator()
file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator='Crlt+E',command=exit_caller)


# for uploading logo Photoimage   this full Edit

copy_icon=tk.PhotoImage(file=r"icons2\copy.png")
paste_icon=tk.PhotoImage(file=r"icons2\paste.png")
cut_icon=tk.PhotoImage(file=r"icons2\cut.png")
clear_all_icon=tk.PhotoImage(file=r"icons2\clear_all.png")
find_icon=tk.PhotoImage(file=r"icons2\find.png")

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& EDIT FUNCTIONALITY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ...........................copy...........................................................
def copy_caller():
    text_writer.event_generate("<Control c>")#using predefinned
# ...........................paste...........................................................

def paste_caller():
    text_writer.event_generate("<Control v>")
# ...........................cut...........................................................

def cut_caller():
    text_writer.event_generate("<Control x>")
# ...........................clearall...........................................................

def clearall_caller():  #on predefined
    text_writer.delete(1.0,tk.END)

# ...........................find...........................................................
def find_caller():
# 1.remove previous tag ,2.serch tag,3.fg bg ,repeat
    def find_control():
        word_input=find_var.get()
        if word_input:
            text_writer.tag_remove('anubhav',1.0,tk.END)  #its only tag anme
            start_idx=1.0
            while True:
                start_idx=text_writer.search(word_input,start_idx,tk.END)
                if not start_idx:
                    break
            # https://stackoverflow.com/questions/57430879/meaning-of
                else:
                    end_idx=f'{start_idx}+{len(word_input)}c'
                    text_writer.tag_add('anubhav',start_idx,end_idx)
                    text_writer.tag_config('anubhav',foreground="blue",background="yellow")
                    start_idx=end_idx
        else:
            messagebox.showwarning('warning','You have not enter the word')
            find_win.destroy()
            find_caller()

        
    def replace_control():
        word_input=find_var.get()
        replace_input=replace_var.get()
        if word_input and replace_input:
            content=text_writer.get(1.0,tk.END)
            content=content.replace(word_input,replace_input)
            text_writer.delete(1.0,tk.END)
            text_writer.insert(1.0,content)

    find_win=tk.Tk()
    find_win.title("Find")
    find_win.geometry('450x150+500+250')
    find_win.resizable(0,0)
    
    # Frame
    find_frame=ttk.Labelframe(find_win,text='Find/Replace')
    find_frame.pack(pady=20)
     # find and replace label
    tk.Label(find_frame,text="Find").grid(row=0,column=0)
    tk.Label(find_frame,text="Replace").grid(row=0,column=3,pady=5)

    # entry for find and replace
    find_var=ttk.Entry(find_frame,text="Find")
    find_var.grid(row=1,column=0)
    replace_var=ttk.Entry(find_frame,text="Replace")
    replace_var.grid(row=1,column=3,padx=10)
    
    # button find and replace
    find_btn=ttk.Button(find_frame,text='Find',command=find_control)
    find_btn.grid(row=2,column=0,pady=7)
     
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace_control)
    replace_btn.grid(row=2,column=3,pady=7,padx=10)
     
    find_win.mainloop()
    




edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator='Crlt+c',command=copy_caller)
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator='Crlt+V',command=paste_caller)
edit.add_separator()
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator='Crlt+X',command=cut_caller)
edit.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator='Crlt+Alt+S',command=clearall_caller)
edit.add_separator()
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator='Crlt+F',command=find_caller)

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& EDIt COMPLETED &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& FUNCTIONALITY &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def status_bar_control():
    # https://effbot.org/tkinterbook/pack.htm
    global status_var
    if status_var:   #declared here glbal no need of get
        status_bar.pack_forget()
        status_var=False
    else:
        status_bar.pack()
        status_var=True
    
def tool_bar_control():
    global tool_var
    if tool_var:
        tool_bar.pack_forget()
        tool_var=False
    else:
        #since tool bar is not coming again so trick
        text_writer.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_writer.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        tool_var = True

# for uploading logo Photoimage   this full View
status_var=tk.BooleanVar()
status_var.set(True)
tool_var=tk.BooleanVar()
tool_var.set(True)

tool_bar_icon=tk.PhotoImage(file=r"icons2\tool_bar.png")
status_bar_icon=tk.PhotoImage(file=r"icons2\status_bar.png")

view.add_checkbutton(label="Status Bar",image=status_bar_icon,variable=status_var,compound=tk.LEFT,command=status_bar_control)
view.add_checkbutton(label="Tool Bar",image=tool_bar_icon,variable=tool_var,compound=tk.LEFT,command=tool_bar_control)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   view completed &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# for uploading logo Photoimage   this full Theme
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& THEME &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&






dark_icon=tk.PhotoImage(file=r"icons2\dark.png")
light_default_icon=tk.PhotoImage(file=r"icons2\light_default.png")
light_plus_icon=tk.PhotoImage(file=r"icons2\light_plus.png")
monokai_icon=tk.PhotoImage(file=r"icons2\monokai.png")
night_blue_icon=tk.PhotoImage(file=r"icons2\night_blue.png")
red_icon=tk.PhotoImage(file=r"icons2\red.png")
# https://www.computerhope.com/htmcolor.htm
color_dict = {
     'Dark' : ('#c4c4c4', '#000000'),
     'Light Plus' : ('#000000', '#ffffff'),
    # 'Light' : ('#474747', '#e0e0e0'),
    # 'Light Plus' : ('#000000','#ffffff')
    'Monokai' : ('#C9BE62', '#2e2e2e'),
    'Red' : ('#2d2d2d', '#E27D60'),
    'Midnight Blue' :('#ffffff', '#151B54')
}

theme_var=tk.StringVar()
def theme_changer():
    global theme_var
    chosen_theme = theme_var.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_writer.config(background=bg_color, fg=fg_color) 


theme.add_radiobutton(label="Dark",image=dark_icon,variable=theme_var,compound=tk.LEFT,command=theme_changer)
# theme.add_radiobutton(label="Light",image=light_default_icon,variable=theme_var,compound=tk.LEFT,command=theme_changer)
theme.add_separator()
theme.add_radiobutton(label="Light Plus",image=light_plus_icon,variable=theme_var,compound=tk.LEFT,command=theme_changer)
theme.add_radiobutton(label="Monokai",image=monokai_icon,variable=theme_var,compound=tk.LEFT,command=theme_changer)
theme.add_separator()
theme.add_radiobutton(label="Midnight Blue",image=night_blue_icon,variable=theme_var,compound=tk.LEFT,command=theme_changer)
theme.add_radiobutton(label="Red",image=red_icon,compound=tk.LEFT,variable=theme_var,command=theme_changer)



# .....................................caseding..............................................................................................................
menubar.add_cascade(label='File',menu=file)
menubar.add_cascade(label='Edit',menu=edit)
menubar.add_cascade(label='View',menu=view)
menubar.add_cascade(label='Theme',menu=theme)


# ...................................................&&&&&&&&&&&&&&&&&&&&&&&TOOLBAR&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&...........................................................
# we need toolbar at top so we are creating label and on which add widget
# we cannot bind here becoz we need sizebar and font bar so it should be up of binding code
tool_bar=tk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_base=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_base['values']=font_tuple
font_base.current(font_tuple.index('Arial'))
font_base.grid(row=0,column=0)
# ................................................size bar......................................................................................
size_var=tk.StringVar()
size_bar=ttk.Combobox(tool_bar,width=15,textvariable=size_var,state="readonly")
size_bar['values']=tuple(range(7,85))
size_bar.current(6)
size_bar.grid(row=0,column=1,padx=3)

# .......................................bold............................................................................................

bold_icon=tk.PhotoImage(file=r"icons2\bold.png")

bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=3)
# ........................................itallic...........................................................................
italic_icon=tk.PhotoImage(file=r"icons2\italic.png")

italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=3)

# .....................................................underlines...................................................
underline_icon=tk.PhotoImage(file=r"icons2\underline.png")

underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=3)
# --------------------------------------------------font colour,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
font_color_icon=tk.PhotoImage(file=r"icons2\font_color.png")
# font_color=tk.StringVar()
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=3)

# --------------------------------------------------allign left,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
align_left_icon=tk.PhotoImage(file=r"icons2\align_left.png")

align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=3)
# --------------------------------------------------allign center,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
align_center_icon=tk.PhotoImage(file=r"icons2\align_center.png")

align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=3)
# --------------------------------------------------allign right,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
align_right_icon=tk.PhotoImage(file=r"icons2\align_right.png")

align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=3)

# .&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&TEXT EDITOR&&&&&&&&&&&&&&&&&&&&&&&&&&...........................................

# scroll_bar_h=tk.Scrollbar(main_application,orient=tk.HORIZONTAL)
# scroll_bar_h.pack(side=tk.BOTTOM,fill=tk.X)
scroll_bar=tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_writer=tk.Text(main_application)
text_writer.pack(fill=tk.BOTH,expand=True)
text_writer.focus_set()
text_writer.configure(yscrollcommand=scroll_bar.set)
# text_writer.config(xscrollcommand=scroll_bar_h.set)
scroll_bar.configure(command=text_writer.yview)
# scroll_bar_h.config(command=text_writer.xview)

#$$$$$$$$$$$$$$$$$$$$  ADDING FUCTIONALITY$$$$$$$$$$$$$$$$$$$$$$$$4

# ................font and size family................................
curr_font='Arial'
curr_size=15

def font_change(event):
    global curr_font
    curr_font=font_family.get()
    text_writer.configure(font=(curr_font,curr_size))

def font_size_change(event):
    global curr_size
    curr_size=size_var.get()
    text_writer.configure(font=(curr_font,curr_size))

size_bar.bind("<<ComboboxSelected>>",font_size_change)    
font_base.bind("<<ComboboxSelected>>",font_change)

# ......................................bold functionality...................................
# ref.  https://www.tutorialspoint.com/python/tk_fonts.htm,https://www.tcl.tk/man/tcl8.6/TkCmd/font.htm#M24
# we can setting current weight of text below comment..its type is dict
# we have to change normal to bold or bold to normal
# print((tk.font.Font(font=text_writer['font']).actual()))

def weight_changer():
    curr_weight=tk.font.Font(font=text_writer['font']) #dict after.actual
    if curr_weight.actual()['weight'] == 'normal' :
        text_writer.configure(font=(curr_font, curr_size, 'bold'))
    if curr_weight.actual()['weight'] == 'bold': 
        text_writer.configure(font=(curr_font,curr_size,'normal'))
bold_btn.configure(command=weight_changer)

# ..........................................italix functionality,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
            #   slant denote italic or roman

def slant_changer():
    curr_slant=tk.font.Font(font=text_writer['font']) #dict after.actual
    if curr_slant.actual()['slant'] == 'roman' :
        text_writer.configure(font=(curr_font, curr_size, 'italic'))
    if curr_slant.actual()['slant'] == 'italic': 
        text_writer.configure(font=(curr_font,curr_size,'roman'))
italic_btn.configure(command=slant_changer)
# ............................................underline functionality........................................
def underline_changer():
    curr_underline=tk.font.Font(font=text_writer['font']) #dict after.actual
    if curr_underline.actual()['underline'] == 0 :
        text_writer.configure(font=(curr_font, curr_size, 'underline'))
    if curr_underline.actual()['underline'] == 'italic': 
        text_writer.configure(font=(curr_font,curr_size,'normal'))
underline_btn.configure(command=underline_changer)
# ...........................................colour font functiionality .........................................
# adding colorchoser so that it will open a window for choosing colour ,, we will use askcolor for entry
#https://docs.python.org/3.9/library/tkinter.colorchooser.html
def font_color_changer():
    font_var=tk.colorchooser.askcolor()   # it will return tuple 0==rbg code , 1==hexagonal code..using hexagonal 
    text_writer.configure(fg=font_var[1])

font_color_btn.configure(command=font_color_changer)
# ...........................................align left functionality.........................................
# s1=save all text,s2=remove text,s3=set left,s4=inset
#https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget
# https://www.tutorialspoint.com/python/tk_text.htm
# http://effbot.org/tkinterbook/text.htm
def align_left_changer():
    text_var=text_writer.get(1.0,tk.END)
    text_writer.tag_config('l',justify=tk.LEFT)
    text_writer.delete(1.0,tk.END)
    text_writer.insert(tk.INSERT,text_var,'l')

align_left_btn.configure(command=align_left_changer)
# ...........................................aligh centre functionality.........................................
def align_center_changer():
    text_var=text_writer.get(1.0,tk.END)
    text_writer.tag_config('C',justify=tk.CENTER) # we are define here that c is the tog of left postion
    text_writer.delete(1.0,tk.END)
    text_writer.insert(tk.INSERT,text_var,'C')

align_center_btn.configure(command=align_center_changer)
# ...........................................align right functionality.........................................
def align_right_changer():
    text_var=text_writer.get(1.0,tk.END)
    text_writer.tag_config('R',justify=tk.RIGHT)
    text_writer.delete(1.0,tk.END)
    text_writer.insert(tk.INSERT,text_var,'R')

align_right_btn.configure(command=align_right_changer)

text_writer.configure(font='Arial,12')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  status bar &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  Functionality &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

def counter_(event):
    if text_writer.edit_modified():
        words=len(text_writer.get(1.0,'end-1c').split())
        character=len(text_writer.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters: {character} Words: {words}')
    text_writer.edit_modified(False)

# https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
text_writer.bind("<<Modified>>",counter_)


main_application.bind("<<Control-n>>",new_caller)
main_application.bind("<<Control-o>>",open_caller)
main_application.bind("<<Control-s>>",save_caller)
main_application.bind("<<Control-Alt+s>>",saveas_caller)
main_application.bind("<<Control-q>>",exit_caller)
main_application.bind("<<Control-f>>",find_caller)



main_application.config(menu=menubar)
main_application.mainloop()



# ref...
# 1.www.stackoverflow.com
# 2.tutorialspoint.com
# 3.http://effbot.org/tkinterbook/
# 3.geeksforgeeks
# 3.pythondocumentation
# 4.googlesearch
# 5.youtube





