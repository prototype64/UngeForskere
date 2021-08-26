from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

model = load_model('model.h5')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        reshaped = np.reshape(np.array(data), (1, 28, 28, 1))
        print("reshaped shape:", reshaped.shape)

        # print("data is " + format(reshaped))
        prediction = model.predict(reshaped)
        print(prediction)
        return jsonify({"predictions": prediction.tolist()[0]})
    
    return "Invalid request type"

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == "__main__":
    app.run(debug=True)