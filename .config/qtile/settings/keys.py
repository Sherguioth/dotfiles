from libqtile.config import Key
from libqtile.command import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows (vim liked)
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn("firefox-developer-edition")),

    # File explorer
    Key([mod], "e", lazy.spawn("thunar")),

    # Screnshot
    Key([mod], "s", lazy.spawn("scrot")),
    
    # Text editor
    Key([mod], "t", lazy.spawn("code")),


    # Volume from laptop
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]
