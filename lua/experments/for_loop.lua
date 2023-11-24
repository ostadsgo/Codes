local modules = { "config.autocmds", "config.options", "config.keymaps", "config.custom" }

for index, mod in ipairs(modules) do
    print(index, mod)
end
