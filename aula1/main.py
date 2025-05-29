class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')


pessoa = Pessoa('João', 25)
pessoa.apresentar()

nome = 'leandro'
sobrenome = "lovo"
idade = 20
verdade = True
falso = False

def funcao_exemplo():
    print('Função exemplo executada')

funcao_exemplo()


frutas = ['maçã', 'banana', 'laranja', 0]
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


print('fim')