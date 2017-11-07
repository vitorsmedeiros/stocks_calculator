import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ['os','sys','xlsxwriter','xlwt',"pandas","Tkinter","tkMessageBox","tkFileDialog","requests","numpy","datetime","sys",'matplotlib','io','time','xlrd'],
					 "excludes": ["sqlite3","IPython"],
					 "optimize": 2}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Stock Calculator",
        version = "0.3",
        description = "Calculate Stock based a tax",
        options = {"build_exe": build_exe_options},
        executables = [Executable("setup.py", base=base)])

# 
