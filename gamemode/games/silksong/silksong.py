from typing import Callable, Dict
from talon import Module,Context,actions

mod = Module()

ctx = Context()
ctx.matches = """
mode: user.game
and not mode: sleep
user.active_manual_game: silksong
"""

# ctx.settings["key_hold"]  = 32
# ctx.settings["game_dpad_mode"] = "arrows"
# An idea is to have a precision movement mode where movement happens only while holding the noise.
# In order to move and jump you would make the noise and then hiss to jump and the button would be released upon the hiss ending
def directional_attack(direction: str, attack_button: str = "x"):
    actions.user.movement_button_down(direction)
    actions.user.button(attack_button)
    actions.user.movement_button_up(direction)

def dash_downwards():
    direction = None
    if actions.user.button_is_down("right"):
        direction = "right"
    elif actions.user.button_is_down("left"):
        direction = "left"
    
    # Need to stop and restore direction after the dash
    if direction is not None:
        actions.user.movement_button_up(direction)
        actions.user.movement_button_down("down")
        actions.user.button("c")
        actions.user.movement_button_up("down")
        actions.user.movement_button_down(direction)
    else:
        actions.user.movement_button_down("down")
        actions.user.button("c")
        actions.user.movement_button_up("down")

def paired_command_wrapper(first: Callable, second: Callable):
    first()
    second()

def direction_switch_wrapper(action: Callable):
    action()
    actions.user.switch_horizontal()
    
def mode_switch_wrapper(action: Callable, mode: str):
    global parrot_config
    action()
    # parrot_config = mode
    actions.user.parrot_config_set_mode(mode)

# def menu_mode_switch():
#     global parrot_config
#     parrot_config = menu_config
#     # print("Switching to menu")

def default_mode_switch():
    global parrot_config
    # parrot_config = default_config
    actions.user.parrot_config_set_mode("default")
    # print("Switching to default")

def precise_mode_switch():
    global parrot_config
    # parrot_config = precise_movement_config
    actions.user.parrot_config_set_mode("precise")

def stop_mode_switch():
    global parrot_config
    # parrot_config = precise_movement_config
    actions.user.parrot_config_set_mode("stop")

    
"""Challenges: There is no way to stop movement nonverbally so that may need to be a foot pedal
 additional hissing to jump is kind of exhausting so that could be another good use of a foot pedal,  additionally this would help with 
 aerial attacks
  it can be kind of hard in the moment to remember which directional noise is which in order to switch direction quickly
  
  need a menu mode
x
  aUnused noises: ee,oo,er
  
  additions: k sound, g sound, lll, ff, lipsmack(too similar to tut i feel ), platypus, whislte?, zh (beginning of name Jacques)

  ISSUES: er noise is very unreliable to hold. silk skill noise is incredibly unreliable as well and misfires often. I am going to need a more reliable sound for it
  """    

ATTACK_COOLDOWN = 150


"""TODO: refactor this to use modes properly!!!!!!!!!!!!!!!!!!!!!!!!!!"""
default_config = {
    "aa": ('move left' , lambda : actions.user.movement_button_down("left")),
    "oh": ('move right', lambda : actions.user.movement_button_down("right")),
    # "oo": ('up', lambda : actions.user.movement_button_down("up")),
    # "er": ('down' , lambda : actions.user.movement_button_down'switch("down")),
    "eh:th_50": ('stop moving', lambda : actions.user.game_stop(except_for = "z")),
    "shush:th_250": ('switch horizontal', lambda : actions.user.switch_horizontal()),       
    "hiss": ('dash start', lambda : actions.user.button_down("c")),# was oo
    "hiss_stop:db_250": ('dash stop', lambda : actions.user.button_up("c")),
    "ll": ('dash attacks start', lambda : actions.user.button_down("c")),
    "ll_stop": ('dash attack stop', lambda : paired_command_wrapper(lambda : actions.user.button("x"), lambda : actions.user.button_up("c"))),

    "er": ('dash down', lambda : dash_downwards()),

    f"palate_click:th_{ATTACK_COOLDOWN}": ('attack neutral', lambda : actions.user.button("x")),
    f"tut:th_{ATTACK_COOLDOWN}": ('attack up', lambda : directional_attack("up")),
    f"clock:th_{ATTACK_COOLDOWN}": ('attack down', lambda : directional_attack("down")),
    "ee": ('silk skill', lambda : actions.user.button("f")),
    "oo:th_250": ('tool up', lambda : directional_attack("up", "f")),# was hiss
    
    "mm:th_250": ('bind',lambda : actions.user.button("a")),
    
    "buzz:th_250": ('interact', lambda : actions.user.movement_button("up")),
    # "buzz ee": ('quick map', lambda : actions.user.button_toggle("tab")),
    # "buzz aa": ('menu', lambda : actions.user.button("m")),
    

    "high_whistle:th_350": ('escape menu', lambda : actions.user.button("escape")),
}

