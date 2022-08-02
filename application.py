from flask import Flask, render_template
import sys
app = Flask(__name__) #Flask 객체 인스턴스 생성



@app.route("/") # 접속하는 url
def hello():
    return render_template("house.html")

@app.route("/apply") # 집 등록하기
def apply():
    return render_template("apply.html")

@app.route("/resister") # 등록한 집 목록을 보기
def resister():
    return render_template("register.html")


if __name__=="__main__":
    app.run(host="0.0.0.0",port="5001")
    
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True )