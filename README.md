# Dotfiles & Linux Configs

## Table of Contents

- [Overview](#overview)
- [Arch installation](#arch-installation)
- [Login and window manager](#login-and-window-manager)
- [Basic Qtile configuration](#basic-qtile-configuration)
- [Basic system utilities](#basic-system-utilities)
  - [Wallpaper](#wallpaper)
  - [Fonts](#fonts)
  - [Audio](#audio)
  - [Monitors](#monitors)
  - [Storage](#storage)
  - [Network](#network)
  - [Systray](#systray)
  - [Xsession file](#xsession-file)
- [Other configuration and tools](#other-configuration-and-tools)
  - [AUR helper](#aur-helper)
  - [File Manager](#file-manager)
  - [GTK Theming](#gtk-theming)
  - [Lightdm theming](#lightdm-theming)
  - [Multimedia](#multimedia)
    - [Video and audio](#video-and-audio)
- [Software](#software)
  - [Basic utilities](#basic-utilities)
  - [Fonts, theming and GTK](#fonts-theming-and-gtk)
  - [Apps](#apps-1)

## Overview

This is a guide on how to install and use my linux configurations, based on a clean Arch Linux installation. Here a twilight window manager Qtile will be used, which is the one I have initially configured. These configurations are mostly based on this repository of **[here](https://github.com/antoniosarosi/dotfiles)**, owned by **[Antonio Sarosi](https://github.com/antoniosarosi)**.

## Arch installation

The starting point of this guide is right after a complete clean Arch based
distro installation. The
**[Arch Wiki](https://wiki.archlinux.org/index.php/Installation_guide)**
doesn't tell you what to do after setting the root password, it suggests installing
a bootloader, but before that I would make sure to have working internet:

```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

Now you can install a bootloader and test it "safely", this is how to do it on
modern hardware,
[assuming you've mounted the efi partition on /boot](https://wiki.archlinux.org/index.php/Installation_guide#Example_layouts):

```bash
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

Now you can create your user:

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

In order to have root privileges we need sudo:

```bash
pacman -S sudo
```

Edit **/etc/sudoers** with nano or vim by uncommenting this line:

```bash
## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```

Now you can reboot:

```bash
# Exit out of ISO image, unmount it and remove it
exit
umount -R /mnt
reboot
```

After logging in, your internet should be working just fine, but that's only if
your computer is plugged in. If you're on a laptop with no Ethernet ports, you
might have used **[iwctl](https://wiki.archlinux.org/index.php/Iwd#iwctl)**
during installation, but that program is not available anymore unless you have
installed it explicitly. However, we've installed
**[NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager)**,
so no problem, this is how you connect to a wireless LAN with this software:

```bash
# List all available networks
nmcli device wifi list
# Connect to your network
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

Check [this page](https://wiki.archlinux.org/index.php/NetworkManager#nmcli_examples)
for other options provided by _nmcli_. The last thing we need to do before
thinking about desktop environments is installing **[Xorg](https://wiki.archlinux.org/index.php/Xorg)**:

```bash
sudo pacman -S xorg
```

## Login and window manager

First, we need to be able to login and open some programs like a browser and a
terminal, so we'll start by installing **[lighdm](https://wiki.archlinux.org/index.php/LightDM)**
and **[qtile](https://wiki.archlinux.org/index.php/Qtile)**. Lightdm will not
work unless we install a **[greeter](https://wiki.archlinux.org/index.php/LightDM#Greeter)**.
We also need
**[xterm](https://wiki.archlinux.org/index.php/Xterm)** because that's the
terminal emulator qtile will open by default, until we change the config file.
Then, a text editor is necessary for editing config files, you can use
**[vscode](https://wiki.archlinux.org/index.php/Visual_Studio_Code)** or jump
straight into **[neovim](https://wiki.archlinux.org/index.php/Neovim)** if you
have previous experience, otherwise I wouldn't suggest it. Last but not least,
we need a browser.

```bash
sudo pacman -S lightdm lightdm-gtk-greeter qtile xterm code firefox-developer-edition
```

Enable _lightdm_ service and restart your computer, you should be able to log into
Qtile through _lightdm_.

```bash
sudo systemctl enable lightdm
reboot
```

If after reboot dosen't show the _lightdm_ login check with nano or vim the next line, uncommet it and _reboot_.

```bash
# /etc/lightdm/lightdm.conf
[LightDM]
...
## Uncomment to allows show the login graphical
#ligind-check-graphicl=true
...
```

## Basic Qtile configuration

Now that you're in Qtile, you should know some of the default keybindings.

| **Key**               | **Action**                  |
| --------------------- | --------------------------- |
| **mod + return**      | launch terminal             |
| **mod + k**           | next window                 |
| **mod + j**           | previous window             |
| **mod + w**           | kill window                 |
| **mod + [123456789]** | go to workspace [123456789] |
| **mod + ctrl + r**    | restart Qtile               |
| **mod + ctrl + q**    | logout                      |

Before doing anything else, if you don't have a US keyboard, you should
change it using _setxkbmap_. To open xterm use **mod + return**. For example to
change your layout to latam:

```bash
setxkbmap latam
```

There is no menu by default, you have to launch programs through xterm. At this
point, you can pick your terminal emulator of choice and install a program
launcher.

```bash
# Install another terminal emulator if you want
sudo pacman -S alacritty
```

Now open the config file:

```bash
code ~/.config/qtile/config.py
```

At the beginning, after imports, you should find an array called _keys_,
and it contains the following line:

```python
Key([mod], "Return", lazy.spawn("xterm")),
```

Change that line to launch your terminal emulator:

```python
Key([mod], "Return", lazy.spawn("alacritty")),
```

Install a program launcher like
**[dmenu](https://wiki.archlinux.org/index.php/Dmenu)**
or **[rofi](https://wiki.archlinux.org/index.php/Rofi)**:

```bash
sudo pacman -S rofi
```

Then add keybindings for that program:

```python
Key([mod], "m", lazy.spawn("rofi -show drun")),
Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
```

Now restart Qtile with **mod + control + r**. You should be able to open your
menu and terminal emulator with keybindings. If you picked rofi, you can
change its theme like so:

```bash
sudo pacman -S which
rofi-theme-selector
```

That's it for Qtile, now you can start hacking on it and make it your own.
Checkout my custom Qtile config
[here](https://github.com/Sherguioth/dotfiles/tree/main/.config/qtile).
But before that I would recommend configuring basic utilities like audio, mounting drives, etc.

## Basic system utilities

In this section we will cover some software that almost everybody needs on their
system. Keep in mind though that the changes we are going to make
will not be permanent. [This subsection](#xsession-file) describes how to accomplish
that.

### Wallpaper

First things first, your screen looks empty and black, so you might want to have
a wallpaper not to feel so depressed. You can open _firefox_ through _rofi_
using **mod + m** and download one. Then install
**[feh](https://wiki.archlinux.org/index.php/Feh)** or
**[nitrogen](https://wiki.archlinux.org/index.php/Nitrogen)**
and and set your wallpaper:

```bash
sudo pacman -S feh
feh --bg-scale path/to/wallpaper
```

### Fonts

Fonts in Arch Linux are very simples, before running into Arch problems, it would be wise to install some good fonts. First you can just use the simple approach of installing these packages:

```bash
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

To list all available fonts:

```bash
fc-list
```

Personally, I really like the fonts Agave Nerd Font, JetBrains Mono and UbuntuMono Nerd Font. Installing these fonts is very easy, you just have to download the zip file of the fonts you want from [Nerd Fonts](https://www.nerdfonts.com/font-downloads), unzip the zip file with the fonts and copy the folder with the fonts in _/usr/share/fonts_

```bash
cd Downloads
unzip Agave.zip -d Agave
unzip JetBrainsMono.zip -d Jet JetBrainsMono

sudo cp JetBrainsMono/ /usr/share/fonts
sudo cp Agave/ /usr/share/fonts
```

And now you can delete the zip files. To install Ubuntu Mono Nerd Font you can use an AUR helper, in [this section](#aur-helper) you can know how to install one.

### Audio

There is no audio at this point, we need
**[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**.
I suggest also installing a graphical program to control audio like
**[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**,
because we don't have keybindings for that yet:

```bash
sudo pacman -S pulseaudio pavucontrol
```

On Arch,
[pulseaudio is enabled by default](https://wiki.archlinux.org/index.php/PulseAudio#Running),
but you might need to reboot in order for it to actually start. After rebooting,
you can open _pavucontrol_ through _rofi_, unmute the audio, and you should be
just fine.

### Monitors

If you have a multi-monitor set up, you surely want to use all your screens.
Here's how **[xrandr](https://wiki.archlinux.org/index.php/Xrandr)** CLI works:

```bash
# List all available outputs and resolutions
xrandr
# Common setup for two monitors
xrandr --output DP-1 --primary --mode 1920x1080 --pos 0x1080 --output DP-2 --mode 1920x1080 --pos 0x0
```

We need to specify the position for each output, otherwise it will default to
0x0, and all your outputs will be overlapped. Now if you don't want to calculate pixels
and stuff you need a GUI like
**[arandr](https://www.archlinux.org/packages/community/any/arandr/)**:

```bash
sudo pacman -S arandr
```

Open it with _rofi_, arrange your screens however you want, and then you can
save that layout, which will basically give you a shell script with the exact
_xrandr_ command that you need. Save that script, but don't click "apply" just
yet.

For a multi-monitor system, it's recommended to create an instance of a
_Screen_ object for each monitor in your Qtile config.

You'll find an array called _screens_ which contains only one object
initialized with a bar at the bottom. Inside that bar you can see the default
widgets that come with it.

Add as many screens as you have and copy-paste all widgets, later you can
customize them. Now you can go back to arandr, click _apply_, and then restart
Qtile.

Now your multi-monitor system should work.

## Storage

Another basic utility you might need is automounting external hard drives or
USBs. For that I use **[udisks](https://wiki.archlinux.org/index.php/Udisks)**
and **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**.
_udisks_ is a dependency of _udiskie_, so we only need to install the last one.
Install also **[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**
package to read and write NTFS formatted drives:

```bash
sudo pacman -S udiskie ntfs-3g
```

## Network

We have configured the network through _nmcli_, but a graphical frontend is
more friendly. I use
**[nm-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**:

```bash
sudo pacman -S network-manager-applet
```

## Systray

# Systray volume

By default, you have a system tray in Qtile, but there's nothing running in it.
You can launch the programs we've just installed like so:

```bash
udiskie -t &
nm-applet &
```

Now you should see icons that you can click to configure drives and networking.
Optionally, you can install tray icons for volume:

```bash
sudo pacman -S volumeicon
volumeicon &
```

### Xsession file

So far, some of the settings that have been made are not permanent, which means that when you restart the computer they will not be. To solve this, it is necessary to create an .xsesion file that loads all these configurations at the beginning of the session.

Now you can use _~/.xsesion_ to run some configurations and programs before your window manager starts:

```bash
touch ~/.xsesion
```

For example, if you place this in _~.xsesion_:

```bash
# Internet
nm-applet &

# Keyboard layout
setxkbmap latam &

# composer
picom &

# Automount Devices
udiskie -t &

# Wallpaper
feh --bg-scale YOUR_WALLPAPER
```

I recommend that you copy in this file the other configs that be in my [_.xsesion_ file](https://github.com/Sherguioth/dotfiles/blob/main/.xsession). Every time you login you will have all systray utilities, your keyboard layout and the other configs ready.

## Other configuration and tools

### AUR helper

Now that you have some software that allows you tu use your computer without
losing your patience, it's time to do more interesting stuff. First, install an
**[AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers)**, I use
**[yay](https://github.com/Jguer/yay)**:

```bash
sudo pacman -S base-devel git
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```

With an _Arch User Repository helper_, you can basically install
any piece of software on this planet that was meant to run on Linux.

### File Manager

We've done all files stuff through a terminal up to this point, but you can
install graphical or terminal based file managers.
For a graphical one, I suggest
**[thunar](https://wiki.archlinux.org/index.php/Thunar)**
and for a terminal based one,
**[ranger](https://wiki.archlinux.org/index.php/Ranger)**, although this one
is very vim-like, only use it if you know how to move in vim.

```bash
sudo pacman -S thunar ranger
```

### GTK Theming

The moment you have been wating for has arrived, you are finally going to
install a dark theme. I use _Material Black Colors_, so go grab a flavor
[here](https://www.gnome-look.org/p/1316887/) and the matching icons
[here](https://www.pling.com/p/1333360/).

I suggest starting with
_Material-Black-Blueberry_ and _Material-Black-Blueberry-Suru_. You can find
other GTK themes [on this page](https://www.gnome-look.org/browse/cat/135/).
Once you have your theme folders downloaded, this is what you do:

```bash
# Assuming you have downloaded Material-Black-Blueberry
cd Downloads/
sudo pacman -S unzip
unzip Material-Black-Blueberry.zip
unzip Material-Black-Blueberry-Suru.zip
rm Material-Black*.zip
# Make your themes available
sudo mv Material-Black-Blueberry /usr/share/themes
sudo mv Material-Black-Blueberry-Suru /usr/share/icons
```

Now edit **~/.gtkrc-2.0** and **~/.config/gtk-3.0/settings.ini** by adding
these lines:

```ini
# ~/.gtkrc-2.0
gtk-theme-name = "Material-Black-Blueberry"
gtk-icon-theme-name = "Material-Black-Blueberry-Suru"
# ~/.config/gtk-3.0/settings.ini
gtk-theme-name = Material-Black-Blueberry
gtk-icon-theme-name = Material-Black-Blueberry-Suru
```

Next time you log in, these changes will be visible. You can also install a
different cursor theme, for that you need
**[xcb-util-cursor](https://www.archlinux.org/packages/extra/x86_64/xcb-util-cursor/)**.
The theme I use is
[Breeze](https://www.gnome-look.org/p/999927/), download it and then:

```bash
sudo pacman -S xcb-util-cursor
cd Downloads/
tar -xf Breeze.tar.gz
sudo mv Breeze /usr/share/icons
```

Edit **/usr/share/icons/default/index.theme** by adding this:

```ini
[Icon Theme]
Inherits = Breeze
```

Now, again, edit **~/.gtkrc-2.0** and **~/.config/gtk-3.0/settings.ini**:

```ini
# ~/.gtkrc-2.0
gtk-cursor-theme-name = "Breeze"
# ~/.config/gtk-3.0/settings.ini
gtk-cursor-theme-name = Breeze
```

Make sure not to mistype the names of your themes and icons, they should
match the names of the directories where they are located, the ones you can
see in this output:

```bash
ls /usr/share/themes
ls /usr/share/icons
```

Remember that you will only see the new theme if you log in again.
There are also graphical frontends for changing themes, I just prefer the
traditional way of editing files though, but you can use
**[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**,
which is a desktop environment independent GUI for this task, and it lets you
preview themes.

```bash
sudo pacman -S lxappearance
```

Finally, if you want tranparency and fancy looking things, install a compositor:

```bash
sudo pacman -S picom
# Run it like so, place it in ~/.xrofile
picom &
```

### Lightdm theming

We can also change the theme of _lightdm_ and make it look cooler, because why
not? We need another greeter, and some theme, namely
**[lightdm-webkit2-greeter](https://www.archlinux.org/packages/community/x86_64/lightdm-webkit2-greeter/)**
and **[lightdm-webkit-theme-aether](https://aur.archlinux.org/packages/lightdm-webkit-theme-aether/)**:

```bash
sudo pacman -S lightdm-webkit2-greeter
yay -S lightdm-webkit-theme-aether
```

These are the configs you need to make:

```ini
# /etc/lightdm/lightdm.conf
[Seat:*]
# ...
# Uncomment this line and set this value
greeter-session = lightdm-webkit2-greeter
# ...
# /etc/lightdm/lightdm-webkit2-greeter.conf
[greeter]
# ...
webkit_theme = lightdm-webkit-theme-aether
```

Ready to go.

### Multimedia

There are dozens of programs for multimedia stuff, check
[this page](https://wiki.archlinux.org/index.php/List_of_applications/Multimedia).

#### Video and audio

No doubt
[vlc](<https://wiki.archlinux.org/index.php/VLC_media_player_(Espa%C3%B1ol)>)
is exactly what you need:

```bash
sudo pacman -S vlc
```

## Apps

| Key                 | Action                        |
| ------------------- | ----------------------------- |
| **mod + m**         | launch rofi                   |
| **mod + shift + m** | window nav (rofi)             |
| **mod + b**         | launch browser (firefox)      |
| **mod + e**         | launch file explorer (thunar) |
| **mod + return**    | launch terminal (alacritty)   |
| **mod + r**         | redshift                      |
| **mod + shift + r** | stop redshift                 |
| **mod + s**         | screenshot (scrot)            |

## Software

### Basic utilities

| Software                                                                                    | Utility                  |
| ------------------------------------------------------------------------------------------- | ------------------------ |
| **[networkmanager](https://wiki.archlinux.org/index.php/NetworkManager)**                   | Self explanatory         |
| **[network-manager-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)** | _NetworkManager_ systray |
| **[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**                           | Self explanatory         |
| **[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**             | _pulseaudio_ GUI         |
| **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**                    | Automounter              |
| **[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**                                 | NTFS read & write        |
| **[arandr](https://www.archlinux.org/packages/community/any/arandr/)**                      | GUI for _xrandr_         |
| **[volumeicon](https://www.archlinux.org/packages/community/x86_64/volumeicon/)**           | Volume systray           |

### Fonts, theming and GTK

| Software                                                                               | Utility                    |
| -------------------------------------------------------------------------------------- | -------------------------- |
| **[Picom](https://wiki.archlinux.org/index.php/Picom)**                                | Compositor for Xorg        |
| **[Agave Nerd Font](https://github.com/blobject/agave)**                               | Nerd Font for icons        |
| **[JetBrainsMono Nerd Font](https://www.jetbrains.com/lp/mono/)**                      | Nerd Font for icons        |
| **[UbuntuMono Nerd Font](https://aur.archlinux.org/packages/nerd-fonts-ubuntu-mono/)** | Nerd Font for icons        |
| **[Material Black](https://www.gnome-look.org/p/1316887/)**                            | GTK theme and icons        |
| **[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**  | GUI for changing themes    |
| **[feh](https://wiki.archlinux.org/index.php/Feh)**                                    | CLI for setting wallpapers |

### Apps

| Software                                                              | Utility                  |
| --------------------------------------------------------------------- | ------------------------ |
| **[alacritty](https://wiki.archlinux.org/index.php/Alacritty)**       | Terminal emulator        |
| **[thunar](https://wiki.archlinux.org/index.php/Thunar)**             | Graphical file explorer  |
| **[ranger](https://wiki.archlinux.org/index.php/Ranger)**             | Terminal based explorer  |
| **[neovim](https://wiki.archlinux.org/index.php/Neovim)**             | Terminal based editor    |
| **[rofi](https://wiki.archlinux.org/index.php/Rofi)**                 | Menu and window switcher |
| **[scrot](https://wiki.archlinux.org/index.php/Screen_capture)**      | Screenshot               |
| **[trayer](https://www.archlinux.org/packages/extra/x86_64/trayer/)** | Systray                  |
| **[nvm](https://github.com/nvm-sh/nvm)**                              | Node Verson Manager      |
