-- TODO: how to set this up with separate modules?
if vim.g.vscode then
    local vscode = require("vscode")
    -- vscode neovim options
    -- Leader key
    vim.g.mapleader = " "      -- space leader key
    vim.g.maplocalleader = " " -- space local leader key
    vim.keymap.set("n", "<Space>", "<Nop>", { desc = "Don't move cursor when using leader key" })
    vim.opt.timeoutlen =  2000 -- time in msecs to wait for a mapped sequence

    vim.opt.clipboard = "unnamedplus" -- use system clipboard:
    vim.keymap.set("v", "<Leader>p", '"_dP') -- paste without overwriting the register

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
    vim.keymap.set("n", "<Leader>/", ":noh<CR>", { desc = "Clear search highlighting" })
    vim.keymap.set({ "n", "v" }, "]q", function()
        vscode.action("search.action.focusNextSearchResult")
        vscode.action("vscode-neovim.escape")
    end)
    vim.keymap.set({ "n", "v" }, "[q", function()
        vscode.action("search.action.focusPreviousSearchResult")
        vscode.action("vscode-neovim.escape")
    end)

    -- source control
    vim.keymap.set("n", "<Leader>scm", function()
        vscode.action("workbench.view.scm")
    end)

    -- files navigation
    vim.keymap.set("n", "<Leader>f", function()
        vscode.action("workbench.files.action.showActiveFileInExplorer")
    end)
    vim.keymap.set("n", "<Leader>ff", function()
        vscode.action("workbench.action.findInFiles")
    end)
    -- buffers (=views)
    vim.keymap.set("n", "<Leader>b", function()
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
    vim.keymap.set("n", "<Leader>t", function()
        vscode.action("workbench.action.terminal.toggleTerminal")
    end)
    vim.keymap.set("n", "<Leader>tt", function()
        vscode.action("workbench.action.terminal.new")
    end)
    -- output
    vim.keymap.set("n", "<Leader>to", function()
        vscode.action("workbench.action.output.toggleOutput")
    end)
    -- debug
    vim.keymap.set("n", "<Leader>tr", function()
        vscode.action("workbench.debug.action.toggleRepl")
    end)
    vim.keymap.set("n", "<Leader>dd", function()
        vscode.action("workbench.view.debug")
    end)

    -- code
    vim.keymap.set({"n", "v"}, "<Leader>cr", function()
        vscode.action("editor.action.rename")
    end)

    -- file
    vim.keymap.set("n", "<Leader>w", function()
        vscode.action("workbench.action.files.save")
    end)
    vim.keymap.set("n", "<Leader>q", function()
        vscode.action("workbench.action.closeActiveEditor")
    end)
else
    -- TODO: set up undo dir/undo file?
    vim.g.mapleader = " "      -- space leader key
    vim.g.maplocalleader = " " -- space local leader key
    vim.keymap.set("n", "<Space>", "<Nop>", { desc = "Don't move cursor when using leader key" })
    vim.opt.clipboard = "unnamedplus" -- use system clipboard:
    vim.keymap.set({"n", "v"}, "<Leader>p", '"_dP', { desc = "Paste without overwriting the register" })
    -- vim.keymap.set({"n", "v"}, "d", '"_d', { desc = "Delete to lackhole register" })
    -- vim.keymap.set({"n", "v"}, "x", '"_x', { desc = "Delete char to blackhole register" })
    vim.opt.ignorecase = true -- case-insensitive search
    vim.opt.smartcase = true  -- case-sensitive if uppercase in search term
    vim.opt.hlsearch = true   -- highlight search results
    vim.opt.incsearch = true -- incremental search results
    -- vim.opt.number = true -- show line numbers
    -- vim.opt.relativenumber = true -- show relative line numbers
    vim.opt.termguicolors = true -- enable true colors
    vim.opt.swapfile = false -- disable swapfiles
    vim.opt.backup = false -- disable backup files
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
    vim.opt.sidescrolloff = 5 -- keep 5 columns left/right of cursor
    vim.opt.cmdheight = 1 -- linesize of the cmdline
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
            if vim.bo.filetype ~= "netrw" then
                vim.opt.signcolumn = "number"
                vim.opt.foldcolumn = "auto"
                vim.opt.number = true
                vim.opt.relativenumber = true
            end
        end
    })
    vim.api.nvim_create_autocmd({"WinLeave", "BufLeave"}, {
        callback = function()
            if vim.bo.filetype ~= "netrw" then
                vim.opt.signcolumn = "no"
                vim.opt.foldcolumn = "0"
                vim.opt.number = false
                vim.opt.relativenumber = false
            end
        end
    })

    -- vim.g.netrw_keepdir = 0 -- keep current dir and browse dir synced
    vim.g.netrw_banner = 0 -- disable banner
    vim.g.netrw_liststyle = 3 -- tree style listing
    vim.g.netrw_winsize = 15 -- window size of the explorer

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
    vim.lsp.config("roslyn_ls", {
        cmd = {
            "dotnet",
            "/home/jappe/Documents/roslyn_ls/lib/net10.0/Microsoft.CodeAnalysis.LanguageServer.dll",
            "--logLevel", -- this property is required by the server
            "Information",
            "--extensionLogDirectory", -- this property is required by the server
            vim.fs.joinpath(vim.uv.os_tmpdir(), 'roslyn_ls/logs'),
            "--stdio",
        }
    })
    vim.lsp.enable("roslyn_ls")
    vim.lsp.enable("ts_ls")
    vim.lsp.enable("ty")
    vim.lsp.inlay_hint.enable(true) -- inlay parameter hints
    vim.opt.winborder = 'rounded'
    vim.opt.winblend = 0 -- no floating window transparency

    local diagnostic_goto = function(next)
        return function()
            vim.diagnostic.jump({ count = next and 1 or -1, float = true })
        end
    end
    vim.keymap.set("n", "]d", diagnostic_goto(true), { desc = "Next diagnostics" })
    vim.keymap.set("n", "[d", diagnostic_goto(false), { desc = "Previous diagnostics" })
    vim.keymap.set("n", "<Leader>d", vim.diagnostic.open_float, { desc = "Floating line diagnostics" })

    -- file/buffers
    vim.keymap.set("n", "<Esc>", function()
        if vim.bo.filetype == "netrw" then
            vim.cmd("bd")
        end
    end)
    vim.keymap.set("n", "<Leader>f", ":Lex<CR>", { desc = "Open netrw file explorer" })
    vim.keymap.set("n", "<Leader>w", ":w<CR>", { desc = "Save current buffer" })
    vim.keymap.set("n", "<Leader>b", ":ls<CR>", { desc = "Show buffers" })
    vim.keymap.set("n", "<Leader>q", ":bd<CR>", { desc = "Close current buffer" })

    -- term
    vim.keymap.set("n", "<Leader>t", ":term<CR>", { desc = "Open terminal buffer" })
    vim.keymap.set("t", "<Esc>", "<C-\\><C-n>", { desc = "Leave terminal buffer insert mode" })
    vim.keymap.set("t", "<Leader><Esc>", "<Esc>", { desc = "Send <Esc> to terminal buffer" })

    -- search
    vim.keymap.set("n", "<Leader>/", ":noh<CR>", { desc = "Clear search highlighting" })
end
