-- TODO: how to set this up with separate modules?
if vim.g.vscode then
    local vscode = require("vscode")
    -- vscode neovim options
    -- leader key
    vim.g.mapleader = " "      -- space leader key
    vim.g.maplocalleader = " " -- space local leader key
    vim.keymap.set("n", "<Space>", "<Nop>", { desc = "Don't move cursor when using leader key" })
    vim.opt.timeoutlen =  2000 -- time in msecs to wait for a mapped sequence

    vim.opt.clipboard = "unnamedplus" -- use system clipboard:
    vim.keymap.set("v", "<leader>p", '"_dP') -- paste without overwriting the register

    -- auto leave insert mode when changing buffers or window losing focus
    vim.api.nvim_create_autocmd({"BufLeave", "FocusLost"}, {
        pattern = "*",
        command = "stopinsert"
    })

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
    vim.keymap.set({"n", "v"}, "<leader>cr", function()
        vscode.action("editor.action.rename")
    end)

    -- file
    vim.keymap.set("n", "<leader>w", function()
        vscode.action("workbench.action.files.save")
    end)
    vim.keymap.set("n", "<leader>q", function()
        vscode.action("workbench.action.closeActiveEditor")
    end)
else
    -- TODO: set up undo dir?
    vim.g.mapleader = " "      -- space leader key
    vim.g.maplocalleader = " " -- space local leader key
    vim.keymap.set("n", "<Space>", "<Nop>", { desc = "Don't move cursor when using leader key" })
    vim.opt.clipboard = "unnamedplus" -- use system clipboard:
    vim.keymap.set("v", "<leader>p", '"_dp', { desc = "Paste without overwriting the register" })
    vim.opt.ignorecase = true -- case-insensitive search
    vim.opt.smartcase = true  -- case-sensitive if uppercase in search term
    vim.opt.hlsearch = true   -- highlight search results
    -- vim.opt.number = true -- show line numbers
    -- vim.opt.relativenumber = true -- show relative line numbers
    vim.opt.termguicolors = true -- enable true colors
    vim.opt.swapfile = false -- disable swapfiles
    vim.opt.autoindent = true -- enable auto indentation
    vim.opt.shiftwidth = 4 -- tab size for indentation
    vim.opt.expandtab = true -- use spaces for tabs
    vim.opt.tabstop = 4 -- tab size
    vim.opt.softtabstop = 4 -- tab size insert mode
    vim.opt.autoindent = true -- copy indent form cursorline
    vim.opt.smartindent = true -- smart auto indenting
    vim.opt.cursorline = true -- highlight cursor line
    -- vim.opt.signcolumn = "number" -- show sign column in the number column
    vim.opt.colorcolumn = "100" -- show column line at 100 chars
    vim.opt.wrap = true -- enable word wrap
    vim.opt.breakindent = true -- wrap lines continue visually
    vim.opt.scrolloff = 10 -- keep 10 lines above/below cursor
    vim.opt.cmdheight = 0 -- linesize of the cmdline
    vim.opt.splitright = true -- split windows right by default

    vim.opt.grepprg = "rg --vimgrep" -- use ripgrep
    vim.opt.path:append("**") -- buildin fuzzy finding

    vim.pack.add { "https://github.com/nvim-treesitter/nvim-treesitter" }
    require'nvim-treesitter'.install({
        "c_sharp",
        "cpp",
        "python",
        "typescript"
    })

    vim.opt.foldmethod = "expr"
    vim.opt.foldexpr =  "v:lua.vim.treesitter.foldexpr()"
    -- vim.opt.foldexpr = "v:lua.vim.lsp.foldexpr()"
    vim.opt.foldlevel = 99
    -- vim.opt.foldcolumn = "auto"
    vim.opt.fillchars = [[fold: ,foldopen:▼,foldclose:▶,foldsep: ,foldinner: ]]

    -- auto leave insert mode when changing windows or nvim losing focus
    vim.api.nvim_create_autocmd({"WinLeave", "FocusLost"}, {
        command = "stopinsert"
    })

    -- show sign/number only in active window
    vim.api.nvim_create_autocmd({"WinEnter", "BufEnter"}, {
        callback = function()
            vim.opt.signcolumn = "number"
            vim.opt.foldcolumn = "auto"
            vim.opt.number = true
            vim.opt.relativenumber = true
        end
    })
    vim.api.nvim_create_autocmd({"WinLeave", "BufLeave"}, {
        callback = function()
            vim.opt.signcolumn = "no"
            vim.opt.foldcolumn = "0"
            vim.opt.number = false
            vim.opt.relativenumber = false
        end
    })

    vim.g.netrw_keepdir = 0 -- keep current dir and browse dir synced
    -- vim.g.netrw_banner = 0 -- disable banner
    vim.g.netrw_liststyle = 3 -- tree style listing

    vim.pack.add({
      "https://github.com/projekt0n/github-nvim-theme"
    })
    vim.cmd[[colorscheme github_dark_default]]
    -- remove nvim window background for parent opacity
    vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
    vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    vim.api.nvim_set_hl(0, "NormalNC", { bg = "none" })

    vim.pack.add { "https://github.com/neovim/nvim-lspconfig" }

    vim.lsp.enable("clangd")
    vim.lsp.enable("lua_ls")
    vim.lsp.config("roslyn", {
        cmd = {
            'dotnet',
            '/home/jappe/.local/.bin/Microsoft.CodeAnalysis.LanguageServer.dll',
            '--logLevel', -- this property is required by the server
            'Information',
            '--extensionLogDirectory', -- this property is required by the server
            vim.fs.joinpath(vim.uv.os_tmpdir(), 'roslyn_ls/logs'),
            '--stdio',
        }
    })
    vim.lsp.enable("roslyn")
    vim.lsp.enable("ts_ls")
    vim.lsp.enable("ty")
    vim.lsp.inlay_hint.enable(true)

    -- file
    vim.keymap.set("n", "<leader>w", ":w<CR>", { desc = "Save current buffer" })
    vim.keymap.set("n", "<leader>q", ":bd<CR>", { desc = "Close current buffer" })
end
