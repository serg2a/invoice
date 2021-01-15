import flask

import persone

app = flask.Flask(__name__)
@app.route('/invoices/<name>', methods = ['GET'])
def invoic(name):
    page = flask.request.args.get('p')
    person = persone.Persones(name)

    if page:
        pop = person.web(int(page))
    else:
        page = 0
        pop = person.web(page)

    return str(pop)

if __name__ == '__main__':
    app.run()
