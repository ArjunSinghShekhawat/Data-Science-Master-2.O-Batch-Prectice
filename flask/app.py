from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if(ops=='add'):
            r = num1+num2
            result = "The sum of num1 = {} and num2 = {} will be result =  {} ".format(num1,num2,r)

        if(ops=='subtract'):
            r = num1-num2
            result = "The subtract of num1 = {} and num2 = {} will be result =  {} ".format(num1,num2,r)

        if(ops=='multiply'):
            r = num1*num2s
            result = "The multiply of num1 = {} and num2 = {} will be result =  {} ".format(num1,num2,r)

        if(ops=='divide'):
            r = num1/num2
            result = "The divide of num1 = {} and num2 = {} will be result =  {} ".format(num1,num2,r)
        
        return render_template('results.html',result=result)
        

if __name__=='__main__':
    app.run(host='0.0.0.0')
