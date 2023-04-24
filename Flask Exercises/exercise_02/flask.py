from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/calculate')
def calc(number=None):
    # if user navigates to calculate page directly there will be no requests
    if len(request.args)==0:
        return render_template('calculate.html')
    number = request.args['number']
    # user's input value will be set as even or odd
    try:
        if int(number)%2==0:
            msg='even'
        elif int(number)%2!=0:
            msg='odd'
    # user must type in a real value         
    except:
        msg='not an integer!'
    return render_template('calculate.html', num=number, name=msg)

if __name__ == "__main__":
    app.run()