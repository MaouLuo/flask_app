# -*- coding:utf-8 -*-

import os
import json
from flask import Flask, request, url_for, render_template, jsonify, send_file
# app = Flask(__name__, template_folder='./templates', static_url_path='', root_path=os.getcwd()) # 设置当前路径为默认
app = Flask(__name__, template_folder='templates', static_url_path='') # 设置当前路径为默认



@app.route('/i')
def index():
    return 'Index Page'
    
@app.route('/')
def demo():
    return render_template('portfolio.html')

@app.route('/test/')
def test():
    variable = {'username': 'Pang', 'site': 'stackoverflow.com'}
    return render_template('test.html', data=variable)

@app.route('/api/test/', methods=['GET','POST'])
def api_test():
    variable = [{'username': 'Pang', 'site': 'stackoverflow.com'}, {'username': 'Huyg', 'site': 'verflow.net'}]
    return jsonify(variable) # 返回json格式数据

@app.route('/api/addition/', methods=['POST', 'GET']) # 按照表单格式接收
def addition():
    if request.method == 'POST':
        numa = request.form.get('numa', 0)
        numb = request.form.get('numb', 0)
        total = numa + numb
        return jsonify({'count':total})
    if request.method == 'GET':
        numa = request.args.get('numa', 0)
        numb = request.args.get('numb', 0)
        total = numa + numb
        return jsonify({'count':total})

@app.route('/api/addition_json/', methods=['POST', 'GET']) # 按照表单格式接收
def addition_json():
    rv = json.loads(request.get_data()) 
    #data = request.get_json()
    #print(data)
    #rv = json.loads(data, encoding='utf-8')
    
    total = rv['numa'] + rv['numb']
    return jsonify({'count':total})

@app.route('/ip') # test ip proxy
def proxy_test():
    return 'sucess'

@app.route('/aidemo/')
def baidu_ai_demo():
    return 'baidu hi'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    