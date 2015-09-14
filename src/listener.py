import os
import speech_recognition as sr
from media_controls import MediaControls

class Listener():
  def __init__(self, google_key):
    self.google_key = google_key
    self.r = sr.Recognizer()
    self.m = sr.Microphone()
    self.controls = MediaControls()
    self.commands = {
      'volume up': self.controls.volume_up,
      'sound up': self.controls.volume_down,
      'volume max': self.controls.volume_max,
      'sound max': self.controls.volume_max,
      'volume down': self.controls.volume_down,
      'sound down': self.controls.volume_down,
      'mute': self.controls.mute,
      'volume off': self.controls.mute,
      'sound off': self.controls.mute,
      'play': self.controls.play,
      'pause': self.controls.pause,
      'skip': self.controls.next,
      'next': self.controls.next,
      'previous': self.controls.previous,
      'last': self.controls.previous,
      'rewind': self.controls.rewind,
      'back': self.controls.rewind,
      'forward': self.controls.fast_forward,
      'fast forward': self.controls.fast_forward
    }

  def __take_action(self, recognizer, audio):
    print "inside take_action"

    try:
      phrase = recognizer.recognize_google(audio, key = self.google_key)

      if phrase in self.commands:
        print "phrase does map to a command, about to execute"
        self.commands[phrase]()

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
      print("\nNot currently listening, will exit.\n")