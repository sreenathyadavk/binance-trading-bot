"""
Interactive CLI for the trading bot
Built with Rich library for better UI
"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from trading_bot.bot import BasicBot
from trading_bot.config import Config
from trading_bot.logger import logger, get_log_file_path
from trading_bot.orders import OrderFormatter
from binance.exceptions import BinanceAPIException

console = Console()


class TradingBotCLI:
    """Interactive command-line interface for the trading bot"""
    
    def __init__(self):
        """Initialize the CLI"""
        self.bot = None
        self.running = True
    
    def display_banner(self):
        """Display welcome banner"""
        banner = """
[bold cyan]╔═══════════════════════════════════════════╗[/bold cyan]
[bold cyan]║[/bold cyan]   [bold yellow]Binance Futures Trading Bot[/bold yellow]       [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]   [dim]Testnet Mode - Risk-Free Trading[/dim]    [bold cyan]║[/bold cyan]
[bold cyan]╚═══════════════════════════════════════════╝[/bold cyan]
        """
        console.print(banner)
        console.print(f"[dim]Log file: {get_log_file_path()}[/dim]\n")
    
    def initialize_bot(self):
        """Initialize the bot with credentials"""
        try:
            console.print("[bold]Initializing bot...[/bold]")
            Config.validate()
            
            self.bot = BasicBot(
                api_key=Config.API_KEY,
                api_secret=Config.API_SECRET,
                testnet=Config.TESTNET
            )
            
            console.print("[bold green]✓ Bot initialized successfully![/bold green]\n")
            return True
            
        except ValueError as e:
            console.print(f"[bold red]Configuration Error:[/bold red] {e}")
            console.print("\n[yellow]Please update your .env file with valid API credentials.[/yellow]")
            console.print("[dim]Get credentials from: https://testnet.binancefuture.com/[/dim]")
            return False
        except BinanceAPIException as e:
            console.print(f"[bold red]API Error:[/bold red] {e.message}")
            return False
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
            return False
    
    def display_menu(self):
        """Display main menu"""
        menu = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
        menu.add_column("Option", style="bold cyan", width=4)
        menu.add_column("Action", style="white")
        
        menu.add_row("1", "Place Market Order")
        menu.add_row("2", "Place Limit Order")
        menu.add_row("3", "Place Stop-Limit Order [dim](Bonus)[/dim]")
        menu.add_row("4", "View Account Balance")
        menu.add_row("5", "View Open Orders")
        menu.add_row("6", "View Positions")
        menu.add_row("7", "Cancel Order")
        menu.add_row("0", "Exit")
        
        console.print(Panel(menu, title="[bold]Main Menu[/bold]", border_style="cyan"))
    
    def place_market_order(self):
        """Handle market order placement"""
        try:
            console.print("\n[bold]Place Market Order[/bold]")
            
            symbol = Prompt.ask("Symbol (e.g., BTCUSDT)").upper()
            side = Prompt.ask("Side", choices=["BUY", "SELL"]).upper()
            quantity = Prompt.ask("Quantity")
            
            # Confirm order
            console.print(f"\n[yellow]Order Preview:[/yellow]")
            console.print(f"  Type: MARKET")
            console.print(f"  Symbol: {symbol}")
            console.print(f"  Side: {side}")
            console.print(f"  Quantity: {quantity}")
            
            if Confirm.ask("\nConfirm order?", default=False):
                order = self.bot.place_market_order(
                    symbol=symbol,
                    side=side,
                    quantity=float(quantity)
                )
                
                table = OrderFormatter.format_order_response(order)
                console.print("\n")
                console.print(table)
                console.print("[bold green]✓ Order executed successfully![/bold green]")
            else:
                console.print("[yellow]Order cancelled[/yellow]")
                
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def place_limit_order(self):
        """Handle limit order placement"""
        try:
            console.print("\n[bold]Place Limit Order[/bold]")
            
            symbol = Prompt.ask("Symbol (e.g., BTCUSDT)").upper()
            side = Prompt.ask("Side", choices=["BUY", "SELL"]).upper()
            quantity = Prompt.ask("Quantity")
            price = Prompt.ask("Limit Price")
            
            # Confirm order
            console.print(f"\n[yellow]Order Preview:[/yellow]")
            console.print(f"  Type: LIMIT")
            console.print(f"  Symbol: {symbol}")
            console.print(f"  Side: {side}")
            console.print(f"  Quantity: {quantity}")
            console.print(f"  Price: {price}")
            
            if Confirm.ask("\nConfirm order?", default=False):
                order = self.bot.place_limit_order(
                    symbol=symbol,
                    side=side,
                    quantity=float(quantity),
                    price=float(price)
                )
                
                table = OrderFormatter.format_order_response(order)
                console.print("\n")
                console.print(table)
                console.print("[bold green]✓ Order placed successfully![/bold green]")
            else:
                console.print("[yellow]Order cancelled[/yellow]")
                
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def place_stop_limit_order(self):
        """Handle stop-limit order placement"""
        try:
            console.print("\n[bold]Place Stop-Limit Order[/bold] [dim](Bonus Feature)[/dim]")
            
            symbol = Prompt.ask("Symbol (e.g., BTCUSDT)").upper()
            side = Prompt.ask("Side", choices=["BUY", "SELL"]).upper()
            quantity = Prompt.ask("Quantity")
            stop_price = Prompt.ask("Stop Price (trigger)")
            limit_price = Prompt.ask("Limit Price (execution)")
            
            # Confirm order
            console.print(f"\n[yellow]Order Preview:[/yellow]")
            console.print(f"  Type: STOP-LIMIT")
            console.print(f"  Symbol: {symbol}")
            console.print(f"  Side: {side}")
            console.print(f"  Quantity: {quantity}")
            console.print(f"  Stop Price: {stop_price}")
            console.print(f"  Limit Price: {limit_price}")
            
            if Confirm.ask("\nConfirm order?", default=False):
                order = self.bot.place_stop_limit_order(
                    symbol=symbol,
                    side=side,
                    quantity=float(quantity),
                    price=float(limit_price),
                    stop_price=float(stop_price)
                )
                
                table = OrderFormatter.format_order_response(order)
                console.print("\n")
                console.print(table)
                console.print("[bold green]✓ Order placed successfully![/bold green]")
            else:
                console.print("[yellow]Order cancelled[/yellow]")
                
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def view_balance(self):
        """Display account balance"""
        try:
            console.print("\n[bold]Fetching account balance...[/bold]")
            balance = self.bot.get_account_balance()
            
            table = OrderFormatter.format_balance(balance)
            console.print("\n")
            console.print(table)
            
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def view_open_orders(self):
        """Display open orders"""
        try:
            console.print("\n[bold]Fetching open orders...[/bold]")
            
            symbol = Prompt.ask("Symbol (leave empty for all)", default="")
            orders = self.bot.get_open_orders(symbol if symbol else None)
            
            if not orders:
                console.print("[yellow]No open orders found[/yellow]")
                return
            
            for order in orders:
                table = OrderFormatter.format_order_response(order)
                console.print("\n")
                console.print(table)
                
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def view_positions(self):
        """Display open positions"""
        try:
            console.print("\n[bold]Fetching positions...[/bold]")
            positions = self.bot.get_positions()
            
            table = OrderFormatter.format_positions(positions)
            console.print("\n")
            console.print(table)
            
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def cancel_order(self):
        """Cancel an order"""
        try:
            console.print("\n[bold]Cancel Order[/bold]")
            
            symbol = Prompt.ask("Symbol").upper()
            order_id = Prompt.ask("Order ID")
            
            if Confirm.ask(f"\nCancel order {order_id} for {symbol}?", default=False):
                result = self.bot.cancel_order(symbol, int(order_id))
                console.print("[bold green]✓ Order cancelled successfully![/bold green]")
            else:
                console.print("[yellow]Cancellation aborted[/yellow]")
                
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
    
    def run(self):
        """Run the CLI"""
        self.display_banner()
        
        if not self.initialize_bot():
            return
        
        while self.running:
            try:
                console.print()
                self.display_menu()
                console.print()
                
                choice = Prompt.ask("Select option", choices=["0", "1", "2", "3", "4", "5", "6", "7"])
                
                if choice == "1":
                    self.place_market_order()
                elif choice == "2":
                    self.place_limit_order()
                elif choice == "3":
                    self.place_stop_limit_order()
                elif choice == "4":
                    self.view_balance()
                elif choice == "5":
                    self.view_open_orders()
                elif choice == "6":
                    self.view_positions()
                elif choice == "7":
                    self.cancel_order()
                elif choice == "0":
                    console.print("\n[bold cyan]Thank you for using the Trading Bot![/bold cyan]")
                    console.print(f"[dim]Logs saved to: {get_log_file_path()}[/dim]\n")
                    self.running = False
                
                if self.running and choice != "0":
                    console.print("\n" + "─" * 50)
                    
            except KeyboardInterrupt:
                console.print("\n\n[yellow]Interrupted by user[/yellow]")
                self.running = False
            except Exception as e:
                console.print(f"\n[bold red]Unexpected error:[/bold red] {e}")
                logger.exception("Unexpected error in CLI")


def main():
    """Main entry point"""
    cli = TradingBotCLI()
    cli.run()


if __name__ == "__main__":
    main()
