from protocols import Display
from artifacts import ConversionHistory, AppConfig

class ConsoleDisplay(Display):
    def __init__(self, config: AppConfig, history: ConversionHistory):
        self.config = config
        self.history = history
    
    def show_menu(self) -> None:
        print("\n" + "="*50)
        print("           КОНВЕРТЕР ВАЛЮТ")
        print("="*50)
        currencies = ", ".join(self.config.available_currencies)
        print(f"Доступные валюты: {currencies}")
        print("команды: 0 - выход, history - история, clear - очистить историю")
        print("-"*50)
    
    def show_result(self, amount: float, from_curr: str, result: float, to_curr: str) -> None:
        if result is None:
            print("ошибка конвертации! Проверьте валюты.")
        else:
            print(f"результат: {amount} {from_curr} = {result:.2f} {to_curr}")
    
    def show_history(self) -> None:
        if not self.history.conversions:
            print("история конвертаций пуста")
            return
        
        print("\nпоследние конвертации:")
        for i, conv in enumerate(self.history.get_last_n(5), 1):
            print(f"{i}. {conv.amount} {conv.from_currency} → "
                  f"{conv.result} {conv.to_currency} "
                  f"(курс: {conv.rate})")
    
    def show_error(self, message: str) -> None:
        print(f"ошибка: {message}")