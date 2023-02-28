from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route ( '/' )
def index():
    if 'username' in session:
        return  'Logado como %s ' %escape( session['username'])
    return  'Você não está logado'

@app.route ( '/login' ,  methods= [ 'GET' ,  'POST' ])
def login():
    if request.method == 'POST':
        session['nome de usuário'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post"> 
            <p><input type=text name=username>
            <p><input type=enviar valor=Login> 
        </form> 
    '''

@app.route ( '/logout' )
def logout():
    # remove o nome de usuário da sessão se estiver lá
    session.pop('username',  None)
    return redirect(url_for('index'))

# define a chave secreta. mantenha isso realmente em segredo:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'