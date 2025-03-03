    # Pisun Editor - Open-source text editor with theme features and Discord RPC
    # Copyright (C) 2025  Aibo The Dog

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.
import tkinter as tk
from tkinter import filedialog
import multiprocessing
import Pisun_editor_rpc
selected_theme = "Light"
state = "Blank document"
details = "Blank file"
smallimage = "blank"
smallimage_text = f"Blank file"
smallimage_nonpriv = "blank"
smallimage_text_nonprv = "Blank file"
details_nonpriv = ""
state_nonpriv = ""
priv_mode = False
acent_color = "white"
secondary_acent = "gray84"
version = "RELEASE 2.3.25c PUBLIC"
version_nonpriv = ""
connected =True

text_accent = "black"
def setRPC(detail, status, image, image_text,vers):
    global priv_mode, details, state, details_nonpriv, state_nonpriv, smallimage_text_nonprv, smallimage, smallimage_text, smallimage_nonpriv,version,version_nonpriv
    if priv_mode:
        details = "Info hidden"
        state = "Privacy mode enabled"
        smallimage = "privacy_mode"
        smallimage_text = "Privacy mode enabled"
        version = "Info hidden, privacy mode enabled"
        details_nonpriv = detail
        state_nonpriv = status
        smallimage_text_nonprv = image_text
        smallimage_nonpriv = image
        version_nonpriv = vers
    else:
        details = detail
        state = status
        smallimage = image
        smallimage_text = f"{image_text}"
        version = vers
def start_rpc(state, details, image, image_text,ver):
    Pisun_editor_rpc.discord_rpc(details=details, state=state, smallpic=image, smallpic_text=image_text, version=version)
def new_file():
    global Pisun_editor_rpc_multprcs, state, details, smallimage, smallimage_text
    text_area.delete(1.0, tk.END)
    root.wm_title("Pisun Editor - Blank file")
    Pisun_editor_rpc_multprcs.terminate()
    Pisun_editor_rpc_multprcs.join()  
    setRPC(detail="Blank file", status="Blank document", image="blank", image_text=f"Blank File",vers=version)
    Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
    Pisun_editor_rpc_multprcs.start()
def open_file():
    global Pisun_editor_rpc_multprcs, state, details, smallimage, smallimage_text
    file_path = filedialog.askopenfilename()
    if file_path:
        root.wm_title(f"Pisun Editor - {file_path}")
        Pisun_editor_rpc_multprcs.terminate()
        Pisun_editor_rpc_multprcs.join()  
        setRPC(detail=file_path, status="Editing", image="editing", image_text=f"Editing File",vers=version)
        Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
        Pisun_editor_rpc_multprcs.start()
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
def open_about():
    child = tk.Toplevel(root,bg=acent_color)
    appname_text = tk.Label(child, text=f"Pisun Editor {version}",bg=acent_color,fg=text_accent)
    author_text = tk.Label(child, text="By Aibo The Dog",bg=acent_color,fg=text_accent)
    about_text = tk.Label(child, text="Pisun Editor - Open-source text editor\nwith theme features and \nDiscord RPC",bg=acent_color,fg=text_accent)
    gnu_text = tk.Label(child, text="\nGNU GENERAL PUBLIC LICENSE applied on this app. \nRead LICENSE on repo for the license ",bg=acent_color,fg=text_accent)
    appname_text.pack()
    author_text.pack()
    about_text.pack()
    gnu_text.pack()
    child.title("Pisun editor - About")
    child.resizable(False, False)
    child.mainloop()
def exit_editor():
    root.destroy()
