from talon import Module,Context,actions

def update_tag(muted: bool = None):
    if muted:
        ctx.tags = ["discord_muted"]
    else:
        ctx.tags = []
    

mod = Module()
mod.tag("discord_muted",desc="Tracks whether discord is muted or not")

ctx = Context()




@mod.action_class
class DiscordTalonSwitcher:
    def switch_to_talon():
        """Switches to enabling talon voice while disabling discord voice"""
        actions.sound.set_microphone("System Default")
        actions.key('`')
        update_tag(True)
        

    def switch_to_discord():
        """Switches to enabling discord voice while disabling talon voice"""
        actions.sound.set_microphone("None")
        actions.key('`')
        update_tag(False)

    def toggle_discord_talon():
        """Alternates between having talon or discord enabled. Due to discord only having one hot key for both functions,
        This working correctly requires that discord is manually muted while talon is active"""
        print(ctx.tags)
        if "discord_muted" in ctx.tags:
            print('going to discord')
            actions.user.switch_to_discord()
        else:
            print("going to talon")
            actions.user.switch_to_talon()