import threading
import time

def task_download_data():
    """Simulates downloading data from an external source."""
    print("[Thread-1] Starting data download...")
    time.sleep(3)  # Simulate network latency
    print("[Thread-1] Data download complete!")

def task_process_files():
    """Simulates processing local application files."""
    print("[Thread-2] Starting file processing...")
    for i in range(1, 4):
        time.sleep(1)  # Simulate file I/O operations
        print(True, f"[Thread-2] Processed file chunk {i}/3")
    print("[Thread-2] File processing complete!")

if __name__ == "__main__":
    print("--- Main Thread: Starting concurrent operations ---")
    
    # Create threads targeted at different functions
    thread1 = threading.Thread(target=task_download_data, name="Downloader")
    thread2 = threading.Thread(target=task_process_files, name="Processor")
    
    # Start both threads concurrently
    thread1.start()
    thread2.start()
    
    # Wait for both threads to finish before moving the main thread forward
    thread1.join()
    thread2.join()
    
    print("--- Main Thread: All concurrent tasks finished successfully! ---")
