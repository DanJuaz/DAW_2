//Mostrar la tabla de multiplicar de un número del 1 al 10 que introduzca el usuario (preguntar utilizando prompt).
let num = parseInt(prompt("Introduce un numero para su tabla de multiplicar: "));
console.log(`Tabla de multiplicar de ${num}`);
for(let i = 0;i<=10;i++){
    let result = num * i;
    console.log(`${num} x ${i} = ${result}`);
}

//Dado un número mostrar los números pares hasta ese número.
let numPar = parseInt(prompt("Introduce un numero para su mostrar sus numeros pares: "));
let array = [];
for(let i = 0;i<=numPar;i++){
   if(i%2===0){
    array.push(i)
   }
}

//Dado un número mostrar los números primos hasta ese número.
let numPrimos = parseInt(prompt("Introduce un numero para su mostrar sus numeros primos: "));
let arrayPrimos = [];
for(let i = 0;i <= numPrimos;i++){
   if(i%1===0 && i%i===0){
    array.push(i)
   }
}
console.log(arrayPrimos)
//Dado un número calcular el factorial de dicho número. Utilizar una función.
function calculateFactorial(n){
   if(n < 0){
      return ("No hay factoriales para numeros negativos.")
   }else if(n == 0 || n == 1){
      return 1;  
   }else{
      let fact = 1;
      for(let i = 2; i <= n; i++){
         fact *= i;
      }
      return fact;
   }
}
console.log(calculateFactorial(5));
//Pide una edad a través del comando prompt y muestra en pantalla (DOM) lo siguiente:
//Si la edad se corresponde a una persona mayor o menor de edad.
//Considerando el año actual (new Date().setFullYear()) mostrar los años que han sido bisiestos (considerar los que son divisibles entre 4) desde su año de nacimiento (incluido) hasta el año actual.
let edad = parseInt(prompt("Dame tu edad actual:"));
if(edad < 18){
   console.log("Menor de edad");
}else{
   console.log("Mayor de edad");
}
let thisYear = new Date().getFullYear();
let bornYear = thisYear - edad;
let bisiestos = [];
for(let i = bornYear; i < thisYear; i++){
   if(esBisiesto(i)){
      bisiestos.push(i);
   }
}
return console.log(bisiestos);
function esBisiesto(year) {
   return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}   
//Sacar los dados (aleatorio entero entre 1 y 6). Mostrar en pantalla:
//Los 2 valores de los dados
//Si son iguales o no. En el caso de que no sean iguales indicar si el primero o el segundo dado es mayor.
//Mostrar los dados como imágenes.


 