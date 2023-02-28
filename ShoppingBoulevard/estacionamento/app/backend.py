from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('zzz.html')
    elif request.method == 'POST':
        name = request.form['name']
        print(name)
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port=3000)
