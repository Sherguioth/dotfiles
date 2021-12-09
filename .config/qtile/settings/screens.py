from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.95)


screens = [Screen(top=status_bar(primary_widgets))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

if command.returncode != 0:
    error = command.stderr.decode('UTF-8')
    logger.error(f'Failed counting monitors using {xrandr}: \n{error}')
    coonnected_monitors = 1
else:
    coonnected_monitors = int(command.stdout.decode('UTF-8'))
    
if coonnected_monitors > 1:
    for _ in range(1, coonnected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))
