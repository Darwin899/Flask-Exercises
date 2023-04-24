from flask import Flask, render_template 
# Current time
import datetime 
# Current date
import calendar 
# Current TimeZone 
import pytz 

#Create a flask app
test = Flask(__name__)

#routing at '/'
@test.route('/')
def index():
    #Zone based time
    current_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    ctime = current_time.strftime("%B %d %Y %H:%M:%S")
    return render_template('index.html', ctime = calendar.day_name[current_time.weekday()] + ', ' +ctime)

if __name__ == '__main__':
    test.run()