def open_prefs():
    def apply_theme():
        global acent_color,secondary_acent,text_accent,selected_theme,Pisun_editor_rpc_multprcs
        selected_indices = theme_selector.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            theme_selected = theme_selector.get(selected_index)
            print(f"Selected theme: {theme_selected}")
            if theme_selected == "Dark":
                selected_theme = "Dark"
                root.config(bg="gray26")
                menu_bar.config(bg="gray33",fg="gray77")
                text_area.config(bg="gray26",fg="gray77")
                prefs.config(bg="gray26")
                apply_theme_button.config(bg="gray26",fg="gray77")
                theme_selector.config(bg="gray26",fg="gray77")
                themer_text.config(bg="gray26",fg="gray77")
                file_menu.config(bg="gray33",fg="gray77")
                aboutmenu.config(bg="gray33",fg="gray77")
                applied_theme_text.config(bg="gray26",fg="gray77",text=f"Applied theme: {selected_theme}")
                acent_color = "gray26"
                secondary_acent = "gray33"
                text_accent = "gray77"
            elif theme_selected == "Black":
                selected_theme = "Black"
                root.config(bg="black")
                menu_bar.config(bg="gray7",fg="white")
                text_area.config(bg="black",fg="white")
                prefs.config(bg="black")
                apply_theme_button.config(bg="gray7",fg="white")
                theme_selector.config(bg="gray7",fg="white")
                themer_text.config(bg="black",fg="white")
                file_menu.config(bg="gray7",fg="white")
                aboutmenu.config(bg="gray7",fg="white")
                applied_theme_text.config(bg="black",fg="white",text=f"Applied theme: {selected_theme}")
                acent_color = "black"
                secondary_acent = "gray6"
                text_accent = "white"
            elif theme_selected == "Light":
                selected_theme = "Light"
                root.config(bg="white")
                menu_bar.config(bg="gray84",fg="black")
                text_area.config(bg="white",fg="black")
                prefs.config(bg="white")
                apply_theme_button.config(bg="gray84",fg="black")
                theme_selector.config(bg="gray84",fg="black")
                themer_text.config(bg="white",fg="black")
                file_menu.config(bg="gray84",fg="black")
                aboutmenu.config(bg="gray84",fg="black")
                applied_theme_text.config(bg="white",fg="black",text=f"Applied theme: {selected_theme}")
                acent_color = "white"
                secondary_acent = "gray84"
                text_accent = "black"
            elif theme_selected == "Custom theme":
                set_custom_theme()
        else:
            print("No theme selected")
    def set_custom_theme():
        global acent_color,secondary_acent,text_accent,selected_theme,Pisun_editor_rpc_multprcs
        themefile = filedialog.askopenfilename()
        if themefile:
            with open(themefile,'r') as file:
                lines = [line.replace("\n","") for line in file.readlines()]
            print(lines)
            selected_theme = f"{lines[0]}"
            root.config(bg=f"{lines[1]}")
            menu_bar.config(bg=f"{lines[2]}",fg=f"{lines[3]}")
            text_area.config(bg=f"{lines[1]}",fg=f"{lines[3]}")
            prefs.config(bg=f"{lines[1]}")
            apply_theme_button.config(bg=f"{lines[2]}",fg=f"{lines[3]}")
            theme_selector.config(bg=f"{lines[2]}",fg=f"{lines[3]}")
            themer_text.config(bg=f"{lines[1]}",fg=f"{lines[3]}")
            file_menu.config(bg=f"{lines[2]}",fg=f"{lines[3]}")
            aboutmenu.config(bg=f"{lines[2]}",fg=f"{lines[3]}")
            applied_theme_text.config(bg=f"{lines[1]}",fg=f"{lines[3]}",text=f"Applied theme: {selected_theme}")
            acent_color = f"{lines[1]}"
            secondary_acent = f"{lines[2]}"
            text_accent = f"{lines[3]}"
        
            
    global acent_color,secondary_acent,text_accent
    prefs = tk.Toplevel(root,bg=acent_color)
    prefs.title("Pisun editor - Preferences")
    themer_text = tk.Label(prefs,text="Theme selector",bg=acent_color,fg=text_accent)
    themer_text.pack()
    theme_selector = tk.Listbox(prefs,height=4,selectmode="single",bg=secondary_acent,fg=text_accent)
    themes = ["Light", "Dark", "Black","Custom theme"]
    theme_selector.pack()
    for i in themes:
        theme_selector.insert(tk.END,i)
    applied_theme_text = tk.Label(prefs,text=f"Applied theme: {selected_theme}",bg=acent_color,fg=text_accent)
    applied_theme_text.pack()
    apply_theme_button = tk.Button(prefs,text="Apply theme",command=apply_theme,bg=secondary_acent,fg=text_accent)
    apply_theme_button.pack()
    prefs.resizable(False,False)
    prefs.mainloop()
