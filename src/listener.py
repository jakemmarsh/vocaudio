import os
import speech_recognition as sr
from media_controls import MediaControls

class Listener():
  def __init__(self, google_key):
    self.google_key = google_key
    self.r = sr.Recognizer()
    self.m = sr.Microphone()
    self.controls = MediaControls()

  def __take_action(self, recognizer, audio):
    print "inside take_action"

    try:
      phrase = recognizer.recognize_google(audio, key = self.google_key)

      if phrase == 'volume up' or phrase == 'sound up':
        self.controls.sound_up()
      elif phrase == 'volume down' or phrase == 'sound down':
        self.controls.sound_down()

      print("Google Speech Recognition thinks you said " + phrase)
    except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
      os.system("say 'That command was not recognized.'")
    except sr.RequestError:
      print("Could not request results from Google Speech Recognition service")
      os.system("say 'Error requesting results from Google Speech Recognition.'")

  def run(self):
    self.__stop_listening = self.r.listen_in_background(self.m, self.__take_action)

  def stop(self):
    try:
      self.__stop_listening()
    except:
      print("Not currently listening, will exit.")