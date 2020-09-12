# -*- coding:utf-8 -*-

import os
import json
from flask import Flask, request, url_for, render_template, jsonify, send_file
import tools
# app = Flask(__name__, template_folder='./templates', static_url_path='', root_path=os.getcwd()) # 设置当前路径为默认
app = Flask(__name__, template_folder='templates', static_url_path='') # 设置当前路径为默认

def dd_msg():
    d =  tools.Dingding()
    d.send_text('from flask')

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
    print('i get a json data')
    return jsonify({'count':total})

@app.route('/ip/') # test ip proxy
def proxy_test():
    dd_msg()
    #return 'sucess'+'</br>'+'jahaha'

@app.route('/aidemo/')
def baidu_ai_demo():    
    return 'baidu hi'

@app.route('/temp/')
def temperature():
    text = ''
    with open('./temp.log', 'r', encoding='utf-8') as f:
        for i in f:
            text += (i+'</br>')
    return text

@app.route('/callback/test/', methods=['POST']) # 仅用于POST请求，无法接收表单数据
def cb_test():
    data = json.loads(request.get_data())
    if data['token'] == 'zhimakaimen':
        return 'Welcome to pass the test'
    else:
        return 'Identity verification failed'

@app.route('/formdeal/test_token/', methods=['GET', 'POST'])
def fd_t_token():
    if request.method == 'POST':
        token = request.form.get('token', 0)
        date = request.form.get('date', 0)

        #if date:
        print(date)
        #numb = request.form.get('numb', 0)
        if token == 'zhimakaimen':
            return 'Welcome to pass the test'
        else:
            return 'Identity verification failed'
    if request.method == 'GET':
        date = request.args.get('date', 0)
        #numb = request.args.get('numb', 0)
        #total = numa + numb
        print(date)
        return jsonify({'count':date})




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    