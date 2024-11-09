import os
from flask import Flask, request, jsonify , render_template
import util
app = Flask(__name__)


app = Flask(__name__, static_folder='../../ui/static', template_folder='../../ui/templates')

@app.route('/')
def home():
    return render_template('app.html')


@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")  #The browser will allow the frontend application to make requests to the backend.
    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("server starting >>")
    util.load_saved_artifacts()
    port = int(os.environ.get("PORT", 10000))  # Set default to 10000
    app.run(host='0.0.0.0', port=port)
