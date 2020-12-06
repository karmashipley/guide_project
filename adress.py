from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 파일을 읽어드려서 데이터 베이스에 저장
def address_to_database():
    f = open("./address", 'r')

    lines = f.readlines()
    for line in lines:
        if '폐지' not in line:
            # address_arr = line.split()
            address = {'info': line.split()}
            db.addresses.insert_one(address)
    f.close()

# 저장된 주소데이터에서 시,도 정보를 출력
def list_do():
    addresses = list(db.addresses.find({ 'info': { '$size': 3 }}))
    for address in addresses:
        print(address['info'][0], address['info'][1])


list_do()

