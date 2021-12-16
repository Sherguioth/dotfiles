let g:mapleader = "\<Space>"

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>

nmap <C-s> :w<CR>
nmap <C-q> :wq!<CR>

:imap jj <Esc>

nmap <Leader>; $a;<Esc>
nmap <Leader>rp :let @*=expand("%")<CR>
nmap <Leader>x :!node %<CR>

nmap <TAB> :bnext<CR>
nmap <S-TAB> :bprevious<CR>

xnoremap K :move '<-2<CR>gv-gv
xnoremap J :move '>+1<CR>gv-gv
