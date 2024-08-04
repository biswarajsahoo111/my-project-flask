from flask import Flask, jsonify
import requests

app = Flask(__name__)

# List of URLs to ping
urls = ['https://en.wikipedia.org', 'https://www.google.com']

@app.route('/ping-urls', methods=['GET'])
def ping_urls():
    results = {}

    for url in urls:
        try:
            response = requests.get(url)
            results[url] = response.status_code == 200
        except requests.RequestException:
            results[url] = False

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

