#!/usr/bin/env python3
#coding:utf-8

PROGRAM = "YT-DLP+Tkinter"
VERSION = "Ver.iwm20260729"

import os
import shutil
import subprocess
import sys
import time
import tkinter as Tk
import tkinter.filedialog as Tk_Fd
import tkinter.scrolledtext as Tk_St
import tkinter.ttk as Tk_Ttk

from ctypes import *
from ctypes.wintypes import *
from tkinter import messagebox

try:
	import winreg
except Exception:
	pass

#-------------------------------------------------------------------------------
# My Config
#-------------------------------------------------------------------------------
# YT-DLP Command & Option
LIST_COMMAND = """
yt-dlp -f bestvideo*+bestaudio/best
yt-dlp -x --audio-format mp3
yt-dlp --help
echo
wget -rN
"""

# Base
FontType  = "TkFixedFont"
FontColor = "#fff"
BackColor = "#363636"

#-------------------------------------------------------------------------------
# W0 = Window[0]
#-------------------------------------------------------------------------------
class _Terminal:
	def Help():
		BG = " " * 60
		print(
			"\033[97;44m" +
			BG +
			"\033[2G" +
			"簡易ヘルプ" +
			"\033[0m" +
			"\n" +
			"\n" +
			"\033[2G" +
			"\033[93m" +
			"YT-DLP コマンド／オプション" +
			"\n" +
			"\n" +
			"\033[5G" +
			"\033[96m" +
			"yt-dlp -f bestvideo*+bestaudio/best" +
			"\n" +
			"\033[9G" +
			"\033[97m" +
			"動画ファイルを最高画質でダウンロード" +
			"\n" +
			"\n" +
			"\033[5G" +
			"\033[96m" +
			"yt-dlp -x --audio-format mp3" +
			"\n" +
			"\033[9G" +
			"\033[97m" +
			"音声ファイルをMP3でダウンロード" +
			"\n" +
			"\n" +
			"\033[5G" +
			"\033[96m" +
			"yt-dlp --help" +
			"\n" +
			"\033[9G" +
			"\033[97m" +
			"オプション・ヘルプ" +
			"\n" +
			"\n" +
			"\033[97;44m" +
			BG +
			"\033[2G" +
			"END" +
			"\033[0m" +
			"\n"
		)

	def Clear():
		# おまじない
		subprocess.run("clear || cls", shell=True)

	def YtDlp_Update():
		_Terminal.Clear()
		Cmd = "yt-dlp"
		if shutil.which(Cmd):
			rtn = messagebox.askyesno(PROGRAM, "YT-DLP の更新を確認しますか ?")
			if rtn:
				print(
					"\033[38;2;255;192;0m" +
					subprocess.run(
						f"{Cmd} --update-to nightly",
						shell=True,
						capture_output=True,
						text=True
					).stdout.strip() +
					"\033[0m"
				)
			print()
			_Terminal.Help()
		else:
			print(
				"\033[97;41m " +
				"YT-DLP は以下のサイトから入手できます。" +
				" \033[0m" +
				"\n" +
				"\033[5G" +
				"\033[97m" +
				"https://github.com/yt-dlp/yt-dlp#release-files" +
				"\n" +
				"\033[9G" +
				"\033[96m" +
				"Recommended（推奨版）" +
				"\033[0m"
			)

class _W0:
	#---------
	# 前処理
	#---------
	# ダイアログは最前面に "固定表示されない" ので別途表示
	_Terminal.YtDlp_Update()

	#-----
	# W0
	#-----
	global W0
	W0 = Tk.Tk()

class _C11:
	C11 = Tk.Label(
		text="YT-DLP コマンド",
		font=(FontType, 9, "bold"),
		fg=FontColor,
		bg=BackColor
	)
	C11.place(x=4, y=2)

