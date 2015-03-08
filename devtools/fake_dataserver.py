"""
A fake time series data server used during development to serve up JSON
for live updating plot rendering in the browser. The test datafile has
25000 points and cycles through this entire series every 60 minutes.

Examples
--------
>>> python fake_dataserver.py
>>> import requests; requests.get('http://127.0.0.1:5000/10').content

"""

from datetime import datetime
from flask import Flask, jsonify
app = Flask(__name__)

# Open local datafile (omit the standard error column)
with open ("time_val_error_data.dat","r") as datafile:
    lines = datafile.readlines()
    (t, v) = zip(*[(float(l.split()[0]), float(l.split()[1])) for l in lines])

@app.route("/", defaults={'points': 100})
@app.route("/<int:points>", methods=["GET"])
def get_data(points):
    now = datetime.now()
    fraction=int(len(t)*(now.minute+(now.second/60.0))/60.0)
    t_slice = t[fraction:fraction+points]
    v_slice = v[fraction:fraction+points]
    ts = {'time': [t_slice],
          'value': [v_slice]}
    return jsonify({'ts': ts})

if __name__ == "__main__":
    app.run(port=5000)
