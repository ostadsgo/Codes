# --------------------------------------------
def search_key(config_key: str, config: dict):
    # TODO: FIX SHITTY CODE
    for key in config.keys():
        if key == config_key:
            return config_key


# -----------------------------------------------
def search_key2(config_key: str, config: dict):
    return config.get(config_key)
