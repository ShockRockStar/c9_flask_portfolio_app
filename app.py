from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	new_name=str(name) +" likes to eat mangos"
	return render_template('index.html', name=new_name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 1
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total *= int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)
	
conversion = {'in':[2.54,'cm'],'cm':[0.393701,'in'],'ft':[0.3048,'m'],'m':[3.28084,'ft'],'lb':[0.453592,'kg'],'kg':[2.20462,'lb']}

def convert(number,unit):
  return number * conversion[unit][0]

def find_bmi(weight,height): #in kg/m
  return weight/(height**2)

def bmi_calc():
  print('Do you use inches or centimeters?')
  unit = input('Enter "i" for inches or "c" for centimeters: ')
  if unit == "i":
    feet = int(input('Enter your height in feet: '))
    inches = int(input('And how many inches?'))
    height_m = convert(feet*12 + inches,'in') / 100
    pounds = int(input('Enter your weight in lbs: '))
    weight_kg = convert(pounds,'lb')
  if unit == "c":
    height_m = int(input('Enter your height in cm: ')) / 100
    weight_kg = int(input('Enter your weight in kgs: '))
  
  #print("Your height in m is: " + str(height_m))
  #print("Your weight in kg is: " + str(weight_kg))
  print("Your BMI is: " + str(find_bmi(weight_kg,height_m)))

bmi_calc()

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)
