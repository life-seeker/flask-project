from flask import Flask ,request,render_template,redirect,url_for, send_from_directory,abort, url_for, jsonify
import os
app = Flask(__name__) 
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/home')
def home():
    return "hello<h1>what</h1> <a href='https://google.com'> fashion </a>"

#@app.route('/<name>')
#def home2(name):
    #return f"{name}nike of page,image" 
@app.route('/uploadpannu')
def home4():
    return render_template('index.html')
@app.route('/show/<filename>')
def show_file(filename):
    return render_template("show.html", filename=filename)
@app.route('/upload', methods=['POST'])
def home3():
    file=request.files['file']
    file.save(f'static/uploads/{file.filename}')
    #return redirect('/uploadpannu')
    return redirect("/album")
@app.route('/album')
def gallery():
    print("input",app.config['UPLOAD_FOLDER'])
    photos = os.listdir(app.config['UPLOAD_FOLDER'])
    print("photos variable list",photos)
    photos = [p for p in photos if p.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
    return render_template("gallery.html", photos=photos)
@app.route('/download/<filename>')
def download_file(filename):
    safe_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(safe_path):
      abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"{filename} deleted"}), 200
    else:
        return jsonify({"error": "File not found"}), 404
if __name__=="__main__":
   app.run(host='0.0.0.0', port=5555, debug=True)
   
   
   