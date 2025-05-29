class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')


pessoa = Pessoa('João', 25)

# ""+""
# f'{pessoa.nome} eh str'
# " 'nome' {0}".format('maria nascimento')



descricao = """ 
oi
comentario muito grande
"""

print(descricao)

pessoa.apresentar()

frutas = ['maçã', 'banana', 'laranja', 0]
nome = 'leandro'
sobrenome = "lovo"
idade = 20
verdade = True
falso = False

dicionario = {
    'Aluno 1': "Davi",
    'Aluno 2': "Daniel",
    0: "Valor 0",
    'frutas': frutas,
}

print(dicionario['Aluno 1'])
print(dicionario)



def funcao_exemplo():
    print('Função exemplo executada')

funcao_exemplo()

for fruta in frutas:
    print('Fruta:', fruta)


if(verdade):
    print('Verdadeiro')
else:
    print('Falso')

while(idade < 30):
    print('Idade: ', idade)
    idade = 31

if (verdade):
    pass


print(nome)

# and, or e not

diga = str(input('Digite seu nome: '))

print('fim')