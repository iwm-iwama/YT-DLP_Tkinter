【バグ情報】

	Ver.iwm20250414
	Ver.iwm20250418
		一部の操作時に期待しない処理をする。

【実行に必要なライブラリ】

	Tkinter

【動作確認済】

	Windows10: MSYS2/MinGW-w64
	Linux

【このスクリプトについて】

	YT-DLP(YouTube Downloader)の操作を補助するGUIプログラムです。
	(YT-DLP は本家HPから入手してください。https://github.com/yt-dlp/yt-dlp#release-files)

	端末（DOSプロンプト／Terminal）から起動しますが、基本操作はマウスで行います。
	実行オプションについては、目的に応じてスクリプト内の変数「List_Cmd =」を変更してください。

 	Ver.20240513では、並列処理が実装されました。
 	Ver.20240606では、並列処理（非同期処理）と同期処理を選択できるようになりました。
