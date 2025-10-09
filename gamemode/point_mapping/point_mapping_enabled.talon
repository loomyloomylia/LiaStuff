mode: user.game
tag: user.point_mapping_enabled
-
^shortcut map <user.word>$:
    user.flex_grid_map_point_here(word)

^shortcut (nmap|unmap) <user.word>$:
    user.flex_grid_unmap_point(word)

^shortcut unmap everything yes I mean it$:
    user.flex_grid_unmap_point("")

^shortcut unmap everything$:
    app.notify("Do you mean it?")

disable point mapping:
    user.disable_point_mapping()