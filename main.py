from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def announce():
    if request.method == 'POST':
        pass
    # show the quick info about the upcoming site
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()