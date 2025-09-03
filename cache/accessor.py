from redis import asyncio as redis

from setting import Setting


def get_redis_connection() -> redis.Redis:
    setting = Setting()
    return redis.Redis(host=setting.CACHE_HOST, port=setting.CACHE_PORT)