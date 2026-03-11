from flask import Flask, render_template, redirect, url_for
import requests
import time
from datetime import datetime

app = Flask(__name__)


db_runs = []
run_counter = 1

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', runs=db_runs)


@app.route('/run')
def trigger_run():
    global run_counter
    

    api_url = "https://api.agify.io?name=michael"
    
    start_time = time.time()
    passed = 0
    failed = 0
    
    try:
     
        response = requests.get(api_url, timeout=3)
        latency = int((time.time() - start_time) * 1000)
        

        if response.status_code == 200:
            passed += 1
        else:
            failed += 1
            
       
        try:
            data = response.json()
            passed += 1
        except ValueError:
            failed += 1
            
        status = "success" if failed == 0 else "warning"
        
    except requests.exceptions.RequestException:
        
        latency = int((time.time() - start_time) * 1000)
        failed = 2
        status = "danger"
        

    new_run = {
        "id": run_counter,
        "timestamp": datetime.now().strftime("%d %b %Y - %H:%M:%S"),
        "api": "Agify",
        "passed": passed,
        "failed": failed,
        "latency_avg_ms": latency,
        "status": status
    }
    

    db_runs.insert(0, new_run)
    run_counter += 1
    
   
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
