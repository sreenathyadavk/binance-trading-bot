# Binance Futures Trading Bot

A trading bot for Binance Futures Testnet built as part of my internship application. Built with Python, it supports multiple order types and features an interactive CLI interface with comprehensive logging.

## Features

### Core Functionality
- Market Orders - Execute instant buy/sell orders at current market price
- Limit Orders - Place orders at specific price points
- Stop-Limit Orders - Advanced order type for risk management (Bonus Feature)
- Account Management - View balances, positions, and open orders
- Order Cancellation - Cancel pending orders

### Technical Highlights
- Beautiful CLI - Rich, interactive command-line interface with color-coded output
- Comprehensive Logging - All API requests, responses, and errors logged to file
- Input Validation - Robust validation for all user inputs
- Secure Configuration - Environment-based credential management
- Testnet Support - Risk-free testing on Binance Futures Testnet
- Modular Architecture - Clean, maintainable, and extensible code structure

## Prerequisites

- Python 3.8 or higher
- Binance Futures Testnet account
- API credentials (API Key and Secret)

## Quick Start

### 1. Register for Binance Testnet

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Click **"Sign Up"** or log in with GitHub
3. Complete registration and email verification
4. Fund your testnet account with virtual USDT (available in the faucet)

### 2. Generate API Credentials

