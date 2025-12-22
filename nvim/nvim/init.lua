if vim.g.vscode then
    local vscode = require("vscode")
    -- vscode neovim options
    -- leader key
    vim.g.mapleader = " "      -- space leader key
    vim.g.maplocalleader = " " -- space local leader key
    vim.keymap.set('n', '<Space>', '<Nop>', { desc = "Don't move cursor when using leader key" })
    vim.opt.timeoutlen =  2000 -- time in msecs to wait for a mapped sequence

    vim.opt.clipboard = "unnamedplus" -- use system clipboard:

    -- auto leave insert mode when changing buffers or window losing focus
    vim.api.nvim_create_autocmd({"BufLeave", "FocusLost"}, {
        pattern = "*",
        command = "stopinsert"
    })

    -- center screen when jumping
    vim.keymap.set("n", "n", "nzzzv", { desc = "Next search result (centered)" })
    vim.keymap.set("n", "N", "Nzzzv", { desc = "Previous search result (centered)" })
    vim.keymap.set("n", "<C-d>", "<C-d>zz", { desc = "Half page down (centered)" })
    vim.keymap.set("n", "<C-u>", "<C-u>zz", { desc = "Half page up (centered)" })

    vim.opt.path:append("**")        -- build in fuzzy find
    vim.opt.grepprg = "rg --vimgrep" -- use ripgrep if available

    -- search options
    vim.opt.ignorecase = true -- case-insensitive search
    vim.opt.smartcase = true  -- case-sensitive if uppercase in search term
    vim.opt.hlsearch = true   -- highlight search results
    vim.keymap.set("n", "<leader>/", ":noh<CR>", { desc = "Clear search highlighting" })
    vim.keymap.set({ "n", "v" }, "]q", function()
        vscode.action("search.action.focusNextSearchResult")
        vscode.action("vscode-neovim.escape")
    end)
    vim.keymap.set({ "n", "v" }, "[q", function()
        vscode.action("search.action.focusPreviousSearchResult")
        vscode.action("vscode-neovim.escape")
    end)

    -- source control
    vim.keymap.set("n", "<leader>scm", function()
        vscode.action("workbench.view.scm")
    end)

    -- files navigation
    vim.keymap.set("n", "<leader>cd", function()
        vscode.action("workbench.files.action.showActiveFileInExplorer")
    end)
    vim.keymap.set("n", "<leader>ff", function()
        vscode.action("workbench.action.findInFiles")
    end)
    -- buffers (=views)
    vim.keymap.set("n", "<leader>bd", function()
        vscode.action("workbench.action.closeActiveEditor")
    end)
    vim.keymap.set("n", "<leader>bb", function()
        vscode.action("workbench.action.quickOpen")
    end)
    -- buffer navigation
    vim.keymap.set("n", "<C-h>", function()
        vscode.action("workbench.action.navigateLeft")
    end)
    vim.keymap.set("n", "<C-j>", function()
        vscode.action("workbench.action.navigateDown")
    end)
    vim.keymap.set("n", "<C-k>", function()
        vscode.action("workbench.action.navigateUp")
    end)
    vim.keymap.set("n", "<C-l>", function()
        vscode.action("workbench.action.navigateRight")
    end)
    vim.keymap.set("n", "<Tab>", function()
        vscode.action("workbench.action.nextEditorInGroup")
    end)
    vim.keymap.set("n", "<S-Tab>", function()
        vscode.action("workbench.action.previousEditorInGroup")
    end)

    -- terminal
    vim.keymap.set("n", "<leader>t", function()
        vscode.action("workbench.action.terminal.toggleTerminal")
    end)
    vim.keymap.set("n", "<leader>tt", function()
        vscode.action("workbench.action.terminal.new")
    end)
    -- output
    vim.keymap.set("n", "<leader>to", function()
        vscode.action("workbench.action.output.toggleOutput")
    end)
    -- debug
    vim.keymap.set("n", "<leader>tr", function()
        vscode.action("workbench.debug.action.toggleRepl")
    end)
    vim.keymap.set("n", "<leader>dd", function()
        vscode.action("workbench.view.debug")
    end)

    -- code
    vim.keymap.set("n", "<leader>cr", function()
        vscode.action("editor.action.rename")
    end)

    -- file
    vim.keymap.set("n", "<leader>w", function()
        vscode.action("workbench.action.files.save")
    end)
else
    require("configs.options")
    require("configs.globals")
    require("configs.keymaps")
    require("configs.autocmds")
    -- require("plugins.treesitter")
    -- require("plugins.nvim-lspconfig")
end
