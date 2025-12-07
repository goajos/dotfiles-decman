vim.g.mapleader =" " -- space leader key

local o = vim.opt

o.tabstop = 4 -- tab character is 4 spaces
o.expandtab = true -- pressing tab inserts spaces instead of a tab
o.softtabstop = 4 -- number of spaces inserted instead of a tab character
o.shiftwidth = 4 -- number of spaces inserted when indenting
o.number = true -- enable line numbers
o.relativenumber = true -- enable relative line numbers
o.smartindent = true -- enable correctly indenting after {
o.autoindent = true -- enable copying indent from current line
o.cursorline = true -- enable cursor line
o.hlsearch = true -- enable highlighted search
o.ignorecase = true -- enable ingore case when searching
o.incsearch = true -- enable incremental search
o.swapfile = true -- disable swapfile
o.wrap = false -- disable line wrapping
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
