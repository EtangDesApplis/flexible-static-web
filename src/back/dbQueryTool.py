from pymongo import MongoClient

class dbQueryTool:
    def __init__(self,target):
        connection = MongoClient(target)
        self.db=connection['chefphan']
    
    def getOrderProjection(self,timeStamp,nbOfDays):
        # get list of orders and its status from a date timeStamp within nbOfDays days
        pass

    def getOrders(self,timeStamp):
        # get orders with details of a given date
        pass
    
    def getClientStatus(self,phoneNb):
        #return status of client with telephone number
        pass

    def getClients(self):
        #return details of all clients
        pass
    
    def updateOrder(self,orderId,status):
        #update status of Order
        # if order status is changed to done (delivered) update client record too
        order=self.db["orders"].find({"id":order_id})
        pass

    def updateClient(self,phoneNb,status):
        #update status of Client
        pass

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
        if self.db["orders"].find({"id":order_id})==None:
            order["id"]=order_id
            #pending/confirmed/done/canceled/refused
            order["status"]="pending" 
            # if client does not exist, it will be create automatically
            if self.db["clients"].find({"tel":order["tel"]})==None:
                self.registerClient({\
                    "tel":order["tel"], \
                    "name": order["name"], \
                    "adresse": order["deliveryAddr"] \
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
        client["ItemRecord"]={}
        self.db["clients"].insert_one(client)

if __name__=="__main__":
    #test here
    pass