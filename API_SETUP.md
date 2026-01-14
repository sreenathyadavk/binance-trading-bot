# API Credentials Setup Guide

## Step 1: Register for Binance Futures Testnet

1. Open your browser and go to: https://testnet.binancefuture.com/
2. Click **"Sign Up"** button (top right)
3. You can:
   - Register with email
   - OR login with GitHub account (recommended for quick setup)
4. Complete email verification if using email registration

## Step 2: Get Testnet Funds

1. After logging in, click on the **Wallet** icon
2. Click **"Get Test Funds"** or find the faucet option
3. Request USDT testnet funds (usually 10,000 USDT)
4. Funds should appear in your account immediately

## Step 3: Generate API Credentials

1. Click on **"API Management"** or your profile icon → **"API Key"**
2. Click **"Create API Key"**
3. Enter a label for your API key (e.g., "Trading Bot")
4. Complete any security verification (may require 2FA if enabled)
5. **IMPORTANT**: Copy and save both:
   - API Key
   - Secret Key (shown only once!)
6. Enable **Futures Trading** permission for the API key
7. (Optional) Set IP whitelist for additional security

## Step 4: Add Credentials to Bot

1. In your project directory, create `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` file:
   ```bash
   nano .env
   # or use any text editor
   ```

3. Add your credentials:
   ```env
   BINANCE_API_KEY=paste_your_api_key_here
   BINANCE_API_SECRET=paste_your_secret_key_here
   TESTNET=True
   ```

4. Save and close the file

## Step 5: Test Connection

Run the bot to test connection:
```bash
source venv/bin/activate
python main.py
```

If successful, you should see:
```
✓ Successfully connected to Binance Futures API
```

## Security Best Practices

✅ **DO:**
- Keep your API secret secure
- Use testnet for learning/testing
- Enable IP whitelist if possible
- Disable API key when not in use

❌ **DON'T:**
- Share your API secret
- Commit .env file to GitHub
- Use testnet keys on mainnet
- Give API keys withdrawal permissions (for real accounts)

## Troubleshooting

### "Invalid API-key" Error
- Check that you copied the entire API key
- Make sure there are no extra spaces
- Verify you're using Futures Testnet credentials

### "Signature invalid" Error
- Check that the API secret is correct
- Try regenerating the API key
- Ensure system time is synchronized

### "IP restricted" Error
- Add your current IP to whitelist in Binance
- OR remove IP restriction from API settings

## Need Help?

- Binance Testnet: https://testnet.binancefuture.com/
- Binance API Docs: https://binance-docs.github.io/apidocs/futures/en/
