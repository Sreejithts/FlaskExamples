from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    name="abc"
    list1=[10,20,30]
    return render_template('tmp.html',name=name)
@app.route('/list')
def index1():
    list1=[10,20,30]
    return render_template('tmp.html',list1=list1)
@app.route('/tuple')
def index2():
    tuple1=(10,20,30)
    return render_template('tmp.html',tuple1=tuple1)


if __name__=="__main__":
    app.run(debug=True)
