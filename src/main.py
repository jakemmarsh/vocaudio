import os, ConfigParser, atexit
from listener import Listener

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'settings.cfg'))

if __name__ == '__main__':
  listener = Listener(google_key = config.get('google', 'key'))
  listener.run()
  atexit.register(listener.stop)
