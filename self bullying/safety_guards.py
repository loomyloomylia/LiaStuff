from talon import Module,app

mod = Module()

@mod.action_class
class Actions:
    def not_allowed():
        """Gives me a message for when I say something illegal"""
        app.notify('Try again princess :)')
    
