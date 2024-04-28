import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory # type: ignore
from werkzeug.utils import secure_filename # type: ignore

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = { 'png', 'jpeg', 'jpg' }

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About Us page
@app.route('/about')
def about():
    return render_template('AboutUs.html')

@app.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template("index.html", uploaded_file=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg')
        return redirect(request.url)

@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.secret_key = "ladfhjkh"
    app.run()