import sys

def print_python_version():
    print(sys.version)

def ordenar_letras_alfabeticamente(texto):
    return ''.join(sorted(texto)) # Ordena as letras da palavra em ordem alfabética

palavra = "gjmdpdcq"
palavra_ordenada = ordenar_letras_alfabeticamente(palavra)
print(f"A palavra '{palavra}' ordenada alfabeticamente é '{palavra_ordenada}'")
