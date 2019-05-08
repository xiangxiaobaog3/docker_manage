# -*- coding:utf-8 -*-

from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    url_str = 'www.xiangxiaobao.com'

    return render_template('index.html', url_str=url_str)

@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    return 'order_id %s' % order_id

if __name__ == '__main__':
    app.run()
