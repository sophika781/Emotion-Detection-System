from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app= Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyse= request.args.get("textToAnalyze")
    response= emotion_detector(text_to_analyse)
    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"
    return str(f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']},  'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port= 5000)

