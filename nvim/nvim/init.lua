if vim.g.vscode then
    -- vscode neovim options
    -- leader key
    vim.g.mapleader =" " -- space leader key
    vim.g.maplocalleader =" " -- space local leader key
    vim.keymap.set('n','<Space>','<Nop>', { desc = "Don't move cursor when using leader key" })

    -- center screen when jumping
    vim.keymap.set("n", "n", "nzzzv", { desc = "Next search result (centered)" })
    vim.keymap.set("n", "N", "Nzzzv", { desc = "Previous search result (centered)" })
    vim.keymap.set("n", "<C-d>", "<C-d>zz", { desc = "Half page down (centered)" })
    vim.keymap.set("n", "<C-u>", "<C-u>zz", { desc = "Half page up (centered)" })

    vim.opt.path:append("**") -- build in fuzzy find
    vim.opt.grepprg = "rg --vimgrep" -- use ripgrep if available

    -- search options
    vim.opt.ignorecase = true -- case-insensitive search
    vim.opt.smartcase = true -- case-sensitive if uppercase in search term
    vim.opt.hlsearch = true -- highlight search results
    vim.keymap.set("n", "<leader>/", ":noh<CR>", { desc = "Clear search highlighting" })
    
    -- files navigation
    vim.keymap.set("n","<leader>cd",":Ex<CR>")
    vim.keymap.set("n", "<leader>ff", ":find ")
else
    require("configs.options")
    require("configs.globals")
    require("configs.keymaps")
    require("configs.autocmds")
    require("plugins.github-nvim-theme")
end