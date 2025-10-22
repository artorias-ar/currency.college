from protocols import CurrencyCalculator
from artifacts import ConversionResult, AppConfig
from datetime import datetime

class CurrencyConverter(CurrencyCalculator):
    def __init__(self, config: AppConfig):
        self.config = config
    
    def convert(self, amount: float, rate: float) -> float:
        return round(amount * rate, self.config.decimal_places)
    
    def validate_amount(self, amount: float) -> bool:
        return amount > 0
    
    def create_conversion_result(self, amount: float, from_currency: str, 
                               to_currency: str, rate: float) -> ConversionResult:
        result = self.convert(amount, rate)
        return ConversionResult(
            amount=amount,
            from_currency=from_currency,
            to_currency=to_currency,
            rate=rate,
            result=result,
            timestamp=datetime.now()
        )