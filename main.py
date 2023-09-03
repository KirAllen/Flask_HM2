from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key='70d47e4f20dd88595b33ac763152ad40a9c9a5ba8c138e821ec88a78b2a8badd'


@app.route('/main/')
def main():
    return render_template('index.html')

@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['email'] = request.form.get('email')
        return redirect(url_for('main'))
    return render_template('flash.form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
