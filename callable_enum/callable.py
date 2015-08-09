
class Callable:
    """ Simple wrapper to wrap function objects so they can be added to Enums """
    
    def __init__(self, func):
        """ Initialize with the function to wrap """
        self.func = func
        
    def __call__(self, *args, **kwargs):
        """ Call the wrapped function """
        return self.func(*args, **kwargs)