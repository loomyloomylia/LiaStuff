-
key(shift-f9):
    sound.set_microphone("None")
    app.notify("Talon full muted.")


key(shift-f10):
    sound.set_microphone("System Default")
    app.notify("Talon re-enabled")
