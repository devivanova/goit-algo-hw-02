import queue
import random
import time
import threading

request_queue = queue.Queue()


# Генерація нових заявок
def generate_requests():
    request_id = 1
    while True:
        request = f"Заявка {request_id}"
        print(f"Нова заявка додана до черги: {request}")
        request_queue.put(request)
        request_id += 1
        time.sleep(random.uniform(1, 3))


# Обробка заявок
def process_requests():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Обробляється {request}...")
            time.sleep(random.uniform(0.5, 2))
            print(f"{request} оброблено.")
        else:
            print("Черга пуста, немає заявок для обробки.")
            time.sleep(2)


def main():
    # Створюємо потік для генерації заявок
    generator_thread = threading.Thread(target=generate_requests)

    # Створюємо потік для обробки заявок
    processor_thread = threading.Thread(target=process_requests)

    generator_thread.start()
    processor_thread.start()

    generator_thread.join()
    processor_thread.join()


if __name__ == "__main__":
    main()
