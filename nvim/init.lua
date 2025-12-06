vim.g.mapleader =" " -- space leader key

local o = vim.opt

o.number = true -- enable line numbers
o.relativenumber = true -- enable relative line numbers
o.smartindent = true -- enable correctly indenting after {
o.autoindent = true -- enable copying indent from current line
o.cursorline = true -- enable cursor line
o.hlsearch = true -- enable highlighted search
o.ignorecase = true -- enable ingore case when searching
o.incsearch = true -- enable incremental search
o.swapfile = true -- disable swapfile
o.winborder = "rounded" -- set rounded border for hover popup

vim.lsp.enable({
    "lua_ls",
    "ruff",
    "rust_analyzer",
    "ts_ls",
    "ty",
})
vim.diagnostic.config({virtual_text = true})
o.signcolumn = 'yes' -- always who the sign column
