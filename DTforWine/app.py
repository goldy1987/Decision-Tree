# required imports
from flask import Flask, request, render_template
from flask_cors import CORS
import pickle


# initiatting app
app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['GET'])
def homepage():
    return render_template('index.html')

@app.route('/predict', methods = ['POST','GET'])
def predict():
    if request.method ==  'POST':
        try:
            # retreiving feature values from index page
            fixed_acidity = request.form['fixed_acidity']
            volatile_acidity = request.form['volatile_acidity']
            citric_acid = request.form['citric_acid']
            residual_sugar = request.form['residual_sugar']
            chlorides = request.form['chlorides']
            free_sulphur_dioxide = request.form['free_sulphur_dioxide']
            total_sulphur_dioxide = request.form['total_sulphur_dioxide']
            density = request.form['density']
            pH = request.form['pH']
            sulphates = request.form['sulphates']
            alcohol = request.form['alcohol']

            # loading DT model
            filename = 'DTmodelforPred.sav'
            load_model = pickle.load(open(filename,'rb'))

            # predicting quality using DT model
            data=[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,
                  free_sulphur_dioxide,total_sulphur_dioxide,density,pH,sulphates,alcohol]
            prediction = load_model.predict([data])

            # displaying prediction
            if prediction==3:
                return render_template('3.html')
            elif prediction ==4:
                return render_template('4.html')
            elif prediction == 5:
                return render_template('5.html')
            elif prediction == 6:
                return render_template('6.html')
            elif prediction == 7:
                return render_template('7.html')
            else:
                return render_template('8.html')

        except Exception as e:
            print('Exception message is: ', e)
            return'Something is Wrong'
    else:
        return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)
