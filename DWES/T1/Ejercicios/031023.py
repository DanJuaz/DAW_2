import re
# REGEX


def ab(text):
    """
    Escribir una función que nos diga si en un texto hay alguna palabra que empiece por 'ab' o 'Ab'
    """
    patron = "r'\b[abAB]\w*\b'"
    palabras = re.findall(patron, text)
    return len(palabras) >= 0


def begincendtoea(text):
    """
    Crear una función que nos diga si en un texto hay alguna palabra que empiece por 'c' y termine por 'e' o por 'a'
    """
    p = "r'\b[c]\w*[e|a]\b'"
    return len(re.findall(p, text)) > 0


def foundfirstword(texto, palabra):
    """
    Crear una función que nos diga si una frase comienza por una palabra que le pasamos como parámetro,
    sin diferenciar mayúsculas y minúsculas.
    """
    palabra = palabra.lower()
    patron = fr'^{palabra}\b'

    return re.match(patron, texto, re.IGNORECASE) is not None


def flastword(paragraph, word):
    """Crear una función que nos diga si una frase termina por una palabra
    (puede haber uno o varios puntos al final) que le pasamos como parámetro.
    """
    pattern = rf'\b{word}(?:\.[^\s\?]+)*[^\?\s]*[.?]?'
    return re.search(pattern, paragraph, re.IGNORECASE) is not None


def changemultiesapceforone(paragraph):
    """
    Escribir una función de Python que sustituya todos los espacios múltiples de una frase por u único espacio.
    """
    paragraph = re.sub(r'\s+', ' ', paragraph)
    return print(paragraph)


if __name__ == '__main__':
    lorem = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, " \
            "totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta " \
            "sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, " \
            "sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, " \
            "qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi " \
            "tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, " \
            "quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi " \
            "consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae " \
            "consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla     pariatur?"
    print(ab(lorem))
    print(begincendtoea(lorem))
    print(foundfirstword(lorem, palabra="Sed"))
    print(flastword(lorem, "pariatur"))
    print(changemultiesapceforone(lorem))
