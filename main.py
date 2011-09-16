from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def announce():
    if request.method == 'POST':
        pass
    return render_template("index.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")
    
if __name__ == '__main__':
    app.debug = True
    app.run()