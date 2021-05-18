from markupsafe import escape
from flask import Flask, url_for, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def main(chat_alldata=None):
    con = sqlite3.connect('chat.db')
    cur = con.cursor()

    if 'name' in request.args and request.args['name'] != "":
        cur.execute("select * from chat where name=? ", (request.args['name'],))
        print("true")
    else:
        cur.execute("select * from chat ")
        print("false")

    chat_alldata = cur.fetchall()
    con.close()
    print("chat_alldataは", chat_alldata, "です。")
    return render_template('chat.html', chat_alldata=chat_alldata)

@app.route('/submit',methods=['POST']) 
def submit():
    con = sqlite3.connect('chat.db')
    cur = con.cursor()
    cur.execute("insert into chat values (?, ?)", (request.form["chat_name"] , request.form["chat_text"]))
    con.commit()
    con.close()
    return "%s, %s"  % (request.form["chat_name"],request.form["chat_text"])