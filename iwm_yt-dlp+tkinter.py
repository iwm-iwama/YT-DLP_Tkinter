#!/usr/bin/python3
#coding:utf-8

PROGRAM = "YT-DLP+Tkinter"
VERSION = "Ver.iwm20240504"

import shutil
import subprocess
import tkinter as Tk
import tkinter.scrolledtext as Tk_St
import tkinter.ttk as Tk_Ttk

from ctypes import *
from ctypes.wintypes import *
from tkinter import messagebox

#-------------------------------------------------------------------------------
# My Config
#-------------------------------------------------------------------------------
# YT-DLP Command & Option
CmdOpt = """
yt-dlp -f b
yt-dlp -x --audio-format mp3
echo
yt-dlp --help
"""

#-------------------------------------------------------------------------------
# Function
#-------------------------------------------------------------------------------
def Sub_Clear():
	# おまじない
	subprocess.run("clear || cls", shell=True)

def Sub_SimpleHelp():
	print(
		"\033[97;104m 簡易ヘルプ \033[0m" +
		"\n" +
		"\033[5G"  + "\033[93mYT-DLP コマンド／オプション" +
		"\n" +
		"\033[9G"  + "\033[96myt-dlp -f b" +
		"\n" +
		"\033[14G" + "\033[37m動画ファイルを最高画質でダウンロード" +
		"\n" +
		"\033[9G"  + "\033[96myt-dlp -x --audio-format mp3" +
		"\n" +
		"\033[14G" + "\033[37m音声ファイルをMP3でダウンロード" +
		"\n" +
		"\033[9G"  + "\033[96mecho" +
		"\n" +
		"\033[14G" + "\033[37mテスト" +
		"\n" +
		"\033[9G"  + "\033[96myt-dlp --help" +
		"\n" +
		"\033[14G" + "\033[37mオプション・ヘルプ" +
		"\n" +
		"\033[97;104m (END) \033[0m" +
		"\n"
	)

def Sub_YtDlp_Update():
	Cmd = "yt-dlp"
	if shutil.which(Cmd):
		Select = messagebox.askyesno(PROGRAM, "YT-DLP の更新を確認しますか ?")
		if Select == True:
			print(
				"\033[97;104m " + Cmd + " \033[0m" +
				"\n" +
				"    " +
				"\033[97m" + subprocess.run((Cmd + " --update-to nightly"), shell=True, capture_output=True, text=True).stdout.strip().replace("\n", "\n    ") +
				"\n" +
				"\033[97;104m (END) \033[0m" +
				"\n"
			)
		Sub_SimpleHelp()
	else:
		print(
			"\033[97;101m YT-DLP は以下のサイトから入手できます。 \033[0m" +
			"\n" +
			"\033[5G" + "\033[97mhttps://github.com/yt-dlp/yt-dlp#release-files" +
			"\n" +
			"\033[9G" + "\033[92mRecommended（推奨版）" +
			"\033[0m" + "\n"
		)

def Sub_Terminal_Reposition():
	# Windows以外で例外発生
	try:
		hwnd = windll.user32.GetForegroundWindow()
		windll.user32.MoveWindow(hwnd, int(30), int(60), int((Root.winfo_screenwidth() / 2) - 240), int(Root.winfo_screenheight() - 120), True)
	except(NameError, SyntaxError):
		pass

def Sub_Root_Resize(e):
	if e.widget is Root:
		CmdOpt_Cb1.place(width=e.width-152)
		CmdOpt_Exec_Btn1.place(x=e.width-147)
		Args_St1.place(width=e.width-10, height=e.height-79)
		Args_Clear_Btn1.place(x=e.width-147)
		Args_Paste_Btn1.place(x=e.width-85)

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
	else:
		a1 += [s2]
	Sub_Clear()
	Cnt = 0
	for _s1 in a1:
		_s1 = _s1.strip()
		print("\033[97;104m " + _s1 + " \033[0m")
		try:
			subprocess.run(_s1, shell=True)
			Cnt += 1
		except:
			break
	a1 = []
	AddStr = str(Cnt) + " Count"
	if Cnt > 1:
		AddStr += "s"
	print("\n" + "\033[97;104m (END) " + AddStr + " \033[0m")

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
# Window 初期サイズ
min = {
	"W": 480,
	"H": 300
}
# Window 初期ポジション
pos = {
	"X": int((Root.winfo_screenwidth() - min["W"]) / 2),
	"Y": int((Root.winfo_screenheight() - min["H"]) / 2)
}
Root.bind("<Configure>", Sub_Root_Resize)
Root.configure(bg="#555")
Root.geometry(f'{min["W"]}x{min["H"]}+{pos["X"]}+{pos["Y"]}')
Root.minsize(width=min["W"], height=min["H"])
Root.resizable(width=True, height=True)
Root.title(PROGRAM + " " + VERSION)

#-------------------------------------------------------------------------------
# Command & Option
#-------------------------------------------------------------------------------
CmdOpt_Lbl1 = Tk.Label(text="YT-DLP コマンド／オプション", font=("Helvetica", 10, "bold"), fg="white", bg="#555")

a1 = CmdOpt.strip().split("\n")
CmdOpt_Cb1 = Tk_Ttk.Combobox(Root, font=("Courier", 10), values=(a1))
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
Args_Lbl1 = Tk.Label(text="YouTube URL／改行区切り", font=("Helvetica", 10, "bold"), fg="white", bg="#555")

Args_St1 = Tk_St.ScrolledText(Root, font=("Courier", 11), relief="flat", borderwidth=0, undo="true", insertofftime=0)
obj1 = Args_St1
obj1.bind("<Button-3>", Sub_Args_St1_ContextMenu)
obj1.configure(state="normal")

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

Args_Clear_Btn1 = Tk.Button(Root, text="クリア", font=("Helvetica", 9), fg="white", bg="navy", relief="flat", cursor="hand2", command=Sub_St_Clear_All(obj=Args_St1))
Args_Paste_Btn1 = Tk.Button(Root, text="ペースト", font=("Helvetica", 9), fg="white", bg="mediumblue", relief="flat", cursor="hand2", command=Sub_St_Paste_All(obj=Args_St1))

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------
CmdOpt_Lbl1.place(x=5, y=3)
CmdOpt_Cb1.place(x=5, y=23, height=20)
CmdOpt_Exec_Btn1.place(y=23, width=62, height=20)
Args_Lbl1.place(x=5, y=53)
Args_St1.place(x=5, y=73)
Args_Clear_Btn1.place(y=53, width=62, height=20)
Args_Paste_Btn1.place(y=53, width=80, height=20)

# 前処理
Sub_Terminal_Reposition()
Sub_Clear()
Sub_YtDlp_Update()
CmdOpt_Cb1.focus_force()

Root.mainloop()
Root.quit()
