call plug#begin('~/.config/nvim/plugged')

" Themes --------------------------------
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" IDE -----------------------------------
Plug 'sheerun/vim-polyglot'		 " Syntax support
Plug 'easymotion/vim-easymotion'
Plug 'mattn/emmet-vim'
Plug 'junegunn/fzf', {'do': {-> fzf#install()}}
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'scrooloose/nerdtree'
Plug 'alvan/vim-closetag'
Plug 'ryanoasis/vim-devicons'

" Typing -------------------------------
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-commentary'

call plug#end()
