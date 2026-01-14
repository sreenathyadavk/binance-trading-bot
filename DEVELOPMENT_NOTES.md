# Development Notes

## What I Built

This is my trading bot project for the internship application. Spent about a week working on it, learning the Binance API documentation and implementing all the required features.

## Challenges I Faced

1. **API Documentation** - Binance docs were a bit confusing at first, especially understanding the difference between spot and futures markets. Had to read through multiple examples.

2. **Stop-Limit Orders** - Took me a while to understand the difference between stop price and limit price. Finally got it working after some trial and error on testnet.

3. **Error Handling** - Initially didn't handle API errors properly. Added try-except blocks after getting some connection errors during testing.

4. **CLI Interface** - Wanted something better than basic print statements. Found the Rich library which made the interface look much better.

## What I Learned

- Working with REST APIs and handling authentication
- Using python-binance library
- Input validation is really important when dealing with trading
- Logging everything helps a lot with debugging
- Environment variables for keeping API keys secure

## Future Improvements

If I had more time, I would add:
- Order history tracking with database
- Real-time price monitoring with WebSockets
- More advanced order types (OCO, trailing stop)
- Email notifications for executed orders
- Maybe a simple web dashboard

## Testing

Tested on Binance Futures Testnet with the free $10,000 USDT they give you. Placed multiple orders to make sure everything works. All the test logs are in the logs/ folder.

## Resources Used

- Binance Futures API docs: https://binance-docs.github.io/apidocs/futures/en/
- python-binance GitHub: https://github.com/sammchardy/python-binance
- Rich library docs: https://rich.readthedocs.io/
- Stack Overflow for some error handling tips

---

**Sreenath**  
Pulla Reddy Engineering College
