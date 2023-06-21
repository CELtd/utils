import os
import pickle

def cache_data(directory):
    def decorator(func):
        def wrapper(*args):
            filename = os.path.join(directory, func.__name__+'.pkl')
            if os.path.exists(filename):
                with open(filename, "rb") as f:
                    return pickle.load(f)
            else:
                result = func(*args)
                with open(filename, "wb") as f:
                    pickle.dump(result, f)
                return result
        return wrapper
    return decorator