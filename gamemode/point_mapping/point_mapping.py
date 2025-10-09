from talon import Module,Context,actions

mod = Module()
mod.tag("point_mapping",desc="Allows the remapping of specifically named points on the screen for the current game")
mod.tag("point_mapping_enabled",desc="Toggles the set of voice commands that allow remapping. Lessens the chance of accidental remapping")

ctx = Context()

@mod.action_class
class PointMapToggle:
    def enable_point_mapping():
        """Enables the ability to remap specifically name points on the screen for the current game"""
        ctx.tags = ["user.point_mapping_enabled"]

    def disable_point_mapping():
        """Disables the ability to remap specifically name points on the screen for the current game"""
        ctx.tags = []