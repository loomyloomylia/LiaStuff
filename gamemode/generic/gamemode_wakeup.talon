mode: user.game
mode: sleep
not speech.engine: dragon
not tag: user.deep_sleep
-
^(wake up)+$:
    speech.enable()
    user.wake_up_color_preset()
    app.notify("working")
    mode.enable("noise")