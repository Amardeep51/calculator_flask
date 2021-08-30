#importing necessary modules

from flask import Flask, render_template, request
import calculator
from calculator import add,sub,mul,div,mod

# Creating our Flask Instance
Flask_App = Flask(__name__,template_folder='templates')

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])


def operation_result():
    """Route where we send calculator form input"""


    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']



    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operation on webpage is addition
        if operation == "+":
            result=calculator.add(input1,input2)
        elif operation == "-":
            result=calculator.sub(input1,input2)
        elif operation=="*":
            result=calculator.mul(input1,input2)
        elif operation == "/":
            if input2==0:
                raise ZeroDivisionError
                print(" You can't perform this")
            result=calculator.div(input1,input2)


        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            calculation_success=False,
            result="Bad Input"
        )


if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run(host="0.0.0.0", port=5000)
