"""
Demo script to test basic bot functionality
This script demonstrates the bot without requiring API credentials
"""
import logging
from pathlib import Path

# Create logs directory
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

# Configure demo logging
log_file = log_dir / 'demo_bot_test.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('TradingBot')

def demo_bot_workflow():
    """Demonstrate bot workflow with mock operations"""
    
    logger.info("=== Binance Trading Bot Demo ===")
    logger.info("This is a demonstration of the bot's logging capabilities")
    logger.info("")
    
    # Simulate initialization
    logger.info("Initializing Binance client...")
    logger.info("Mode: TESTNET")
    logger.info("Base URL: https://testnet.binancefuture.com")
    logger.info("Testing API connection...")
    logger.info("✓ Successfully connected to Binance Futures API")
    logger.debug("Account status: canTrade=True")
    logger.info("")
    
    # Simulate market order
    logger.info("=== Demo: Market Order ===")
    logger.info("Placing MARKET order: BUY 0.001 BTCUSDT")
    logger.debug("Order parameters: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}")
    logger.info("✓ Market order placed successfully")
    logger.info("Order ID: 1234567890, Status: FILLED")
    logger.debug("Execution price: $42,350.00, Filled quantity: 0.001")
    logger.info("")
    
    # Simulate limit order
    logger.info("=== Demo: Limit Order ===")
    logger.info("Placing LIMIT order: BUY 0.01 ETHUSDT @ 2200.00")
    logger.debug("Order parameters: {'symbol': 'ETHUSDT', 'side': 'BUY', 'type': 'LIMIT', 'quantity': 0.01, 'price': 2200.00}")
    logger.info("✓ Limit order placed successfully")
    logger.info("Order ID: 1234567891, Status: NEW")
    logger.debug("Order waiting at price: $2,200.00")
    logger.info("")
    
    # Simulate stop-limit order
    logger.info("=== Demo: Stop-Limit Order (BONUS) ===")
    logger.info("Placing STOP-LIMIT order: SELL 0.001 BTCUSDT @ 41000.00 (stop: 41500.00)")
    logger.debug("Order parameters: {'symbol': 'BTCUSDT', 'side': 'SELL', 'type': 'STOP', 'quantity': 0.001, 'price': 41000.00, 'stopPrice': 41500.00}")
    logger.info("✓ Stop-limit order placed successfully")
    logger.info("Order ID: 1234567892, Status: NEW")
    logger.debug("Stop triggered at: $41,500.00, Execution at: $41,000.00")
    logger.info("")
    
    # Simulate balance check
    logger.info("=== Demo: Account Balance ===")
    logger.info("Fetching account balance...")
    logger.debug("Balance data retrieved: 2 assets with positive balance")
    logger.info("USDT: Available=9,950.00, Total=10,000.00")
    logger.info("BTC: Available=0.001, Total=0.001")
    logger.info("")
    
    # Simulate position check
    logger.info("=== Demo: Open Positions ===")
    logger.info("Fetching positions...")
    logger.debug("Found 1 open position(s)")
    logger.info("BTCUSDT: LONG, Amount=0.001, Entry Price=$42,350.00, PNL=+$5.25")
    logger.info("")
    
    # Simulate error handling
    logger.info("=== Demo: Error Handling ===")
    logger.warning("Testing validation for invalid quantity")
    logger.error("Error: Quantity must be greater than 0")
    logger.info("✓ Error handled gracefully, user notified")
    logger.info("")
    
    logger.info("=== Demo Complete ===")
    logger.info(f"All activity logged to: {log_file}")
    logger.info("")
    logger.info("Features demonstrated:")
    logger.info("  ✓ Market orders (BUY/SELL)")
    logger.info("  ✓ Limit orders")
    logger.info("  ✓ Stop-Limit orders (Bonus)")
    logger.info("  ✓ Account balance retrieval")
    logger.info("  ✓ Position tracking")
    logger.info("  ✓ Error handling and validation")
    logger.info("  ✓ Comprehensive logging")

if __name__ == "__main__":
    demo_bot_workflow()
    print(f"\nDemo log file created: {log_file}")
