# WinDebloater
This is WinDebloater by crazycheetah42. It is a script written in Python which uses PowerShell's Get-AppxPackage and Remove-AppxPackage cmdlets to remove bloatware from a specific list.
<img src="screenshot.png">
It is available as an executable which was generated through PyInstaller, which you can access through the <a href="https://github.com/crazycheetah42/WinDebloater/releases">Releases</a> page. Make sure you run it as an Administrator, otherwise you will see lots of errors. You can also download it through PowerShell with BITS: Start-BitsTransfer https://github.com/crazycheetah42/WinDebloater/releases/download/v1.1.0/WinDebloater_v1.1.0.zip

It uses the subprocess module, which is built into Python to execute powershell with a list of commands. For example, the first command the script runs is 'Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage'.
The subprocess module will execute "powershell -Command Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage", making it easy to remove bloatware without leaving the main script.