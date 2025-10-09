from talon import Module,Context,actions,cron

ctx = Context()
ctx.matches = """
mode: user.game
and not mode: sleep
user.active_manual_game: eldenring
"""

"""Click for light attack, clock for heady, perhaps double clock for charge heavy? Unsure if this will cause an unacceptable amount of latency, tut for ash  of war
I can do buzz for interact,
Perhaps I can just use click and clockFor attack. Clock for heavy, clock clock for charged, clock click for ash. then I could use tut for something else.The problem with this is that I cannot use parries because there will be latency on the ash of war can I bay wear

 center foot pedal for dodge
 left foot pedal for bloc
right for dpad context switch

Unused: oo, buzz, mm, t

Actions Needing Mapping:
jump
    - shush
crouch
    - hiss?
dpad switching
    - While holding right foot petal activate a mode where all directional inputs become discrete and on the dpad
        map buzz
        menu mm
        (this matches silksong)


use item
    - Use top foot petal to activate a mode where all noises become different items
        - hp, oh
        - mana aa
        - flask ee
        - torrent er
        - item slot eh
two hand
    - While above mod is active changed some miscellaneous sounds to be other functions
        - two hand: oo


Issues: laggy when reasserting direction
I think forward and backward direction should automatically cancel out horizontals when entered, but not other way around

I think sometimes the directional buttons double fire in quick succession causing other inputs to be canceled out
To fix this I may have to throttle inputs on the four directional+o
"""

parrot_config = {
    "aa:th_150": ('move left' , lambda : actions.user.movement_button_down("left")),
    "oh:th_150": ('move right', lambda : actions.user.movement_button_down("right")),
    "ee:th_100": ('move up'   , lambda : actions.user.movement_button_down("up")),
    "er:th_150": ('move down' , lambda : actions.user.movement_button_down("down")),
    "eh": ('stop moving', lambda : actions.user.game_stop()),
    "hiss": (),
    "hiss_stop:db_250": (),
    "shush": (),    
    "shush_stop:db_250": (),
    "palate_click": ('light attack', lambda : actions.user.mouse_button(0, 16000)),
    "oo": ('heavy attack', lambda : actions.user.mouse_button_down(2)),  
    "oo_stop": ('heavy attack release', lambda : actions.user.mouse_button_up(2)),
    "tut": ('ash of war', lambda : actions.user.button("p")),

    "clock": (),
    # "clock clock": ('heavy attack charged', lambda : actions.user.mouse_button_hold(2, )),
    "buzz:th_250": ('interact', lambda : actions.user.button("e")),
    "mm:th_400": (lambda : actions.user.button("q")),
    # "t": ('tester', lambda : print("tut")),
    # "t aa": ('tester', lambda : print("aa")),
    # "t ee": ('tester', lambda : print("ee")),
    # "t oh": ('tester', lambda : print("oh")),
}

@ctx.action_class("user")
class EldenringOverrides:
    def parrot_config():
        return parrot_config

    def foot_switch_left_down():
        """Foot switch button top:down"""
        actions.user.mouse_button_down(1)

    def foot_switch_left_up(held: bool):
        """Foot switch button top:up"""
        actions.user.mouse_button_up(1)

    def foot_switch_center_down():
        """Foot switch button center:down"""
        actions.user.button_down("l")

    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""
        actions.user.button_up("l")

    def foot_switch_right_down():
        """Foot switch button right:down"""
        global parrot_config
            

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""
        actions.skip()

    def foot_switch_top_down():
        """Foot switch button left:down"""
        actions.skip()

    def foot_switch_top_up(held: bool):
        """Foot switch button left:up"""
        actions.skip()
        
        
        