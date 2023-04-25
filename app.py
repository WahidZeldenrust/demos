from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        return render_template('output.html', text=text)
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
