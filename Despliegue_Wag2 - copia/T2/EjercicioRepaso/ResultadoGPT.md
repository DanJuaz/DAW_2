**
### Ejercicio 1

```powershell
New-ADOrganizationalUnit -Name "Administración" -Path "OU=Miempresa,DC=tuDominio,DC=com"
New-ADOrganizationalUnit -Name "RRHH" -Path "OU=Miempresa,DC=tuDominio,DC=com"
New-ADOrganizationalUnit -Name "Formación" -Path "OU=RRHH,OU=Miempresa,DC=tuDominio,DC=com"
New-ADOrganizationalUnit -Name "Contratación" -Path "OU=RRHH,OU=Miempresa,DC=tuDominio,DC=com"
New-ADOrganizationalUnit -Name "Selección" -Path "OU=RRHH,OU=Miempresa,DC=tuDominio,DC=com"
New-ADOrganizationalUnit -Name "Producción" -Path "OU=Miempresa,DC=tuDominio,DC=com"
New-ADOrganizationalUnit -Name "Ventas" -Path "OU=Miempresa,DC=tuDominio,DC=com"

```
**Pd: Actualizar Dominio**

### Ejercicio 2

```powershell
# Añadir usuarios a las unidades organizativas
Add-ADGroupMember -Identity "Administradores" -Members "Usuario1", "Usuario2"
Add-ADGroupMember -Identity "Formación" -Members "Usuario3", "Usuario4"
# Continuar con el mismo proceso para las demás unidades organizativas
```

### Ejercicio 3

```powershell
# Exportar usuarios de la unidad organizativa Miempresa a un archivo usuarios.csv
Get-ADUser -Filter * -SearchBase "OU=Miempresa Producción,DC=tuDominio,DC=com" | Export-Csv -Path "C:\Ruta\usuarios.csv" -NoTypeInformation
```

### Ejercicio 4

```powershell
# Obtener todas las propiedades de un usuario del dominio
Get-ADUser -Identity "NombreUsuario" -Properties * | Select-Object Name, EmailAddress, LastLogonDate
```

### Ejercicio 5

```powershell
# Obtener usuarios de una unidad organizativa seleccionando propiedades específicas
Get-ADUser -Filter * -SearchBase "OU=Miempresa Producción,DC=tuDominio,DC=com" | Select-Object Name, EmailAddress, LastLogonDate
```

### Ejercicio 6

```powershell
# Eliminar una unidad organizativa
Remove-ADOrganizationalUnit -Identity "NombreUO" -Recursive
```
```powershell
# Desactivar la protección contra eliminación accidental (si está activada)
Set-ADOrganizationalUnit -Identity "NombreUO" -ProtectedFromAccidentalDeletion $false

# Borrar la unidad organizativa
Remove-ADOrganizationalUnit -Identity "NombreUO" -Recursive

```

### Ejercicio 7

```powershell
# Crear recursos compartidos para cada departamento y uno general
New-Item -Path "C:\Ruta\RecursoDepartamento" -ItemType Directory
New-Item -Path "C:\Ruta\RecursoGeneral" -ItemType Directory

# Asignar permisos de acceso
# Por ejemplo, para dar acceso a los usuarios de Ventas al recurso de Ventas
$ventasGroup = Get-ADGroup "Ventas"
$ventasAcl = Get-Acl "C:\Ruta\RecursoVentas"
$ventasPermission = New-Object System.Security.AccessControl.FileSystemAccessRule("Ventas", "Read", "Allow")
$ventasAcl.SetAccessRule($ventasPermission)
Set-Acl "C:\Ruta\RecursoVentas" $ventasAcl
```
