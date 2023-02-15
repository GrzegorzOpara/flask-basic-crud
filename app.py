# app.py

# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import auth, credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('serviceAccountKey.json')
default_app = initialize_app(cred)
db = firestore.client()
collection_ref = db.collection('profiles')

def getUidFromToken(token):
    decoded_token = auth.verify_id_token(token)
    return decoded_token['uid']

@app.route('/api/v1/', methods=['POST'])
def create():
    try:
        document_id = getUidFromToken(request.json['token'])
        collection_ref.document(document_id).set({'city': request.json['city']})
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/v1/', methods=['GET'])
def read():
    try:
        document_id = getUidFromToken(request.json['token'])
        profile = collection_ref.document(document_id).get()
        return jsonify(profile.to_dict()), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
