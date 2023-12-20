La biblioteca `json` en Python proporciona funciones para trabajar con datos JSON (JavaScript Object Notation). Aquí tienes una breve documentación sobre las funciones más comunes de la biblioteca `json`:

### 1. `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
- **Descripción:** Convierte un objeto de Python a una cadena JSON.
- **Parámetros:**
  - `obj`: Objeto de Python a convertir.
  - `skipkeys`: Si es `True`, las claves que no son cadenas Python válidas se omitirán. Default es `False`.
  - `ensure_ascii`: Si es `True`, todos los caracteres no ASCII se escaparán en la salida. Default es `True`.
  - `indent`: Indentación para la salida. Puede ser un número o una cadena. Default es `None`.
  - Otros parámetros: Ver [documentación oficial](https://docs.python.org/3/library/json.html#json.dumps).

### 2. `json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
- **Descripción:** Escribe un objeto Python en un archivo en formato JSON.
- **Parámetros:**
  - `obj`: Objeto de Python a convertir y escribir.
  - `fp`: Archivo o descriptor de archivo donde se escribirá el JSON.
  - Otros parámetros: Ver [documentación oficial](https://docs.python.org/3/library/json.html#json.dump).

### 3. `json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`
- **Descripción:** Lee un archivo JSON y lo convierte en un objeto de Python.
- **Parámetros:**
  - `fp`: Archivo o descriptor de archivo desde donde se leerá el JSON.
  - Otros parámetros: Ver [documentación oficial](https://docs.python.org/3/library/json.html#json.load).

### 4. `json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`
- **Descripción:** Convierte una cadena JSON en un objeto de Python.
- **Parámetros:**
  - `s`: Cadena JSON a convertir.
  - Otros parámetros: Ver [documentación oficial](https://docs.python.org/3/library/json.html#json.loads).

### 5. `json.JSONEncoder`
- **Descripción:** Clase base para definir codificadores personalizados para objetos no serializables por defecto.
- Ver [documentación oficial](https://docs.python.org/3/library/json.html#json.JSONEncoder).

### 6. `json.JSONDecoder`
- **Descripción:** Clase base para definir decodificadores personalizados para tipos de datos no serializables por defecto.
- Ver [documentación oficial](https://docs.python.org/3/library/json.html#json.JSONDecoder).

### Ejemplo de Uso:
```python
import json

# Convertir un objeto Python a JSON
data = {"name": "John", "age": 30, "city": "New York"}
json_str = json.dumps(data, indent=2)
print(json_str)

# Escribir un objeto Python en un archivo JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# Leer un archivo JSON y convertirlo a un objeto Python
with open("input.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

Esta documentación proporciona una visión general de las funciones más comunes de la biblioteca `json`. Puedes encontrar información más detallada en la [documentación oficial de json en Python](https://docs.python.org/3/library/json.html).