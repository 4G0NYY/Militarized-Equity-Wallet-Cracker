#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Failed to install dependencies. Exiting."
    exit 1
fi

echo "Dependencies installed successfully."
echo "Starting the application..."
python index.py
