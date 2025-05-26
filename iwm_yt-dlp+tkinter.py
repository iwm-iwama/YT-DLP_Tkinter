#!/usr/bin/env python3
#coding:utf-8

PROGRAM = "YT-DLP+Tkinter"
VERSION = "Ver.iwm20250526"

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
BackColor = "#383838"

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
	global C11
	C11 = Tk.Label(
		text="YT-DLP コマンド",
		font=(FontType, 9, "bold"),
		fg=FontColor,
		bg=BackColor
	)
	C11.place(x=5, y=4)

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
			global C21_ContextMenu
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
		global C21_ContextMenu
		C21_ContextMenu = obj1

	def Button_3(e):
		obj1 = Tk.Menu(W0, tearoff=0, font=(FontType, 10))
		obj1.add_command(label="全クリア", command=_C21.Clear(obj=C21, select_all=True))
		obj1.add_separator()
		obj1.add_command(label="全コピー", command=_C21.Copy(obj=C21, select_all=True))
		obj1.add_command(label="全カット", command=_C21.Cut(obj=C21, select_all=True))
		obj1.add_command(label="ペースト", command=_C21.Paste(obj=C21, select_all=True))
		obj1.post(e.x_root, e.y_root)
		global C21_ContextMenu
		C21_ContextMenu = obj1

	a1 = LIST_COMMAND.strip().split("\n")

	global C21
	C21 = Tk_Ttk.Combobox(
		W0,
		font=(FontType, 11),
		values=a1
	)
	C21.place(x=5, y=23, height=22)
	C21.bind("<Button-1>", Button_1)
	C21.bind("<ButtonRelease-1>", ButtonRelease_1)
	C21.bind("<Button-3>", Button_3)
	C21.insert("end", a1[0])

class _C22:
	def Click(e = None):
		_Terminal.Clear()
		TmBgn = time.time()
		sData = C41.get("1.0", "end-1c").strip()
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
		ListPS = []
		# 並列処理数(Min=2)は動的に変更
		GblPS = 2
		CntParallel = 0
		Cnt = 0
		for _s1 in aCmd:
			Cnt += 1
			print(f"\033[97;44m({Cnt}) {_s1}\033[0m")
			try:
				_ps = subprocess.Popen(_s1.split(), shell=False)
				# 並列処理のとき
				if C23_Var.get():
					# PSリスト作成
					ListPS.append(_ps)
					CntParallel += 1
					if CntParallel >= GblPS:
						CntParallel = 0
						# 計測開始
						SwBgn = time.perf_counter()
						for _ps in ListPS:
							_ps.wait()
						ListPS = []
						# 計測終了
						SwEnd = time.perf_counter()
						# 計測時間が 1秒未満 なら並列処理数 +2
						if (SwEnd - SwBgn) < 1.0:
							GblPS += 2
						# 計測時間が 1秒以上 なら並列処理数 -1 ただし 最低値は 2
						else:
							if GblPS > 2:
								GblPS -= 1
						print(f"\033[94m[Concurrent Processes = {GblPS}]\033[0m")
				# 単一処理のとき
				else:
					_ps.wait()
			except:
				print(
					"\033[91m" +
					"[Err] コマンドを間違っていませんか？"
				)
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
		command=Click
	)
	C22.place(y=24, width=60, height=20)

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
		selectcolor="#111",
		variable=C23_Var
	)
	C23.place(y=24, width=80, height=20)

# C41 < C37, C38, C39
class _C41:
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
			global C41_ContextMenu
			C41_ContextMenu.destroy()
		except:
			pass

	def ButtonRelease_1(e):
		obj1 = Tk.Menu(W0, font=(FontType, 10), tearoff=0)
		if C41.tag_ranges("sel"):
			obj1.add_command(label="クリア", command=_C41.Clear(obj=C41, select_all=False))
			obj1.add_separator()
			obj1.add_command(label="コピー", command=_C41.Copy(obj=C41, select_all=False))
			obj1.add_command(label="カット", command=_C41.Cut(obj=C41, select_all=False))
			obj1.add_command(label="ペースト", command=_C41.Paste(obj=C41, select_all=False))
		obj1.post(e.x_root, e.y_root)
		global C41_ContextMenu
		C41_ContextMenu = obj1

	def Button_3(e):
		obj1 = Tk.Menu(W0, font=(FontType, 10), tearoff=0)
		obj1.add_command(label="全クリア", command=_C41.Clear(obj=C41, select_all=True))
		obj1.add_separator()
		obj1.add_command(label="全コピー", command=_C41.Copy(obj=C41, select_all=True))
		obj1.add_command(label="全カット", command=_C41.Cut(obj=C41, select_all=True))
		obj1.add_command(label="ペースト", command=_C41.Paste(obj=C41, select_all=True))
		obj1.post(e.x_root, e.y_root)
		global C41_ContextMenu
		C41_ContextMenu = obj1

	global C41
	C41 = Tk_St.ScrolledText(
		W0,
		font=(FontType, 11),
		relief="flat",
		borderwidth=0,
		undo="true",
		insertofftime=0
	)
	C41.place(x=5, y=73)
	C41.bind("<Button-1>", Button_1)
	C41.bind("<ButtonRelease-1>", ButtonRelease_1)
	C41.bind("<Button-3>", Button_3)
	C41.configure(state="normal")

class _C31:
	global C31
	C31 = Tk.Label(
		text="YouTube URL（改行区切り）",
		font=(FontType, 9, "bold"),
		fg=FontColor,
		bg=BackColor
	)
	C31.place(x=5, y=52)

class _C37:
	global C37
	C37 = Tk.Button(
		W0,
		text="ファイル",
		font=(FontType, 9),
		fg=FontColor,
		bg="purple",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		command=_C41.FileRead(obj=C41)
	)
	C37.place(y=53, width=70, height=20)

class _C38:
	global C38
	C38 = Tk.Button(
		W0,
		text="クリア",
		font=(FontType, 9),
		fg=FontColor,
		bg="navy",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		command=_C41.Clear(obj=C41, select_all=True)
	)
	C38.place(y=53, width=70, height=20)

class _C39:
	global C39
	C39 = Tk.Button(
		W0,
		text="ペースト",
		font=(FontType, 9),
		fg=FontColor,
		bg="mediumblue",
		highlightthickness=0,
		relief="flat",
		cursor="hand2",
		command=_C41.Add(obj=C41)
	)
	C39.place(y=53, width=70, height=20)

class _W0_Main:
	def Resize(e):
		if e.widget is W0:
			C21.place(width=e.width-155)
			C22.place(x=e.width-150)
			C23.place(x=e.width-90)
			C37.place(x=e.width-215)
			C38.place(x=e.width-145)
			C39.place(x=e.width-75)
			C41.place(width=e.width-10, height=e.height-79)

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
	AryC41 = []
	for _s1 in sys.argv:
		AryC41.append(_s1.strip())
	del AryC41[0]
	for _s1 in AryC41:
		try:
			with open(_s1) as iFp:
				C41.insert("insert", iFp.read().rstrip() + "\n")
		except:
			pass
	C41.see("insert")

	#-------------
	# フォーカス
	#-------------
	C21.focus_force()

	#-------
	# Main
	#-------
	W0.mainloop()
	W0.quit()

