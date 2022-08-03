from flask import Flask, render_template, request, redirect, url_for
import sys
app = Flask(__name__) #Flask 객체 인스턴스 생성
import database  # database라는 모듈(파일)을 로딩합니다.



@app.route("/") # 홈 화면 접속하는 url
def hello():
    return render_template("house.html")  # render_template: stirng대신 HTML파일을 return한다.

@app.route("/apply") # 집 등록하기
def apply():
    return render_template("apply.html")

@app.route("/applyphoto") # 사진 등록하기
def applyphoto():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built_in")
    if cleaness == None:
        cleaness = False
    else:
        cleaness = True
    database.save(location, cleaness, built_in)  # database라는 모듈에서 save라는 함수를 호출합니다.
    return render_template("apply_photo.html")
 
@app.route("/resister") # 등록한 집 목록을 보기
def resister():
    return render_template("register.html")

@app.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("hello"))

if __name__=="__main__":
    app.run(host="0.0.0.0",port="5001")
    
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True )