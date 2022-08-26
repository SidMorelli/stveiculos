
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# usar "" para rota
@app.route("/templates")
def index():
    return render_template('modelo.html')



if __name__ == '__main__':
    #app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)