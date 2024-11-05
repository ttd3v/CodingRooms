from flask import Flask,request
from Crypto.Hash import MD5
import json,requests
app = Flask(__name__)

@app.route('/make_login',methods=['POST'])
def make_login():
    if request.data:
        data = None
        try:
            data = json.loads(request.data)
        except Exception as err:
            print(err)
        finally:
            if not data:
                return {}
        if 'email' in data and 'password' in data:

            encryption_md5 = MD5.new()
            encryption_md5.update(str(data['password']).encode('utf-8'))
            hash_password = str(encryption_md5.hexdigest())
            request_post = requests.post(
                'http://localhost:5000/db/command',
                data={'command':'get_user','args':(data['email'],hash_password)},
                headers={'Content-Type':'application/json'}
            )
            if request_post.ok:
                user_data = request_post.json()
                print(user_data)
            else:
                return None
        else:
            return {}
    else:
        return {'msg':'failed','type':'E'}


@app.route('/make_register',methods=['POST'])
def make_register():
    data = request.data
    if 'email' in data and 'password' in data:
        request_post = requests.post(
            'http://localhost:5000/check_email_exists',
            data={'email':data['email']},
            headers={'Content-Type':'application/json'}
        )
        if 'email_exists' in request_post.json() and not request_post.json()['email_exists']:
            encryption_md5 = MD5.new()
            encryption_md5.update(str(data['password']).encode('utf-8'))
            hash_password = str(encryption_md5.hexdigest())
            request_post = requests.post(
                'http://localhost:5000/db/command',
                data={'command':'create_new_user','args':(data['email'],hash_password)},
                headers={'Content-Type':'application/json'}
            )
            if request_post.ok:
                return {'sucess':True}
            else:
                return {'sucess':False}
        else:
            return {}


if __name__ == "__main__":
    app.run(port=5100)