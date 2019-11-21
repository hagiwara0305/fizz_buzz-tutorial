from bottle import route, run, template, post, request
from fizz_buzz import Controller

fizz_buzz_object = Controller()

# indexページ
@route('/')
def index():
    return template('index.html', items=fizz_buzz_object.get_items())

@post('/')
def item_post():
    loop_value = request.forms.get('loopvalue')
    print(loop_value)
    try:
        return template('index.html', items=fizz_buzz_object.get_items(int(loop_value)))
    except:
        return "<p>500 Error</p><a href="">Index前の画面に戻る</a>"

# webサーバ実行
run(host='localhost', port=8080, debug=True, reloader=True)