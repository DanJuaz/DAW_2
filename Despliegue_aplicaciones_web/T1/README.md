# DOM
DOM (Document Object Model) es esencialmente una interfaz de plataforma, o API de programacion para documentos HTML, que proporiciona un conjunto estándar de objetos para representar documentos HTML.
´´´

    DOM, que significa Document Object Model (Modelo de Objeto del Documento), es una interfaz de programación de aplicaciones (API) que representa la estructura de un documento HTML o XML como un árbol de objetos. En el contexto de JavaScript, el DOM es utilizado para interactuar dinámicamente con documentos HTML mediante la manipulación de los elementos y atributos del documento.

    El DOM organiza la estructura del documento en un árbol jerárquico de objetos, donde cada nodo del árbol representa un elemento del documento, como un elemento HTML, un atributo, un fragmento de texto, etc. El DOM proporciona una interfaz para que los programadores puedan acceder, modificar y manipular estos nodos, lo que permite la creación de páginas web interactivas y dinámicas.

    representa una interfaz que permite a los programas y scripts acceder y manipular la estructura, estilo y contenido de documentos HTML.
´´´ 
# QUEY SELECTOR
Query selecto muestra la query que le hagas, si hay mas de uno.
querySelector: Devuelve el primer elemento que coincide con el selector CSS especificado.

    <div id="miDiv">Hola</div>
    <script>
        var elemento = document.querySelector('#miDiv');
        console.log(elemento.innerHTML); // Salida: Hola
    </script>

# QUERY SELECTOR ALL
Query selector all te muestra todos los elementos que busques en la query, te lo devuelve como un array si hay mas de uno.
querySelectorAll: Devuelve todos los elementos que coinciden con el selector CSS especificado.

        <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
    <script>
        var elementos = document.querySelectorAll('li');
        elementos.forEach(function(elemento) {
            console.log(elemento.innerHTML);
        });
        // Salida:
        // Elemento 1
        // Elemento 2
        // Elemento 3
    </script>

# GETELECMENTBYID
getElementById: Devuelve el elemento con el ID especificado

    <dIv id="miDiv">Hola</dIv>
    <script>
        var elemento = document.getElementById('miDiv');
        console.log(elemento.innerHTML); // Salida: Hola
    </script>

# GETELEMENTSBYCLASSNAME
getElementsByClassName: Devuelve una colección de elementos con la clase especificada.

    <p class="parrafo">Primer párrafo</p>
    <p class="parrafo">Segundo párrafo</p>
    <script>
        var elementos = document.getElementsByClassName('parrafo');
        for (var i = 0; i < elementos.length; i++) {
            console.log(elementos[i].innerHTML);
        }
        // Salida:
        // Primer párrafo
        // Segundo párrafo
    </script>

# GETELEMENTSBYTAGNAME
getElementsByTagName: Devuelve una colección de elementos con el nombre de la etiqueta especificada.

    <ul>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
    </ul>
    <script>
        var elementos = document.getElementsByTagName('li');
        for (var i = 0; i < elementos.length; i++) {
            console.log(elementos[i].innerHTML);
        }
        // Salida:
        // Elemento 1
        // Elemento 2
        // Elemento 3
    </script>

# INNERTEXT 
Devuelve texto
# CONTENTTEXT
ContentText te devuelve el contenido del texto

# En JS con selectorById y addEventListener para llamar a uan función.

# Eventos de raton y teclado
Eventos de Teclado:
## keydown:

Descripción: Se activa cuando una tecla del teclado se presiona.

    document.addEventListener('keydown', function(event) {
        console.log('Tecla presionada:', event.key);
    });

## keyup:

Descripción: Se activa cuando se suelta una tecla del teclado.

    document.addEventListener('keyup', function(event) {
        console.log('Tecla liberada:', event.key);
    });

## Eventos de Ratón:
## click:

Descripción: Se activa cuando se hace clic con el botón izquierdo del ratón.

    document.addEventListener('click', function(event) {
        console.log('Clic en:', event.clientX, event.clientY);
    });

