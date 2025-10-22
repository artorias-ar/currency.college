from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class ConversionResult:
    amount: float
    from_currency: str
    to_currency: str
    rate: float
    result: float
    timestamp: datetime
    
    def to_dict(self) -> dict:
        return {
            'amount': self.amount,
            'from_currency': self.from_currency,
            'to_currency': self.to_currency,
            'rate': self.rate,
            'result': self.result,
            'timestamp': self.timestamp.isoformat()
        }

@dataclass
class ConversionHistory:
    conversions: List[ConversionResult]
    
    def add_conversion(self, conversion: ConversionResult):
        self.conversions.append(conversion)
    
    def get_last_n(self, n: int) -> List[ConversionResult]:
        return self.conversions[-n:]
    
    def clear_history(self):
        self.conversions.clear()

@dataclass
class AppConfig:
    default_currency: str = "RUB"
    decimal_places: int = 2
    history_size: int = 10
    available_currencies: tuple = ("USD", "EUR", "RUB", "KZT")