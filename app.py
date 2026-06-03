from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello():
    return '''
    <html>
    <head><title>Hello World</title></head>
    <body style="font-family:Arial;text-align:center;margin-top:100px">
        <h1 style="color:#4A90D9">Hello, World!</h1>
        <p>Deployed with Jenkins CI/CD Pipeline</p>
        <p style="color:red;font-size:14px;margin-top:30px;">
            Made by Abdallah Ahmed
        </p>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)