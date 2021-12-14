# Created by Sherguioth for 5.8

# Themes
# git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
# source ~/powerlevel10k/powerlevel10k.zsh-theme
eval "$(starship init zsh)"

# Plugins
# curl -sL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh -o ~/.sudo.plugin.zsh
sudo=~/.sudo.plugin.zsh

# sudo pacman -S zsh-autosuggestions
autosuggestions=/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# sudo pacman -S zsh-syntax-highlighting
syntax=/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
# ~/.fzf/install
fzf=~/.fzf.zsh


# Aliases

alias grep='grep --color=auto'
alias cat='bat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'
alias dotfiles="git --git-dir $HOME/.dotfiles/ --work-tree $HOME"


# Colors

typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=magenta'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=magenta'
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=magenta'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=red'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=cyan'
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=cyan'
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=blue'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=blue'
ZSH_HIGHLIGHT_STYLES[path]='fg=blue'

# History

HISTSIZE=100000
SAVEHIST=100000
HISTFILE=~/.cache/zsh/history


# Vim keybindings

bindkey -v
export KEYTIMEOUT=1


# Autocomplete

setopt autocd
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list '' \
  'm:{a-z\-}={A-Z\_}' \
  'r:[^[:alpha:]]||[[:alpha:]]=** r:|=* m:{a-z\-}={A-Z\_}' \
  'r:|?=** m:{a-z\-}={A-Z\_}'
zmodload zsh/complist
autoload -Uz compinit
compinit

# Source plugins

if [[ -f $sudo ]]; then
    source $sudo
    bindkey -M vicmd '^[s' sudo-command-line # ALT + s
    bindkey -M viins '^[s' sudo-command-line # ALT + s
fi

[[ -f $autosuggestions ]] && source $autosuggestions
[[ -f $syntax ]] && source $syntax
[[ -f $fzf ]] && source $fzf


