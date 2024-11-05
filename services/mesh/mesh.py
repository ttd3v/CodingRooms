from flask import Flask,request
import requests as req
import re as regex
## creating types
class db_run_command:
    command : str = ''
    args : tuple = ()
    def __init__(self,command : str,args : tuple) -> None:
        self.command = command
        self.args = args
        pass
class db_run_writen(db_run_command):
    def __init__(self,command : str,args : tuple) -> None:
        self.command = command
        self.args = args
        pass

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    data = request.data
    if 'email' in data and 'password' in data:
        post_request = req.post(
            'http://localhost:5100/make_login',
            data={'email' : data['email'], 'password' : data['password']},
            headers={'Content-Type':'application/json'}
        )
        if post_request.ok:
            return post_request.json()
        else:
            return {}
    else:
        return {}
@app.route('/db/<where:str>')
def db_run_command(where):
    if not where or not where in ['command','writen']:
        return {}
    data = request.data
    if 'command' in data and 'args' in data:
        post_request = req.post(
            'http://localhost:5300/command',
            data={'command' : data['command'], 'args' : data['args'], 'mesh_key':'my_db'},
            headers={'Content-Type':'application/json'}
        )
        if post_request.ok:
            return post_request.json()
        else:
            return {}
    else:
        return {}
    
@app.route('/check_email_exists')
def check_email_exists():
    fail_response = {'email_exists',False}
    if 'email' in request.data:
        email = request.data['email']
        if regex.match(r"^\S+@\S+\.\S+$",email):
            print('pattern found')
            request_post = req.post(
                'http://localhost:5300/check_email_exists',
                {'email':email},
                headers={'Content-Type':'application/json'}
            )
            if request_post.ok:
                return request_post.json()
            else:
                return fail_response
        else:
            return fail_response
    else:
        return fail_response
    
if __name__ == "__main__":
    app.run(port=5000)