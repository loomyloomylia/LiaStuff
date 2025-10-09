os: windows
mode: sleep
and mode: command
user.running: zoom
-

^mute:
    speech.enable()
    user.focus_zoom_and_toggle_mute()

parrot(palate_click):
      user.parrot_config_noise("palate_click")

parrot(clock):
      user.parrot_config_noise("clock")

parrot(tut):
      user.parrot_config_noise("tut")

parrot(shush):
      user.parrot_config_noise("shush")

parrot(shush:stop):
      user.parrot_config_noise("shush_stop")

key(f6):
      user.parrot_config_noise("mode_switch")  