from flask import Flask, request, jsonify, render_template
import util
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/get_location_names',methods = ['GET'])
def get_location_names():
    response = jsonify({
        'location':util.get_location_names()
    })