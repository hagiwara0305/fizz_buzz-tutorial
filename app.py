from bottle import route, run, template, post, request

# indexページ
@route('/')
def index():
    return template('index.html', items=getItems())

@post('/')
def item_post():
    loop_value = request.forms.get('loopvalue')
    print(loop_value)
    return template('index.html', items=getItems(int(loop_value)))

# fizzbuzzを返す
def getItems(value=100):
    items = []

    for n in range(1, value + 1):
        if n % 3 == 0 and n % 5 == 0:
            items.append("FizzBuzz")
        elif n % 3 == 0:
            items.append("Fizz")
        elif n % 5 == 0:
            items.append("Buzz")
        else:
            items.append(n)
    return items

# webサーバ実行
run(host='localhost', port=8080, debug=True, reloader=True)