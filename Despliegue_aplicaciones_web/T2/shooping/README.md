# Carrito De La Compra (Vue, TailwindCSS)

## Vue
<p>Uso vue como los Component</p>

```
Vue.component('product', {
    props: ['articulo'],
    template: `
        <div class="flex flex-col md:flex-row border-b border-gray-400 py-4">
            <div class="flex-shrink-0 w-20 h-auto text-4xl">
                {{articulo.img}}
            </div>
            <div class="mt-4 md:mt-0 md:ml-6 text-xl">
                <h2 class="text-lg font-bold">{{articulo.title}}</h2>
                <p class="mt-2 text-gray-600">{{articulo.description}}</p>
                <div class="mt-4 flex items-center">
                    <span class="ml-auto font-bold">{{articulo.price}} €</span>
                    <button @click="agregarArticuloAlCarrito(articulo.id, articulo.title, articulo.img, articulo.price)" class="hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                        Añadir al carrito
                    </button>
                </div>
            </div>
        </div>
    `,
    methods: {
        agregarArticuloAlCarrito(id, title, img, price) {
            this.$emit('agregar_articulo_al_carrito', { id, title, img, price });
        }
    }
});
```


## TailwindCSS
<p>Tailwindcss frameworl css, para maquetar mas rapido y eficientemente código CSS.</p>

## Speed Wev ( Google Page Speed Insight )