
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# usar "" para rota
@app.route("/templates")
def index():
    return render_template('modelo.html')



if __name__ == '__main__':
    app.run()