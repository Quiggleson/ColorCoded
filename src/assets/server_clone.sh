#!/bin/bash

# Hello
echo "Hello!"

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Check if git is installed
if ! command -v git &> /dev/null
then
    # If it isn't, install it
    sudo apt install git -y
fi

# Set the script's current working directory
DIR="/home/$USER"

# Set the target directory to the current directory + color-coded
TARGET_DIR="$DIR/color-coded"

# Print target dir to terminal
echo "Target directory: $TARGET_DIR"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    # If it doesn't exist, clone the repo to the target directory
    git clone https://github.com/Quiggleson/ColorCoded.git "$TARGET_DIR"
else
    # If it does exist, cd into it and pull the latest changes
    cd "$TARGET_DIR"
    git pull
fi

# Check if node is installed
if ! command -v node &> /dev/null
then
    echo "Please install node"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null
then
    echo "Please install npm"
    exit 1
fi

# Run npm i in $TARGET_DIR
npm i --prefix "$TARGET_DIR"

# Create the venv for python in $TARGET_DIR if it doesn't exist
if [ ! -d "$TARGET_DIR/.venv" ]; then
    python3 -m venv "$TARGET_DIR/.venv"
fi

# Move into the venv for python
source "$TARGET_DIR/.venv/bin/activate"

# Run pip install -r ./src/api/requirements.txt
pip3 install -r "$TARGET_DIR/src/api/requirements.txt"

# Run the python server
python3 "$TARGET_DIR/src/api/app.py" &

# Change directory into $TARGET_DIR and run ng serve
cd "$TARGET_DIR" && ng serve

# Running
echo "Still running!"

# Handle Control+C to stop the servers
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

# Wait for the servers to stop
wait

# Goodbye
echo "Goodbye!"

# Exit the script
exit 0