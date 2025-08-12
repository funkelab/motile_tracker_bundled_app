from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('motile_launcher')

print("Loaded motile_launcher!", datas, binaries, hiddenimports)
