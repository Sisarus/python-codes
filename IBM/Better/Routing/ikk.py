def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput
@jsonify_decorator
def hello():
    return 'hello world'
@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)
print(hello())
print(add())



@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"


@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid