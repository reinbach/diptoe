import datetime
import os
import re

from flask import Flask, render_template, request, flash, session
app = Flask(__name__)
app.secret_key = "\xdchU\xe8\xe1\x06\xd3\xf6\xa5-\xae\x08Fpn\x1fq[\xef\xfdQ\xad*e"

#---------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def announce():
    error = None
    if request.method == 'POST':
        if not validate_email_address(request.form.get('email', '')):
            error = 'Invalid Email Address'
        else:
            # store email address
            # once saved store email address in session and if same email address
            # ignore and act like we have signed user up again
            try:
                if session.get('email', '') != request.form.get('email'):
                    filepath, filename = os.path.split(os.path.abspath(__file__))
                    app.logger.debug("%s: %s" % (filepath, filename))
                    fp = open("%s/data/emails.txt" % filepath, "a")
                    fp.write("%s|%s\n" % (datetime.datetime.now(), request.form.get('email')))
                    fp.close()
                    session['email'] = request.form.get('email')
                flash("Woohoo, we got your Sign Up", "success")
            except Exception, e:
                app.logger.error(
                    "Failed to record email address (%s)): %s" % (
                        request.form.get('email'),
                        e
                    )
                )
                flash("Yikes, there was an issure recording your Sign Up", "error")
    return render_template("index.html", error=error)

#---------------------------------------------------------------------------
@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

#---------------------------------------------------------------------------
def validate_email_address(email):
    email_re = re.compile(
        # dot-atom
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
        # quoted-string
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'
        # domain
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)
    if not email_re.search(email):
        return False
    return True
    
if __name__ == '__main__':
    app.debug = True
    app.run()