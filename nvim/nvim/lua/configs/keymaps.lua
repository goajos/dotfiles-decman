-- leader key
vim.keymap.set('n','<Space>','<Nop>', { desc = "Don't move cursor when using leader key" })

-- center screen when jumping
vim.keymap.set("n", "n", "nzzzv", { desc = "Next search result (centered)" })
vim.keymap.set("n", "N", "Nzzzv", { desc = "Previous search result (centered)" })
vim.keymap.set("n", "<C-d>", "<C-d>zz", { desc = "Half page down (centered)" })
vim.keymap.set("n", "<C-u>", "<C-u>zz", { desc = "Half page up (centered)" })

-- files navigation
vim.keymap.set("n","<leader>cd",":Lexplore<CR>", { desc = "Open the netrw directory listing" })
vim.keymap.set("n", "<leader>ff", ":find ", { desc = "Find file" })

-- buffers
vim.keymap.set("n", "<leader>bn", "<Cmd>bnext<CR>", { desc = "Next buffer" })
vim.keymap.set("n", "<leader>bp", "<Cmd>bprevious<CR>", { desc = "Previous buffer" })
vim.keymap.set("n", "<leader>bb", ":buffers<CR>", { desc = "Show all active buffers" })

-- terminals
vim.keymap.set("t", "<Esc>", "<C-\\><C-n>", { desc = "Leave terminal mode"})
vim.keymap.set("t", "<C-v><Esc>", "<Esc>", { desc = "Map <Esc> to terminal buffer" })
vim.keymap.set("n", "<leader>t", ":tabedit | :terminal<CR>", { desc = "Open a terminal buffer in a new tab" })

-- search
vim.keymap.set("n", "<leader>/", ":noh<CR>", { desc = "Clear search highlighting" })