STOP_CALLABLE = lambda : actions.user.game_stop(except_for = "z")

def stop_action_builder(action: Callable):
    return lambda : paired_command_wrapper(action, STOP_CALLABLE)

# stop_actions = {
#     "hiss": ('dash start', stop_action_builder(lambda : actions.user.button_down("c"))),# was oo
#     "er": ('dash down', stop_action_builder(lambda : dash_downwards())),
#     f"palate_click:th_{ATTACK_COOLDOWN}": ('attack neutral', stop_action_builder(lambda : actions.user.button("x"))),
#     f"tut:th_{ATTACK_COOLDOWN}": ('attack up', stop_action_builder(lambda : directional_attack("up"))),
    
#     f"clock:th_{ATTACK_COOLDOWN}": ('attack down', stop_action_builder(lambda : directional_attack("down"))),
    
#     "ee": ('silk skill', stop_action_builder(lambda : actions.user.button("f"))),
#     "oo:th_250": ('tool up', stop_action_builder(lambda : directional_attack("up", "f"))),# was hiss
# }

reversed_actions = {
    f"palate_click:th_{ATTACK_COOLDOWN}": ('attack neutral', lambda : direction_switch_wrapper(lambda : actions.user.button("x"))),
    f"tut:th_{ATTACK_COOLDOWN}": ('attack up', lambda : direction_switch_wrapper(lambda : directional_attack("up"))),
    f"clock:th_{ATTACK_COOLDOWN}": ('attack down', lambda : direction_switch_wrapper(lambda : directional_attack("down"))),
    "oo:th_250": ('tool up', lambda : direction_switch_wrapper(lambda : directional_attack("up", "f"))), # was oo
}

precise_movement_actions = {
    "ee": ('up', lambda : actions.user.movement_button_down("up")),
    "er": ('down' , lambda : actions.user.movement_button_down("down")),
    "aa_stop": ('move left' , lambda : actions.user.movement_button_up("left")),
    "oh_stop": ('move right', lambda : actions.user.movement_button_up("right")),
    "ee_stop": ('up', lambda : actions.user.movement_button_up("up")),
    "er_stop": ('down' , lambda : actions.user.movement_button_up("down")),
    
    "buzz": ('quick map', lambda : mode_switch_wrapper(lambda : actions.user.button_toggle("tab"), "default")),
    "mm": ('menu', lambda : actions.user.button("m")),
    "hiss_stop": ('dash start', lambda : mode_switch_wrapper(lambda : actions.user.button_down("c"), "default")),
}


    
    
reversed_config = {
    **default_config,
    **reversed_actions
}

precise_movement_config = {
    **default_config,
    **precise_movement_actions
}

# parrot_config = default_config

parrot_config = {
    "default": default_config,
    "reversed": reversed_config,
    "precise": precise_movement_config,
}

@ctx.action_class("user")
class SilksongActions:
    def parrot_config():
        return parrot_config

    def foot_switch_left_down():
        """Foot switch button top:down"""
        global parrot_config
        # parrot_config = reversed_config
        actions.user.parrot_config_set_mode("reversed")

    def foot_switch_left_up(held: bool):
        """Foot switch button top:up"""
        global parrot_config
        actions.user.parrot_config_set_mode("default")

    def foot_switch_center_down():
        """Foot switch button center:down"""
        actions.user.button_down("z")
        if parrot_config is reversed_config:
            #actions.user.switch_horizontal()
            pass


    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""
        actions.user.button_up("z")

    def foot_switch_right_down():
        """Foot switch button right:down"""
        global parrot_config
        if actions.user.parrot_config_get_mode() == "default":
            # parrot_config = precise_movement_config
            actions.user.parrot_config_set_mode("precise")
        elif actions.user.parrot_config_get_mode() == "precise":
            # parrot_config = default_config
            actions.user.parrot_config_set_mode("default")
            

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""
        actions.skip()

    def foot_switch_top_down():
        """Foot switch button left:down"""
        actions.user.game_stop("z")# state

    def foot_switch_top_up(held: bool):
        """Foot switch button left:up"""