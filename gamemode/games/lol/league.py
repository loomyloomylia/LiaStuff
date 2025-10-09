from talon import Context,Module,actions,ctrl, screen
import math

ctx = Context()
ctx.matches = """
os: windows
user.active_manual_game: lol
mode: user.game
"""

"""
I want all four abilities to be holdable if needed
 they should be able to be configured on a champ by champ basis
  whether they cast instantly or hold until the sound ends
   this means I need reliable sounds
Q oh
W aa
e ee
r er

hiss: walk towards cursor
shush: walk away?

clock: atk move

Left Petal: head tracking only
tut: tab menu
buzz: recall

t: item 2

t t: ward

mm: pan camera? in a moment 




"""


main_screen=screen.main()
screen_width = main_screen.width
screen_height = main_screen.height

tab_down = False
def tab_toggle():
    global tab_down
    if tab_down:
        actions.user.button_down("tab")
    else:
        actions.user.button_up("tab")
    tab_down = not tab_down

def invert_mouse_position():
    angle = actions.user.get_mouse_bearing_from_center() + math.pi
    actions.user.save_mouse_position()
    actions.tracking.control_toggle(False)
    ctrl.mouse_move(screen_width/2 + math.cos(angle) * 400, screen_height/2 + math.sin(angle) * 400)
    ctrl.mouse_click(button=1)
    actions.sleep(0.2)
    actions.tracking.control_toggle(True)
    actions.user.load_mouse_position()


parrot_config = {
    "oh": ("q",lambda: actions.user.button("q")),
    "aa": ("w",lambda: actions.user.button("w")),
    "ee": ("e",lambda: actions.user.button("e")),
    "er": ("r",lambda: actions.user.button("r")),
    "hiss": ("right click",lambda: actions.user.mouse_drag(1)),
    "hiss_stop": ("right click endp",lambda: actions.user.mouse_drag_end()),
    "clock": ("attack move",lambda: actions.user.button("a")),
    "palate_click": ('left click',lambda: actions.user.mouse_button(0)),
    #"tut": ("tab open",lambda: tab_toggle()),
    "buzz": ('recall',lambda: actions.user.button("b")),
    "t": ("flash",lambda: actions.user.button("d")),
    "t t": ("flash",lambda: actions.user.button("f")),
    "shush:th_250": ('walk backwards',lambda: invert_mouse_position()),
}

@ctx.action_class("user")
class LeagueActions:
    def parrot_config():
        """Returns the parrot config"""
        return parrot_config
    
    def foot_switch_left_down():
        """Foot switch button left:down"""
        actions.tracking.control_gaze_toggle(False)
        print("Down")

    def foot_switch_left_up(held: bool):
        """Foot switch button left:up"""
        actions.tracking.control_gaze_toggle(True)
    