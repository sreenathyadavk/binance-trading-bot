#!/bin/bash

# Binance Trading Bot - Quick Setup Script
# This script automates the setup process for the trading bot

echo "========================================"
echo "Binance Trading Bot - Setup"
echo "========================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "IMPORTANT: Please edit .env file and add your Binance API credentials:"
    echo "  nano .env"
    echo ""
    echo "Get your credentials from: https://testnet.binancefuture.com/"
else
    echo ""
    echo "✓ .env file already exists"
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To run the bot:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Update .env with your API credentials"
echo "  3. Run the bot: python main.py"
echo ""
