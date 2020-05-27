from flask import Flask, render_template, redirect, url_for, request
import sql

app = Flask(__name__)

@app.route('/')
def index():
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute(" SELECT * FROM items ORDER BY name")
    result_raw = cur.fetchmany(1000)
    conn.close()
    return(render_template('main.html', items=result_raw))

@app.route('/add-<item>')
def add(item):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute(" SELECT * FROM items WHERE name=?", [item])
    cur_count_raw = cur.fetchone()
    cur_count = cur_count_raw[1] + 1
    print(cur_count)
    cur.execute(" UPDATE items SET quantity=? WHERE name=?", [cur_count, item])
    conn.commit()
    conn.close()
    return(redirect(url_for('index')))

@app.route('/sub-<item>')
def sub(item):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute(" SELECT * FROM items WHERE name=?", [item])
    cur_count_raw = cur.fetchone()
    cur_count = cur_count_raw[1] - 1
    print(cur_count)
    cur.execute(" UPDATE items SET quantity=? WHERE name=?", [cur_count, item])
    conn.commit()
    conn.close()
    return(redirect(url_for('index')))

@app.route('/edit-<item>', methods=['GET', 'POST'])
def edit_item(item):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute(" SELECT * FROM items WHERE name=?", [item])
    cur_item = cur.fetchone()
    if request.method == 'POST':
        new_name = request.form['nameinput']
        new_qty = request.form['qtyinput']
        new_volume = request.form['sizeinput']
        print("got here")

        conn = sql.connect()
        cur = conn.cursor()
        cur.execute(" UPDATE items SET name=?,quantity=?,volume=? WHERE name=?", [new_name, new_qty, new_volume, cur_item[0]])
        cur.execute(" SELECT * FROM items WHERE name=?", [cur_item[0]])
        print("got here")
        conn.commit()
        conn.close()
        return(redirect(url_for('index')))
    
    if request.method == 'GET':
        return(render_template('create.html', task='edit', name=cur_item[0], quantity=cur_item[1], size=cur_item[2]))

@app.route('/delete-<item>')
def delete_item(item):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute(" DELETE FROM items WHERE name=?", [item])
    conn.commit()
    conn.close()
    return(redirect(url_for('index')))
    
    

@app.route('/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        name = request.form['nameinput']
        qty = request.form['qtyinput']
        volume = request.form['sizeinput']

        conn = sql.connect()
        cur = conn.cursor()
        cur.execute(" INSERT INTO items(name, quantity, volume) VALUES(?, ?, ?) ", [name.lower(), qty, volume.lower()])
        conn.commit()
        conn.close()
        return(redirect(url_for('index')))
    if request.method == 'GET':
        return(render_template("create.html", task='create'))