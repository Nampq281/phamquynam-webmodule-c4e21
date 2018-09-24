from flask import Flask

app = Flask(__name__)
content = [
"Severely underweight",
"Underweight",
"Normal",
"Overweight",
"Obese"
]
@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
    bmi = (w*2.20462)/((h*0.393701)**2)*703
    post_1= "Your bmi: " + str(bmi)
    if bmi <16:
        return post_1 +" "+ content[0]
    elif 16 <= bmi < 18.5:
        return post_1 +" "+ content[1]
    elif 18.5 <= bmi < 25:
        return post_1 +" "+ content[2]
    elif 25 <= bmi < 30:
        return post_1 +" "+ content[3]
    elif bmi > 30:
        return post_1 +" "+ content[4]
print('running app')
if __name__ == "__main__":
    app.run(debug=True)