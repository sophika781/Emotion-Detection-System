'''
    Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app= Flask(__name__)

@app.route("/emotionDetector")
def emotiondetector():
    '''
        This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions, their scores and the dominant emotion.
    '''
    text_to_analyse= request.args.get("textToAnalyze")
    response= emotion_detector(text_to_analyse)
    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"
    emotions = {key: response[key] for key in list(response)[:5]}
    emotions= str(emotions)
    emotions= emotions[1:-1]
    dominant= response['dominant_emotion']
    emotions_statement= f"For the given statement, the system response is {emotions}."
    dominant_statement= f" The dominant emotion is {dominant}"
    return emotions_statement + dominant_statement

@app.route("/")
def render_index_page():
    '''
        This function initiates the rendering of the main application
        page over the Flask channel        
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port= 5000)
