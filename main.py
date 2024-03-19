import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import tix
import sv_ttk, darkdetect
import os

root = tix.Tk()
root.geometry("800x600")
root.title("WinDebloater")
root.wm_title("WinDebloater")

header_lbl = ttk.Label(root, text="WinDebloater", font=("Segoe UI", 22))
header_lbl.pack()

info_lbl = ttk.Label(root, text="Welcome to WinDebloater! Please hover over each option to see what it does.", font=("Segoe UI", 14))
info_lbl.pack()

def start_debloat(commands):
    for command in commands:
        subprocess.run(["powershell", "-Command", command], shell=True)

def basic_debloat():
    powershell_commands = [
        'Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsMaps | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.XboxApp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MixedReality.Portal | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.SkypeApp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftSolitaireCollection | Remove-AppxPackage',
        'Get-AppxPackage SpotifyAB.SpotifyMusic | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftOfficeHub | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.People | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Windows.PeopleExperienceHost | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.BingNews | Remove-AppxPackage'
    ]
    start_debloat(powershell_commands)
def standard_debloat():
    powershell_commands = [
        'Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.BingWeather | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.GetHelp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsMaps | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.XboxApp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MixedReality.Portal | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.SkypeApp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsFeedbackHub | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftSolitaireCollection | Remove-AppxPackage',
        'Get-AppxPackage SpotifyAB.SpotifyMusic | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Getstarted | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.People | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Windows.PeopleExperienceHost | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Todos | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftStickyNotes | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.BingNews | Remove-AppxPackage',
    ]
    start_debloat(powershell_commands)
    from tkinter import messagebox
    messagebox.showinfo("Debloat complete!", "Your Windows machine has been debloated! Check your Start Menu, it should be much cleaner now.")
def advanced_debloat():
    powershell_commands = [
        'Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.BingWeather | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.GetHelp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsMaps | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.XboxApp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MixedReality.Portal | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.SkypeApp | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsFeedbackHub | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftSolitaireCollection | Remove-AppxPackage',
        'Get-AppxPackage SpotifyAB.SpotifyMusic | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Getstarted | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftStickyNotes | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Office.OneNote | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.MicrosoftOfficeHub | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsSoundRecorder | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.People | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsCalculator | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Windows.PeopleExperienceHost | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.Todos | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.BingNews | Remove-AppxPackage',
        'Get-AppxPackage Clipchamp.Clipchamp | Remove-AppxPackage',
        'Get-AppxPackage MicrosoftTeams | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.WindowsNotepad | Remove-AppxPackage'
    ]
    start_debloat(powershell_commands)

def winutil_run():
    subprocess.run(["powershell", "-Command", "irm christitus.com/win | iex"], shell=True)

def set_pwrplan():
    def ultperfmode():
        os.system('cmd /c "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"')
        os.system('cmd /c "powercfg -s e9a42b02-d5df-448d-aa00-03f14749eb61"')
    def highperfmode():
        os.system('cmd /c "powercfg -s 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"')
    def balancedmode():
        os.system('cmd /c "powercfg -s 381b4222-f694-41f0-9685-ff5bb260df2e"')
    def pwrsvrmode():
        os.system('cmd /c "powercfg -s a1841308-3541-4fab-bc81-f71556f20b4a"')
    pwrplanwindow = tk.Tk()
    pwrplanwindow.geometry("400x300")
    pwrplanwindow.title("Choose a Power Plan")
    hdr_lbl = ttk.Label(pwrplanwindow, text="Choose a Power Plan", font=("Segoe UI", 20))
    hdr_lbl.pack()
    ultperf = ttk.Button(pwrplanwindow, text="Ultimate Performance", command=ultperfmode)
    highperf = ttk.Button(pwrplanwindow, text="High Performance", command=highperfmode)
    balanced = ttk.Button(pwrplanwindow, text="Balanced", command=balancedmode)
    pwrsvr = ttk.Button(pwrplanwindow, text="Power Saver", command=pwrsvrmode)
    ultperf.pack()
    highperf.pack()
    balanced.pack()
    pwrsvr.pack()

    pwrplanwindow.mainloop()

basic_debloat_btn = ttk.Button(root, text="Basic Debloat", command=basic_debloat)
basic_tooltip = tix.Balloon(root)
basic_tooltip.subwidget('label')['bg'] = 'black'
basic_tooltip.subwidget('message')['bg'] = 'black'
basic_tooltip.bind_widget(basic_debloat_btn, balloonmsg="This removes the basic annoyances and bloat.")
basic_debloat_btn.pack()

standard_debloat_btn = ttk.Button(root, text="Standard Debloat (Recommended)", command=standard_debloat)
standard_debloat_tooltip = tix.Balloon(root)
standard_debloat_tooltip.subwidget('label')['bg'] = 'black'
standard_debloat_tooltip.subwidget('message')['bg'] = 'black'
standard_debloat_tooltip.bind_widget(standard_debloat_btn, balloonmsg="This removes most of the bloatware pre-installed. Recommended option for most people with decent PCs.")
standard_debloat_btn.pack()

advanced_debloat_btn = ttk.Button(root, text="Advanced Debloat", command=advanced_debloat)
advanced_debloat_tooltip = tix.Balloon(root)
advanced_debloat_tooltip.subwidget('label')['bg'] = 'black'
advanced_debloat_tooltip.subwidget('message')['bg'] = 'black'
advanced_debloat_tooltip.bind_widget(advanced_debloat_btn, balloonmsg="This removes as much bloatware as possible. This is not recommended unless you know what you're doing or you have a really slow PC.")
advanced_debloat_btn.pack()

winutil_btn = ttk.Button(root, text="Run ChrisTitusTech's winutil", command=winutil_run)
winutil_tooltip = tix.Balloon(root)
winutil_tooltip.subwidget('label')['bg'] = 'black'
winutil_tooltip.subwidget('message')['bg'] = 'black'
winutil_tooltip.bind_widget(winutil_btn, balloonmsg="This runs ChrisTitusTech's Windows Utility which is an all-in-one tool to install, tweak, configure, and change your update cycle. This is recommended after using one of the debloat modes.")
winutil_btn.pack()

pwrplan_btn = ttk.Button(root, text="Set Power Plan", command=set_pwrplan)
pwrplan_tooltip = tix.Balloon(root)
pwrplan_tooltip.subwidget('label')['bg'] = 'black'
pwrplan_tooltip.subwidget('message')['bg'] = 'black'
pwrplan_tooltip.bind_widget(pwrplan_btn, balloonmsg="Set a power plan to adjust for high/ultimate performance or balanced/power saver.")
pwrplan_btn.pack()

if darkdetect.isDark():
    sv_ttk.set_theme("dark")
elif darkdetect.isLight():
    sv_ttk.set_theme("light")

root.mainloop()