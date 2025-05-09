# 目的: 列印 City Amsterdam is in the country Netherlands

city = "Amsterdam"
country = "Netherlands"

# 傳遞引數的值
print("City", city, 'is in the country', country) # City Amsterdam is in the country Netherlands

# 格式化字串 (順序傳遞)
print("City {} is in the country {}".format(city, country)) # City Amsterdam is in the country Netherlands

# 格式化字串 (建立數字索引)
print("City {1} is in the country {0}, yes, in {0}".format(country, city)) # City Amsterdam is in the country Netherlands, yes, in Netherlands
 
# 格式化字串 (給每個引用命名)
print("City {city} is in the country {country}".format(country=country, city=city)) # City Amsterdam is in the country Netherlands

# 多個引數組成元組來傳遞引數
print("City %s is in the country %s" %(city, country)) # City Amsterdam is in the country Netherlands
