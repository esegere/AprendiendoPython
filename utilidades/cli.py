"""clases para el manejo de comandos desde terminal
"""


class FunctionHandler:

    def __init__(self, *, loop_function: callable):
        self.__loop_function = loop_function
        self.function_parameters = ()
        self.__functions = {}
        self.__default_function = lambda: None

    def call_when(self, option: str) -> callable:
        def decorator(function: callable) -> callable:
            self.__functions[option] = function
            return function

        return decorator

    def call_default(self, function: callable) -> callable:
        self.__default_function = function
        return function

    def loop_until(self, option: str):
        print(self.__functions.keys())
        while (loop_func_res := self.__loop_function()) != option:
            if loop_func_res in self.__functions.keys():
                self.__functions[loop_func_res](*self.function_parameters)
            else:
                self.__default_function()
