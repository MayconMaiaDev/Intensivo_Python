# Desenvolvido por: MayconMaiaDev

# Formatando string com o método string.format
a = 'MMMMMM'
b = 'AAAAAA'
c = 1.5
string = 'a={nome2} m={nome1} m={nome1} c={nome3:.2f}' # variavel string recebendo os valores
formato = string.format(
    nome1=a, nome2=b, nome3=c # método format recebendo os valores da variavels string
)

print(formato)