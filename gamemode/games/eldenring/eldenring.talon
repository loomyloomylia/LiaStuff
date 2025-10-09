mode: user.game
and not mode: sleep
user.active_manual_game: eldenring
-
settings(): 
    key_hold = 100
    user.game_dpad_mode = "WASD"
    user.dpad_reassert_direction_possible = true

parrot(palate_click_game):
    user.parrot_config_noise("palate_click")

key(space):
    speech.disable()
    user.sleep_mode_color_preset()

parrot(clock):
    user.parrot_config_noise("clock")

parrot(tut):
    user.parrot_config_noise("tut")

parrot(oo_lenient):
    user.parrot_config_noise("oo")

parrot(oo_lenient:stop):
    user.parrot_config_noise("oo_stop")

parrot(buzz):
    user.parrot_config_noise("buzz")

parrot(er):
    user.parrot_config_noise("er")

parrot(er:stop):
    user.parrot_config_noise("er_stop")

parrot(t_lenient):
    user.parrot_config_noise("t")

parrot(eh):
    user.parrot_config_noise("eh")

parrot(aa):
    user.parrot_config_noise("aa")

parrot(aa:stop):
    user.parrot_config_noise("aa_stop")

parrot(ee):
    user.parrot_config_noise("ee")
    
parrot(ee:stop):
    user.parrot_config_noise("ee_stop")

parrot(oh):
    user.parrot_config_noise("oh")

parrot(oh:stop):
    user.parrot_config_noise("oh_stop")

parrot(shush):
    user.parrot_config_noise("shush")

parrot(shush:stop):
    user.parrot_config_noise("shush_stop")

parrot(hiss):
    user.parrot_config_noise("hiss")

parrot(hiss:stop):
    user.parrot_config_noise("hiss_stop")

parrot(mm):
    user.parrot_config_noise("mm")

parrot(mm:stop):
    user.parrot_config_noise("mm_stop")

^test eldenring$:
    print("eldenring working")