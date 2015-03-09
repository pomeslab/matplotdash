"""
A fake time series data server used during development to serve up JSON
for live updating plot rendering in the browser. The test datafile has
25000 points and cycles through this entire series every 60 minutes.

Examples
--------
>>> python fake_dataserver.py
>>> import requests; requests.get('http://127.0.0.1:5000/ts/10').content

"""

from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask import make_response, request, current_app
from functools import update_wrapper
app = Flask(__name__)
points_per_hour = 6000

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

# Open local datafile (omit the standard error column)
with open ("time_val_error_data.dat","r") as datafile:
    lines = datafile.readlines()[:points_per_hour]
    (t, v) = zip(*[(float(l.split()[0]), float(l.split()[1])) for l in lines])

@app.route("/ts/", defaults={'points': 100})
@app.route("/ts/<int:points>", methods=["GET"])
@crossdomain(origin='*')
def get_data(points):
    now = datetime.now()
    fraction=int(len(t)*(now.minute+(now.second/60.0))/60.0)
    ts = {'time': range(points),
          'value': v[fraction:fraction+points]}
    #ts = {'time': t[fraction:fraction+points],
    #      'value': v[fraction:fraction+points]}
    return jsonify({'ts': ts})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
