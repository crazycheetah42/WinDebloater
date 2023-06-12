@ECHO off

echo 1. Uninstall bloatware
powershell Remove-AppxPackage Microsoft.Microsoft3DBuilder
powershell Remove-AppxPackage Microsoft.BingWeather
powershell Remove-AppxPackage Microsoft.GetHelp
powershell Remove-AppxPackage Microsoft.WindowsMaps
powershell Remove-AppxPackage Microsoft.YourPhone
powershell Remove-AppxPackage Microsoft.XboxGamingOverlay