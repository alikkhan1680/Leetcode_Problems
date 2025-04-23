import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Asosiy funksiya chaqiriladi
        end_time = time.time()
        print(f"{func.__name__} ishlash vaqti: {end_time - start_time:.4f} sekund")
        return result
    return wrapper

@time_decorator
def uzun_hisoblash():
    time.sleep(2)  # 2 soniya kutish
    print("Hisoblash yakunlandi")

uzun_hisoblash()
