from flask import Flask

app = Flask(__name__)
users = {
    "Huy":{
        "name":"Nguyen Quang Huy",
        "gender": "male",
        "hobby":"69"
    },
    "Nam":{
        "name":"Pham Quy Nam",
        "gender": "male",
        "hobby":"69"
    },
    "Manh":{
        "name":"Pham Duc Manh",
        "gender": "male",
        "hobby":"69"
    },
}

@app.route("/user/<username>")
def username(username):
    if username in users.keys():
        return str(users[username])  
    else:
        return "User not found"

print('running app')
if __name__ == "__main__":
    app.run(debug=True)
