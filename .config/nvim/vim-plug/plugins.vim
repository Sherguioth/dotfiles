call plug#begin('~/.config/nvim/plugged')

" Themes --------------------------------
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'joshdick/onedark.vim'

" IDE -----------------------------------
Plug 'sheerun/vim-polyglot'		 " Syntax support
Plug 'easymotion/vim-easymotion' " Easy navetation in file
Plug 'mattn/emmet-vim'           " HTML/ CSS snipets
Plug 'junegunn/fzf', {'do': {-> fzf#install()}}
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'scrooloose/nerdtree'
Plug 'alvan/vim-closetag'
Plug 'ryanoasis/vim-devicons'
Plug 'airblade/vim-rooter'
Plug 'Yggdroot/indentLine'
Plug 'kevinhwang91/rnvimr', {'do': 'make sync'} " Ranger

" Typing -------------------------------
Plug 'jiangmiao/auto-pairs'    " Auto close brackets
Plug 'tpope/vim-commentary'    " Easy commentaries
Plug 'editorconfig/editorconfig-vim'
Plug 'prettier/vim-prettier', {'do': 'yarn install'}

" Git ----------------------------------
Plug 'tpope/vim-fugitive'
Plug 'mhinz/vim-signify'

call plug#end()
