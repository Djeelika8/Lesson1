import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valut = list(data['Valute'].values())
    return valut


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for val in valutes:
        text += '<tr>'
        for v in val.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()

'''
Running on http://127.0.0.1:5000/ 

Курс валют
R01010	036	AUD	1	Австралийский доллар	                   35.9552	37.1232
R01020A	944	AZN	1	Азербайджанский манат	                   32.5286	33.7724
R01035	826	GBP	1	Фунт стерлингов Соединенного королевства   61.0166	61.6903
R01060	051	AMD	100	Армянских драмов	                       13.6321	14.1436

и т.д.

'''