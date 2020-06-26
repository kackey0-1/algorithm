import json

j = {
    "employee":
        [
            {"id": 111, "name": "健太郎"},
            {"id": 222, "name": "Nancy"}
        ]
}
print(j)
print(f'{"#"*25}')
print(json.dumps(j))
print(json.dumps(j, ensure_ascii=False))

print(f'{"@"*25}')
tmp = json.dumps(j)
print(json.loads(tmp))
print(f'{"@"*25}')

with open('data/test.json', 'w') as f:
    json.dump(j, f, ensure_ascii=False)

print(f'{"#"*25}')

with open('data/test.json', 'r') as f:
    print(json.load(f))