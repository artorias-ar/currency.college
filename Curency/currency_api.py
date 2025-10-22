from protocols import CurrencyDataProvider
from artifacts import AppConfig
from typing import Optional

class FixedRatesProvider(CurrencyDataProvider):
    def __init__(self, config: AppConfig):
        self.rates = {
            'USD': {'RUB': 90.0, 'EUR': 0.85, 'KZT': 430.0},
            'EUR': {'RUB': 95.0, 'USD': 1.18, 'KZT': 510.0},
            'RUB': {'USD': 0.011, 'EUR': 0.0105, 'KZT': 4.8},
            'KZT': {'USD': 0.0023, 'EUR': 0.0020, 'RUB': 0.21}
        }
        self.config = config
    
    def get_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        if from_currency in self.rates and to_currency in self.rates[from_currency]:
            return self.rates[from_currency][to_currency]
        return None
    
    def get_available_currencies(self) -> list[str]:
        return list(self.config.available_currencies)