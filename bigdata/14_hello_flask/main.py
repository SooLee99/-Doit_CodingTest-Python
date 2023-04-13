rom flask import Flask, render_template,request

app = Flask("Hello Falsk")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/search")
def search():
    print(request.args)
    keyword = request.args.get('keyword')
    return render_template('search.html',kw = keyword)

app.run("0.0.0.0")