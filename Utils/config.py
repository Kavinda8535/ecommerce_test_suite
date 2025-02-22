import yaml

#class Config:

# def __init__(self):

def load_config(env="dev"):  # Default to "dev"
    # with open('config.yaml', "r") as file:
    #     config = yaml.safe_load(file)
    # return config["environments"].get(env, config["environments"]["dev"])  # Fallback to dev
    # ****************
    with open("../config.yaml", "r") as stream:
        config = yaml.safe_load(stream)
    return config["environments"].get(env, config["environments"]["dev"])


# Example Usage
current_env = "dev"  # Change this to "dev", "test", or "prod" according to the what has in the config.yaml file...
CONFIG = load_config(current_env)

# Access values like:
# CONFIG["BASE_URL"]
# CONFIG["USERNAME"]
# CONFIG["PASSWORD"]
