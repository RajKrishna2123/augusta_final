import os

# Function to parse env_var.yaml manually and convert it to a string of environment variables
def parse_env_vars(file_path):
    env_vars = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any surrounding whitespace and skip empty lines or comments
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Split the line into key and value
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip().strip('"').strip("'")
                value = value.strip().strip('"').strip("'")
                print(value)
                env_vars.append(f'-e "{key}"="{value}"')
            else:
                print(f"Warning: Skipping malformed line: {line}")

    return ' '.join(env_vars)

# Constants
IMAGE_NAME = 'rkd3d9/django:latest'
CONTAINER_NAME = 'augusta_crm'
ENV_FILE_PATH = 'env_var.yaml'

# Get local path from user
LOCAL_PATH = str(input("Enter the local full path from source disk to the project DIR: "))

# Parse environment variables from env_var.yaml
env_vars = parse_env_vars(ENV_FILE_PATH)

# Docker run command
docker_command = (
    f"docker run -it --rm {env_vars} -p 9199:9199 -p 9099:9099 -p 9005:9005 -p 9000:9000 -p 8085:8085 -p 8080:8080 -p 5001:5001 -p 5000:5000 -p 4000:4000 -p 9299:9299 -p 9399:9399 -p 8000:8000 -v {LOCAL_PATH}:/app --name {CONTAINER_NAME} {IMAGE_NAME}"
)

print(docker_command)
os.system(docker_command)