class _C21:
	def Clear(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			if select_all:
				obj.delete("0", "end")
			else:
				obj.delete("sel.first", "sel.last")
		return inner

	def Copy(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all:
				obj.clipboard_append(obj.get())
			else:
				obj.clipboard_append(obj.selection_get())
		return inner

	def Cut(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all:
				obj.clipboard_append(obj.get())
				obj.delete("0", "end")
			else:
				obj.clipboard_append(obj.selection_get())
				obj.delete("sel.first", "sel.last")
		return inner

	def Paste(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			text = obj.selection_get(selection="CLIPBOARD").rstrip()
			if select_all == False:
				obj.delete("sel.first", "sel.last")
			obj.insert("insert", text)
		return inner

	def Button_1(e):
		try:
			C21_ContextMenu.destroy()
		except:
			pass

	def ButtonRelease_1(e):
		obj1 = Tk.Menu(W0, tearoff=0, font=(FontType, 10))
		if C21.selection_present():
			obj1.add_command(label="クリア", command=_C21.Clear(obj=C21, select_all=False))
			obj1.add_separator()
			obj1.add_command(label="コピー", command=_C21.Copy(obj=C21, select_all=False))
			obj1.add_command(label="カット", command=_C21.Cut(obj=C21, select_all=False))
			obj1.add_command(label="ペースト", command=_C21.Paste(obj=C21, select_all=False))
		obj1.post(e.x_root, e.y_root)
		C21_ContextMenu = obj1

	def Button_3(e):
		obj1 = Tk.Menu(W0, tearoff=0, font=(FontType, 10))
		obj1.add_command(label="全クリア", command=_C21.Clear(obj=C21, select_all=True))
		obj1.add_separator()
		obj1.add_command(label="全コピー", command=_C21.Copy(obj=C21, select_all=True))
		obj1.add_command(label="全カット", command=_C21.Cut(obj=C21, select_all=True))
		obj1.add_command(label="ペースト", command=_C21.Paste(obj=C21, select_all=True))
		obj1.post(e.x_root, e.y_root)
		C21_ContextMenu = obj1

	a1 = LIST_COMMAND.strip().split("\n")

	global C21
	C21 = Tk_Ttk.Combobox(
		W0,
		font=(FontType, 11),
		values=a1
	)
	C21.place(x=4, y=22, height=20)
	C21.bind("<Button-1>", Button_1)
	C21.bind("<ButtonRelease-1>", ButtonRelease_1)
	C21.bind("<Button-3>", Button_3)
	C21.insert("end", a1[0])

class _C22:
	def Click(e = None):
		_Terminal.Clear()
		TmBgn = time.time()
		sData = C51.get("1.0", "end-1c").strip()
		sCmd = C21.get().strip()
		aCmd = []
		if sData:
			# yt-dlp コマンドのときはオプション追記（後述）
			iCmd = sCmd.upper().find("YT-DLP")
			for _data in sData.split("\n"):
				_data = _data.strip()
				if _data:
					# DLファイル名の文字数制限オプション追記
					#   (例) "あ" = １文字／3byte
					#     255 / 3 ≒ 85 > 80
					#     80 - DLフォルダ長
					_sCmd = sCmd
					if iCmd >= 0:
						_sCmd += f" --trim-filenames {(80 - len(os.getcwd()))}"
					# 末尾に引数追記
					_sCmd += f" {_data}"
					# エラーになる文字を変換
					aCmd += [(_sCmd.replace("&", "%26"))]
		else:
			aCmd += [sCmd]
		# 並列処理数(Min=2)は動的に変更
		GblPS = 2
		ListPS = []
		CntParallel = 0
		Cnt = 0
		for _s1 in aCmd:
			Cnt += 1
			print(f"\033[97;44m({Cnt}) {_s1}\033[0m")
			try:
				# 計測開始
				SwBgn = time.perf_counter()

				_ps = subprocess.Popen(_s1.split(), shell=False)

				# 計測終了
				SwEnd = time.perf_counter()

				# 並列処理のとき
				if C23_Var.get():
					# PSリスト作成
					ListPS.append(_ps)
					CntParallel += 1
					if CntParallel >= GblPS:
						CntParallel = 0
						# 計測時間が 1秒未満 なら並列処理数 +2
						if (SwEnd - SwBgn) < 1.0:
							GblPS += 2
						# 計測時間が 1秒以上 なら並列処理数 -1 ただし 最低値は 2
						else:
							if GblPS > 2:
								GblPS -= 1
						print(f"\033[95m[Concurrent Processes = {GblPS}]\033[0m")
				# 単一処理のとき
				else:
					_ps.wait()
			except:
				print(
					"\033[91m" +
					"[Err] コマンドを間違っていませんか？"
				)
			# Debug
			##except Exception as e:
			##print(str(e))
		# 処理待ち
		for _ps in ListPS:
			_ps.wait()
		TmEnd = time.time()
		s1 = "counts" if Cnt > 1 else "count"
		s2 = ""
		# 経過時間
		diffSec = TmEnd - TmBgn
		if diffSec >= 60.0:
			d1 = diffSec
			iH = int(d1 / 3600)
			d1 -= (iH * 3600)
			iM = int(d1 / 60)
			d1 -= (iM * 60)
			iS = int(d1)
			if diffSec >= 3600.0:
				s2 = f"{iH:d}h {iM:d}m {iS:d}s"
			elif diffSec >= 60.0:
				s2 = f"{iM:d}m {iS:d}s"
		else:
			s2 = f"{diffSec:.2f}s"
		print(f"\n\033[97;44m(END) {Cnt} {s1} / {s2} \033[0m")
		print()

	global C22
	C22 = Tk.Button(
		W0,
		text="実行",
		font=(FontType, 9),
		fg=FontColor,
		bg="crimson",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		activebackground="orange",
		activeforeground="black",
		command=Click
	)
	C22.place(y=22, width=60, height=20)

class _C23:
	global C23, C23_Var
	C23_Var = Tk.IntVar()
	C23_Var.set(True)
	C23 = Tk.Checkbutton(
		W0,
		text="並列処理",
		font=(FontType, 9),
		fg=FontColor,
		bg=BackColor,
		highlightthickness=0,
		cursor="hand2",
		activebackground="orange",
		activeforeground="black",
		selectcolor="black",
		variable=C23_Var
	)
	C23.place(y=22, width=80, height=20)

class _C31:
	C31 = Tk.Label(
		text="=>",
		font=(FontType, 9, "bold"),
		fg="gray60",
		bg=BackColor
	)
	C31.place(x=4, y=48)

class _C32:
	if os.path.isdir("/usr/bin"):
		path = os.getcwd()
	else:
		def getWinDesktopPath():
			key = winreg.OpenKey(
				winreg.HKEY_CURRENT_USER,
				r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
			)
			path, _ = winreg.QueryValueEx(key, "Desktop")
			return os.path.expandvars(path)
		path = getWinDesktopPath()

	os.chdir(path)
	curDir = Tk.StringVar(value=path)

	global C32
	C32 = Tk.Entry(
		W0,
		font=(FontType, 9),
		fg=FontColor,
		bg=BackColor,
		readonlybackground=BackColor,
		relief="flat",
		highlightthickness=1,
		highlightbackground="gray40",
		highlightcolor="gray40",
		textvariable=curDir,
		state="readonly"
	)
	C32.place(x=25, y=48, height=20)

class _C33:
	def fileDialog():
		path = Tk_Fd.askdirectory(initialdir=C32.get())
		if path:
			C32.config(state="normal")
			C32.delete(0, Tk.END)
			C32.insert(0, path)
			C32.config(state="readonly")
			os.chdir(path)

	global C33
	C33 = Tk.Button(
		W0,
		text="選択",
		font=(FontType, 9),
		fg=FontColor,
		bg="gray40",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		activebackground="orange",
		activeforeground="black",
		command=fileDialog
	)
	C33.place(y=48, width=60, height=20)

# C51 < C47, C48, C49
class _C51:
	def FileRead(obj = None, e = None):
		if obj == None:
			return
		def inner():
			filetype = [("All Files", "*")]
			path = Tk_Fd.askopenfilename(initialdir=".", filetypes=filetype)
			if len(path) == 0 or os.path.isfile(path) == False:
				return
			with open(path, "rb") as iFp:
				bin = iFp.read()
			if not bin:
				messagebox.showerror(PROGRAM, "空のファイル")
				return
			rtn = ""
			# CP932 ?
			try:
				rtn = bin.decode("CP932")
			except:
				rtn = ""
			# CP65001 ?
			if not rtn:
				try:
					rtn = bin.decode("CP65001")
					# BOM ?
					if rtn[0] == "\ufeff":
						rtn = rtn[1:len(rtn)]
				except:
					rtn = ""
			# Binary ?
			if not rtn:
				messagebox.showerror(PROGRAM, "ファイル読込失敗")
				return
			# 改行を '\n' に統一
			rtn = rtn.replace("\r\n", "\n").rstrip() + "\n"
			obj.insert("insert", rtn)
			obj.see("insert")
		return inner

	def Clear(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			if select_all:
				obj.delete("1.0", "end")
			else:
				obj.delete("sel.first", "sel.last")
		return inner

	def Copy(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all:
				obj.clipboard_append(obj.get("1.0", "end-1c"))
			else:
				obj.clipboard_append(obj.get("sel.first", "sel.last"))
		return inner

	def Cut(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all:
				obj.clipboard_append(obj.get("1.0", "end-1c"))
				obj.delete("1.0", "end")
			else:
				obj.clipboard_append(obj.get("sel.first", "sel.last"))
				obj.delete("sel.first", "sel.last")
		return inner

	def Paste(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			text = obj.selection_get(selection="CLIPBOARD").rstrip()
			if select_all == False:
				obj.delete("sel.first", "sel.last")
			obj.insert("insert", text)
			obj.see("insert")
		return inner

	def Add(obj = None, e = None):
		if obj == None:
			return
		def inner():
			s1 = obj.get("1.0", "end").strip()
			if s1:
				s1 += "\n"
			obj.delete("1.0", "end")
			s2 = ""
			try:
				s2 = obj.selection_get(selection="CLIPBOARD").strip()
				if s2:
					s2 += "\n"
			except:
				pass
			obj.insert("insert", (s1 + s2))
			obj.see("insert")
		return inner

	def Button_1(e):
		try:
			C51_ContextMenu.destroy()
		except:
			pass

	def ButtonRelease_1(e):
		obj1 = Tk.Menu(W0, font=(FontType, 10), tearoff=0)
		if C51.tag_ranges("sel"):
			obj1.add_command(label="クリア", command=_C51.Clear(obj=C51, select_all=False))
			obj1.add_separator()
			obj1.add_command(label="コピー", command=_C51.Copy(obj=C51, select_all=False))
			obj1.add_command(label="カット", command=_C51.Cut(obj=C51, select_all=False))
			obj1.add_command(label="ペースト", command=_C51.Paste(obj=C51, select_all=False))
		obj1.post(e.x_root, e.y_root)
		C51_ContextMenu = obj1

	def Button_3(e):
		obj1 = Tk.Menu(W0, font=(FontType, 10), tearoff=0)
		obj1.add_command(label="全クリア", command=_C51.Clear(obj=C51, select_all=True))
		obj1.add_separator()
		obj1.add_command(label="全コピー", command=_C51.Copy(obj=C51, select_all=True))
		obj1.add_command(label="全カット", command=_C51.Cut(obj=C51, select_all=True))
		obj1.add_command(label="ペースト", command=_C51.Paste(obj=C51, select_all=True))
		obj1.post(e.x_root, e.y_root)
		C51_ContextMenu = obj1

	global C51
	C51 = Tk_St.ScrolledText(
		W0,
		font=(FontType, 11),
		relief="flat",
		borderwidth=0,
		undo="true",
		insertofftime=0
	)
	C51.place(x=4, y=95)
	C51.bind("<Button-1>", Button_1)
	C51.bind("<ButtonRelease-1>", ButtonRelease_1)
	C51.bind("<Button-3>", Button_3)
	C51.configure(state="normal")

class _C41:
	C41 = Tk.Label(
		text="YouTube URL（改行区切り）",
		font=(FontType, 9, "bold"),
		fg=FontColor,
		bg=BackColor
	)
	C41.place(x=4, y=73)

class _C47:
	global C47
	C47 = Tk.Button(
		W0,
		text="ファイル",
		font=(FontType, 9),
		fg=FontColor,
		bg="purple",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		activebackground="orange",
		activeforeground="black",
		command=_C51.FileRead(obj=C51)
	)
	C47.place(y=76, width=70, height=18)

class _C48:
	global C48
	C48 = Tk.Button(
		W0,
		text="クリア",
		font=(FontType, 9),
		fg=FontColor,
		bg="navy",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		activebackground="orange",
		activeforeground="black",
		command=_C51.Clear(obj=C51, select_all=True)
	)
	C48.place(y=76, width=70, height=18)

class _C49:
	global C49
	C49 = Tk.Button(
		W0,
		text="ペースト",
		font=(FontType, 9),
		fg=FontColor,
		bg="mediumblue",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		activebackground="orange",
		activeforeground="black",
		command=_C51.Add(obj=C51)
	)
	C49.place(y=76, width=70, height=18)

class _W0_Main:
	def Resize(e):
		if e.widget is W0:
			C21.place(width=e.width-155)
			C22.place(x=e.width-150)
			C23.place(x=e.width-90)
			C32.place(width=e.width-176)
			C33.place(x=e.width-150)
			C47.place(x=e.width-213)
			C48.place(x=e.width-143)
			C49.place(x=e.width-73)
			C51.place(width=e.width-8, height=e.height-100)

	# Window 初期サイズ
	min = {
		"W": 480,
		"H": 240
	}
	# Window 初期ポジション
	pos = {
		"X": int((W0.winfo_screenwidth()-min["W"])/2),
		"Y": int((W0.winfo_screenheight()-min["H"])/2)
	}
	W0.bind("<Configure>", Resize)
	W0.configure(bg=BackColor)
	W0.geometry(f'{min["W"]}x{min["H"]}+{pos["X"]}+{pos["Y"]}')
	W0.minsize(width=min["W"], height=min["H"])
	W0.resizable(width=True, height=True)
	W0.title(f"{PROGRAM} {VERSION}")
	W0.attributes("-topmost", True)

	#---------------
	# 表示位置変更
	#---------------
	# Windows以外で例外発生
	try:
		hwnd = windll.user32.GetForegroundWindow()
		windll.user32.MoveWindow(
			hwnd,
			30,
			60,
			int((W0.winfo_screenwidth()/2)-240),
			int(W0.winfo_screenheight()-120),
			True
		)
	except(NameError, SyntaxError):
		pass

	#---------------------------------
	# 引数のファイル名からリスト読込
	#---------------------------------
	AryC51 = []
	for _s1 in sys.argv:
		AryC51.append(_s1.strip())
	del AryC51[0]
	for _s1 in AryC51:
		try:
			with open(_s1) as iFp:
				C51.insert("insert", iFp.read().rstrip() + "\n")
		except:
			pass
	C51.see("insert")

	#-------------
	# フォーカス
	#-------------
	C21.focus_force()

	#-------
	# Main
	#-------
	W0.mainloop()
	W0.quit()
