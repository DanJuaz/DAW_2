# Ejercicio 1: Crear UOs con protección accidental contra borrado
New-ADOrganizationalUnit -Name Nazaret -ProtectedFromAccidentalDeletion:$false
# Ejercicio 2: Obtener información de UOs con el parámetro -Filter
Get-ADOrganizationalUnit -Filter *|FT
# Ejercicio 3: Cambiar la descripción y el país de algunas UOs
Set-ADOrganizationalUnit -Identity "Nazaret" -Description "Nueva descripción" -Country "NuevoPaís"
# Ejercicio 4: Borrar UOs
Remove-ADOrganizationalUnit -Identity "Nazaret" -Confirm:$false
# Ejercicio 5: Crear varias UOs usando archivo CSV/XLSX con PowerShell
Import-Csv -Path "Z:\csvrj.csv" | ForEach-Object {
    New-ADOrganizationalUnit -Name $_.Name -Description $_.Description -Country $_.Country
}
# Ejercicio 6: Mover todos los usuarios de una UO a otra UO
Get-ADUser -Filter * -SearchBase "OU=Nazaret,DC=nz-julio,DC=eus" | Move-ADObject -TargetPath "OU=NZ,DC=nz-julio,DC=eus"
# Ejercicio 7: Mover usuarios desde un archivo CSV/Excel a otra UO existente
Import-Csv -Path "Z:\csvrj.csv" | ForEach-Object {
    Get-ADUser -Filter {Name -eq $_.Name -or SamAccountName -eq $_.SamAccountName} | Move-ADObject -TargetPath "OU=Destino,DC=dominio,DC=com"
}
# Ejercicio 8: Comprobar si existe una UO
$rutaOU = "OU=NombreOU,DC=dominio,DC=com"
[adsi]::Exists("LDAP://$rutaOU")
# Ejercicio 9: Función que cree una UO comprobando su existencia
function Crear-UO {
    param (
        [string]$Nombre,
        [string]$Descripcion,
        [string]$Pais
    )

    $rutaOU = "OU=$Nombre,DC=dominio,DC=com"

    if (-not [adsi]::Exists("LDAP://$rutaOU")) {
        New-ADOrganizationalUnit -Name $Nombre -Description $Descripcion -Country $Pais
        Write-Host "UO creada exitosamente." -ForegroundColor DarkGreen
    } else {
        Write-Host "La UO ya existe." -ForegroundColor DarkRed
    }
}

# Ejemplos de llamada a la función
Crear-UO -Nombre "NuevaOU" -Descripcion "DescripciónNueva" -Pais "NuevoPais"
Crear-UO -Nombre "OUExistente" -Descripcion "DescripciónExistente" -Pais "ExistentePais"