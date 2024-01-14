# Tarea: Creación de una Lista de Tareas con React

## Paso 1: Configuración del Proyecto
1. Inicia un nuevo proyecto React utilizando Create React App.
2. Crea los archivos de momento vacíos ListaTareas.js e ItemTareas.js para albergar
posteriormente los elementos correspondientes.
## Paso 2: Creación de Datos Estáticos
1. En ListaTareas.js, define un array o lista de objetos que representen tareas (cada objeto debe
tener las propiedades id, title, description, y completed).
2. Pasa este array como prop al componente ListaTareas.
3. Muestra las tareas en ListaTareas utilizando el método map().
## Paso 3: Interactividad con Estado
1. Agrega estado al componente App para manejar la lista de tareas.
2. Implementa funciones en App para agregar y eliminar tareas.
3. Pasa la función de eliminarTarea como propiedad a TaskList y utiliza eventos para
manejar las interacciones correspondientes del usuario.
## Paso 4: Creación del componente AgregarTareas
1. Crea un nuevo archivo ‘.js’ para un nuevo componente llamado AgregarTareas que
tenga un formulario simple para agregar nuevas tareas.
2. Integra AgregarTareas en App y utiliza su estado para manejar la entrada del usuario.
3. Al enviar el formulario, agrega una nueva tarea al estado de App y actualiza la lista de
tareas.
## Paso 5: Estilo y Personalización
1. Aplica estilos CSS para mejorar la apariencia de la aplicación.
2. Añade una funcionalidades adicional para marcar tareas como completadas.