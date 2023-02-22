from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from config import config
from datetime import datetime
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

path = "C:/Archivos Subidos"

app.config['UPLOAD_FOLDER'] = path

conexion = MySQL(app)


@app.route('/')
def getForm():
    return render_template("index.html")

@app.route('/files')
def filelist():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, filename, fecha, createdBy, routes FROM file"
        cursor.execute(sql)
        datos = cursor.fetchall()
    except Exception as e:
        return jsonify({'mensaje':"Error"}) 
    finally: 
        return render_template("biblio.html", files = datos)

@app.route('/create', methods=['POST'])
def createFile():
    try:
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO file(filename, fecha, createdBy, routes) 
        VALUES('{0}','{1}', '{2}', '{3}')""".format(filename, datetime.now(), "Marcos Alejos", path + "/" + filename)
        cursor.execute(sql)
        conexion.connection.commit()
        return redirect(url_for('filelist'))
    except Exception as e:
        return "ERROR"

@app.route('/delete/<id>')
def deleteFile(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT routes FROM file WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        ruta = cursor.fetchall()
        os.remove(ruta[0][0])
        sql = "DELETE FROM file WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return redirect(url_for('filelist'))
    except Exception as e:
        return "Error"

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    try:
        if request.method == "POST":
            texto = request.form['']
            
    except Exception as e:
        return "Error"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()