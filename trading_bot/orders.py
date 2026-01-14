"""
Order management and validation utilities
TODO: Maybe add order history tracking in future version
"""
from enum import Enum
from typing import Dict, Any
from rich.table import Table
from rich.console import Console

console = Console()


class OrderSide(Enum):
    """Order side enumeration"""
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    """Order type enumeration"""
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP_MARKET = "STOP_MARKET"
    STOP = "STOP"  # Stop-Limit
    TAKE_PROFIT_MARKET = "TAKE_PROFIT_MARKET"


class OrderValidator:
    """Validate order parameters"""
    
    @staticmethod
    def validate_symbol(symbol: str) -> str:
        """Validate and format symbol"""
        symbol = symbol.upper().strip()
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        return symbol
    
    @staticmethod
    def validate_quantity(quantity: float) -> float:
        """Validate order quantity"""
        try:
            qty = float(quantity)
            if qty <= 0:
                raise ValueError("Quantity must be greater than 0")
            return qty
        except (ValueError, TypeError):
            raise ValueError("Invalid quantity. Must be a positive number")
    
    @staticmethod
    def validate_price(price: float) -> float:
        """Validate order price"""
        try:
            p = float(price)
            if p <= 0:
                raise ValueError("Price must be greater than 0")
            return p
        except (ValueError, TypeError):
            raise ValueError("Invalid price. Must be a positive number")
    
    @staticmethod
    def validate_side(side: str) -> str:
        """Validate order side"""
        side = side.upper().strip()
        if side not in [OrderSide.BUY.value, OrderSide.SELL.value]:
            raise ValueError(f"Invalid side. Must be BUY or SELL")
        return side


class OrderFormatter:
    """Format order information for display"""
    
    @staticmethod
    def format_order_response(order: Dict[str, Any]) -> Table:
        """Format order response as a rich table"""
        table = Table(title="Order Details", show_header=True, header_style="bold magenta")
        table.add_column("Field", style="cyan", width=20)
        table.add_column("Value", style="green")
        
        # Key fields to display
        fields = [
            ("Order ID", "orderId"),
            ("Symbol", "symbol"),
            ("Side", "side"),
            ("Type", "type"),
            ("Status", "status"),
            ("Quantity", "origQty"),
            ("Price", "price"),
            ("Stop Price", "stopPrice"),
            ("Executed Qty", "executedQty"),
            ("Time", "updateTime"),
        ]
        
        for label, key in fields:
            value = order.get(key, "N/A")
            if value != "N/A" and value not in ["", 0, "0", None]:
                # Format timestamp
                if key == "updateTime" and value != "N/A":
                    from datetime import datetime
                    value = datetime.fromtimestamp(int(value) / 1000).strftime('%Y-%m-%d %H:%M:%S')
                
                table.add_row(label, str(value))
        
        return table
    
    @staticmethod
    def format_balance(balance_info: Dict[str, Any]) -> Table:
        """Format account balance as a rich table"""
        table = Table(title="Account Balance", show_header=True, header_style="bold magenta")
        table.add_column("Asset", style="cyan", width=15)
        table.add_column("Available", style="green", justify="right")
        table.add_column("Total", style="yellow", justify="right")
        
        if 'assets' in balance_info:
            for asset in balance_info['assets']:
                if float(asset['walletBalance']) > 0:
                    table.add_row(
                        asset['asset'],
                        f"{float(asset['availableBalance']):.8f}",
                        f"{float(asset['walletBalance']):.8f}"
                    )
        
        return table
    
    @staticmethod
    def format_positions(positions: list) -> Table:
        """Format open positions as a rich table"""
        table = Table(title="Open Positions", show_header=True, header_style="bold magenta")
        table.add_column("Symbol", style="cyan")
        table.add_column("Side", style="yellow")
        table.add_column("Amount", style="green", justify="right")
        table.add_column("Entry Price", style="blue", justify="right")
        table.add_column("Unrealized PNL", style="magenta", justify="right")
        
        has_positions = False
        for pos in positions:
            if float(pos['positionAmt']) != 0:
                has_positions = True
                pnl = float(pos['unRealizedProfit'])
                pnl_color = "green" if pnl >= 0 else "red"
                
                table.add_row(
                    pos['symbol'],
                    "LONG" if float(pos['positionAmt']) > 0 else "SHORT",
                    pos['positionAmt'],
                    pos['entryPrice'],
                    f"[{pnl_color}]{pnl:.2f}[/{pnl_color}]"
                )
        
        if not has_positions:
            table.add_row("No open positions", "", "", "", "")
        
        return table
