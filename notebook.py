from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity
contact_dict = {}

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    number = request.form['number']
    gmail = request.form['gmail']
    contact_dict[name] = f"{number} | {gmail}"
    return redirect(url_for('index'))

@app.route('/show')
def show_contacts():
    return '<br>'.join([f"{name} | {details}" for name, details in contact_dict.items()])

if __name__ == '__main__':
    app.run(debug=True)
