#!/usr/bin/python3
#coding:utf-8

VERSION = "YT-DLP+Tkinter Ver.iwm20231227"

import shutil
import subprocess
import tkinter as Tk
import tkinter.scrolledtext as Tk_St
import tkinter.ttk as Tk_Ttk

from ctypes import *
from ctypes.wintypes import *

#-------------------------------------------------------------------------------
# My Config
#-------------------------------------------------------------------------------
# YT-DLP Command & Option
CmdOpt = """
yt-dlp -f b
yt-dlp -x --audio-format mp3
echo
"""

#-------------------------------------------------------------------------------
# Function
#-------------------------------------------------------------------------------
def Sub_Clear():
	# WindowsでESCを有効にするおまじない
	subprocess.run("cls || clear", shell=True)

def Sub_Terminal_Reposition():
	# Windows以外で例外発生
	try:
		hwnd = windll.user32.GetForegroundWindow()
		windll.user32.MoveWindow(hwnd, int(30), int(60), int(640), int(Root.winfo_screenheight() - 120), True)
	except(NameError, SyntaxError):
		pass

def Sub_YtDlp_Update():
	print("\033[97;104m YT-DLP Update \033[0m")
	CMD = "yt-dlp"
	if shutil.which(CMD):
		print(
			"\033[93m",
			subprocess.run(CMD + " --update-to nightly", shell=True, capture_output=True, text=True).stdout,
			"\033[0m"
		)
	else:
		print(
			"   \033[91mNot Installed.\033[0m\n",
			"   YT-DLP は以下のサイトから入手できます。\n",
			"     \033[93mhttps://github.com/yt-dlp/yt-dlp#release-files\033[0m\n",
			"     \033[96m・Recommended（推奨版）\033[0m"
		)
	print("\033[97;104m (END) \033[0m")

def Sub_Root_Resize(e):
	if e.widget is Root:
		CmdOpt_Cb1.place(width=e.width-170)
		CmdOpt_Exec_Btn1.place(x=e.width-160)
		Args_St1.place(width=e.width-10, height=e.height-90)
		Args_Clear_Btn1.place(x=e.width-160)
		Args_Paste_Btn1.place(x=e.width-100)

def Sub_CmdOpt_Cb1_ContextMenu(e):
	obj1 = CmdOpt_Cb1
	obj2 = None
	if obj1.selection_present() == True:
		obj2 = Cb_ContextMenu_Select
	else:
		obj2 = Cb_ContextMenu_All
	obj2.post(e.x_root, e.y_root)

def Sub_Cb_Clear_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_Cb_Clear_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.delete("0", "end")
	return inner

def Sub_Cb_Copy_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.selection_get())
	return inner

def Sub_Cb_Copy_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get())
	return inner

def Sub_Cb_Cut_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.selection_get())
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_Cb_Cut_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get())
		obj.delete("0", "end")
	return inner

def Sub_Cb_Paste_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		try:
			text = Root.selection_get(selection="CLIPBOARD").rstrip()
			obj.delete("sel.first", "sel.last")
			obj.insert("insert", text)
		except:
			pass
	return inner

def Sub_Cb_Paste_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		try:
			text = Root.selection_(selection="CLIPBOARD").rstrip()
			obj.insert("insert", text)
		except:
			pass
	return inner

def Sub_CmdOpt_Exec_Btn1(e=None):
	obj1 = Args_St1
	obj2 = CmdOpt_Cb1
	s1 = obj1.get("1.0", "end-1c").strip()
	s2 = obj2.get().strip()
	a1 = []
	if len(s1) > 0:
		for _ln in s1.split("\n"):
			_ln = _ln.strip()
			if len(_ln) > 0:
				a1 += [(s2 + " " + _ln)]
	Sub_Clear()
	if len(a1) == 0:
		print("\033[39;101m No input data! \033[0m")
		return
	for _s1 in a1:
		_s1 = _s1.strip()
		print("\033[97;44m ", _s1, " \033[0m")
		try:
			subprocess.run(_s1, shell=True)
		except:
			break
		print("\033[97;44m (END) \033[0m\n")
	a1 = []

def Sub_Args_St1_ContextMenu(e):
	obj1 = Args_St1
	obj2 = None
	if obj1.tag_ranges("sel"):
		obj2 = St_ContextMenu_Select
	else:
		obj2 = St_ContextMenu_All
	obj2.post(e.x_root, e.y_root)

def Sub_St_Clear_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_St_Clear_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.delete("1.0", "end")
	return inner

def Sub_St_Copy_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("sel.first", "sel.last"))
	return inner

def Sub_St_Copy_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("1.0", "end-1c"))
	return inner

def Sub_St_Cut_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("sel.first", "sel.last"))
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_St_Cut_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("1.0", "end-1c"))
		obj.delete("1.0", "end")
	return inner

def Sub_St_Paste_Select(obj=None, e=None):
	if obj == None:
		return
	def inner():
		try:
			text = Root.selection_get(selection="CLIPBOARD").rstrip()
			obj.delete("sel.first", "sel.last")
			obj.insert("insert", text + "\n")
			obj.see("insert")
		except:
			pass
	return inner

def Sub_St_Paste_All(obj=None, e=None):
	if obj == None:
		return
	def inner():
		try:
			text = Root.selection_get(selection="CLIPBOARD").rstrip()
			obj.insert("insert", text + "\n")
			obj.see("insert")
		except:
			pass
	return inner

