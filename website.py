import flask

app = flask.Flask('housing_prices')


@app.route('/')
def foo():
    return flask.render_template('map1.html')


if __name__ == '__main__':
    app.run(debug=True)
