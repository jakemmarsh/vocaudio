from setuptools import setup

setup(
  name='vocaudio',

  version='0.0.1',

  description='Trigger OSX media player controls with voice actions.',

  url='https://github.com/jakemmarsh/vocaudio',

  author='Jake Marsh',
  author_email='jakemmarsh@gmail.com',

  license='MIT',

  keywords='voice control osx audio speech',

  install_requires = [
    'SpeechRecognition',
    'PyAudio',
    'pyobjc-framework-Quartz'
  ]
)