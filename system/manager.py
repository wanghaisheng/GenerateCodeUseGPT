
from system.settings import settings
from system.llm import openai_util 
from system.llm import googleai_util
from system.prompt import database

def call_system_decorator(system_name):
    """
    A decorator that calls a method of a system module specified by `system_name` with the keyword arguments `kwargs`.

    Args:
        system_name (str): The name of the system module to call.

    Returns:
        A decorator that wraps methods of the `MainManager` class that call methods of system modules.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if func(self) is False:
                return None
            module = getattr(self, system_name)
            if module is None:
                return None

            # if 'func' exists in kwargs, call the function specified by 'func'
            if 'func' not in kwargs or kwargs['func'] is None:
                funcname = args[0]
            # else use the first argument as the function name
            else:
                funcname = kwargs['func']

            if not funcname.startswith('Interface'):
                print("Cannot call system function directly, Please call 'InterfaceXXX' method instead.")
                return None
            execute_func = getattr(module, funcname)
            if execute_func is None:
                return None
            func_kwargs = {k: v for k, v in kwargs.items() if k != 'func'}
            # get args[1:] as the arguments of the function
            return execute_func(*args[1:], **func_kwargs)
        return wrapper
    return decorator


class MainManager(object):
    '''
    MainManager is the main manager of the system.
    It's a singleton class.
    It controls the whole system.
    '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.api_supply_dict = {}
        self.init_systems()

    def init_systems(self):

        self.settings = settings.Settings()
        self.database = database.ResultDatabase()
        self.openai_util = openai_util.OpenAIUtil(self.settings.InterfaceGetOpenAIKey())
        self.googleai_util = googleai_util.GoogleAIUtil(self.settings.InterfaceGetGooglePalmKey())

        # insert the valid llm interface
        if self.openai_util.InterfaceIsValid():
            self.api_supply_dict[self.openai_util.InterfaceGetSupplyName()] = self.call_openai_util
        if self.googleai_util.InterfaceIsValid():
            self.api_supply_dict[self.googleai_util.InterfaceGetSupplyName()] = self.call_googleai_util

    @call_system_decorator("settings")
    def call_settings(self, *args, **kwargs):
        return True

    @call_system_decorator("openai_util")
    def call_openai_util(self, *args, **kwargs):
        if self.openai_util.InterfaceIsValid():
            return True
        else:
            return False

    @call_system_decorator("googleai_util")
    def call_googleai_util(self, *args, **kwargs):
        if self.googleai_util.InterfaceIsValid():
            return True
        else:
            return False

    @call_system_decorator("database")
    def call_database(self, *args, **kwargs):
        return True

    def call_llm(self, *args, **kwargs):
        if 'supply' in kwargs and kwargs['supply'] is not None:
            supply = kwargs['supply']
        else:
            supply = args[0]

        if supply not in self.api_supply_dict:
            print("Cannot find valid api supply name {}".format(supply))
            return None
        else:
            func_kwargs = {k: v for k, v in kwargs.items() if k != 'supply'}
            return self.api_supply_dict[supply](*args[1:], **func_kwargs)

    def get_all_models(self):
        """
        Get all the models of the system.

        Returns:
            A dict of all the models of the system.
        """
        result = {}
        for api_supply in self.api_supply_dict:
            result[api_supply] = self.call_llm(api_supply, "InterfaceGetAllModelNames")
        return result