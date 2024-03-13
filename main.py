import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import tix
import sv_ttk, darkdetect
import ctypes

root = tix.Tk()
root.geometry("800x600")
root.title("WinDebloater")
root.wm_title("WinDebloater")
root.attributes('-topmost',True)

header_lbl = ttk.Label(root, text="WinDebloater", font=("Segoe UI", 22))
header_lbl.pack()

info_lbl = ttk.Label(root, text="Welcome to WinDebloater! Please hover over each option to see what it does.", font=("Segoe UI", 14))
info_lbl.pack()

def is_running_as_admin() -> bool:
    # If the below function returns 0, it means that the script isn't running as admin.
    # It'll return 1 otherwise.
    # NOTE: This is calling a win32 API, meaning this won't work on UNIX-based systems (MacOS & Linux), as well as FreeBSD.
    # Credit to og-mrk for this amazing function
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
if not is_running_as_admin:
    from tkinter import messagebox
    messagebox.showerror("Need Admin permissions", "Please close and relaunch this program as Administrator.")
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
        'Get-AppxPackage Microsoft.BingNews | Remove-AppxPackage',
    ]
    start_debloat(powershell_commands)
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

winutil_btn = ttk.Button(root, text="Run ChrisTitusTech's winutil", command=advanced_debloat)
winutil_tooltip = tix.Balloon(root)
winutil_tooltip.subwidget('label')['bg'] = 'black'
winutil_tooltip.subwidget('message')['bg'] = 'black'
winutil_tooltip.bind_widget(winutil_btn, balloonmsg="This runs ChrisTitusTech's Windows Utility which is an all-in-one tool to install, tweak, configure, and change your update cycle. This is recommended after using one of the debloat modes.")
winutil_btn.pack()

if darkdetect.isDark():
    sv_ttk.set_theme("dark")
elif darkdetect.isLight():
    sv_ttk.set_theme("light")

root.mainloop()