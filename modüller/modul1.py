# Json modülü

# Verileri insanlar tarafından okunabilir ve yazılabilir bir formatta temsil etmek için kullanılan hafif bir veri değişim formatıdır.



# json.loads
import json

json_str = '{"name": "John", "age": 30, "city": "New York"}'
python_obj = json.loads(json_str)

print(python_obj)  # {'name': 'John', 'age': 30, 'city': 'New York'}
# json.loads(): JSON formatındaki bir dizeyi alır ve bu dizeyi Python nesnelerine (örneğin, sözlükler, listeler, diziler) dönüştürür.



# json.dumps
import json

python_obj = {'name': 'John', 'age': 30, 'city': 'New York'}
json_str = json.dumps(python_obj)

print(json_str)  # '{"name": "John", "age": 30, "city": "New York"}'

# json.dumps(): Python nesnelerini alır ve bunları JSON formatında bir dize olarak döndürür.
