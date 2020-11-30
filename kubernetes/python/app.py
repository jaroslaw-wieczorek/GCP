import os
import socket
from datetime import datetime


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = f"Hello World from Jarosław Wieczorek <br>" \
    	f"Hostname: {socket.gethostname()} <br>" \
		f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} "
 	
    return data

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
