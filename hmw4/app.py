from flask import Flask
from flask import render_template
from datafoo import get_data
# import json
# import requests
# URL = 'http://stash.compjour.org/samples/cpsc/recalls201604.json'

# def get_data():
#     resp = requests.get(URL)
#     datarows = json.loads(resp.text)
#     return datarows

app = Flask(__name__)
recalls_data = get_data()

@app.route("/")
def homepage():
    # datarows = get_data()
    # htmlstr = "<h1>Hello world!</h1>"
    # htmlstr += "<p>There have been {num} recalls</p>".format(num=len(datarows))
    # for d in datarows:
    #     htmlstr += """<p><a href="{url}">{title}</a></p>""".format(title=d['Title'], url=d['URL'])
    # return htmlstr
    return render_template('homepage.html', recalls=recalls_data, recalls_count=len(recalls_data))

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)