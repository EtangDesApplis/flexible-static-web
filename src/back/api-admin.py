from flask import Flask, render_template, request
import pprint
app = Flask(__name__)
from dbQueryTool import *

DB_URL="192.168.1.42:32017"

@app.route('/detail', methods=['POST','GET'])
def detail():
    #data=request.form
    #print(data.get('date'))

    dbq=dbQueryTool(DB_URL)
    timeStamp=request.form.get('date')

    #dict = {'date': data.get('date') , 'content':{'order1':50,'order2':60}}
    return render_template('detail.html', date=timeStamp, orders=dbq.getOrders(timeStamp))

@app.route('/test')
def test():
    dbq=dbQueryTool(DB_URL)
    dbq.registerOrder(
        {
            "name": "client1",
            "tel": "0912345678",
            "deliveryAddr": "address",
            "deliveryDate": "20201222",
            "remarks": "entry code",
            "content": [
                {"item":"cake1", "quantity":1},
                {"item":"cake2", "quantity":3},
            ],
            "voucher": "",
            "value": 100
        }
    )
    return "fake order placed"

@app.route('/orders')
def orders():
    #https://stackoverflow.com/questions/25373154/how-to-iterate-through-a-list-of-dictionaries-in-jinja-template
    dbq=dbQueryTool(DB_URL)
    result=dbq.getOrderProjection("20201221",14)
    pprint.pprint(result)
    return render_template('orders.html', data = result)

if __name__ == '__main__':
    app.run(debug = True)