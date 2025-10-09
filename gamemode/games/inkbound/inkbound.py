from typing import Callable, Dict
from talon import Module,Context,actions

mod = Module()

ctx = Context()
ctx.matches = """
mode: user.game
and not mode: sleep
user.active_manual_game: inkbound
"""

default_config = {
    "aa": ('move left' , lambda : actions.user.movement_button_down("left")),
    "oh": ('move right', lambda : actions.user.movement_button_down("right")),
    "oo": ('up', lambda : actions.user.movement_button_down("up")),
    "er": ('down' , lambda : actions.user.movement_button_down("down")),
    "eh": ('stop moving', lambda : actions.user.game_stop()),
    "palate_click": ('left quick', lambda : actions.user.mouse_button(0,16000)),
    "tut": ('cancel', lambda : actions.user.mouse_button(1)),
    "ee": ('interact', lambda : actions.user.button("e")),
    "mm:th_250": ('interact switch', lambda : actions.user.button("q")),
    "shush:th_250": ('reset position', lambda : actions.user.button("r")),
}

cast_actions = {
    "oh": ('move right', lambda : actions.user.button("1")),
    "aa": ('move left' , lambda : actions.user.button("2")),
    "ee": ('interact', lambda : actions.user.button("3")),
    "er": ('down' , lambda : actions.user.button("4")),
    "eh": ('stop moving', lambda : actions.user.button("5")),
}

cast_config = {
    **default_config,
    **cast_actions
}

parrot_config = cast_config

@ctx.action_class("user")
class InkboundOverrides:
    def parrot_config():
        return parrot_config
    
    def foot_switch_top_down():
        """Foot switch button top:down"""
        actions.user.toggle_discord_talon()

    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""

    def foot_switch_center_down():
        """Foot switch button center:down"""
        global parrot_config
        parrot_config = default_config

    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""
        global parrot_config
        parrot_config = cast_config

    def foot_switch_left_down():
        """Foot switch button left:down"""
        actions.tracking.control_gaze_toggle(False)

    def foot_switch_left_up(held: bool):
        """Foot switch button left:up"""
        actions.tracking.control_gaze_toggle(True)

    def foot_switch_right_down():
        """Foot switch button right:down"""
        actions.user.button("g")
 
    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""

    