Lamentablemente, no puedo ejecutar comandos directamente ni interactuar con sistemas externos, pero puedo proporcionarte ejemplos de cómo realizar estos ejercicios utilizando PowerShell y los cmdlets de Active Directory. Ten en cuenta que estos ejemplos son hipotéticos y deberían adaptarse a tu entorno específico.

### Ejercicio 1: Crear UOs con protección accidental contra borrado

```powershell
New-ADOrganizationalUnit -Name "OU1" -ProtectedFromAccidentalDeletion $true
New-ADOrganizationalUnit -Name "OU2" -ProtectedFromAccidentalDeletion $true
```

### Ejercicio 2: Obtener información de UOs con el parámetro -Filter

```powershell
Get-ADOrganizationalUnit -Filter 'Name -like "OU*"' | Format-Table Name, DistinguishedName
```

### Ejercicio 3: Cambiar la descripción y el país de algunas UOs

```powershell
Set-ADOrganizationalUnit -Identity "OU1" -Description "Nueva descripción" -Country "NuevoPaís"
Set-ADOrganizationalUnit -Identity "OU2" -Description "Otra descripción" -Country "OtroPaís"
```

### Ejercicio 4: Borrar UOs

```powershell
Remove-ADOrganizationalUnit -Identity "OU1" -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU2" -Confirm:$false
```

### Ejercicio 5: Crear varias UOs usando archivo CSV/XLSX con PowerShell

Crear un archivo CSV (por ejemplo, "UOs.csv") con la siguiente estructura:

```csv
Name,Description,Country
OU3,Descripción3,País3
OU4,Descripción4,País4
```

Luego ejecuta el siguiente comando:

```powershell
Import-Csv -Path "C:\Ruta\UOs.csv" | ForEach-Object {
    New-ADOrganizationalUnit -Name $_.Name -Description $_.Description -Country $_.Country
}
```

### Ejercicio 6: Mover todos los usuarios de una UO a otra UO

```powershell
Get-ADUser -Filter * -SearchBase "OU=Origen,DC=dominio,DC=com" | Move-ADObject -TargetPath "OU=Destino,DC=dominio,DC=com"
```

### Ejercicio 7: Mover usuarios desde un archivo CSV/Excel a otra UO existente

Supongamos que tienes un archivo CSV ("UsuariosAMover.csv") con las columnas "Name" y "SamAccountName". Luego puedes ejecutar:

```powershell
Import-Csv -Path "C:\Ruta\UsuariosAMover.csv" | ForEach-Object {
    Get-ADUser -Filter {Name -eq $_.Name -or SamAccountName -eq $_.SamAccountName} | Move-ADObject -TargetPath "OU=Destino,DC=dominio,DC=com"
}
```

### Ejercicio 8: Comprobar si existe una UO

```powershell
$rutaOU = "OU=NombreOU,DC=dominio,DC=com"
[adsi]::Exists("LDAP://$rutaOU")
```

### Ejercicio 9: Función que cree una UO comprobando su existencia

```powershell
function Crear-UO {
    param (
        [string]$Nombre,
        [string]$Descripcion,
        [string]$Pais
    )

    $rutaOU = "OU=$Nombre,DC=dominio,DC=com"

    if (-not [adsi]::Exists("LDAP://$rutaOU")) {
        New-ADOrganizationalUnit -Name $Nombre -Description $Descripcion -Country $Pais
        Write-Host "UO creada exitosamente."
    } else {
        Write-Host "La UO ya existe."
    }
}

# Ejemplos de llamada a la función
Crear-UO -Nombre "NuevaOU" -Descripcion "DescripciónNueva" -Pais "NuevoPais"
Crear-UO -Nombre "OUExistente" -Descripcion "DescripciónExistente" -Pais "ExistentePais"
```

Estos son ejemplos básicos y deberías adaptarlos según tus necesidades y estructura de Active Directory. ¡Asegúrate de entender y probar los comandos en un entorno de prueba antes de aplicarlos en producción!