import mysql.connector
from datetime import *
import re

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'estacionamento'

def conectar_banco(host, user, password, database):
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,

    )
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor



def ultimo_veiculo(): # encontra o id do ultimo veiculo cadastrado
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )


    comando = 'select * from veiculos ;'

    cursor.execute(comando)

    resultado = cursor.fetchall()  # ler o banco de dados

    conexao.close()

    if len(resultado) == 0:
        return 1

    else:
        return resultado[-1]["id"]



def get_id_by_cpf(cpf):# encontra o id da ultima pessoa cadastrada
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cpf = pontuar_cpf(cpf)
    comando = f"""SELECT id FROM pessoas
     where cpf = '{cpf}';"""
    cursor.execute(comando)
    resultado = cursor.fetchone()  # ler o banco de dados
    conexao.close()
    if resultado:
        return resultado["id"]




def hora_atual():
    hora = list
    hora = str(datetime.today().now().time())
    list(hora)
    return hora[:8]


def data_atual():
    data = date.today()
    return data


def valor_estadia(idveiculo):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    agora = datetime.now()
    comando = f'select * from vagas where idveiculo = "{idveiculo}";'

    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados
    dia = int(str(resultado[-1]['data_entrada'])[8:10])

    diferença_dia = agora.day - dia

    if diferença_dia > 0:
        valor = '180,00'
    else:
        comando = f'select data_entrada, hora from vagas where idveiculo = "{idveiculo}";'

        cursor.execute(comando)

        resultado = cursor.fetchall()  # ler o banco de dados
        conexao.close()

        b = int(str(resultado[-1]['hora'])[:2])

        agora = datetime.now()

        if not int(agora.hour) == b:
            estadia = int(agora.hour) - b
            valor = estadia * 15
        else:
            valor = '15,00'

    return f'Total a ser pago R${valor}'



def valida_cpf(cpf):
    cpf = str(cpf)
    if len(cpf) == 11:
        return True
    else:
        return 'ERRO cpf invalido.'


def pontuar_cpf(cpf):
    cpf = str(cpf)
    cpf_parte1 = cpf[0:3]
    cpf_parte2 = cpf[3:6]
    cpf_parte3 = cpf[6:9]
    cpf_parte4 = cpf[9:]
    return f'{cpf_parte1}.{cpf_parte2}.{cpf_parte3}-{cpf_parte4}'


def validar_placa(placa):
    pt = re.compile('[A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]')
    if pt.match(placa):
        return True
    else:
        return False


def pontuar_placa(placa):
    placa1 = placa[0:3]
    placa2 = placa[3:]
    return f'{placa1}-{placa2}'





