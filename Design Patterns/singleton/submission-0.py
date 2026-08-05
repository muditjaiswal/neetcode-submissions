class Singleton:
    _unique_instance = None
    _singleton_val = ""

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super().__new__(cls)
        return cls._unique_instance

    def getValue(self) -> str:
        return Singleton._singleton_val

    def setValue(self, value: str):
        Singleton._singleton_val = value
