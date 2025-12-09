-- basic keybinds
vim.g.mapleader =" " -- space leader key
local map = vim.api.nvim_set_keymap
map('n','<leader>cd',':Ex<CR>', {noremap=true})

local o = vim.opt
-- basic options
o.swapfile = true -- disable swapfile
o.number = true -- enable line numbers
o.relativenumber = true -- enable relative line numbers
o.autoindent = true -- enable copying indent from current line
o.expandtab = true -- pressing tab inserts spaces instead of a tab
o.shiftwidth = 4 -- number of spaces inserted when indenting
o.softtabstop = 4 -- number of spaces inserted instead of a tab character
o.tabstop = 4 -- tab character is 4 spaces
o.smartindent = true -- enable correctly indenting after {
o.cursorline = true -- enable cursor line highlight
o.hlsearch = true -- enable highlighted search
o.wrap = false -- disable line wrapping

-- optional options
o.winborder = "rounded" -- set rounded border for hover popup

-- basic packages
vim.pack.add({
    {src= "https://github.com/ibhagwan/fzf-lua"},
})
map('n','<leader>ff',':FzfLua files<CR>', {noremap=true})
map('n','<leader>fb',':FzfLua buffers<CR>', {noremap=true})
map('n','<leader>fg',':FzfLua grep<CR>', {noremap=true})

-- lsp setup
vim.lsp.enable({
    "lua_ls",
    "ruff",
    "rust_analyzer",
    "ts_ls",
    "ty",
})
o.signcolumn = 'yes' -- always who the sign colum
vim.diagnostic.config({virtual_text = true})
