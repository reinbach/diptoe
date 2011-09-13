from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def announce():
    if request.method == 'POST':
        pass
    # show the quick info about the upcoming site
    return "This piece of software is new and we want you to want it, real bad"

if __name__ == '__main__':
    app.debug = True
    app.run()