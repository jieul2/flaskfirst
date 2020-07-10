from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/mvp')
def mvp():
    return render_template('mvp.html')

if __name__ == '__main__':
    app.run(host = '192.168.0.2', port = 8080)