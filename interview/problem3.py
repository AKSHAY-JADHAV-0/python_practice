'''Write a Python script to read this log file server_logs.txt.
Calculate and print:
The total number of requests.
The number of requests per HTTP method (GET, POST, etc.).
The average response time for each URL endpoint.
The IP address with the most requests.'''

Text_file= "/home/akshay/Items/python_practice/interview/server_logs.txt"

with open(Text_file, "r") as file:
    content = file.read()

print(content)

for requests in content:
    get_list=[]
    post_list=[]
    if requests.find("GET"):
        get_list.append()
        print(get_list)

    elif requests.find("POST"):
        post_list.append()
        print(post_list)

print(get_list)
print(post_list)
