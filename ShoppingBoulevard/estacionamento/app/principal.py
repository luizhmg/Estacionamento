from time import *
from utils import *
from dao import *
from flask import Flask, render_template, request, redirect, url_for, session




app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    if 'usuario_logado' in session.keys() and session['usuario_logado'] != None:
        name = get_user_data_by_id(session['usuario_logado'])
        return render_template('index.html', nome=name)
    else:
        return redirect(url_for('login_funcionario'))



@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'GET':
        return render_template('cadastro.html')

    elif request.method == 'POST':
        nome = request.form['name']
        cpf = request.form['cpf']
        marca = request.form['marca']
        modelo = request.form['modelo']
        cor = request.form['cor']
        placa = request.form['placa']
        tipo = request.form['tipo_veiculo']


        cadastro(n=nome, cp=cpf)

        cadastro_veiculo(mar=marca, mod=modelo, cor=cor, pla=placa, cpf=cpf)

        return redirect(url_for('estacionar_veiculo', tipo=tipo))



@app.route('/cadastro_funcionario', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'GET':

        return render_template('cadastro_funcionario.html')

    elif request.method == 'POST':

        nome = request.form['nome']
        cpf = request.form['cpf']
        senha = request.form['senha']

        cadastro_funcionario_dao(nome=nome, cpf=cpf, senha=senha)

        return redirect(url_for('index'))



@app.route('/login', methods= ['GET', 'POST'])
def login_funcionario():

    if request.method == 'GET':
        return render_template('login_funcionario.html')

    elif request.method == 'POST':

        cpf = pontuar_cpf(request.form['cpf'])
        senha = request.form['senha']

        result = validar_login_funcionario(cpf=cpf, senha=senha)

        id_funcionario = result[1]

        if result[0] == True:
            session['usuario_logado'] = id_funcionario

            return redirect(url_for('index'))
        else:
            session['usuario_logado'] = None

            return redirect(url_for('login_funcionario'))


@app.route('/logout')
def logout_funcionario():
    session['usuario_logado'] = None

    return redirect(url_for('login_funcionario'))



@app.route('/estacionar/<tipo>', methods=['GET', 'POST'])
def estacionar_veiculo(tipo):

    if request.method == 'GET':
        lista = mostravaga(tipo=tipo)

        return render_template('Estacionar.html', vagas=lista)

    elif request.method == 'POST':

        id_vaga = request.form.get('id_vaga')
        id_funcionario = session['usuario_logado']

        preenche_vaga(id_vaga=id_vaga, id_funcionario=id_funcionario)

        return redirect(url_for('index'))


@app.route('/Retirar Veiculo', methods=['GET', 'POST'])
def retirar():
    if request.method == 'GET':

        lista = mostravaga_retirada()

        return render_template('Retirar.html', vagas=lista)

    elif request.method == 'POST':

        idveiculo = request.form.get('id_veiculo')

        return redirect(url_for('retirada', idveiculo=idveiculo))



@app.route('/Dados/<idveiculo>', methods=['GET', 'POST'])
def retirada(idveiculo):
    if request.method == 'GET':
        lista = retirar_veiculo(idveiculo)
        dados_veiculo = lista[0]
        dados_motorista = lista[1]
        valor_estadia = lista[2]

        return render_template('Dados_retirada.html',
                               veiculo=dados_veiculo,
                               motorista=dados_motorista,
                               valor_estadia=valor_estadia)

    elif request.method == 'POST':
        id_proprietario = request.form.get('id_proprietario')

        deletar_dados(id_proprietario=id_proprietario)

        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

