import requests
import schedule
import time

def send_request_to_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Status code: {response.status_code}, Response: {response.text}")

# Các URL cần gửi yêu cầu đến
url1 = "https://gynzstore.site/cron/vtpay.php"
url2 = "https://gynzstore.site/cron/mb.php"

# Thiết lập công việc định kỳ cho từng URL
schedule.every(10).seconds.do(send_request_to_url, url=url1)
schedule.every(10).seconds.do(send_request_to_url, url=url2)

while True:
    # Chạy các công việc đã định kỳ
    schedule.run_pending()
    # Đợi 1 giây trước khi kiểm tra lại
    time.sleep(1)
