from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/dashboard')
def dashboard():
   
    
    mock_runs = [
        {
            "id": 3,
            "timestamp": "11 Mars 2026 - 15:25",
            "api": "Agify",
            "passed": 6,
            "failed": 0,
            "latency_avg_ms": 145,
            "status": "success"
        },
        {
            "id": 2,
            "timestamp": "11 Mars 2026 - 15:20",
            "api": "Agify",
            "passed": 5,
            "failed": 1,
            "latency_avg_ms": 520,
            "status": "warning"
        },
        {
            "id": 1,
            "timestamp": "11 Mars 2026 - 15:15",
            "api": "Agify",
            "passed": 6,
            "failed": 0,
            "latency_avg_ms": 130,
            "status": "success"
        }
    ]
    
    return render_template('dashboard.html', runs=mock_runs)

if __name__ == '__main__':
    app.run(debug=True)
