from talon import Context,Module,actions,ctrl, screen
import math

ctx = Context()
ctx.matches = """
os: windows
user.active_manual_game: hots
mode: user.game
"""

main_screen=screen.main()
screen_width = main_screen.width
screen_height = main_screen.height

CHAR_POSITION = (1280,650)

tab_down = False
def tab_toggle():
    global tab_down
    if tab_down:
        actions.user.button_down("tab")
    else:
        actions.user.button_up("tab")
    tab_down = not tab_down



def invert_mouse_position():
    angle = actions.user.get_mouse_bearing_from_point(CHAR_POSITION[0], CHAR_POSITION[1]) + math.pi
    actions.user.save_mouse_position()
    actions.tracking.control_toggle(False)
    ctrl.mouse_move(CHAR_POSITION[0] + math.cos(angle) * 800, CHAR_POSITION[1] + math.sin(angle) * 800)
    ctrl.mouse_click(button=1)
    actions.sleep(0.2)
    actions.tracking.control_toggle(True)
    actions.user.load_mouse_position()

def center_camera():
    actions.user.button("l")
    actions.user.button("space")

def talent_config_switch():
    global parrot_config
    actions.user.button_down("ctrl")
    parrot_config =talent_config

def default_config_switch():
    global parrot_config
    actions.user.button_up("ctrl")
    parrot_config =default_config

def choose_talent(num: str):
    global parrot_config
    actions.user.button(num)
    default_config_switch()
        

# oo and mm are unused, Need mounting as well as lock cam controls for if I need to pan away
# also need to pick talents,probably using qwer
default_config = {
    "oh": ("q",lambda: actions.user.button("q")),
    "aa": ("w",lambda: actions.user.button("w")),
    "ee": ("e",lambda: actions.user.button("e")),
    "er": ("r",lambda: actions.user.button("r")),
    "eh": ("d",lambda: actions.user.button("d")),
    "hiss": ("right click",lambda: actions.user.mouse_drag(1)),
    "hiss_stop": ("right click end",lambda: actions.user.mouse_drag_end()),
    "clock": ("attack move",lambda: actions.user.button("a")),
    "palate_click": ('left click',lambda: actions.user.mouse_button(0)),
    "tut": ("tab open",lambda: tab_toggle()),
    "palate_click palate_click": ('pick talent', lambda: talent_config_switch()),
    "buzz": ('recall',lambda: actions.user.button("b")),
    "t": ("extra 1",lambda: actions.user.button("1")),
    "t t": ("extra 2",lambda: actions.user.button("2")),
    "mm": ('mount',lambda: actions.user.button('z')),
    "shush:th_250": ('walk backwards',lambda: invert_mouse_position()),
    "oo:th_1000": ('center camera',lambda: center_camera()),
}

talent_config = {
    **default_config,
    "oh": ("q",lambda: choose_talent("1")),
    "aa": ("w",lambda: choose_talent("2")),
    "ee": ("e",lambda: choose_talent("3")),
    "er": ("r",lambda: choose_talent("4")),
    "eh": ("d",lambda: choose_talent("5")),
    "palate_click palate_click": ('go back', lambda: default_config_switch()),
    
}

parrot_config = default_config


@ctx.action_class("user")
class HotsActions:
    def parrot_config():
        """Returns the parrot config"""
        return parrot_config
    
    def foot_switch_center_down():
        """Foot switch button left:down"""
        actions.tracking.jump()
        actions.tracking.control_gaze_toggle(False)

    def foot_switch_center_up(held: bool):
        """Foot switch button left:up"""
        actions.tracking.control_gaze_toggle(True)

    def foot_switch_top_down():
        """Foot switch button top:down"""
        actions.user.toggle_discord_talon()

    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""
    