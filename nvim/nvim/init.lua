if vim.g.vscode then
    local vscode = require("vscode")
    -- vscode neovim options
    -- leader key
    vim.g.mapleader =" " -- space leader key
    vim.g.maplocalleader =" " -- space local leader key
    vim.keymap.set('n','<Space>','<Nop>', { desc = "Don't move cursor when using leader key" })

    vim.opt.clipboard = "unnamedplus" -- use system clipboard:

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
    vim.keymap.set({"n", "v"}, "]q", function()
        vscode.call("search.action.focusNextSearchResult")
        vscode.call("vscode-neovim.escape")
    end)
    vim.keymap.set({"n", "v"}, "[q", function()
        vscode.call("search.action.focusPreviousSearchResult")
        vscode.call("vscode-neovim.escape")
    end)

    -- files navigation
    vim.keymap.set("n","<leader>cd", function()
        vscode.call("workbench.view.explorer")
    end)
    vim.keymap.set("n", "<leader>ff", function()
        vscode.call("workbench.action.findInFiles")
    end)

    -- terminal
    vim.keymap.set("n", "<leader>t", function()
        vscode.call("workbench.action.terminal.toggleTerminal")
    end)
    vim.keymap.set("n", "<leader>tt", function()
        vscode.call("workbench.action.terminal.new")
    end)

    -- debug
    vim.keymap.set("n", "<leader>dr", function()
        vscode.call("workbench.debug.action.toggleRepl")
    end)

    -- code actions
    vim.keymap.set("n", "<leader>gra", function()
        vscode.call("editor.action.quickFix")
    end)
    vim.keymap.set("n", "<leader>gri", function()
        vscode.call("editor.action.goToImplementation")
    end)
    vim.keymap.set("n", "<leader>grn", function()
        vscode.call("editor.action.rename")
    end)
    vim.keymap.set("n", "<leader>grr", function()
        vscode.call("editor.action.referenceSearch.trigger")
    end)
    vim.keymap.set("n", "<leader>grt", function()
        vscode.call("editor.action.goToTypeDefinition")
    end)
    vim.keymap.set("n", "gd", function()
        vscode.call("editor.action.revealDefinition")
    end)
    vim.keymap.set("n", "<leader>gD", function()
        vscode.call("editor.action.revealDeclaration")
    end)
    vim.keymap.set("n", "<leader>gO", function()
        vscode.call("workbench.action.gotoSymbol")
    end)
    -- invalid with vscode save and save as?
    -- vim.keymap.set("i", "<C-S>", function()
    --     vscode.call("editor.action.triggerParameterHints")
    -- end)
    vim.keymap.set("n", "K", function()
        vscode.call("editor.action.showHover")
    end)
    vim.keymap.set("n", "<leader>F", function()
        vscode.call("editor.action.formatDocument")
    end)

else
    -- require("configs.options")
    -- require("configs.globals")
    -- require("configs.keymaps")
    -- require("configs.autocmds")
    -- require("plugins.github-nvim-theme")
    -- require("plugins.treesitter")
    -- require("plugins.nvim-lspconfig")
end
