user.active_manual_game: tabletopsimulator
mode: user.game
-
tag(): user.point_mapping

test tabletop simulator:
    app.notify('tabletop simulator recognized')

touch:
    mouse_click(0)

menu:
    mouse_click(1)

midclick:
    mouse_click(2)

duke:
    mouse_click(0)
    mouse_click(0)

escape:
    key(escape)

magnify:
    key("m:down")

magnify done:
    key("m:up")

camera reset:
    key("r")

camera mode:
    key("p")

group:
    key("g")

flip:
    key("f")

tap:
    key("e")

(untap | on top):
    key("q")

zoom out:
    user.mouse_scroll_down()

zoom out big:
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    

zoom in:
    user.mouse_scroll_up()

zoom in big:
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
        

<user.ordinals>:
    user.repeat_command(ordinals  -1)

gamepad(right_xy:change):
    user.tabletop_joystick_pan(x,y)