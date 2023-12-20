<?php
// Datos de conexión a la base de datos
$host = "fdb1030.awardspace.net";
$puerto = 3306;
$nombreBD = "4242024_dbprueba";
$usuario = "4242024_dbprueba";
$contraseña = "bu)d-YZs6(9j[@ag"; // Reemplaza "TuContraseña" con la contraseña real

// Crear una conexión a la base de datos
$conexion = new mysqli($host, $usuario, $contraseña, $nombreBD, $puerto);

// Verificar si la conexión fue exitosa
if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Consulta para seleccionar todos los registros de la tabla "usuarios"
$sql = "SELECT * FROM usuarios";
$resultado = $conexion->query($sql);

// Verificar si se encontraron registros
if ($resultado->num_rows > 0) {
    echo "<table>";
    echo "<tr><th>Nombre</th><th>Edad</th><th>Profesión</th></tr>";
    while ($fila = $resultado->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $fila["nombre"] . "</td>";
        echo "<td>" . $fila["edad"] . "</td>";
        echo "<td>" . $fila["profesion"] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
} else {
    echo "No se encontraron registros.";
}

// Cerrar la conexión cuando hayas terminado
$conexion->close();
?>
