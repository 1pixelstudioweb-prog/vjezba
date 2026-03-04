from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        sifra = request.form.get('sifra')

        # TVOJA LOGIKA
        if email.endswith("@gmail.com"):
            duzina_sifre = len(sifra)
            if duzina_sifre < 8:
                return "Sifra je prekratka! <a href='/login'>Nazad</a>"
            elif duzina_sifre > 16:
                return "Sifra je predugacka! <a href='/login'>Nazad</a>"
            else:
                # Sifra je ispravna
                return redirect('/chat')
        else:
            return "Email nije ispravan! <a href='/login'>Nazad</a>"
            
    return render_template('login.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
