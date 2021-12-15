from libqtile import widget
from .theme import colors


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text='?'):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg='light', bg='dark'):
    return widget.TextBox(
        **base(fg, bg),
        text='',
        fontsize=37,
        padding=-3
    )


def updates(fg='text', bg='dark'):
    return widget.CheckUpdates(
        **base(fg, bg), 
        colour_have_updates=colors[fg],
        colour_no_updates=colors[fg],
        display_format='{updates}',
        execute='alacritty', 
        update_interval=60, 
        no_update_string='0'
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Agave Nerd Font',
            fontsize=20,
            margin_y=3,
            margin_x=5,
            padding_y=10,
            padding_x=10,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(
            **base(fg='focus'),
            fontsize=15,
            padding=5
        ),
        separator(),
    ]


widget_defaults = dict(
    font='Agave Nerd Font',
    fontsize=15,
    padding=3,
)

extension_defaults = widget_defaults.copy()

primary_widgets = [
    *workspaces(),
    separator(),
    powerline('color4', 'dark'),
    icon(bg='color4', text=' '),
    updates(bg='color4'),
    powerline('color3', 'color4'),
    icon(bg='color3', text=' '),
    widget.Net(**base(bg='color3'), interface='wlp5s0'),
    powerline('color2', 'color3'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'), padding=5),
    powerline('color1', 'color2'),
    icon(bg='color1', fontsize=20, text=' '),
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    powerline('dark', 'color1'),
    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=5),
    powerline('color2', 'color1'),
    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
]
