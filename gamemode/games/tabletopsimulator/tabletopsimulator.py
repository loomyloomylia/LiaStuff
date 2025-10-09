from talon import Module,Context,actions

ctx = Context()
ctx.matches = """
mode: user.game
user.active_manual_game: tabletopsimulator
"""

parrot_config = {
    "palate_click": ('left click', lambda: actions.user.mouse_button(0)),
    "tut": ('right click', lambda: actions.user.mouse_button(1)),
    "clock": ('quick action', lambda: actions.core.repeat_phrase(1)),
    # "hiss:db_120": ('tap', lambda: actions.user.button('e')),
    # "shush:db_120": ('untap', lambda: actions.user.button('q')),
    
}




@ctx.action_class("user")
class TabletopOverrides:
    def foot_switch_top_down():
        """Foot switch button top:down"""
        actions.user.mouse_button_down(2)
        
    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""
        actions.user.mouse_button_up(2)

    def foot_switch_center_down():
        """Foot switch button center:down"""
        actions.user.mouse_drag(0)

    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""
        actions.user.mouse_drag_end()

    def foot_switch_left_down():
        """Foot switch button left:down"""
        actions.tracking.control_gaze_toggle(False)

    def foot_switch_left_up(held: bool):
        """Foot switch button left:up"""
        actions.tracking.control_gaze_toggle(True)

    def foot_switch_right_down():
        """Foot switch button right:down"""
        actions.user.button_down("alt")

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""
        actions.user.button_up("alt")

    def parrot_config():
        """Returns the current parrot config"""
        return parrot_config

mod = Module()
@mod.action_class
class TabletopActions:
    def tabletop_joystick_pan(x: float,y: float):
        """"""

        if x > 0:
            actions.user.button_down("d")
        else:
            actions.user.button_up("d")
            
        if x < 0:
            actions.user.button_down("a")
        else:
            actions.user.button_up("a")
            
        if y < 0:
            actions.user.button_down("s")
        else:
            actions.user.button_up("s")
            
        if y > 0:
            actions.user.button_down("w")
        else:
            actions.user.button_up("w")