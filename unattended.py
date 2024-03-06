import subprocess
import logging

logging.basicConfig(filename="WinDebloater.log", level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
powershell_commands = []
def apps_uninstall():
    global powershell_commands
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
        'Get-AppxPackage Microsoft.Todos | Remove-AppxPackage',
        'Get-AppxPackage Microsoft.BingNews | Remove-AppxPackage',
    ]

    for command in powershell_commands:
        try:
            subprocess.run(["powershell", "-Command", command], check=True)
            logging.info(f"Successfully executed: {command}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to execute: {command}. Error: {e}")

print("Welcome to WinDebloater (Unattended)!")
print("Please press Enter to start the debloat process:")
input()
print(f"Step 1 of the debloat process is running - Uninstall Bloatware")
apps_uninstall()