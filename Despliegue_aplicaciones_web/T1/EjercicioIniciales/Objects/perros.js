const perros = [
    {
        nombre: "Toby",
        raza: "Pitbull",
        edad: 3,
        leGusta: ["Hueso", "Pollo", "Chololate"]
    },
    {
        nombre: "Pichi",
        raza: "Doberman",
        edad: 8,
        leGusta: ["Hueso", "Carne", "Fruta", "Pienso"]
    },
    {
        nombre: "Tiger",
        raza: "Chihuaua",
        edad: 11,
        leGusta: ["Sopa de fideos", "Zanahoria", "Fresa", "Coco"]
    }
];


//Todo (perros)
console.log(perros)
//La información del segundo perro
console.log(perros[1])
//El nombre del tercer perro
console.log(perros[2].nombre)
//La raza del primer perro
console.log(perros[0].raza)
//La segunda cosa que le gusta al primer perro
console.log(perros[0].leGusta[1])
//La última cosa que le gusta al último perro
console.log(perros[2].leGusta[3])
//La cantidad de cosas que le gusta al segundo perro, y lo que le gusta (número y lista de cosas que le gustan)
const segundoPerroGustos = perros[1].leGusta.length;
console.log(`Le gusta ${segundoPerroGustos} cosas: ${perros[1].leGusta}`);
//El nombre del perro con más edad
let perroMasViejo = perros[0];
for (const perro of perros) {
  if (perro.edad > perroMasViejo.edad) {
    perroMasViejo = perro;
  }
}
console.log(`El perro más viejo es: ${perroMasViejo.nombre}`);
//La lista de cosas que le gustan tanto al primer como al segundo perro
console.log(`Le gusta ${segundoPerroGustos} al 2 perro "${perros[1].nombre}": ${perros[1].leGusta}`);
const primerPerro = perros[0].leGusta.length
console.log(`Le gusta ${primerPerro} al 2 perro "${perros[0].nombre}": ${perros[0].leGusta}`);







