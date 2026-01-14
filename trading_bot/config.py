"""
Configuration management for the trading bot
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""
    
    # API Credentials
    API_KEY = os.getenv('BINANCE_API_KEY')
    API_SECRET = os.getenv('BINANCE_API_SECRET')
    
    # Trading mode
    TESTNET = os.getenv('TESTNET', 'True').lower() == 'true'
    
    # Binance URLs
    TESTNET_BASE_URL = 'https://testnet.binancefuture.com'
    MAINNET_BASE_URL = 'https://fapi.binance.com'
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.API_KEY or not cls.API_SECRET:
            raise ValueError(
                "API credentials not found. Please set BINANCE_API_KEY and "
                "BINANCE_API_SECRET in .env file"
            )
        
        if cls.API_KEY == 'your_api_key_here':
            raise ValueError(
                "Please update .env file with your actual API credentials from "
                "https://testnet.binancefuture.com/"
            )
        
        return True
    
    @classmethod
    def get_base_url(cls):
        """Get the appropriate base URL"""
        return cls.TESTNET_BASE_URL if cls.TESTNET else cls.MAINNET_BASE_URL
