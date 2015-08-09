from enum import Enum

class CallableEnum(Enum):
    """ Helper class to allow Callable Attributes """
    
    def __call__(self, *args, **kwargs):
        """ Call the value function """
        return self.value(*args, **kwargs)