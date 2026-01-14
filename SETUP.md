# SETUP INSTRUCTIONS

## Prerequisites
- Python 3.8+
- Binance Futures Testnet account
- API credentials (Key + Secret)

## Quick Setup

1. **Get API Credentials**
   - Visit: https://testnet.binancefuture.com/
   - Register/Login
   - Generate API Key with Futures permissions

2. **Install Bot**
   ```bash
   # Run setup script (automatic)
   ./setup.sh
   
   # OR manual setup:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure API**
   ```bash
   cp .env.example .env
   nano .env  # Add your API key and secret
   ```

4. **Run Bot**
   ```bash
   source venv/bin/activate
   python main.py
   ```
