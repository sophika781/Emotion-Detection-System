from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        dominant_emotion1= emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(dominant_emotion1, "joy") 

        dominant_emotion2= emotion_detector("I am really mad about this")['dominant_emotion'] 
        self.assertEqual(dominant_emotion2, "anger") 

        dominant_emotion3= emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'] 
        self.assertEqual(dominant_emotion3, "disgust") 

        dominant_emotion4= emotion_detector("I am so sad about this")['dominant_emotion'] 
        self.assertEqual(dominant_emotion4, "sadness") 

        dominant_emotion5= emotion_detector("I am really afraid that this will happen")['dominant_emotion'] 
        self.assertEqual(dominant_emotion5, "fear") 

unittest.main()