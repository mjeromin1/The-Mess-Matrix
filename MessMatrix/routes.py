from flask import render_template, url_for, flash, request, redirect
from MessMatrix.forms import LoginForm
from MessMatrix import app
import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = ''
answer = ''
num = 1
len_of_chars = 0
accounts = [
        {
            'username': 'Skyler',
            'password': 'NOPE'
        },
        {
            'username':'Mike',
            'password':'Mount'
        },
        {
            'username':'Molly',
            'password':'Teee'
        },
        {
            'username':'Ebraheem',
            'password':'Mount'
        }
]



@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/MessMatrix", methods=['GET', 'POST'])
def MM():
    global password
    global answer
    global num
    if request.method == 'POST':
        if request.form['submit_button'] == 'Yes' and answer == 'yes':
            if len(password) != 1:
                num += 1
                password = password[1:]
                answer, matrix = MessMatrix(password)
                return render_template('MessMatrix.html', matrix=matrix, num=num)
            else:
                flash('Correct Credentials!')
                return redirect(url_for('loginpage'))
        elif request.form['submit_button'] == 'No' and answer == 'no':
            answer, matrix = MessMatrix(password)
            return render_template('MessMatrix.html', matrix=matrix,num=num)
    elif request.method == 'GET':
        answer, matrix = MessMatrix(password)
        return render_template('MessMatrix.html', matrix=matrix, num=num)

@app.route("/loginpage", methods=['GET', 'POST'])
def loginpage():
    form = LoginForm()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Normal Login':
            for account in accounts:
                if account['username'] == form.username.data and account['password'] == form.password.data:
                    flash('Correct Credentials!')
                    return render_template('loginpage.html', form=form)
            flash('Incorrect Credentials!')
            return render_template('loginpage.html', form=form)
        elif request.form['submit_button'] == 'Matrix Login':
            for account in accounts:
                if account['username'] == form.username.data:
                    global password
                    global len_of_chars
                    global chars
                    global num
                    num = 1
                    password = account['password']
                    len_of_chars = len(chars) - len(password) - 1
                    return redirect(url_for('MM'))
            flash('Incorrect Credentials!')
            return render_template('loginpage.html', form=form)
    elif request.method == 'GET':
        return render_template('loginpage.html', form=form)

def MessMatrix(password):
    global chars
    global len_of_chars
    for x in password:
        if x in chars:
            chars.remove(x)  # remove all password chars
    print(chars)
    rnum = random.randint(0,1)
    list1 = []
    list2 = []
    list3 = []
    print(len_of_chars)
    for x in range(0, 3):
        list1.append(chars[random.randint(0, len_of_chars)])
    for x in range(0, 3):
        list2.append(chars[random.randint(0, len_of_chars)])
    for x in range(0, 3):
        list3.append(chars[random.randint(0, len_of_chars)])
    if rnum == 1:
        print(f'Password: {password}')
        listrnum = random.randint(0,2)
        if listrnum == 0:
            list1[random.randint(0,2)] = password[0]
        elif listrnum == 1:
            list2[random.randint(0,2)] = password[0]
        elif listrnum == 2:
            list3[random.randint(0,2)] = password[0]
        return 'yes', [list1,list2,list3]
    elif rnum == 0:
        return 'no', [list1,list2,list3]
