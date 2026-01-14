"""
Core trading bot implementation
"""
from binance.client import Client
from binance.exceptions import BinanceAPIException
from typing import Dict, Any, Optional
from .config import Config
from .logger import logger
from .orders import OrderValidator, OrderSide, OrderType

# Main bot class for handling Binance Futures trading


class BasicBot:
    """
    Simplified trading bot for Binance Futures Testnet
    
    Supports market, limit, and stop-limit orders with comprehensive
    logging and error handling.
    """
    
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        """
        Initialize the trading bot
        
        Args:
            api_key: Binance API key
            api_secret: Binance API secret
            testnet: Whether to use testnet (default: True)
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        
        try:
            logger.info("Initializing Binance client...")
            logger.info(f"Mode: {'TESTNET' if testnet else 'MAINNET'}")
            
            # Initialize Binance client
            self.client = Client(
                api_key=api_key,
                api_secret=api_secret,
                testnet=testnet
            )
            
            # Set base URL for futures
            if testnet:
                self.client.API_URL = 'https://testnet.binancefuture.com'
            
            # Test connection
            logger.info("Testing API connection...")
            account_info = self.client.futures_account()
            logger.info("✓ Successfully connected to Binance Futures API")
            logger.debug(f"Account status: {account_info.get('canTrade', False)}")
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error during initialization: {e}")
            raise
        except Exception as e:
            logger.error(f"Error initializing bot: {e}")
            raise
    
    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float
    ) -> Dict[str, Any]:
        """
        Place a market order
        
        Args:
            symbol: Trading pair symbol (e.g., 'BTCUSDT')
            side: Order side ('BUY' or 'SELL')
            quantity: Order quantity
            
        Returns:
            Order response from Binance API
        """
        try:
            # Validate inputs
            symbol = OrderValidator.validate_symbol(symbol)
            side = OrderValidator.validate_side(side)
            quantity = OrderValidator.validate_quantity(quantity)
            
            logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")
            
            # Place order
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=OrderType.MARKET.value,
                quantity=quantity
            )
            
            logger.info(f"✓ Market order placed successfully")
            logger.info(f"Order ID: {order['orderId']}, Status: {order['status']}")
            logger.debug(f"Full order response: {order}")
            
            return order
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            logger.error(f"Error code: {e.code}, Message: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Error placing market order: {e}")
            raise
    
    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
        time_in_force: str = 'GTC'
    ) -> Dict[str, Any]:
        """
        Place a limit order
        
        Args:
            symbol: Trading pair symbol (e.g., 'BTCUSDT')
            side: Order side ('BUY' or 'SELL')
            quantity: Order quantity
            price: Limit price
            time_in_force: Time in force (default: 'GTC' - Good Till Cancel)
            
        Returns:
            Order response from Binance API
        """
        try:
            # Validate inputs
            symbol = OrderValidator.validate_symbol(symbol)
            side = OrderValidator.validate_side(side)
            quantity = OrderValidator.validate_quantity(quantity)
            price = OrderValidator.validate_price(price)
            
            logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")
            
            # Place order
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=OrderType.LIMIT.value,
                quantity=quantity,
                price=price,
                timeInForce=time_in_force
            )
            
            logger.info(f"✓ Limit order placed successfully")
            logger.info(f"Order ID: {order['orderId']}, Status: {order['status']}")
            logger.debug(f"Full order response: {order}")
            
            return order
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            logger.error(f"Error code: {e.code}, Message: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Error placing limit order: {e}")
            raise
    
    def place_stop_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
        stop_price: float,
        time_in_force: str = 'GTC'
    ) -> Dict[str, Any]:
        """
        Place a stop-limit order (BONUS FEATURE)
        
        Args:
            symbol: Trading pair symbol (e.g., 'BTCUSDT')
            side: Order side ('BUY' or 'SELL')
            quantity: Order quantity
            price: Limit price (price to execute at when stop is triggered)
            stop_price: Stop price (trigger price)
            time_in_force: Time in force (default: 'GTC')
            
        Returns:
            Order response from Binance API
        """
        try:
            # Validate inputs
            symbol = OrderValidator.validate_symbol(symbol)
            side = OrderValidator.validate_side(side)
            quantity = OrderValidator.validate_quantity(quantity)
            price = OrderValidator.validate_price(price)
            stop_price = OrderValidator.validate_price(stop_price)
            
            logger.info(
                f"Placing STOP-LIMIT order: {side} {quantity} {symbol} "
                f"@ {price} (stop: {stop_price})"
            )
            
            # Place order
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=OrderType.STOP.value,
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce=time_in_force
            )
            
            logger.info(f"✓ Stop-limit order placed successfully")
            logger.info(f"Order ID: {order['orderId']}, Status: {order['status']}")
            logger.debug(f"Full order response: {order}")
            
            return order
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            logger.error(f"Error code: {e.code}, Message: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Error placing stop-limit order: {e}")
            raise
    
    def get_account_balance(self) -> Dict[str, Any]:
        """
        Get account balance information
        
        Returns:
            Account balance data
        """
        try:
            logger.info("Fetching account balance...")
            balance = self.client.futures_account_balance()
            account = self.client.futures_account()
            
            logger.debug(f"Balance data: {balance}")
            return account
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            raise
    
    def get_open_orders(self, symbol: Optional[str] = None) -> list:
        """
        Get open orders
        
        Args:
            symbol: Optional symbol to filter orders
            
        Returns:
            List of open orders
        """
        try:
            logger.info(f"Fetching open orders{' for ' + symbol if symbol else ''}...")
            
            params = {}
            if symbol:
                params['symbol'] = OrderValidator.validate_symbol(symbol)
            
            orders = self.client.futures_get_open_orders(**params)
            logger.info(f"Found {len(orders)} open order(s)")
            logger.debug(f"Orders: {orders}")
            
            return orders
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error fetching open orders: {e}")
            raise
    
    def get_positions(self) -> list:
        """
        Get open positions
        
        Returns:
            List of positions
        """
        try:
            logger.info("Fetching positions...")
            positions = self.client.futures_position_information()
            logger.debug(f"Positions: {positions}")
            
            return positions
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            raise
    
    def cancel_order(self, symbol: str, order_id: int) -> Dict[str, Any]:
        """
        Cancel an open order
        
        Args:
            symbol: Trading pair symbol
            order_id: Order ID to cancel
            
        Returns:
            Cancellation response
        """
        try:
            symbol = OrderValidator.validate_symbol(symbol)
            logger.info(f"Cancelling order {order_id} for {symbol}...")
            
            result = self.client.futures_cancel_order(
                symbol=symbol,
                orderId=order_id
            )
            
            logger.info(f"✓ Order cancelled successfully")
            logger.debug(f"Cancellation response: {result}")
            
            return result
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error cancelling order: {e}")
            raise
