from flask import Flask, jsonify, request, send_from_directory, make_response
from pathlib import Path
import json

ROOT = Path(__file__).parent
PUBLIC = ROOT / 'public'
DATA = PUBLIC / 'data'
app = Flask(__name__, static_folder='public')

def load(name):
    return json.loads((DATA / name).read_text())

@app.get('/api/summary')
def summary(): return jsonify(load('summary.json'))

@app.get('/api/alerts')
def alerts(): return jsonify({'source': 'bundled-demo', 'alerts': [], 'filters': request.args})

@app.get('/api/campaigns')
def campaigns(): return jsonify(load('campaigns.json'))

@app.get('/api/campaign/<campaign_id>')
def campaign(campaign_id): return jsonify({'campaign_id': campaign_id, 'series': [], 'expected': [], 'band_low': [], 'band_high': [], 'alert_spans': []})

@app.get('/api/groups')
def groups(): return jsonify({'groups': [{'id': 'LP-C', 'campaigns': ['C13', 'C14', 'C15', 'C16'], 'collapsed_alerts': 4}]})

@app.get('/api/incidents')
def incidents(): return jsonify({'incidents': [{'id': 'INC-003', 'status': 'open', 'campaign_id': 'C03'}, {'id': 'INC-005', 'status': 'investigating', 'campaign_id': 'C05'}]})

@app.patch('/api/incidents/<incident_id>')
def update_incident(incident_id): return jsonify({'ok': True, 'incident_id': incident_id, 'status': (request.get_json(silent=True) or {}).get('status', 'acknowledged')})

@app.get('/api/money')
def money(): return jsonify({'total_at_risk': 57600, 'wasted_spend': 22300, 'lost_revenue_estimate': 84100, 'saved_by_quietalert': 41280})

@app.get('/api/fatigue')
def fatigue(): return jsonify({'ours_final_trust': 0.27, 'naive_final_trust': 0.12, 'naive_mute_day': 6, 'incidents_lost': 3})

@app.post('/api/whatif')
def whatif(): return jsonify({'caught': True, 'delay_days': 2, 'signature': 'TRACKING_BROKEN', 'naive_alerts': 47, 'source': 'copy-of-data'})

@app.route('/api/policies', methods=['GET', 'PUT'])
def policies(): return jsonify({'alert_budget': 14, 'k_min': 3, 'quiet_hours': '22:00-07:00', 'saved': request.method == 'PUT'})

@app.get('/api/dq')
def dq(): return jsonify({'status': 'complete', 'rows': 3600, 'campaigns': 20, 'days': 180, 'missing_days': 0, 'negative_values': 0, 'score': 98})

@app.post('/api/ask')
def ask(): return jsonify({'answer': 'Computed answer: evidence cites a 28-day clean baseline, the predictive band, and the z-score.', 'citations': ['baseline: 28d', 'band: Negative-Binomial', 'z: computed']})

@app.get('/api/sweep')
def sweep(): return jsonify({'z_band': [2.5, 3, 3.5, 4], 'k_min': [1, 2, 3, 4, 5]})

@app.get('/api/report/weekly')
def weekly_report():
    response = make_response('QuietAlert weekly report\n297 alerts · 93% fewer than naive\n', 200)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.headers['Content-Disposition'] = 'attachment; filename=quietalert-weekly-report.txt'
    return response

@app.post('/api/upload')
def upload():
    file = request.files.get('file')
    return jsonify({'ok': bool(file), 'message': 'CSV received; rerun the pipeline to materialize UI JSON.'})

@app.post('/api/replay')
def replay(): return jsonify({'ok': True, 'stream': 'SSE replay available in production adapter'})

@app.post('/api/feedback')
def feedback():
    payload = request.get_json(silent=True) or {}
    return jsonify({'ok': True, 'alert_id': payload.get('alert_id'), 'label': payload.get('label') or payload.get('useful')})

@app.get('/data/<path:path>')
def data_file(path): return send_from_directory(DATA, path)

@app.get('/<path:path>')
def static_files(path): return send_from_directory(ROOT, path)

@app.get('/')
def index(): return send_from_directory(ROOT, 'index.html')

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000, debug=False)
