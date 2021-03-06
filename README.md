vocaudio
========

Trigger OSX media player controls with voice actions. Speech recognition is carried out using the [SpeechRecognition](https://github.com/Uberi/speech_recognition) library.

### Getting up and running

1. Clone this repo: `git clone https://github.com/jakemmarsh/vocaudio.git`
2. `brew install flac` (assuming you have [homebrew](http://brew.sh/) installed)
3. `brew install portaudio`
4. `sudo pip install --allow-external pyaudio --allow-unverified pyaudio pyaudio`
5. Install remaining dependencies: `sudo python setup.py install`
6. Run: `python src/main.py`

---

### Sample configuration file

Currently, this project uses a `settings.cfg` file to store and read the Google Speech Recognition API key. This file should be created in the root directory, and uses the following format:

```
[google]
key : <YOUR_KEY_HERE>
```

---

### Possible voice commands

This project provides a handful of voice commands by default. When these voice commands are recognized, the corresponding media button presses are simulated. These commands are:

- **Increase volume:** responds to commands `volume up` and `sound up`
- **Decrease volume:** responds to commands `volume down` and `sound down`
- **Max volume:** responds to commands `volume max`, `max volume`, and `sound max`
- **Mute:** responds to commands `mute`, `volume off` and `sound off`
- **Play:** responds to command `play`
- **Pause:** responds to command `pause`
- **Next track:** responds to commands `next` and `skip`
- **Previous track:** responds to commands `previous` and `last`
- **Rewind:** responds to commands `rewind` and `back`
- **Fast-forward:** responds to commands `forward` and `fast forward`
