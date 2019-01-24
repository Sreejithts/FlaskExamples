from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    marks={'Maths':80,'C':70,'java':60}
    return render_template('table.html',marks=marks)



if __name__=="__main__":
    app.run(debug=True)
