#Web - Calculadora 

nome_pagina = 'Calculadora'
from flask import Flask, render_template, request
from calculoExercicio import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo =nome_pagina)


@app.route('/calcular')
def calcular():
    x = int(request.args['numero1'])
    y = int(request.args['numero2'])
    r_soma = soma(x,y)
    r_sub = sub(x,y)
    r_multi = multi(x,y)
    r_div = div(x,y)
    r_div_fra = div_fra(x,y)
    r_rest_div = rest_div(x,y)
    r_raiz = raiz(x,y)
    resultados = {'soma':r_soma,'sub':r_sub,'multi':r_multi,'div':r_div,'div_fra':r_div_fra,'rest_div':r_rest_div,'raiz':r_raiz}

    return render_template(
    'resultado.html'
    ,x = x
    ,y = y
    ,resultados = resultados)

app.run()

