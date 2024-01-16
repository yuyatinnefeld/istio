import requests
import concurrent.futures
import time

def fetch_url(url):
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        return str(e)

def benchmark_website(url, total_requests, concurrent_calls):
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_calls) as executor:
        futures = [executor.submit(fetch_url, url) for _ in range(total_requests)]

        # Wait for all the requests to complete
        concurrent.futures.wait(futures)

        # Count successful and failed requests
        successful_requests = sum(1 for future in futures if future.result() == 200)
        failed_requests = total_requests - successful_requests

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\nBenchmark Summary for {url}")
    print(f"Total Requests: {total_requests}")
    print(f"Concurrent Calls: {concurrent_calls}")
    print(f"Successful Requests: {successful_requests}")
    print(f"Failed Requests: {failed_requests}")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Requests per Second: {total_requests / total_time:.2f}")

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    total_requests = int(input("Enter the total number of requests: "))
    concurrent_calls = int(input("Enter the number of concurrent calls: "))

    benchmark_website(website_url, total_requests, concurrent_calls)
