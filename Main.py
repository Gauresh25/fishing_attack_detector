from flask import Flask, render_template, request
from API import get_prediction

app = Flask(__name__)

model_path = r"C:\Other files\GitHub\fishing_attack_detector\models\Malicious_URL_Prediction.h5"

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    url = ""

    if request.method == 'POST':
        url = request.form['url']
        print(url)
        prediction_result = get_prediction(url, model_path)
        print(prediction_result)

    return render_template('index.html', prediction=prediction_result, url=url)

if __name__ == '__main__':
    app.run(debug=True)

#
#
# from API import get_prediction
#
# # path to trained model
# model_path = r"C:\Users\DELL\PycharmProjects\pythonProject\Phishing-Attack-Domain-Detection\models\Malicious_URL_Prediction.h5"
#
# # input url
# # url = "https://www.google.com"
# url="https://www.youtube.com/watch?v=0nZ5hNDs3U8&list=RDz1QDVL_IxI8&index=2"
# # url="http://www.onlinesbi.digital"
# # url="http://google.com-redirect@valimail.com"
#
# # returns probability of url being malicious
# prediction = get_prediction(url,model_path)
# print(prediction)
#
#
