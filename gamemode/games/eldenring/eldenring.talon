mode: user.game
and not mode: sleep
user.active_manual_game: eldenring
-
settings(): 
    key_hold = 100
    user.game_dpad_mode = "WASD"
    user.dpad_reassert_direction_possible = true

key(space):
    speech.disable()
    user.sleep_mode_color_preset()

^test eldenring$:
    print("eldenring working")


parrot(palate_click_game):
    user.parrot_config_noise("palate_click")

parrot(clock):
    user.parrot_config_noise("clock")

parrot(tut):
    user.parrot_config_noise("tut")

parrot(alveolar_click):
    user.parrot_config_noise("alveolar_click")

parrot(oh):
    user.parrot_config_noise("oh")

parrot(oh:stop):
    user.parrot_config_noise("oh_stop")

parrot(aa):
    user.parrot_config_noise("aa")

parrot(aa:stop):
    user.parrot_config_noise("aa_stop")

parrot(ee):
    user.parrot_config_noise("ee")
    
parrot(ee:stop):
    user.parrot_config_noise("ee_stop")

parrot(er):
    user.parrot_config_noise("er")

parrot(er:stop):
    user.parrot_config_noise("er_stop")

parrot(oo_lenient):
    user.parrot_config_noise("oo")

parrot(oo_lenient:stop):
    user.parrot_config_noise("oo_stop")    
    
parrot(eh):
    user.parrot_config_noise("eh")

parrot(ll):
    user.parrot_config_noise("ll")

parrot(ll:stop):
    user.parrot_config_noise("ll_stop")

parrot(hiss):
    user.parrot_config_noise("hiss")

parrot(hiss:stop):
    user.parrot_config_noise("hiss_stop")

parrot(shush):
    user.parrot_config_noise("shush")

parrot(shush:stop):
    user.parrot_config_noise("shush_stop")

parrot(mm):
    user.parrot_config_noise("mm")

parrot(mm:stop):
    user.parrot_config_noise("mm_stop")

parrot(buzz):
    user.parrot_config_noise("buzz")

parrot(buzz:stop):
    user.parrot_config_noise("buzz_stop")

parrot(zh):
    user.parrot_config_noise("zh")

parrot(zh:stop):
    user.parrot_config_noise("zh_stop")

parrot(t):
    user.parrot_config_noise("t")

parrot(g):
    user.parrot_config_noise("g")

parrot(high_whistle):
    user.parrot_config_noise("high_whistle")

parrot(high_whistle:stop):
    user.parrot_config_noise("high_whistle_stop")