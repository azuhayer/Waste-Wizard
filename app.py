from flask import Flask, render_template

app = Flask(__name__, template_folder='src')

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About Us page
@app.route('/about')
def about():
    return render_template('AboutUs.html')

if __name__ == '__main__':
    app.run()