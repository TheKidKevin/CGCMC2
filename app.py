from flask import Flask

from samo import *

app = Flask(__name__)


@app.route('/')
def samoyedcoin():
    return 'Samoyedcoin'


@app.route('/supply/total')
def total_supply():
    return str(get_totalsupply())


@app.route('/supply/circulating')
def circulating_supply():
    return str(get_circulating_supply())


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9007)
