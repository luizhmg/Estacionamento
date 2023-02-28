import mysql.connector
import datetime
from datetime import *
from estacionamento.menu import *
from estacionamento.funçoes_adicionais import *
from estacionamento.validaçao_de_dados import *
import re

def hora_atual():
    hora = list
    hora = datetime.today().now().time()

    return hora

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='estacionamento',
)
cursor = conexao.cursor(dictionary=True)

'''def valor_estadia(id):
    agora = datetime.now()
    comando = f'select * from vagas where idveiculo = "{id}";'

    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados
    print(resultado[-1]['hora'])
    dia = int(str(resultado[-1]['data'])[8:10])

    diferença_dia = agora.day - dia

    if diferença_dia > 0:
        valor = '180,00'
    else:
        comando = f'select data, hora from vagas where idveiculo = "{id}";'

        cursor.execute(comando)

        resultado = cursor.fetchall()  # ler o banco de dados

        b = int(str(resultado[-1]['hora'])[:2])
        print(b)

        agora = datetime.now()

        if not int(agora.hour) == b:
            estadia = int(agora.hour) - b
            print(estadia)
            valor = estadia * 15
        else:
            valor = '15,00'

    return f'Total a ser pago R${valor}'''
def pessoas():
    comando = 'select * from pessoas;'

    cursor.execute(comando)

    resultado = cursor.fetchall()

    return resultado

resultado = pessoas()

print(resultado[0])

for c in resultado:
    for pessoas in c.values():
        print(pessoas)

'''def criavaga():

    seçao = 'amarelo'
    numero = 1
    andar = 1
    tipo = 'carro'
    bloco = ''
    status = 'vazio'
    idveiculo = 'vazio'

    for bl in range(1, 5):
        if bl == 1:
            bloco = 'A'

        elif bl == 2:
            bloco = 'B'

        elif bl == 3:
            bloco = 'C'

        elif bl == 4:
            bloco = 'D'
        for ad in range(1, 4):
            if ad == 1:
                andar = 1

            if ad == 2:
                andar = 2

            if ad == 3:
                andar = 3

            for c in range(0, 400):
                if c == 0:
                    tipo = 'carro'

                if c == 280:
                    tipo = 'PCD'

                if c == 300:
                    tipo = 'moto'

                # sistema de seçao do andar 1
                if ad == 1 and c == 200:
                    seçao = 'verde'
                if ad == 1 and c == 400:
                    seçao = 'amarelo'
                # sistema de seçao do andar 2
                if ad == 2 and c == 600:
                    seçao = 'azul'
                if ad == 2 and c == 800:
                    seçao = 'vermelho'
                # sistema de seçao do andar 3
                if ad == 3 and c == 1000:
                    seçao = 'preto'
                if ad == 3 and c == 0:
                    seçao = 'roxo'
                comando = f'INSERT INTO vagas (seçao, numero, andar, tipo, bloco, status) VALUES ' \
                          f' ("{seçao}", "{numero}", "{andar}", "{tipo}", "{bloco}", "{status}")'

                numero += 1
                cursor.execute(comando)
                conexao.commit()  # edita o banco de dados'''

'''nome = str(input('Digite seu primeiro nome:'))

senha = str(input('Digite sua senha:'))

comando = f"INSERT INTO funcionarios (nome, senha) VALUES ('{nome}', '{senha}');"

#comando = 'select * from funcionarios;'

cursor.execute(comando)
conexao.commit()

resultado = cursor.fetchall() # ler o banco de dados'''

'''nome = str(input('Digite seu nome:'))
while True:
    cpf = leiaint('Digite seu cpf [somente numeros] :')
    validar = valida_cpf(cpf)
    if validar == True:
        cpf = pontuar_cpf(cpf)
        break
    else:
        print('cpf invalido digite novamente.')

comando = f'INSERT INTO pessoas (nome, cpf) VALUES ("{nome}", "{cpf}")'
cursor.execute(comando)
conexao.commit()  # edita o banco de dados'''