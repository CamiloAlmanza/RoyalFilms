import re
from flask import Flask, render_template, request, session, redirect, flash
from flask.helpers import url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

#Para ir a la pagina principal
@app.route("/" , methods=['GET', 'POST'] )
def home():
    return render_template('inicio.html')

#Para dirigirse a la pagina de crear pelicula
@app.route ("/crearp")
def crearp():
    return render_template('crearp.html')

#Para ir a la pagina que permitirá editar una pelicula
@app.route ("/editarp/<nombre_pelicula>", methods=["GET", "POST"])
def editarp(nombre_pelicula):
    nombre=nombre_pelicula
    if request.method == 'GET':
        try:
            with sqlite3.connect('Royal Films/base.db') as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM peliculas WHERE nombre_pelicula=?",[nombre])
                row = cur.fetchall()
                if row is None:
                    print('No hay registros')
                return render_template ('/editarp.html', row=row)
        except Error:
            print(Error)
    return render_template ("/mirarp.html")

#Para actualizar una pelicula
@app.route ("/actualizarp", methods=["GET", "POST"])
def actualizarp():
    if request.method == 'POST':
        id_peli=request.form['id']
        nombrepeli=request.form['nombrep']
        idiomapeli=request.form['language']
        clasipeli=request.form['clasi']
        duracionpeli=request.form['tiempo']
        fechapeli=request.form['fecha']
        direccionpeli=request.form['url']
        sinopsispeli=request.form['sinopsis']
        directorpeli=request.form['director']
        repartopeli=request.form['reparto']        
        try:
            with sqlite3.connect("Royal Films/base.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE peliculas SET nombre_pelicula=?, idioma=?, clasificacion=?,duracion=?,fecha_estreno=?,url_trailer=?,sinopsis=?,director_pelicula=?,reparto_pelicula=? WHERE id_pelicula=?",[nombrepeli, idiomapeli, clasipeli, duracionpeli, fechapeli, direccionpeli, sinopsispeli, directorpeli, repartopeli, id_peli])                
                con.commit()
                return redirect(url_for('mirarp'))
        except Error:
            return(Error)
    return render_template('/inicio.html')

#Para eliminar una pelicula
@app.route ("/eliminarp/<nombre_pelicula>", methods=["GET", "POST"])
def eliminarp(nombre_pelicula):
    nombre = nombre_pelicula
    try:
        with sqlite3.connect('Royal Films/base.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM peliculas WHERE nombre_pelicula=?",[nombre])
            con.commit()
            return redirect(url_for('mirarp'))
    except Error:
        return "Error" 

#Para mirar el listado de peliculas
@app.route ("/mirarp", methods=["GET", "POST"])
def mirarp():
    if request.method == 'GET':
        try:
            with sqlite3.connect('Royal Films/base.db') as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM peliculas")
                row = cur.fetchall()
                if row is None:
                    print('No hay registros')
                return render_template ('/mirarp.html', row=row)
        except Error:
            print(Error)
    return render_template ("inicio.html")

#Para crear una pelicula
@app.route ("/crearr", methods=["GET", "POST"])
def crearr():
    if request.method == 'POST':
        nombrepeli=request.form['nombrep']
        idiomapeli=request.form['language']
        clasipeli=request.form['clasi']
        duracionpeli=request.form['tiempo']
        fechapeli=request.form['fecha']
        direccionpeli=request.form['url']
        sinopsispeli=request.form['sinopsis']
        directorpeli=request.form['director']
        repartopeli=request.form['reparto']        
        try:
            with sqlite3.connect("Royal Films/base.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO peliculas (nombre_pelicula,idioma,clasificacion,duracion,fecha_estreno,url_trailer,sinopsis,director_pelicula,reparto_pelicula) VALUES (?,?,?,?,?,?,?,?,?)",(nombrepeli, idiomapeli, clasipeli, duracionpeli, fechapeli, direccionpeli, sinopsispeli, directorpeli, repartopeli))
                con.commit()
                return redirect("/")
        except Error:
            return(Error)
    return render_template('/crearp')

#Para regresar al inicio
@app.route ("/volver")
def volver():
    return render_template('inicio.html')

#Para que se actualice automaticamente
if (__name__ == '__main__'):
    app.run(debug=True, port=8000)