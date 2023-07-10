import subprocess

print("Welcome to WinDebloater! Press Enter to start the debloat...")
input()

powershell_commands = [
    'Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.BingWeather | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.GetHelp | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.WindowsMaps | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.YourPhone | Remove-AppxPackage',
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
    'Get-AppxPackage Microsoft.MSPaint | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.WindowsSoundRecorder | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.People | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.WindowsCalculator | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.Windows.PeopleExperienceHost | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.Todos | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.PowerAutomateDesktop | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.BingNews | Remove-AppxPackage',
    'Get-AppxPackage Clipchamp.Clipchamp | Remove-AppxPackage',
    'Get-AppxPackage MicrosoftTeams | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.ZuneVideo | Remove-AppxPackage',
    'Get-AppxPackage Microsoft.ZuneMusic | Remove-AppxPackage'
]

for command in powershell_commands:
    subprocess.run(["powershell", "-Command", command], shell=True)