#!/bin/bash
set -e

# Get information about the container and the user
echo "User: $(whoami)"
echo "Home: $HOME"
echo "Shell: $SHELL"
echo "PWD: $PWD"

sudo service ssh start
sleep infinity