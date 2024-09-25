def verificando_caracter(palavra):
    palavra_convertida = palavra.lower()
    qntd_de_a = palavra_convertida.count('a')

    if qntd_de_a>0:
        print(f"A letra 'a' aparece {qntd_de_a} vezes na palavra: {palavra_convertida}.")
    else:
        print(f"A letra 'a' não aparece na palavra: {palavra_convertida}.")

palavra = input("Informe uma palavra: ")
verificando_caracter(palavra)