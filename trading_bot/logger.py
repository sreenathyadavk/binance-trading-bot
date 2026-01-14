"""
Logging configuration for the trading bot
"""
import logging
import os
from datetime import datetime
from pathlib import Path


class BotLogger:
    """Custom logger for trading bot with file and console output"""
    
    def __init__(self, name='TradingBot'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Prevent duplicate handlers
        if self.logger.handlers:
            return
        
        # Create logs directory if it doesn't exist
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        
        # Create log filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = log_dir / f'trading_bot_{timestamp}.log'
        
        # File handler - detailed logs
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_format)
        
        # Console handler - important logs only
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        console_handler.setFormatter(console_format)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.log_file_path = str(log_file)
        self.logger.info(f"Logging initialized. Log file: {log_file}")
    
    def get_logger(self):
        """Get the logger instance"""
        return self.logger
    
    def get_log_file(self):
        """Get the current log file path"""
        return self.log_file_path


# Singleton logger instance
_bot_logger = BotLogger()
logger = _bot_logger.get_logger()


def get_log_file_path():
    """Get the current log file path"""
    return _bot_logger.get_log_file()
