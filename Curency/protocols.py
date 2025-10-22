from typing import Protocol, Dict, Optional

class CurrencyDataProvider(Protocol):
    def get_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        ...
    
    def get_available_currencies(self) -> list[str]:
        ...

class CurrencyCalculator(Protocol):
    def convert(self, amount: float, rate: float) -> float:
        ...
    
    def validate_amount(self, amount: float) -> bool:
        ...

class Display(Protocol):
    def show_menu(self) -> None:
        ...
    
    def show_result(self, amount: float, from_curr: str, result: float, to_curr: str) -> None:
        ...