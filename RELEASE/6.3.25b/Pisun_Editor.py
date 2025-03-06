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
version = "RELEASE 6.3.25b PUBLIC"
version_nonpriv = ""
connected =True
filepath_save = ""
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
    global Pisun_editor_rpc_multprcs, state, details, smallimage, smallimage_text,filepath_save
    filepath_save = ""
    text_area.delete(1.0, tk.END)
    root.wm_title("Pisun Editor - Blank file")
    Pisun_editor_rpc_multprcs.terminate()
    Pisun_editor_rpc_multprcs.join()  
    setRPC(detail="Blank file", status="Blank document", image="blank", image_text=f"Blank File",vers=version)
    Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
    Pisun_editor_rpc_multprcs.start()
def open_file():
    global Pisun_editor_rpc_multprcs, state, details, smallimage, smallimage_text,filepath_save
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        filepath_save = file_path
        root.wm_title(f"Pisun Editor - {file_path}")
        Pisun_editor_rpc_multprcs.terminate()
        Pisun_editor_rpc_multprcs.join()  
        setRPC(detail=file_path, status="Editing", image="editing", image_text=f"Editing {file_path}",vers=version)
        Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
        Pisun_editor_rpc_multprcs.start()
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
def saveas_file():
    global filepath_save,Pisun_editor_rpc_multprcs
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        filepath_save = file_path
        root.wm_title(f"Pisun Editor - {file_path}")
        Pisun_editor_rpc_multprcs.terminate()
        Pisun_editor_rpc_multprcs.join()  
        setRPC(detail=f"{file_path}", status="Editing", image="editing", image_text=f"Editing {file_path}",vers=version)
        Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
        Pisun_editor_rpc_multprcs.start()
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
def save_file():
    global filepath_save,Pisun_editor_rpc_multprcs
    if filepath_save:
        with open(filepath_save, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            filepath_save = file_path
            root.wm_title(f"Pisun Editor - {file_path}")
            Pisun_editor_rpc_multprcs.terminate()
            Pisun_editor_rpc_multprcs.join()  
            setRPC(detail=f"{file_path}", status="Editing", image="editing", image_text=f"Editing {file_path}",vers=version)
            Pisun_editor_rpc_multprcs = multiprocessing.Process(target=start_rpc, args=(details, state, smallimage, smallimage_text,version), daemon=True)
            Pisun_editor_rpc_multprcs.start()
            with open(file_path, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
def open_about():
    about_window = tk.Toplevel(root,bg=acent_color)
    appname_text = tk.Label(about_window, text=f"Pisun Editor {version}",bg=acent_color,fg=text_accent)
    author_text = tk.Label(about_window, text="By Aibo The Dog",bg=acent_color,fg=text_accent)
    about_text = tk.Label(about_window, text="Pisun Editor - Open-source text editor\nwith theme features and \nDiscord RPC",bg=acent_color,fg=text_accent)
    gnu_text = tk.Label(about_window, text="\nGNU GENERAL PUBLIC LICENSE applied on this app. \nRead LICENSE on repo for the license ",bg=acent_color,fg=text_accent)
    appname_text.pack()
    author_text.pack()
    about_text.pack()
    gnu_text.pack()
    about_window.title("Pisun editor - About")
    about_window.resizable(False, False)
    about_window.mainloop()
def exit_editor():
    root.destroy()
def open_themer():
    def set_theme():
        global acent_color,secondary_acent,text_accent,selected_theme,Pisun_editor_rpc_multprcs
        selected_indices = theme_selector.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            theme_selected = theme_selector.get(selected_index)
            print(f"Selected theme: {theme_selected}")
            if theme_selected == "Dark":
                selected_theme = "Dark"
                acent_color = "gray26"
                secondary_acent = "gray33"
                text_accent = "gray77"
                apply_theme(acent_color,secondary_acent,text_accent)
            elif theme_selected == "Black":
                selected_theme = "Black"
                acent_color = "black"
                secondary_acent = "gray6"
                text_accent = "white"
                apply_theme(acent_color,secondary_acent,text_accent)
            elif theme_selected == "Light":
                selected_theme = "Light"
                acent_color = "white"
                secondary_acent = "gray84"
                text_accent = "black"
                apply_theme(acent_color,secondary_acent,text_accent)
            elif theme_selected == "Custom theme":
                set_custom_theme()
        else:
            print("No theme selected")
    def apply_theme(prim,secnd,text):
        global RPC
        root.config(bg=prim)
        menu_bar.config(bg=secnd,fg=text)
        text_area.config(bg=prim,fg=text)
        prefs.config(bg=prim)
        apply_theme_button.config(bg=prim,fg=text)
        theme_selector.config(bg=prim,fg=text)
        themer_text.config(bg=prim,fg=text)
        file_menu.config(bg=secnd,fg=text)
        about_menu.config(bg=secnd,fg=text)
        settings_menu.config(bg=secnd,fg=text)
        prefs_dropmenu.config(bg=secnd,fg=text)
        discord_rel_setts.config(bg=secnd,fg=text)
        misc_menu.config(bg=secnd,fg=text)
        applied_theme_text.config(bg=prim,fg=text,text=f"Applied theme: {selected_theme}")
    def set_custom_theme():
        global acent_color,secondary_acent,text_accent,selected_theme,Pisun_editor_rpc_multprcs
        themefile = filedialog.askopenfilename()
        if themefile:
            with open(themefile,'r') as file:
                lines = [line.replace("\n","") for line in file.readlines()]
            print(lines)
            acent_color = f"{lines[1]}"
            secondary_acent = f"{lines[2]}"
            text_accent = f"{lines[3]}"
            selected_theme = f"{lines[0]}"
            apply_theme(acent_color,secondary_acent,text_accent)
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
    apply_theme_button = tk.Button(prefs,text="Apply theme",command=set_theme,bg=secondary_acent,fg=text_accent)
    apply_theme_button.pack()
    prefs.resizable(False,False)
    prefs.mainloop()
def open_privacy_mode_setts_RPC():
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
    bta_warning.resizable(False,False)
    text1_warn.pack()
    text2_warn.pack()
    button1_refuse.pack()
    button2_acknowledge.pack()
    bta_warning.mainloop()
def confirmation(action,action_name):
    def ok():
        confirm_window.destroy()
        action()
    def no():
        confirm_window.destroy()
    confirm_window = tk.Toplevel(root,bg=acent_color)
    confirm_window.title("Pisun editor - Are you sure?")
    confirm_window.resizable(False,False)
    text1 = tk.Label(confirm_window,text=f"Are you sure you want to\n{action_name}?",fg=text_accent,bg=acent_color)
    button1_yes = tk.Button(confirm_window,text="Yes",command=ok,bg=acent_color,fg=text_accent)
    button2_no = tk.Button(confirm_window,text="No",command=no,bg=acent_color,fg=text_accent)
    text1.pack()
    button1_yes.pack(side="left")
    button2_no.pack(side="right")
    confirm_window.mainloop()
def save_and_exit():
    global filepath_save
    save_file()
    if filepath_save:
        root.destroy()
def arbitrary_code_executor():
    code_exector = tk.Toplevel(root,bg=acent_color)
    code_exector.title("Pisun Editor - Code executor")
    text_code_exec = tk.Label(code_exector,text="Code executor\nIt used for executing\nexternal code in Pisun Editor\nRequires one-line code",bg=acent_color,fg=text_accent)
    code_entry = tk.Entry(code_exector,bg=acent_color,fg=text_accent)
    code_execute = tk.Button(code_exector,text="Execute!",bg=acent_color,fg=text_accent, command=lambda: eval(code_entry.get()))
    text_code_exec.pack()
    code_entry.pack()
    code_execute.pack()
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
file_menu.add_command(label="Save as...", command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label="Save and exit", command=lambda: confirmation(save_and_exit,"Save and exit"))
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)
settings_menu = tk.Menu(menu_bar,tearoff=0)
discord_rel_setts = tk.Menu(settings_menu,tearoff=0)
discord_rel_setts.add_command(label="Privacy mode", command=open_privacy_mode_setts_RPC)
prefs_dropmenu = tk.Menu(settings_menu,tearoff=0)
prefs_dropmenu.add_command(label="Themer", command=open_themer)
settings_menu.add_cascade(label="Discord RPC related prefs",menu=discord_rel_setts)
settings_menu.add_cascade(label="Preferences...",menu=prefs_dropmenu)
menu_bar.add_cascade(label="Preferences",menu=settings_menu)
misc_menu = tk.Menu(menu_bar,tearoff=0)
misc_menu.add_command(label="Code executor", command=arbitrary_code_executor)
menu_bar.add_cascade(label="Misc", menu=misc_menu)
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About...", command=open_about)
menu_bar.add_cascade(label="About", menu=about_menu)
root.config(menu=menu_bar)
root.mainloop()