from flask import Flask, jsonify, request

import json
app = Flask(__name__)

@app.route("/<id>", methods=['GET'])
def usuario(id):
    return jsonify({'Usuario':id})

if __name__=="__main__":
    app.run(debug=True)