def open_RPCpreferences():
    def priv_mode_toggle():
        global priv_mode, Pisun_editor_rpc_multprcs, smallimage, smallimage_text
        if priv_mode == False:
            priv_mode = True
            setRPC(detail=details, status=state, image=smallimage, image_text=smallimage_text,vers=version)
            Pisun_editor_rpc_multprcs.terminate()
            Pisun_editor_rpc_multprcs.join()  
            Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
            Pisun_editor_rpc_multprcs.start()
            priv_mode_status.config(text="Privacy mode enabled", bg=acent_color,fg="green")
        else:
            priv_mode = False
            setRPC(detail=details_nonpriv, status=state_nonpriv, image=smallimage_nonpriv, image_text=smallimage_text_nonprv,vers=version_nonpriv)
            Pisun_editor_rpc_multprcs.terminate()
            Pisun_editor_rpc_multprcs.join()  
            Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
            Pisun_editor_rpc_multprcs.start()
            priv_mode_status.config(text="Privacy mode disabled", bg=acent_color,fg="red")
    RPCprefs = tk.Toplevel(root,bg=acent_color)
    RPCprefs.title("Pisun editor - RPC Preferences")
    RPCprefs.resizable(False, False)
    priv_mode_button = tk.Button(RPCprefs, text="Enable/disable privacy mode", command=priv_mode_toggle,bg=acent_color,fg=text_accent)
    priv_mode_status = tk.Label(RPCprefs, text="")
    priv_mode_status.pack()
    priv_mode_button.pack()
    if priv_mode == False:
        priv_mode_status.config(text="Privacy mode disabled", bg=acent_color,fg="red")
    if priv_mode == True:
        priv_mode_status.config(text="Privacy mode enabled",bg=acent_color, fg="green")
    RPCprefs.mainloop()
def beta_warning(feature,feature_name):
    def ackwnowledge():
        bta_warning.destroy()
        feature()
    def refuse():
        bta_warning.destroy()
    bta_warning = tk.Toplevel(root,bg=acent_color)
    bta_warning.title("Pisun editor - Beta feature")
    text1_warn = tk.Label(bta_warning,text=f"!Feature '{feature_name}' still in beta!",fg="red",bg=acent_color)
    text2_warn = tk.Label(bta_warning,text=f"By clicking 'I acknowledge', you will admit\nthat you will be ready for\nconsequences of code instability",bg=acent_color,fg=text_accent)
    button1_refuse = tk.Button(bta_warning,text="No no no! Get me back!",command=refuse,bg=acent_color,fg=text_accent)
    button2_acknowledge = tk.Button(bta_warning,text="I acknowledge",command=ackwnowledge,bg=acent_color,fg=text_accent)
    text1_warn.pack()
    text2_warn.pack()
    button1_refuse.pack()
    button2_acknowledge.pack()
    bta_warning.mainloop()



root = tk.Tk()
text_area = tk.Text(root, wrap='word')
text_area.pack(expand='yes', fill='both')
root.wm_title("Pisun Editor - Blank file")
Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, f"{smallimage_text}",version), daemon=True)
Pisun_editor_rpc_multprcs.start()
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)
aboutmenu = tk.Menu(menu_bar, tearoff=0)
aboutmenu.add_command(label="About...", command=open_about)
aboutmenu.add_command(label="Discord RPC Preferences...", command=open_RPCpreferences)
aboutmenu.add_command(label="Preferences...", command=open_prefs)
menu_bar.add_cascade(label="About", menu=aboutmenu)
root.config(menu=menu_bar)
root.mainloop()