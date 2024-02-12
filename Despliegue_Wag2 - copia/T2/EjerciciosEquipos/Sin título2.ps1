# Ejercicio 1: Crear cuenta de equipo PC01 con sistema operativo Windows 10
Add-Computer -DomainName "nz-julio.eus" -NewName "PC01" -Restart

# Ejercicio 2: Crear cuentas de equipo con sistemas operativos específicos
New-ADComputer -Name PCD01 -Path "OU=NZ,OU=Donostia,OU=Equipos D,DC=nz-julio,DC=eus" -OperatingSystem "Windows 10 Pro"
New-ADComputer -Name PCD02 -Path "OU=NZ,OU=Donostia,OU=Equipos D,DC=nz-julio,DC=eus" -OperatingSystem "Windows 11 Home"
New-ADComputer -Name PCG01 -Path "OU=NZ,OU=Gasteiz,OU=Equipos G,DC=nz-julio,DC=eus" -OperatingSystem "Windows 11 Education"
New-ADComputer -Name PCG02 -Path "OU=NZ,OU=Gasteiz,OU=Equipos G,DC=nz-julio,DC=eus" -OperatingSystem "Windows Server 2019"
New-ADComputer -Name PCF01 -Path "OU=NZ,OU=EEUU,OU=Florida,OU=Equipos F,DC=nz-julio,DC=eus" -OperatingSystem "Windows 11 Pro"
New-ADComputer -Name PCF02 -Path "OU=NZ,OU=EEUU,OU=Florida,OU=Equipos F,DC=nz-julio,DC=eus" -OperatingSystem "Windows Server 2022"

# Ejercicio 3: Obtener información del equipo PCF01.
Get-ADComputer PCF01

# Ejercicio 4: Visualizar propiedades de todos los equipos del dominio.
Get-ADComputer -Filter * -Properties Name, OperatingSystem, OperatingSystemServicePack | Format-Table Name, OperatingSystem, OperatingSystemServicePack -AutoSize

# Ejercicio 5: Exportar información de equipos con sistema operativo Windows Server a un archivo CSV.
Get-ADComputer -Filter {OperatingSystem -like 'Windows Server*'} -Properties Name, OperatingSystem, OperatingSystemVersion, ipv4Address | Select-Object Name, OperatingSystem, OperatingSystemVersion, ipv4Address | Export-Csv -Path ListadoServer.csv -NoTypeInformation

# Ejercicio 6: Mover equipos al contenedor específico.
Move-ADObject -Identity "OU=NZ,DC=nz-julio,DC=eus" -TargetPath "OU=Computers,DC=nz-julio,DC=eus"

# Ejercicio 7: Volver a colocar la ubicación por defecto al contenedor Computers.
Move-ADObject -Identity "OU=Computers,DC=nz-julio,DC=eus" -TargetPath "OU=NZ,DC=nz-julio,DC=eus"

# Ejercicio 8: Importar equipos desde un archivo CSV.
Import-Csv -Path .\Desktop\EQUIPOS.CSV | ForEach-Object {
    Add-Computer -DomainName "nz-julio.eus" -NewName $_.Name -Restart
}

# Ejercicio 9: Borrar equipos desde un archivo CSV.
Import-Csv -Path .\Desktop\EQUIPOS.CSV | ForEach-Object {
    Remove-Computer -Name $_.Name -Force -Confirm:$false
}

# Ejercicio 10: Visualizar la fecha del último inicio de sesión de todos los equipos de nuestro dominio.
Get-ADComputer -Filter * -Properties LastLogonDate | Format-Table Name, LastLogonDate -AutoSize
