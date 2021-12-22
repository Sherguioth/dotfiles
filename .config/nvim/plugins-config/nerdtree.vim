" NerdTree
nmap <Leader>nt :NERDTreeToggle<CR>
nmap <Leader>nf :NERDTreeFind<CR>

" Close NERDTreeFind when opne a file
let NERDTreeQuitOnOpen = 1

" Files ignored
let g:NERDTreeIgnore=['\.rcb$', '\.pyc$', '\.db$', '\.sqlite$', '__pycache__']
