import requests

def get_ran():
    url="https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response=requests.get(url)
    data=response.json()

    if "data" in data:
        user=data["data"]
        _id=user["id"]
        return _id
    
    else:
        raise Exception("not found")

def main():
        try:
         id_=get_ran()
         print(f"data :{id_}")
        except:
            print("error")
    
main()