## mousedown:

Descripción: Se activa cuando se presiona un botón del ratón.

    document.addEventListener('mousedown', function(event) {
        console.log('Botón del ratón presionado:', event.button);
    });

## mouseup:

Descripción: Se activa cuando se suelta un botón del ratón.

    document.addEventListener('mouseup', function(event) {
        console.log('Botón del ratón liberado:', event.button);
    });

## mousemove:

Descripción: Se activa cuando se mueve el ratón.
Ejemplo:

    document.addEventListener('mousemove', function(event) {
        console.log('Movimiento del ratón:', event.clientX, event.clientY);
    });

## mouseenter:

Descripción: Se activa cuando el ratón entra en un elemento.

    document.addEventListener('mouseenter', function(event) {
        console.log('El ratón entró en el elemento');
    });
## mouseleave:

Descripción: Se activa cuando el ratón sale de un elemento.

    document.addEventListener('mouseleave', function(event) {
        console.log('El ratón salió del elemento');
    });

# Interval y set timeout
## setInterval:

Descripción: setInterval es una función que se utiliza para ejecutar repetidamente una función o un fragmento de código con un intervalo de tiempo fijo entre cada ejecución.

    var intervalID = setInterval(funcion, intervalo);
    var contador = 0;
    var intervalID = setInterval(function() {
        console.log(contador);
        contador++;
    }, 1000);  // Se ejecutará cada 1000 milisegundos (1 segundo)

## setTimeout:

Descripción: setTimeout es una función que se utiliza para ejecutar una función o un fragmento de código después de un retraso de tiempo específico.

    var timeoutID = setTimeout(funcion, retraso);
    setTimeout(function() {
        console.log('Se ejecutará después de 2000 milisegundos (2 segundos)');
    }, 2000);

# CANVAS
## Dibujar formas basicas
Descripción: Puedes dibujar formas básicas como rectángulos, círculos, líneas, etc.
Ejemplo:

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');
    contexto.fillStyle = 'red';
    contexto.fillRect(10, 10, 50, 50);  // Dibuja un rectángulo rojo

## Dibujar texto:

Descripción: Puedes añadir texto al canvas.

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');
    contexto.font = '20px Arial';
    contexto.fillStyle = 'blue';
    contexto.fillText('Hola, Mundo!', 50, 50);

## Dibujar imágenes:

Descripción: Puedes cargar y mostrar imágenes en el canvas.

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');
    var imagen = new Image();
    imagen.src = 'imagen.png';
    imagen.onload = function() {
        contexto.drawImage(imagen, 10, 10);
    };

## Animaciones:

Descripción: Puedes crear animaciones dibujando sucesivas imágenes en intervalos de tiempo.

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');
    var x = 0;

    function animar() {
        contexto.clearRect(0, 0, canvas.width, canvas.height);
        contexto.fillRect(x, 10, 50, 50);
        x += 5;
        requestAnimationFrame(animar);
    }

    animar();

## Capturar eventos del ratón y teclado:

Descripción: Puedes responder a eventos del ratón o teclado en el canvas.

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');

    canvas.addEventListener('mousemove', function(evento) {
        // Lógica para responder al movimiento del ratón
    });

## Aplicar transformaciones:

Descripción: Puedes aplicar transformaciones como rotaciones y escalas.

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');

    contexto.rotate(Math.PI / 4); // Rota el contexto 45 grados
    contexto.fillRect(50, 50, 50, 50);

## Gradientes y patrones:

Descripción: Puedes llenar formas con gradientes o patrones.

    var canvas = document.getElementById('miCanvas');
    var contexto = canvas.getContext('2d');

    // Gradiente lineal
    var gradiente = contexto.createLinearGradient(0, 0, 200, 0);
    gradiente.addColorStop(0, 'red');
    gradiente.addColorStop(1, 'blue');
    contexto.fillStyle = gradiente;
    contexto.fillRect(10, 10, 200, 100);


