import requests, json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } } 
    response= requests.post(url, json=myobj, headers=headers)
    if response.status_code == 400:
        res= {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return res
    formatted_response= json.loads(response.text)
    
    emotions= formatted_response['emotionPredictions'][0]['emotion']
    anger_score= formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score= formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score= formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score= formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score= formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    dominant_emotion= ""
    for emotion, score in emotions.items():
        if score == max(emotions.values()):
            dominant_emotion= emotion
            break
    res= {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }
    return res