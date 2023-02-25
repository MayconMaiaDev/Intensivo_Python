# Desenvolvido por: MayconMaiaDev
# Aula sobre precedencia de operadores aritiméticos

# 1. (n + n)
# 2. ** elevado
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5 #7
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) #1024
print(conta_2, conta_1)