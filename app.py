from flask import Flask, render_template, request
import urllib.parse
import urllib.request
import json

app = Flask(__name__)

BASE_PATH = 'http://localhost:8983/solr/nba_data/select?'

@app.route('/', methods=["GET", "POST"])
def index():
    numresults = None
    results = None
    query_parts = []
    query = "*:*"
    rows = "1000000"

    if request.method == "POST":
        date = request.form.get("searchDate", "").strip()
        team = request.form.get("searchTeam", "").strip()
        quarter = request.form.get("searchQuarter", "").strip()

        if date:
            query_parts.append(f'Date:"{date}"')
        if team:
            query_parts.append(f'(HomeTeam:"{team}" OR AwayTeam:"{team}")')
        if quarter:
            query_parts.append(f'Quarter:{quarter}')  # Assuming Quarter is an integer field

        query = " AND ".join(query_parts) if query_parts else "*:*"
        solr_query_url = f"{BASE_PATH}{urllib.parse.urlencode({'q': query, 'wt': 'json', 'rows': rows})}"

        try:
            with urllib.request.urlopen(solr_query_url) as response:
                solr_response = json.load(response)
                numresults = solr_response['response']['numFound']
                # If you want to dynamically set rows based on numFound:
                # rows = solr_response['response']['numFound']
                results = solr_response['response']['docs']
        except Exception as e:
            print(f"Error fetching data from Solr: {e}")

    return render_template('index.html', numresults=numresults, results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
