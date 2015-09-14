vocaudio
========

Trigger OSX media player controls with voice actions.

### Getting up and running

1. Clone this repo: `git clone https://github.com/jakemmarsh/vocaudio.git`
2. `brew install portaudio`
3. `sudo pip install --allow-external pyaudio --allow-unverified pyaudio pyaudio`
4. Install remaining dependencies: `sudo python setup.py install`
5. Run: `python src/main.py`

### Sample configuration file

Currently, this project uses a `settings.cfg` file to store and read the Google Speech Recognition API key. This file should be created in the root directory, and uses the following format:

```
[google]
key : <YOUR_KEY_HERE>
```

### Possible voice commands

This project provides a handful of voice commands by default. When these voice commands are recognized, the corresponding media button presses are simulated. These commands are:

- **Increase volume:** responds to commands `volume up` and `sound up`
- **Decrease volume:** responds to commands `volume down` and `sound down`
