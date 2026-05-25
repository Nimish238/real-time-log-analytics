from faker import Faker

import random
import json
import time
from datetime import datetime

fake = Faker()

# list of services being monitored
services=[
    "auth-service",
    "payment-service",
    "inventory-service",
    "shipping-service",
    "search-service"
]

#API endpoints
endpoints=[
    "/login",
    "/payment",
    "/checkout",
    "/products",
    "/search"
]

status_codes=[200,200,401,404,500,503]

#contionous loop
while True:
    
    #randomly selets status code
    status = random.choice(status_codes)
    
    current_timestamp = datetime.now().strftime(
        "%Y-%m-%dT%H:%M:%S"
    )
    #create log directory
    log = {
        
        #event timestamp
        "time-stamp":current_timestamp,
        
        #identifies which microservice generates log
       "service":random.choice(services),
       
       # identifies API endpoint
        "endpoint":random.choice(endpoints),
        
        #success/failure tracking
        "status_codes":status,
        
        #API latency analytics
        "response_time":random.randint(50,5000),
        
        #infrastructure monitoring
        "cpu_usage":random.randint(10,95),
        
        #sserver health monitoring
        "memory_usage":random.randint(20,90),
        
        #security analytics
        "ip_address":fake.ipv4(),
        
        #error monitoring 
        "message":"success" if status == 200 else "Error"
    }
   
   #file name based on current time stamp, created unique log files continously 
    file_name = f"logs/log_{int(time.time())}.json"
    
    #open file in write mode
    with open(file_name,"w") as f:
        
        #writes json log files, spark streaming will read these files continously
        json.dump(log,f)
        
    print(log)
    time.sleep(2) 