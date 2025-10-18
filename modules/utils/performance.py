import time
import functools
from typing import Callable

def timeit(func: Callable) -> Callable:
    """装饰器：测量函数执行时间"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'{func.__name__} 执行耗时: {elapsed:.3f}s')
        return result
    return wrapper

class PerformanceMonitor:
    """性能监控工具"""
    
    def __init__(self):
        self.timings = {}
    
    def start(self, name: str):
        """开始计时"""
        self.timings[name] = time.time()
    
    def end(self, name: str) -> float:
        """结束计时并返回耗时（秒）"""
        if name not in self.timings:
            return 0.0
        elapsed = time.time() - self.timings[name]
        del self.timings[name]
        return elapsed
    
    def log(self, name: str):
        """记录并输出耗时"""
        elapsed = self.end(name)
        print(f'{name} 耗时: {elapsed:.3f}s')
        return elapsed
