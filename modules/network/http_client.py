import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 创建全局的requests session以复用连接
_session = None

def get_session():
    """获取全局HTTP会话，启用连接池和重试机制"""
    global _session
    if _session is None:
        _session = requests.Session()
        
        # 配置重试策略
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.3,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # 配置连接池
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=20
        )
        
        _session.mount("http://", adapter)
        _session.mount("https://", adapter)
        
        # 设置默认超时
        _session.timeout = 10
    
    return _session

def get(url, **kwargs):
    """发送GET请求，使用连接池"""
    session = get_session()
    return session.get(url, **kwargs)

def post(url, **kwargs):
    """发送POST请求，使用连接池"""
    session = get_session()
    return session.post(url, **kwargs)
