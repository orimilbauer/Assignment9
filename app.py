from flask import Flask,render_template
from flask import request
# session is global veriable- relevent for all the pages
from flask import session
app = Flask(__name__)
app.secret_key='123'

@app.route('/',methods=['GET','POST'])
def hello_world():  # put application's code here
    users = {'user1': {'name': 'yossi', 'email': 'Yossi@gmail.com', 'phone': '054-73242332'},
             'user2': {'name': 'ori', 'email': 'ori@gmail.com', 'phone': '054-73242334'},
             'user3': {'name': 'shlomi', 'email': 'shlomi@gmail.com', 'phone': '054-74342332'},
             'user4': {'name': 'bar', 'email': 'bar@gmail.com', 'phone': '054-73243332'},
             'user5': {'name': 'yohi', 'email': 'yohi@gmail.com', 'phone': '054-73242532'}
             }
    if request.method == 'GET':
        if 'user_id' in request.args:
            if request.args.get('user_id') != '':
                uuid=request.args.get('user_id')
                for key in users:
                    if key==uuid:
                        name=users[key]['name']
                        email=users[key]['email']
                        phone=users[key]['phone']
                        return render_template('assignment9.html', user_name=name, email=email, phone=phone)
                return render_template('assignment9.html',not_find='not')
            return  render_template('assignment9.html',users_list=users)
        return render_template('assignment9.html')

    if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # this is the global veriable
            found = True
            if found:
                session['username'] = username
                return render_template('assignment9.html',signin='true')
            else:
                return  render_template('assignment9.html')



@app.route('/logout')
def logout_func():
    session['username']=''
    return render_template('/assignment9.html')

if __name__ == '__main__':
    app.run()
