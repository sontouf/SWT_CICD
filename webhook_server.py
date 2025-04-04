# webhook_server.py

from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    repo_name = data['repository']['name']

    subprocess.call(["/bin/bash", "update_submodules.sh"])

    if repo_name == "SWT_TeamA":
        subprocess.call(["/bin/bash", "run_teamA.sh"])
    elif repo_name == "SWT_TeamB":
        subprocess.call(["/bin/bash", "run_teamB.sh"])
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
