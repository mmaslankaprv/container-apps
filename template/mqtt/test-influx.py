import requests
import time
import random

while True:
    epoch_time = int(time.time())* 1000000000
    raw_data = 'test_metric,host=test01 value={0} {1}'.format(random.uniform(0, 5), epoch_time)
    r = requests.post('http://localhost:10080/telegraf/write', data=raw_data)
    print r
    time.sleep(1)
