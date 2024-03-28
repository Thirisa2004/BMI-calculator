from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    # Calculate BMI
    bmi = weight / (height ** 2)

    return render_template('result.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
