class Calculator:
    def _validate(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Arguments must be numeric, got {type(arg).__name__}")

    def add(self, a, b):
        self._validate(a, b)
        return a + b

    def subtract(self, a, b):
        self._validate(a, b)
        return a - b
