mode: user.game
user.active_manual_game: bg3
-
tag(): user.point_mapping

# Top petal for mute, center for click, left for disabling eye tracker, right for focus
# Having issues with hissing, keeps 

# Using built in hissing until I can find a better way to do this in parrot
# parrot(hiss):
#     key("w:down")

# parrot(hiss:stop):
#     key("w:up")

parrot(paletteclick):
    # mouse_click(0)
    user.parrot_config_noise("paletteclick")
    
touch:
    mouse_click(0)

parrot(clock):
    #   mouse_click(1)
    user.parrot_config_noise("clock")

^zoom out$:
    user.mouse_scroll_down()
    repeat(100)

^zoom in$:
    user.mouse_scroll_up()
    repeat(100)

^portrait one$:
    user.button("f1")

^portrait two$:
    user.button("f2")

^portrait three$:
    user.button("f3")

^portrait four$:
    user.button("f4")

^find me$:
    user.button("home")

^tactical$:
    user.button("o")

^sneak$:
    user.button("c")

^jump$:
    user.button("z")

^shove$:
    user.button("v")
    
^throw$:
    user.button("x")

^(end turn)$:
    user.button("space")

^turn based mode$:
    user.button_down("shift")
    user.button("space")
    user.button_up("shift")

^swap weapons$:
    user.button("f")

^dual wield$:
    user.button("r")

# Menu Commands
scroll down:
    user.mouse_scroll_down()
    repeat(1)

scroll down <number_small>:
    user.mouse_scroll_down()
    repeat(1)
    repeat(2 * number_small)

scroll up:
    user.mouse_scroll_up()
    repeat(1)

scroll up <number_small>:
    user.mouse_scroll_up()
    repeat(1)
    repeat(2 * number_small)

escape:
    user.button("escape")

^show inventory:
    user.button("i")

^show character:
    user.button("n")

^show party:
    user.button("tab")

^show spellbook:
    user.button("k")

^show powers:
    user.button("b")

^show reactions:
    user.button("l")

^show journal:
    user.button("j")

^show map:
    user.button("m")

^show inspiration:
    user.button("p")

^show alchemy:
    user.button("h")

^pin$:
    user.button("t")
 
^number <number_small>$:
    user.button("{number_small}")
# 

