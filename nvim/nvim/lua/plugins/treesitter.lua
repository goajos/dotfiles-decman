vim.pack.add({
    { src = "https://github.com/nvim-treesitter/nvim-treesitter", version = "main" },
})

local ts_parsers = {
    "bash",
    "c",
    "css",
    "csv",
    "dockerfile",
    "gitignore",
    "html",
    "javascript",
    "json",
    "lua",
    "markdown",
    "python",
    "sql",
    "toml",
    "tsx",
    "typescript",
    "vim",
    "vimdoc",
    "yaml"
}

local nts = require("nvim-treesitter")
nts.install(ts_parsers)
vim.api.nvim_create_autocmd("PackChanged", {
    callback = function()
        nts.update()
    end
})

vim.api.nvim_create_autocmd("FileType", {
    callback = function(args)
        local ft = args.match
        local lang = vim.treesitter.language.get_lang(ft)
        if vim.treesitter.language.add(lang) then
            vim.bo.indentexpr = "v:lua.require'nvim-treesitter'.indentexpr()"
            vim.treesitter.start()
        end
    end
})
