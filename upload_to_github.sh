#!/bin/bash

# GitHub Upload Instructions
# Run this after creating a repository on GitHub

echo "========================================"
echo "Uploading to GitHub"
echo "========================================"
echo ""

# Initialize git if not already done
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    echo "✓ Git initialized"
fi

# Configure git with your details
echo ""
echo "Configuring git..."
git config user.name "Sreenath"
git config user.email "sreenathyadavk@gmail.com"
echo "✓ Git configured"

# Add all files
echo ""
echo "Adding files..."
git add .
echo "✓ Files added"

# Commit
echo ""
echo "Creating commit..."
git commit -m "Add Binance Futures Trading Bot - Internship Application

Features:
- Market orders (BUY/SELL)
- Limit orders (BUY/SELL)
- Stop-Limit orders (bonus)
- Enhanced CLI with Rich library (bonus)
- Comprehensive logging
- Professional documentation

Built by: Sreenath
College: Pulla Reddy Engineering College
For: Junior Python Developer position"

echo "✓ Commit created"

echo ""
echo "========================================"
echo "Next Steps:"
echo "========================================"
echo ""
echo "1. Go to: https://github.com/new"
echo "2. Create repository: binance-trading-bot"
echo "3. Make it PUBLIC"
echo "4. DON'T initialize with README"
echo "5. Copy the repository URL"
echo ""
echo "6. Then run:"
echo "   git remote add origin https://github.com/sreenathyadavk/binance-trading-bot.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "Your repository will be at:"
echo "https://github.com/sreenathyadavk/binance-trading-bot"
echo ""
