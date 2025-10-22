from currency_api import FixedRatesProvider
from calculator import CurrencyConverter
from display import ConsoleDisplay
from artifacts import ConversionHistory, AppConfig, ConversionResult

class CurrencyConverterApp:
    def __init__(self):
        self.config = AppConfig()
        self.history = ConversionHistory([])
        self.data_provider = FixedRatesProvider(self.config)
        self.calculator = CurrencyConverter(self.config)
        self.display = ConsoleDisplay(self.config, self.history)
    
    def get_user_input(self):
        try:
            user_input = input("\nвведите сумму: ").strip()
            
            if user_input.lower() == 'history':
                self.display.show_history()
                return None, "", ""
            elif user_input.lower() == 'clear':
                self.history.clear_history()
                print("история очищена")
                return None, "", ""
            elif user_input == '0':
                return 0, "", ""
            
            amount = float(user_input)
            from_currency = input("из валюты: ").upper()
            to_currency = input("в валюту: ").upper()
            
            return amount, from_currency, to_currency
            
        except ValueError:
            self.display.show_error("введите числовое значение или команду")
            return None, "", ""
    
    def run(self):
        print("конвертер валют запущен!")
        
        while True:
            self.display.show_menu()
            amount, from_curr, to_curr = self.get_user_input()
            
            if amount == 0:
                print("выход из программы")
                break
                
            if amount is None:
                continue
            
            if not self.calculator.validate_amount(amount):
                self.display.show_error("сумма должна быть положительной")
                continue
            
            if from_curr not in self.config.available_currencies or to_curr not in self.config.available_currencies:
                self.display.show_error("неверный код валюты")
                continue
            
            rate = self.data_provider.get_rate(from_curr, to_curr)
            if rate is None:
                self.display.show_error("курс для указанных валют не найден")
                continue
            
            conversion_result = self.calculator.create_conversion_result(
                amount, from_curr, to_curr, rate
            )
            self.history.add_conversion(conversion_result)
            
            self.display.show_result(amount, from_curr, conversion_result.result, to_curr)

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.run()