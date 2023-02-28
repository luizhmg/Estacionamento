import mysql.connector

from utils import *
from datetime import *

def cadastro(n, cp):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    # dados da pessoa:
    while True:
        validar = valida_cpf(cp)
        if validar == True:
            cpf = pontuar_cpf(cp)
            break
        else:
            print('cpf invalido digite novamente.')

    comando = f'INSERT INTO pessoas (nome, cpf) VALUES ("{n}", "{cpf}");'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    conexao.close()


def cadastro_funcionario_dao(nome, cpf, senha):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    while True:
        v = valida_cpf(cpf)
        if v:
            cpf = pontuar_cpf(cpf)
            break
        else:
            print('cpf invalido digite novamente.')

    comando = f'INSERT INTO funcionarios (nome, cpf, senha) VALUES ("{nome}", "{cpf}", "{senha}");'

    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    conexao.close()


# dados do veiculo:
def cadastro_veiculo(mar, mod, cor, pla, cpf):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    idproprietario = get_id_by_cpf(cpf)

    while True:
        v = validar_placa(pla)

        if v:
            placa = pontuar_placa(pla)

            break

        else:
            print('Placa invalida. Digite nomvamente.')

    comando = f"""INSERT INTO veiculos (marca, modelo, cor, placa, idproprietario) VALUES
               ('{mar}', '{mod}', '{cor}', '{placa}', '{idproprietario}')"""

    cursor.execute(comando)

    conexao.commit() # edita o banco de dados

    conexao.close()


def criavaga():
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

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
            for c in range(0, 10):
                if c == 0:
                    tipo = 'carro'
                if c == 4:
                    tipo = 'moto'
                if c == 8:
                    tipo = 'PCD'
                # sistema de seçao do andar 1
                if ad == 1 and c == 5:
                    seçao = 'verde'
                if ad == 1 and c == 0:
                    seçao = 'amarelo'
                # sistema de seçao do andar 2
                if ad == 2 and c == 5:
                    seçao = 'azul'
                if ad == 2 and c == 0:
                    seçao = 'vermelho'
                # sistema de seçao do andar 3
                if ad == 3 and c == 5:
                    seçao = 'preto'
                if ad == 3 and c == 0:
                    seçao = 'roxo'
                comando = f'INSERT INTO vagas (seçao, numero, andar, tipo, bloco, status) VALUES ' \
                          f' ("{seçao}", "{numero}", "{andar}", "{tipo}", "{bloco}", "{status}")'

                numero += 1
                cursor.execute(comando)
        conexao.commit()  # edita o banco de dados
        conexao.close()


def mostravaga(tipo):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )



    comando = f'select id, seçao, numero, andar, tipo, bloco, status from vagas ' \
              f'where status = "vazio" and tipo = "{tipo}";'

    cursor.execute(comando)

    resultado = cursor.fetchall()  # ler o banco de dados

    conexao.close()

    return resultado



def preenche_vaga(id_vaga, id_funcionario):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    idveiculo = ultimo_veiculo()
    hora = hora_atual()
    data = data_atual()
    comando = f'UPDATE `estacionamento`.`vagas` SET `idveiculo` = "{idveiculo}", `idfuncionario` = "{id_funcionario}",'\
              f' `status` = "ocupado", `data_entrada` = "{data}", `hora` = "{hora}" WHERE(`id` = "{id_vaga}");'

    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    conexao.close()


def retirar_veiculo(idveiculo):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )



    comando = f'select veiculos.marca, veiculos.modelo, veiculos.cor,  vagas.bloco, vagas.andar,' \
              f' vagas.seçao, vagas.idveiculo, vagas.numero, vagas.tipo from vagas ' \
              f'join veiculos on vagas.idveiculo = veiculos.id where veiculos.id = {idveiculo};'
    cursor.execute(comando)
    resultado1 = cursor.fetchall() # ler o banco de dados

    comando = f'select pessoas.id, pessoas.nome, pessoas.cpf from pessoas ' \
              f'join veiculos on pessoas.id = veiculos.idproprietario where veiculos.id = {idveiculo};'
    cursor.execute(comando)
    resultado2 = cursor.fetchall() # ler o banco de dados
    conexao.close()

    resultado3 = valor_estadia(idveiculo)

    return resultado1, resultado2, resultado3



def deletar_dados(id_proprietario):

    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )


    comando = 'SET FOREIGN_KEY_CHECKS = 0;'
    cursor.execute(comando)
    conexao.commit()


    comando = f'select id from veiculos where idproprietario = {id_proprietario}'
    cursor.execute(comando)
    id_veiculo = cursor.fetchall()[0]['id']


    comando = f'delete pessoas.* from pessoas where id = "{id_proprietario}";'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados


    comando = f'delete veiculos.* from veiculos where idproprietario = "{id_proprietario}";'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados


    comando = f'update estacionamento.vagas set idveiculo = null, data_entrada = null, hora = null,' \
              f' idfuncionario = null, status = "vazio" where idveiculo = "{id_veiculo}";'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados


    comando = 'SET FOREIGN_KEY_CHECKS = 1;'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()



def validar_login_funcionario(cpf, senha):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    comando = f'''select id from funcionarios where cpf='{cpf}' and senha='{senha}';'''

    cursor.execute(comando)
    result = cursor.fetchall()
    conexao.close()

    if result == []:
        return False
    else:
        return True, result[-1]['id']



def get_user_data_by_id(id_user):
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    comando = f'select nome from funcionarios where id = {id_user};'
    cursor.execute(comando)
    name = cursor.fetchone()['nome']
    conexao.close()

    return name



def mostravaga_retirada():
    conexao, cursor = conectar_banco(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    comando = 'select vagas.id, vagas.idveiculo, vagas.seçao, vagas.numero, vagas.andar, vagas.bloco, veiculos.marca, veiculos.modelo,' \
              ' veiculos.placa from vagas join veiculos on vagas.idveiculo = veiculos.id;'


    cursor.execute(comando)

    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)
    conexao.close()

    return resultado




