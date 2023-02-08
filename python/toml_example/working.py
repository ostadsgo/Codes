import tomllib


with open("config.toml", "rb") as toml_file:
    config = tomllib.load(toml_file)

print(config, type(config))
print(config["username"])
print(config["password"])
