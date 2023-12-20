from __future__ import annotations
from routes import routes
from flask import Flask
from firestore import get_instance, add_data_db, read_data_db
import os

app = Flask(__name__)
app.register_blueprint(routes)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cloud-computing-408517-b76998cb0fc6.json'
# os.environ['INSTANCE_CONNECTION_NAME'] = 'cloud-computing-408517:us-central1:cloud-testing'
# os.environ['DB_PORT'] = '3306'
# os.environ['DB_NAME'] = 'Testing'
# os.environ['DB_USER'] = 'samhit'
# os.environ['DB_PASS'] = 'samhit'
# os.environ['INSTANCE_HOST'] = '35.202.158.27'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5035)
