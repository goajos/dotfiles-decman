-- basic options
vim.opt.number = true -- line numbers
vim.opt.relativenumber = true -- relative line numbers
vim.opt.cursorline = true -- highlight current line
vim.opt.scrolloff = 10 -- keep 10 lines above/below cursor
vim.opt.sidescrolloff = 10 -- keep 10 columns left/right of cursor
vim.opt.wrap = false -- don't wrap lines
vim.opt.cmdheight = 1 -- command line height

-- tab/indent options
vim.opt.tabstop = 4 -- tab width
vim.opt.shiftwidth = 4 -- indent width
vim.opt.softtabstop = 4 -- soft tab width
vim.opt.expandtab = true -- use spaces instead of tabs
vim.opt.autoindent = true -- copy indent from currentline
vim.opt.smartindent = true -- smart audo indenting

-- search options
vim.opt.ignorecase = true -- case-insensitive search
vim.opt.smartcase = true -- case-sensitive if uppercase in search term
vim.opt.hlsearch = true -- highlight search results

-- grep options
vim.opt.grepprg = "rg --vimgrep" -- use ripgrep if available

-- visual options
vim.opt.termguicolors = true -- enable 24-bit colors
vim.opt.signcolumn = "yes" -- always show sign column
vim.opt.showmatch = true -- highlight matching brackets
vim.opt.completeopt = "menuone,noinsert,noselect" -- completion options
vim.opt.pumheight = 10 -- max popup menu items
vim.opt.pumblend = 10 -- popup menu transparency
vim.opt.winblend = 10 -- floating window transparency

-- split options
vim.opt.splitbelow = true -- horizontal splits open below
vim.opt.splitright = true -- vertical splits open to the right

-- behavior options
vim.opt.backspace = "indent,eol,start" -- normal backspace behavior
vim.opt.iskeyword:append("-") -- dash is part of a word
vim.opt.path:append("**") -- search in subfolders with `gf`
vim.opt.mouse = "a" -- enable mouse in all modes
vim.opt.wildmode = "longest,list" -- completion mode for cli
vim.opt.wildignorecase = true -- case-insensitive tab completion

-- folding options
vim.opt.foldmethod = "expr" -- use expressions for folding
vim.opt.foldexpr = "v:lua.vim.treesitter.foldexpr()"  -- use treesitter for folding
vim.opt.foldlevel = 99 -- keep all fold open by default

-- file options
vim.opt.backup = false -- no backup file
vim.opt.writebackup = false -- no backup before overwritting
vim.opt.swapfile = false -- no swap file
vim.opt.undofile = true -- persistent undo
vim.opt.autoread = true -- auto reload file if changed from outside
vim.opt.diffopt:append({"vertical"}) -- vertical diff splits
vim.opt.diffopt:append({"linematch:60"}) -- better diff highlighting

-- setup undo directory
local undodir = "/home/jappe/.local/share/nvim/undo"
vim.opt.undodir = undodir
if vim.fn.isdirectory(undodir) == 0 then
    vim.fn.mkdir(undodir, "p")
end

-- transparancy options
vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
vim.api.nvim_set_hl(0, "NormalNC", { bg = "none" })
vim.api.nvim_set_hl(0, "EndOfBuffer", { bg = "none" }
