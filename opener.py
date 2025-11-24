import webbrowser
import os
import subprocess

url = ["https://www.youtube.com/", "https://chatgpt.com/", "https://replit.com/~", "https://github.com/dashboard"]
path = ["C:\\Users\\PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", "C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"]

# open url's 
for item in url:
    print(item)
    webbrowser.open(item)

# open applications or software
for item in path:
    print(item)
    os.startfile(item)

# open this file in this application
subprocess.Popen([path[0], "D:\\web_source_new"]) # note: path[0] = vscode location

# change url's and paths according to your usecase...