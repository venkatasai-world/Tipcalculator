from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        bill = float(request.form['bill'])
        tip = int(request.form['tip'])
        people = int(request.form['people'])

        tip_percent = tip / 100
        total_tip = tip_percent * bill
        total_bill = total_tip + bill
        each_person_bill = round(total_bill / people, 2)

        return render_template("index.html", result=each_person_bill)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
