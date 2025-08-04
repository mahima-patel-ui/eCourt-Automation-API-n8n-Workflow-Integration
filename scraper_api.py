from flask import Flask, request, jsonify
from court_scraper import scrape_case_details  # 👈 your working function

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.get_json()
        cnr = data.get("cnr")

        if not cnr:
            return jsonify({"error": "CNR number missing"}), 400

        result = scrape_case_details(cnr)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
