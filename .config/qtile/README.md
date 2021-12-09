# Qtile

## Instalation (Arch based)

Install Qtile and dependencies:

```bash
sudo pacman -S qtile pacman-contrib
yay -S nerd-fonts-ubuntu-mono
sudo pacman -S python-pip
pip install psutil
```

Clone this repository and copy my configs:

```bash
git clone https://github.com/Sherguioth/dotfiles.git
cp -r dotfiles/.config/qtile ~/.config
```

If the network widget doesn't work check ```./settings/widgets.py``` and look
for this line, you should find it inside a list called *primary_widgets*:

```python
# Change interface arg, use ip address command to find which one you need
 widget.Net(**base(bg='color3'), interface='wlp5s0'),
```