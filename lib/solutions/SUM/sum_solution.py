# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    raise NotImplementedError()
    
def SUM(x,y):
    params = [x,y]
    c = sum(params)
    return c

if __name__ == '__main__':
    SUM(2,2)