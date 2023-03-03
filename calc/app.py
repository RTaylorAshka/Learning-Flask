from flask import Flask, request
from operations import add, mult, sub, div

app = Flask(__name__)


# @app.route('/add')
# def show_calc_homepage():
#     html = """
#     <h1> 'Calculator!' </h1>
#     <form> 
#         <input type = 'number' placeholder = 'a' name = 'a' required>
#         <input type = 'number' placeholder = 'b' name = 'b' required>
#         <br/>
#         <button type = 'submit'>submit</button>

#     </form>


#     """
#     return html

@app.route(f'/add')
def cal_add():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f'{add(a,b)}'

@app.route(f'/sub')
def cal_sub():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f'{sub(a,b)}'


@app.route(f'/mult')
def cal_mult():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f'{mult(a,b)}'


@app.route(f'/div')
def cal_div():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f'{div(a,b)}'


op_convert = {
    'add' : add,
    'sub' : sub,
    'mult' : mult,
    'div' : div
}


@app.route(f'/math/<op>')
def calculate(op):
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f'{op_convert[op](a,b)}'