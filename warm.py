import requests

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

response = requests.get(url)
filename = 'taxi_zone_lookup.csv'


if response.status_code == 200:
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"CSV file downloaded successfully as {filename}")
else:
    print(f"Failed to download CSV file. Status code: {response.status_code}")


data = open(filename).readlines()


print("Number of rows in csv file:", len(data))

x = set()

for i in data:
    x.add(i.split(",")[1])
x = sorted(x)

print("Number of unique zones in csv file:", len(data))

print('Sorted Order Unique Borough:', x)

cnt = 0
for i in data:
    if i.split(',')[1]=='Brooklyn':
        cnt+=1

print('Number of Brooklyn:', cnt)


with open('output.txt', 'w') as file:
    file.write(f"{len(data)}\n")
    file.write(f"{x}\n")
    file.write(f"{cnt}\n")
    file.close()
