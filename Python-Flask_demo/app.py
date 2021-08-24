
from flask import Flask, request, jsonify
app=Flask(__name__)

@app.route('/test',methods=['GET','POST'])
def test():
    if request.method=='GET':
        return jsonify({'reponse':"received "})

@app.route('/{square}',methods=['GET','POST'])       
def square():
    try:
        if request.method=='POST':
            req_Json=request.json
            a=req_Json['num']**2
            return jsonify({"square":a})
    except:
        return jsonify({"error":"invalid input"})


@app.route('/sqrt',methods=['GET','POST'])       
def sqrt():
    try:
        if request.method=='POST':
            req_Json=request.json
            b=req_Json['num']**(0.5)
            return jsonify({"sqrt":b})
    except: 
        return jsonify({"error":"invalid_input"})

if __name__ =='__main__':
    app.run()

