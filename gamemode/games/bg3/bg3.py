from talon import Context,Module,actions,ctrl,cron

"""
Okay so first of all I need a way to manually switch the game to boulders gay three
 Second of all, I am going to use the built-in hissing for now because I cannot get it to work with parent.
  Then I need to get all the contextual actions set up as well as all the other keybines. And the foot pedals.luckexplore
"""

"""The shortcuts don't work perfectly right now because they conflict with the eye tracker. So I need to fix that. I may also have to increase the delay in the mouse click so that it actually has time to find. Fully click th button
 Releasing the mouse drag does not work properly for whatever reason. I also need to get rid of the WASD mod cuz it fights me.  May also need vocal stand-ins for clicks just in case. Of issues with  Parrot.
  Also figure out why the fuck the clicking still works when the voice is supposed to be disabled. Is the microphone actually turning off?s!"""

"""Currently have an issue with invalid shortcuts being recognized anyway and executing part of the commands this means that
if I accidentally say the word quick followed by something else then that leads to the random clicks being happening around the screen py
I may have to modify the flex grid code so that I can actually have a way to check back weather a and works or not.
This will be a little bit awkward because that is not my code so if I ever do a git pull it will get rid of my shit
so should I need do this I will have to look into ways to extend the python class and add new methods to bind
Also the word next is way too forgiving in battle to end turn I need change that key bind"""

mod = Module()

ctx = Context()
ctx.matches = """
os: windows
user.active_manual_game: bg3
mode: user.game
"""

DEBOUNCE_TIMER = 120
cron_job = None

parrot_config = {
    'clock': ('right click', lambda: actions.user.mouse_button(1)),
    'palate_click': ('left click', lambda: actions.user.mouse_button(0)),
    'hiss:db_120': ('camera scroll', lambda: actions.user.mouse_zone_contextual_command()),
    'hiss_stop:db_120': ('camera scrollend', lambda: actions.user.release_all_directional_buttons()),
}


@ctx.action_class("user")
class GateActions:
    def parrot_config():
        """Returns the current parrot config  """
        return parrot_config
    
    def noise_trigger_hiss(active: bool):
        """
        Called when the user makes a 'hiss' noise. Listen to
        https://noise.talonvoice.com/static/previews/hiss.mp3 for an
        example.
        """
        global cron_job

        if active:
            cron_job = cron.after(
                f"{DEBOUNCE_TIMER}ms",
                actions.user.mouse_zone_contextual_command
            )
        else:
            cron.cancel(cron_job)
            cron_job = None
            actions.user.release_all_directional_buttons()


    def mouse_zone_contextual_command(variety: str = None):
        zone = actions.user.get_mouse_zone_3x3()
        # Panning commands
        print(zone)
        if zone == 8:
            actions.user.button_down("w")
        elif zone == 4:
            actions.user.button_down("a")
        elif zone == 2:
            actions.user.button_down("s")
        elif zone == 6:
            actions.user.button_down("d")
        elif zone == 7:
            actions.user.button_down("e")
        elif zone == 9:
            actions.user.button_down("q")

    def release_all_directional_buttons(except_for: str = None):
        """Releases all directional buttons for the current gamef. If argument is specified, then releases all but that one"""
        for button in ["w","a","s","d","q","e"]:
            if except_for is None or except_for != button:
                actions.user.button_up(f"{button}")

    def foot_switch_top_down():
        """Foot switch button top:down"""
        actions.user.toggle_discord_talon()

    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""

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
        actions.user.button_down("shift")
        actions.user.button("\\")

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""
        actions.user.button_up("alt")
        actions.user.button_up("shift")
        actions.user.button("\\")

    def game_click_point(word: str, button: int):
        """Moves the cursor to a previously mapped point and clicks"""
        # Temporarily disables eye tracking and adds a slight delay so that hotbar items don't get thrown into the void
        actions.user.save_mouse_position()
        actions.tracking.control_toggle(False)
        actions.user.flex_grid_go_to_point(word,1,-1)
        ctrl.mouse_click(button=button, hold=16000)
        actions.sleep(0.3)
        actions.tracking.control_toggle(True)
        actions.user.load_mouse_position()