# -*- coding: utf-8 -*-
from bottle import route, run, static_file, template, request, HTTPResponse
import json

@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./dist/static')

@route('/app')
def app():
    return static_file('index.html', root='./dist')

@route('/bot')
def bot():
    return template('''
    <!DOCTYPE html>
<html>
  <head>
    <title>ファイナンシャル・アドバイザーデモ</title>
    <link rel='stylesheet' href='/stylesheets/style.css' />
  </head>
  <body>
    <h1>ファイナンシャル・アドバイザーデモ</h1>

<iframe
    width="350"
    height="500"
    src="https://console.dialogflow.com/api-client/demo/embedded/93173144-ecfd-42ac-a300-3afb166cbaca">
</iframe>
  </body>
</html>
    ''')

@route('/dialogflow', method="POST")
def dialogflow():
    # print('Dialogflow Request body: ' +  json.dumps(request.body))
    body = {'speech': 'hello world', 'displayText': 'hello world'}
    print(json.dumps(body))
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

run(host='localhost', port=3000)
