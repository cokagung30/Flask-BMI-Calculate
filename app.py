from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weight = 0
    height = 0
    bmi = 0

    if request.method == 'POST':
        if 'height' in request.form:
            height = int(request.form.get('height'))
            if height != 0:
                height = height / 100

        if 'weight' in request.form:
            weight = int(request.form.get('weight'))
            if weight != 0:
                bmi = math.ceil(weight / (height * height))

    print(bmi)
    return render_template("index.html", bmi=bmi)

app.run()