1. Log in to [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Click on **API Key** in the top right menu
3. Click **"Create API Key"**
4. Give it a label (e.g., "Trading Bot")
5. **Save your API Key and Secret Key** (you won't be able to see the secret again!)
6. Enable **"Futures"** permissions for the API key

### 3. Installation

```bash
# Clone or navigate to the project directory
cd midnight-meteor

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API credentials
nano .env  # or use any text editor
```

Update `.env` with your credentials:
```env
BINANCE_API_KEY=your_actual_api_key_here
BINANCE_API_SECRET=your_actual_api_secret_here
TESTNET=True
```

### 5. Run the Bot

```bash
python main.py
```

## 📖 Usage Guide

### Main Menu

When you start the bot, you'll see an interactive menu:

```
╔═══════════════════════════════════════════╗
║   Binance Futures Trading Bot             ║
║   Testnet Mode - Risk-Free Trading        ║
╚═══════════════════════════════════════════╝

Main Menu
┌─────┬────────────────────────────────────┐
│  1  │ Place Market Order                 │
│  2  │ Place Limit Order                  │
│  3  │ Place Stop-Limit Order (Bonus)     │
│  4  │ View Account Balance               │
│  5  │ View Open Orders                   │
│  6  │ View Positions                     │
│  7  │ Cancel Order                       │
│  0  │ Exit                               │
└─────┴────────────────────────────────────┘
```

### Example: Placing a Market Order

1. Select option `1` from the menu
2. Enter symbol: `BTCUSDT`
3. Select side: `BUY` or `SELL`
4. Enter quantity: `0.001`
5. Review and confirm the order
6. Order executes immediately at market price

### Example: Placing a Limit Order

1. Select option `2` from the menu
2. Enter symbol: `ETHUSDT`
3. Select side: `BUY` or `SELL`
4. Enter quantity: `0.01`
5. Enter limit price: `2000.00`
6. Review and confirm
7. Order is placed and waits for price to reach your limit

### Example: Stop-Limit Order (Bonus)

1. Select option `3` from the menu
2. Enter symbol: `BTCUSDT`
3. Select side: `SELL` (for stop-loss) or `BUY` (for stop-entry)
4. Enter quantity: `0.001`
5. Enter **stop price** (trigger): `40000`
6. Enter **limit price** (execution): `39950`
7. Order activates when price hits stop, executes at limit

## 🏗️ Project Structure

```
midnight-meteor/
├── trading_bot/
│   ├── __init__.py       # Package initialization
│   ├── bot.py            # Core BasicBot class
│   ├── orders.py         # Order validation and formatting
│   ├── logger.py         # Logging configuration
│   └── config.py         # Configuration management
├── cli.py                # Interactive CLI interface
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment file
├── .env                  # Your credentials (not committed)
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── logs/                 # Log files directory
    └── trading_bot_*.log
```

##  Code Architecture

### BasicBot Class (`trading_bot/bot.py`)

The core trading bot with the following methods:

```python
class BasicBot:
    def __init__(api_key, api_secret, testnet=True)
    def place_market_order(symbol, side, quantity)
    def place_limit_order(symbol, side, quantity, price)
    def place_stop_limit_order(symbol, side, quantity, price, stop_price)
    def get_account_balance()
    def get_open_orders(symbol=None)
    def get_positions()
    def cancel_order(symbol, order_id)
```

### Order Validation (`trading_bot/orders.py`)

Validates all user inputs before sending to API:
- Symbol formatting
- Quantity validation (must be positive)
- Price validation (must be positive)
- Side validation (BUY/SELL only)

### Logging System (`trading_bot/logger.py`)

Dual-output logging:
- **File logs**: Detailed DEBUG level logs with timestamps
- **Console logs**: INFO level for user feedback
- **Format**: `timestamp | level | module | message`

##  API Documentation

### Endpoints Used

- `futures_account()` - Get account information
- `futures_account_balance()` - Get balance details
- `futures_create_order()` - Place orders
- `futures_get_open_orders()` - View pending orders
- `futures_position_information()` - View positions
- `futures_cancel_order()` - Cancel orders

All requests are logged with:
- Request parameters
- Response data
- Error messages (if any)
- Timestamps

##  Log Files

Log files are automatically created in the `logs/` directory with timestamps:

```
logs/trading_bot_20260114_141030.log
```

Each log entry includes:
- Timestamp
- Log level (DEBUG, INFO, WARNING, ERROR)
- Module name
- Detailed message

**Example log entries:**
```
2026-01-14 14:10:30 | INFO     | TradingBot | Initializing Binance client...
2026-01-14 14:10:31 | INFO     | TradingBot | ✓ Successfully connected to Binance Futures API
2026-01-14 14:11:15 | INFO     | TradingBot | Placing MARKET order: BUY 0.001 BTCUSDT
2026-01-14 14:11:16 | INFO     | TradingBot | ✓ Market order placed successfully
2026-01-14 14:11:16 | INFO     | TradingBot | Order ID: 12345, Status: FILLED
```

##  Troubleshooting

### "Configuration Error: API credentials not found"

- Make sure you've created `.env` file from `.env.example`
- Check that `BINANCE_API_KEY` and `BINANCE_API_SECRET` are set
- Ensure there are no extra spaces or quotes

### "API Error: Invalid API-key"

- Verify your API key is correct
- Make sure you copied the entire key without truncation
- Ensure the API key has Futures permissions enabled

### "API Error: Signature for this request is not valid"

- Check that your API secret is correct
- Make sure there are no extra spaces in the secret
- Regenerate API credentials if needed

### "Insufficient balance"

- Your testnet account needs USDT
- Visit the [Testnet Faucet](https://testnet.binancefuture.com/) to get free test funds
- Click on the faucet icon and claim testnet USDT

### Import Errors

- Make sure virtual environment is activated: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`


##  Dependencies

- **python-binance** (1.0.19) - Official Binance API wrapper
- **python-dotenv** (1.0.0) - Environment variable management
- **rich** (13.7.0) - Beautiful terminal formatting

## 🚀 Bonus Features Implemented

1. **Stop-Limit Orders** - Advanced order type for professional trading
2. **Enhanced CLI** - Beautiful, colorful interface with Rich library
3. **Comprehensive Error Handling** - Graceful handling of all edge cases
4. **Professional Logging** - Production-ready logging system
5. **Modular Design** - Clean separation of concerns

## 📧 Submission

This project includes:
- ✅ Complete source code
- ✅ Requirements file for easy setup
- ✅ Comprehensive documentation
- ✅ Log files demonstrating functionality
- ✅ Clean, professional code structure

## Author

**Sreenath**  
Email: sreenathyadavk@gmail.com  
College: Pulla Reddy Engineering College  
GitHub: [@sreenathyadavk](https://github.com/sreenathyadavk)  

Applying for: Junior Python Developer – Crypto Trading Bot

---

Project Repository: https://github.com/sreenathyadavk/binance-trading-bot

##  References

- [Binance Futures Testnet](https://testnet.binancefuture.com/)
- [Binance Futures API Documentation](https://binance-docs.github.io/apidocs/futures/en/)
- [python-binance Documentation](https://python-binance.readthedocs.io/)

##  License

This project is created for educational and internship application purposes.

---

**Note**: This bot uses the Binance Futures **Testnet** with virtual funds. No real money is involved in testing.
