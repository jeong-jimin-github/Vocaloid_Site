from flask import Flask, render_template, request, redirect
import sqlite3
from flask import request
import os
import glob

db = sqlite3.connect("db.db",check_same_thread=False)
cur = db.cursor()

app = Flask(__name__)
@app.route('/')
def index():
    sql = "SELECT * from db"
    cur.execute(sql)

    data_list = cur.fetchall()


    return render_template('main.html', value=data_list)



@app.route('/look/<articleID>/')
def board_content(articleID):
    UserID = articleID

    sql = "SELECT * FROM db WHERE id = '" + UserID + "'"

    cur.execute(sql)

    result = cur.fetchall()

    return render_template("look.html", sm = articleID, result=result)

@app.errorhandler(404)
def page_not_found(error):
     return redirect(request.host_url)


if __name__ == '__main__':
  #  port = int(os.environ.get("PORT", 443))
  #  app.run(host='0.0.0.0', port=port, ssl_context=('/etc/letsencrypt/live/kuuhaku.xyz/fullchain.pem', '/etc/letsencrypt/live/kuuhaku.xyz/privkey.pem'))
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
    
