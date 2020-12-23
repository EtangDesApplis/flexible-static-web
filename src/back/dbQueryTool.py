from pymongo import MongoClient
from time import time
from datetime import datetime

def formatDate(timeStamp):
    day=(int(timeStamp) % 100)
    month=(int(int(timeStamp)/100) % 100)
    year=int(int(timeStamp)/10000)
    return "%02d-%02d-%04d"%(day,month,year)

def epoch2date(epoch):
    return datetime.fromtimestamp(epoch).strftime("%Y%m%d")

def date2epoch(timeStamp):
    #timeStamp in form of YYYYMMDD
    day=(int(timeStamp) % 100)
    month=(int(int(timeStamp)/100) % 100)
    year=int(int(timeStamp)/10000)
    return datetime(year,month,day,0,0).timestamp()

class dbQueryTool:
    def __init__(self,target):
        connection = MongoClient(target)
        self.db=connection['chefphan']
    
    def getOrderProjection(self,timeStamp,nbOfDays):
        # get list of orders and its status from a date timeStamp within nbOfDays days
        """
        Output:
        {
            "category":["cake1","cake2"],
            "data": [
                {"date":"DD-MM-YYYY","orderCount","timeStamp":"YYYYMMDD","cake1":1,"cake2":2,"color":"green"}
            ]
        }
        """
        epoch0=date2epoch(timeStamp)
        res={"category":[],"data":[]}
        tmp_category=[]
        for i in range(nbOfDays):
            ts=epoch2date(epoch0+i*24*3600)
            tmp_data={"date":formatDate(ts),"orderCount":0,"timeStamp":ts,"color":"green"}
            for order in self.db["orders"].find({"deliveryDate":ts}):
                if order["status"] in ["pending", "confirmed", "done"]:
                    tmp_data["orderCount"]+=1
                    if order["status"]=="pending":
                        tmp_data["color"]="yellow"
                    for c in order["content"]:
                        tmp_category.append(c["item"])
                        tmp_data[c["item"]]=c["quantity"]
            if tmp_data["orderCount"]==0:
                tmp_data["color"]="white"
            res["data"].append(tmp_data)
        res["category"]=list(set(tmp_category))
        return res

    def getSummary(self,timeStamp):
        # list cake category vs quantiy of confirmed order
        summary={}
        for order in self.db["orders"].find({"deliveryDate":timeStamp,"status":"confirmed"}):
            summary["value"]+=order["value"]
            for detail in order["content"]:
                if detail["item"] in summary:
                    summary[detail["item"]]+=detail["quantity"]
                else:
                    summary[detail["item"]]=detail["quantity"]
        return summary

    def getOrders(self,timeStamp):
        # get orders with details of a given date
        """
        Output:

        """
        orders=[]
        for order in self.db["orders"].find({"deliveryDate":timeStamp}):
            #return id, status, name, tel, clientStatus, deliveryAddr, deliveryDate, remarks, content, voucher, value
            #return "total" section
            orders.append({
                "id": order["id"],
                "status": order["status"],
                "name": order["name"],
                "tel": order["tel"],
                "clientStatus": self.getClientStatus(order["tel"]),
                "deliveryAddr": order["deliveryAddr"],
                "deliveryDate": order["deliveryDate"],
                "remarks": order["remarks"],
                "content": order["content"],
                "voucher": order["voucher"],
                "value": order["value"],
            })
        return orders
    
    def getClientStatus(self,phoneNb):
        #return status of client with telephone number
        client=self.db["clients"].find_one({"tel":phoneNb})
        try:
            return client["status"]
        except Exception as error:
            print(str(error))
            return "unknown"

    def getClients(self):
        #return details of all clients
        clients={}
        i=1
        for client in self.db["clients"].find():
            # get back name, tel, status, address, OrderRecord, BuyRecord
            clients[i]={
                "name": client["name"],
                "tel": client["tel"],
                "status": client["status"],
                "address": client["address"],
                "OrderRecord": client["OrderRecord"],
                "BuyRecord": client["BuyRecord"]
            }
            i=i+1
        return clients

    def updateOrderStatus(self,orderId,status):
        #update status of Order
        
        order=self.db["orders"].find_one({"id":order_id})
        try:
            #update order
            self.db["orders"].update_one(
                {"id":order_id},
                {"$set": {"status":status}})
            if status=="done":
                # if order status is changed to done (delivered) update client record too
                client=self.db["clients"].find_one({"tel":order["tel"]})
                for data in order["content"]:
                    if data["item"] in client["BuyRecord"]:
                        client["BuyRecord"][data["item"]]+=data["quantity"]
                    else:
                        client["BuyRecord"][data["item"]]=data["quantity"]
                client["OrderRecord"]+=1
                if client["status"]=="new":
                    client["status"]="confirmed"
                #update client
                self.db["clients"].update_one(
                    {"tel":order["tel"]},
                    {"$set": {"status":client["status"],"OrderRecord":client["OrderRecord"],"BuyRecord":client["BuyRecord"]}})

        except Exception as error:
            print(str(error))

    def updateClientStatus(self,phoneNb,status):
        #update status of Client
        try:
            self.db["client"].update_one(
                {"tel":phoneNb},
                {"$set": {"status":status}})
        except Exception as error:
            print(str(error))

    def registerOrder(self,order):
        # order is an JSON
        """
        input:
        {
            "name": "client1",
            "tel": "0912345678",
            "deliveryAddr": "address",
            "deliveryDate": "YYYYMMDD",
            "remarks": "entry code",
            "content": [
                {"item":"cake1", "quantity":1},
                {"item":"cake2", "quantity":3},
            ],
            "voucher": "",
            "value": 100
        }
        """
        reponse=""
        #YYYYMMDD-tel <= unique
        order_id="%s-%s"%(order["deliveryDate"],order["tel"])
        if self.db["orders"].find_one({"id":order_id})==None:
            order["id"]=order_id
            #pending/confirmed/done/canceled/refused
            order["status"]="pending" 
            # if client does not exist, it will be create automatically
            if self.db["clients"].find_one({"tel":order["tel"]})==None:
                self.registerClient({
                    "tel":order["tel"],
                    "name": order["name"],
                    "address": order["deliveryAddr"]
                })
            self.db["orders"].insert_one(order)
            reponse="OK"
        else:
            print("duplicated order")
            reponse="Duplicated"
            
        return reponse

    def registerClient(self,client):
        # client is an JSON
        #status: new/confirmed/vip/blacklisted
        client["status"]="new"
        client["OrderRecord"]=0
        client["BuyRecord"]={}
        self.db["clients"].insert_one(client)

if __name__=="__main__":
    #test here
    pass