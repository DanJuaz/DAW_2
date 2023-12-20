
/* Show window */
function mostrarVentana() {
     var ventanaEmergente = window.open("HOLA MUNDO PRUEBA", "VentanaEmergente", "width=400,height=200");
     ventanaEmergente.document.write("<title>Document</title> <h1> kdnadncjksnk</h1>");
}

 /* Math
 Calcula el coseno de 60 grados.
 Calcula la raiz cuadrada de num1.
 Calcula la división entre num1 y num2 y muestralo con dos decimales.
 ¿Cuál es la diferencia entre Math.round, Math.floor, Math.ceil y Math.toFixed?
 */

function coseno(grados){
   return Math.cos((grados * Math.PI)/180)
}

function raizcuadrada(num1){
   return Math.sqrt(num1);
}

function división(num1, num2){
   return  (num1/num2).toFixed;
}

var numero = 3.75;

console.log(Math.round(numero)); // 4 redondeo hacia arriba
console.log(Math.floor(numero)); // 3 redondeo hacia abajo
console.log(Math.ceil(numero));  // 4 redondeo hacia arriba incluso si es menor que 0.5
console.log(numero.toFixed(1));   // "3.8" numero fijo de decimales


 /*
 String
 Convierte una cadena a mayúsculas.
 Elimina los espacios en blanco de una cadena. Nota: es habitual hacer este proceso en formularios que recogen nombres, nombres de usuario, etc.
 ¿Cómo obtendríamos el quinto carácter de una cadena de texto?
 Pon en mayúscula la primera letra de una cadena de textos.
 Obtén la primera palabra de una cadena de textos.
 Cuenta las vocales que tiene una cadena de textos.
 */
 function mayuscula(text) {
     return text.toUpperCase();
 }

 function deleteSpaceBlank(text){
    return text.replace(/\s/g, '')
 }
 function quintoCaracter(text){
    return text[4];
 }
 function primeraMayus(text){
    return text.charAt(0).toUpperCase() + text.slice(1);
 }

 function primeraPalabra(text){
    var palabra = text.splt('0');
    var primeraPalabra = palabra[0];
    return primeraPalabra;
 }

 function contarVocales(text){
   var vocales = 'aeiouAEIOU';
   var c = 0;

   for(var i = 0; i<text.lenght; i++){
      if(vocales.indexOf(text[i] != -1)){
         c++;
      }
   }
    return c;
}
    
 /*
 Funciones
 Crea una función que devuelva el precio con IVA. Se le pasa un parámetro que indica el precio sin IVA.
 Crea una función que dado un número diga si es par o no.
 Crea una función que calcule y devuelva el área de un círculo dado su radio. Utiliza la fórmula: Área = π * radio^2
 Crea una función que pida dos números como parámetro: valor inferior y valor superior. La función devuelve un número aleatorio entre los dos números.
 Crea una función que dado un número nos diga si es primo o  no.
 Crea una función que dado un número nos devuelva el factorial de dicho número.
 Crea una función que dado un string nos diga si es palíndromo o no (capicúa). 
 */

function masIva(precio, tasa){
   return precioSinIVA * (1 + tasaIVA / 100);
}

function esPar(num){
   return num % 2 === 0;
}

function areaCirculo(r){
 return Math.PI * Math.pow(r,2);
}

function numRandom(min, max){
   return Math.floor(Math.random() * (max - min +1) + min)
}

function esPrimo(numero) {
   if (numero <= 1) {
     return false;
   }
   for (var i = 2; i <= Math.sqrt(numero); i++) {
     if (numero % i === 0) {
       return false;
     }
   }
   return true;
}

function factorial(numero) {
   if (numero === 0 || numero === 1) {
     return 1;
   }
   return numero * factorial(numero - 1);
}
 

function esPalindromo(cadena) {
   cadena = cadena.toLowerCase().replace(/[^a-z0-9]/g, '');
   var cadenaReversa = cadena.split('').reverse().join('');
   return cadena === cadenaReversa;
 }