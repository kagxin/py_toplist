from flask import Flask, render_template, request, jsonify
from flask_site.utils.mongo import m

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/entry')
def entry():
    target = request.args.get('target', '糗事百科')
    page_size = request.args.get('page_size', 20)
    page_count = request.args.get('page', 1)

    data = m.entry.aggregate([{'$match': {'target': target}},
                              {"$project": {"_id": {"$toString": "$_id"}, 'target': 1, 'title': 1, 'rank': 1, 'url': 1,
                                            'release_date': {
                                                '$dateToString': {'format': "%Y-%m-%d %H:%M:%S",
                                                                  'date': "$release_date"}}}},
                              {"$sort": {"rank": 1}},
                              {"$limit": page_size},
                              {"$skip": (page_count - 1) * page_size}
                              ]
                             )
    return jsonify(list(data))


@app.route('/api/site')
def site():
    sites = ("糗事百科", "知乎", "v2ex", "虎扑", "微博", "微信", "GitHub", "segmentfault")
    return jsonify([{"_id": i, "name": name} for i, name in enumerate(sites)])


if __name__ == '__main__':
    app.run(debug=True)
