from bs4 import BeautifulSoup

with open("weather.html", 'r', encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

table_body = soup.find("tbody")

rows = table_body.find_all("tr")

weather_data = []
for row in rows:
    columns = row.find_all("td") 
    day = columns[0].text.strip()
    temperature = columns[1].text.strip()
    condition = columns[2].text.strip()

    weather_data.append((day, temperature, condition))

for data in weather_data:
    print(f"Day:{data[0]}, Temperature: {data[1]}, Condition: {data[2]}")

print("* "*30)
print("Specific data:")
hottest_day = max(weather_data, key=lambda x: x[1])
print(f"Highest temperature is {hottest_day[1]}. It is on {hottest_day[0]}")

sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
print("Days with sunny weather: ", sunny_days)

print("* "*30)

temperatures = [int(temp[:-2]) for _, temp, _ in weather_data]
average_temp = sum(temperatures) / len(temperatures)

print("Average temperature is: ", average_temp)  