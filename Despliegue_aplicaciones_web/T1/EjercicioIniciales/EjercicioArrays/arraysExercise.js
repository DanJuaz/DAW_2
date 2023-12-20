let frutas=["Fresa", "Naranja", "Manzana"];
//Inserta dos elementos al final en un array.
frutas.push("Mango", "Platano");
//Inserta dos elementos al comienzo en un array.
frutas.unshift("Mandarina", "Cereza");
//Elimina dos elementos al final de un array.
frutas.pop();
frutas.pop();
//Elimina dos elementos al comienzo de un array.
frutas.shift();
frutas.shift();
//Dado un array de 10 elementos, crea otros dos arrays: uno con los primeros 5 elementos y el otro con los 5 últimos.
let array = ["Fresa", "Naranja", "Manzana","Mango", "Platano",1,2,3,4,5]

let array1 = array.slice(0,array.length/2);
let array2 = array.slice(array.length/2,array.length)
//Suma de elementos de un array: Escribe una función que sume todos los elementos de un array de números.
let result=0;
for(let i in array2){
    result += array2[i];
}
//Promedio de notas: Calcula el promedio de calificaciones en un array de números y redondea el resultado a dos decimales.
let promedio=0;
for(let i in array2){
    promedio += array2[i];
}
promedio = promedio/promedio.length;
promedio = promedio.toFixed(2);
//Encontrar el número mayor: Escribe una función para encontrar el número más grande en un array de números.
function numMax(array){
    let max=array[0];
    for(let i=0;i<array.length;i++){
        if(array[i]>max){
              max=array[i];  
        }
    }
    return max;
}
//Encontrar el número menor: Encuentra el número más pequeño en un array de números.
function numMin(array){
    let min=array[0];
    for(let i=0;i<array.length;i++){
        if(array[i]<min){
            min=array[i];  
        }
    }
    return min;
}
//Eliminar duplicados: Crea una función que elimine los elementos duplicados de un array.
function borrarDobles(array) {
    const newArray = [];
    
    for (let i = 0; i < array.length; i++) {
        if (newArray.indexOf(array[i]) === -1) {
            newArray.push(array[i]);
        }
    }
    
    return newArray;
}
//Contar elementos: Cuenta cuántas veces aparece un elemento específico en un array.
function repetir(array, num){
    let cont = 0;
    for(let i=0;i<array.length;i++){
        if(array[i]==num){
            cont++;
        }
    }
    return "El "+num+" se repite "+cont+"veces";
}
//Dar la vuelta a un array: Escribe una función que invierta un array dado, de modo que el último elemento se convierta en el primero, y así sucesivamente.
function arrayInvertido(array) {
    const newArray = [];  
    for (let i = array.length-1; i >= 0; i--) { 
        newArray.push(array[i]);
    }
    
    return "El array invertido es : "+newArray;
}
//Dado un texto que contiene un párrafo de varias frases: Crea un array llamado frases donde cada posición del array contiene una frase del párrafo.
function parrafoToFrases(parrafo) {
    const frases = parrafo.split(". "); // Divide el párrafo en frases usando el punto y espacio como separadores.
    return frases;
}
//Ordenar números: Ordena un array de números en orden ascendente y luego en orden descendente.
function ordenarASC(array) {
    const arrayAscendente = [...array]; 
    arrayAscendente.sort((a, b) => a - b);

    return  arrayAscendente;
}
function ordenarDESC(array) {
    const arrayDescendente = [...array]; 
    arrayDescendente.sort((a, b) => b - a);

    return  arrayDescendente;
}
//Crear un array adicional con los  números pares del array.
function arrayPares(array) {
    const newArray = [];  
    for(let i=0;i<array.length;i++){
        if(array[i]%2===0){
            newArray.push(array[i]);
        }
    }
    
    return "El array de pares es : "+newArray;
}
//Unión de arrays: Combina dos arrays en uno solo sin duplicados.
function unirArrays(){
    const newArray=[];
    for (let i = 0; i < arguments.length; i++) {
        newArray.push(...arguments[i]); 
    }
    return newArray;
}
//Eliminar elementos específicos: Elimina un elemento específico de un array y devuelve el nuevo array.
function borrarNum(array, num){
    for(let i = 0; i<array.length;i++){
        if(array[i]===num){
            array.splice(i,num);
            i--;
        }
    }
    return array;
}
//Multiplicar elementos: Multiplica todos los elementos de un array por un valor específico.
function mutlByNum(array,num){
    for(let i=0;i<array.length;i++){
        array[i] = array[i]*num;
    }
    return "El array es: "+array;
}
//Encontrar el índice: Encuentra el índice de un elemento en un array.
function findByIndex(array, num) {
    const index = array.indexOf(num);
    return index !== -1 ? "El índice del elemento es: " + index : "El elemento no se encuentra en el array.";
}
//Dividir array en grupos: Divide un array en grupos de un tamaño específico.
function dividirArrayEnGrupos(array, size) {
    const grupos = [];
    
    for (let i = 0; i < array.length; i += size) {
        grupos.push(array.slice(i, i + size));
    }
    
    return grupos;
}
//Suma de diagonales de un array bidimensional: Calcula la suma de los elementos en las diagonales de una matriz representada como un array de arrays.
function sumDiagonales(matriz) {
    let sumaDiagonalPrincipal = 0;
    let sumaDiagonalSecundaria = 0;

    for (let i = 0; i < matriz.length; i++) {
        sumaDiagonalPrincipal += matriz[i][i]; 
        sumaDiagonalSecundaria += matriz[i][matriz.length - 1 - i];
    }

    return {
        diagonalPrincipal: sumaDiagonalPrincipal,
        diagonalSecundaria: sumaDiagonalSecundaria
    };
}