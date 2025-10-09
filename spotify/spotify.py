from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.spotify = r"""
os: windows
and app.exe: /^spotify\.exe$/i
"""

ctx.matches = r"""
os: windows
app: spotify
"""

# @mod.action_class
# class Actions:
