with open("/home/saeed/.local/share/fish/fish_history") as f:
    lines = f.readlines()

cmds = []
for line in lines:
    if line.startswith('- cmd:'):
       cmd = line.split(':')
       cmds.append(cmd[1])
       

print(len(set(cmds)))
res = "".join(set(cmds))
with open("fishtozsh", 'w') as f:
    f.write(res)



