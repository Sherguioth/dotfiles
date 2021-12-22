# Neovim Configs

To use all plugins and configs we need install some dependencies

```bash
# Install only those you don't have
sudo pacman -S nodejs npm python python python-pip ruby rubygems lua

pip install neovim jedi pylint
gem install neovim
sudo npm i -g neovim

# Some other dependencies
sudo pacman -S xsel fzf ripgrep fd the_silver_searcher prettier
```

Then execute :PlugInstall inside neovim.
