from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    #app.run(port=33507)
    app.run(debug=True)