#-------------------------------------------------------------------------------
# Window Root
#-------------------------------------------------------------------------------
Root = Tk.Tk()
min = {
	"W": 560,
	"H": 320
}
pos = {
	"X": int((Root.winfo_screenwidth() - min["W"]) / 2),
	"Y": int((Root.winfo_screenheight() - min["H"]) / 2)
}
Root.bind("<Configure>", Sub_Root_Resize)
Root.configure(bg="dimgray")
Root.geometry(f'{min["W"]}x{min["H"]}+{pos["X"]}+{pos["Y"]}')
Root.minsize(width=min["W"], height=min["H"])
Root.resizable(width=True, height=True)
Root.title(VERSION)

#-------------------------------------------------------------------------------
# Command & Option
#-------------------------------------------------------------------------------
CmdOpt_Lbl1 = Tk.Label(text="TY-DLP コマンド＆オプション", font=("Helvetica", 10, "bold"), fg="white", bg="dimgray")

a1 = CmdOpt.strip().split("\n")
CmdOpt_Cb1 = Tk_Ttk.Combobox(Root, font=("Courier", 11), values=(a1))
obj1 = CmdOpt_Cb1
obj1.bind("<Button-3>", Sub_CmdOpt_Cb1_ContextMenu)
obj1.insert("end", a1[0])
a1 = []

# 範囲指定あり
Cb_ContextMenu_Select = Tk.Menu(Root, tearoff=0, font=("Helvetica", 10))
obj1 = Cb_ContextMenu_Select
obj1.add_command(label="クリア", command=Sub_Cb_Clear_Select(obj=CmdOpt_Cb1))
obj1.add_separator()
obj1.add_command(label="コピー", command=Sub_Cb_Copy_Select(obj=CmdOpt_Cb1))
obj1.add_command(label="カット", command=Sub_Cb_Cut_Select(obj=CmdOpt_Cb1))
obj1.add_command(label="ペースト", command=Sub_Cb_Paste_Select(obj=CmdOpt_Cb1))

# 範囲指定なし
Cb_ContextMenu_All = Tk.Menu(Root, tearoff=0, font=("Helvetica", 10))
obj1 = Cb_ContextMenu_All
obj1.add_command(label="全クリア", command=Sub_Cb_Clear_All(obj=CmdOpt_Cb1))
obj1.add_separator()
obj1.add_command(label="全コピー", command=Sub_Cb_Copy_All(obj=CmdOpt_Cb1))
obj1.add_command(label="全カット", command=Sub_Cb_Cut_All(obj=CmdOpt_Cb1))
obj1.add_command(label="ペースト", command=Sub_Cb_Paste_All(obj=CmdOpt_Cb1))

CmdOpt_Exec_Btn1 = Tk.Button(Root, text="実行", font=("Helvetica", 10), fg="#ffffff", bg="crimson", relief="flat", cursor="hand2", command=Sub_CmdOpt_Exec_Btn1)

#-------------------------------------------------------------------------------
# Argument
#-------------------------------------------------------------------------------
Args_Lbl1 = Tk.Label(text="YouTube URL／改行区切り", font=("Helvetica", 10, "bold"), fg="white", bg="dimgray")

Args_St1 = Tk_St.ScrolledText(Root, font=("Courier", 11), relief="flat", borderwidth=4, undo="true", highlightthickness=1, highlightbackground="#777777", highlightcolor="#7777ff", insertofftime=0)
obj1 = Args_St1
obj1.bind("<Button-3>", Sub_Args_St1_ContextMenu)
obj1.configure(state="normal")
obj1.focus_set()

# 範囲指定あり
St_ContextMenu_Select = Tk.Menu(Root, font=("Helvetica", 10), tearoff=0)
obj1 = St_ContextMenu_Select
obj1.add_command(label="クリア", command=Sub_St_Clear_Select(obj=Args_St1))
obj1.add_separator()
obj1.add_command(label="コピー", command=Sub_St_Copy_Select(obj=Args_St1))
obj1.add_command(label="カット", command=Sub_St_Cut_Select(obj=Args_St1))
obj1.add_command(label="ペースト", command=Sub_St_Paste_Select(obj=Args_St1))

# 範囲指定なし
St_ContextMenu_All = Tk.Menu(Root, font=("Helvetica", 10), tearoff=0)
obj1 = St_ContextMenu_All
obj1.add_command(label="全クリア", command=Sub_St_Clear_All(obj=Args_St1))
obj1.add_separator()
obj1.add_command(label="全コピー", command=Sub_St_Copy_All(obj=Args_St1))
obj1.add_command(label="全カット", command=Sub_St_Cut_All(obj=Args_St1))
obj1.add_command(label="ペースト", command=Sub_St_Paste_All(obj=Args_St1))

Args_Clear_Btn1 = Tk.Button(Root, text="クリア", font=("Helvetica", 8), fg="white", bg="darkblue", relief="flat", cursor="hand2", command=Sub_St_Clear_All(obj=Args_St1))
Args_Paste_Btn1 = Tk.Button(Root, text="ペースト", font=("Helvetica", 8), fg="white", bg="mediumblue", relief="flat", cursor="hand2", command=Sub_St_Paste_All(obj=Args_St1))

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------
Sub_Clear()
Sub_Terminal_Reposition()
Sub_YtDlp_Update()

# Sub_Root_Resize(e) で自動調整
CmdOpt_Lbl1.place(x=10, y=5)
CmdOpt_Cb1.place(x=10, y=25, height=22)
CmdOpt_Exec_Btn1.place(y=25, width=59, height=22)
Args_Lbl1.place(x=10, y=55)
Args_St1.place(x=10, y=75)
Args_Clear_Btn1.place(y=55, width=59, height=19)
Args_Paste_Btn1.place(y=55, width=83, height=19)

Root.mainloop()
Root.quit()
