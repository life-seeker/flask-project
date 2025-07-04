from flask import Flask ,request,render_template,redirect
app = Flask(__name__) 
@app.route('/home')
def home():
    return "hello<h1>what</h1> <a href='https://google.com'> fashion </a>"

@app.route('/<name>')
def home2(name):
    return f"{name}nike of page,image" 
@app.route('/uploadpannu')
def home4():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def home3():
    file=request.files['file']
    file.save(f'uploads/{file.filename}')
    return redirect('/uploadpannu')

if __name__=="__main__":
   app.run(host='0.0.0.0', port=5555, debug=True)
   
   
   