
with open('test_json.txt','r') as f:
    a = f.read()

    b = a.split(',')[2].split(':')[1]

    print(b)