import Quartz

# NSEvent.h
NSSystemDefined = 14

# hidsystem/ev_keymap.h
NX_KEYTYPE_SOUND_UP = 0
NX_KEYTYPE_SOUND_DOWN = 1
NX_KEYTYPE_PLAY = 16
NX_KEYTYPE_NEXT = 17
NX_KEYTYPE_PREVIOUS = 18
NX_KEYTYPE_FAST = 19
NX_KEYTYPE_REWIND = 20

class MediaControls():
  def __press_key(self, key):
    # http://stackoverflow.com/questions/11045814/emulate-media-key-press-on-mac
    def do_key(down):
      ev = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
        NSSystemDefined, # type
        (0,0), # location
        0xa00 if down else 0xb00, # flags
        0, # timestamp
        0, # window
        0, # ctx
        8, # subtype
        (key << 16) | ((0xa if down else 0xb) << 8), # data1
        -1 # data2
      )
      cev = ev.CGEvent()
      Quartz.CGEventPost(0, cev)

    do_key(True)
    do_key(False)

  def volume_up(self):
    self.__press_key(NX_KEYTYPE_SOUND_UP)

  def volume_max(self):
    for i in range(15):
      self.volume_up()

  def volume_down(self):
    self.__press_key(NX_KEYTYPE_SOUND_DOWN)

  def mute(self):
    for i in range(15):
      self.volume_down()

  def play(self):
    self.__press_key(NX_KEYTYPE_PLAY)

  def pause(self):
    self.play()

  def next(self):
    self.__press_key(NX_KEYTYPE_NEXT)

  def previous(self):
    self.__press_key(NX_KEYTYPE_PREVIOUS)

  def fast_forward(self):
    self.__press_key(NX_KEYTYPE_FAST)

  def rewind(self):
    self.__press_key(NX_KEYTYPE_REWIND)
