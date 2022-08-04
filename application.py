from flask import Flask, render_template, request, redirect, url_for
import sys
app = Flask(__name__) #Flask 객체 인스턴스 생성
import database  # database라는 모듈(파일)을 로딩합니다.



@app.route("/") # 홈 화면 접속하는 url
def hello():
    return render_template("house.html")  # render_template: templates폴더의 HTML파일을 return한다.

@app.route("/apply") # 집 등록하기
def apply():
    return render_template("apply.html")

@app.route("/applyphoto") # 사진 등록하기
def applyphoto():
    location = request.args.get("location")  # 사용자에게 데이터를 요청
    cleaness = request.args.get("clean")
    built_in = request.args.get("built_in")
    if cleaness == None:
        cleaness = False
    else:
        cleaness = True
    database.save(location, cleaness, built_in)  # database라는 모듈에서 save라는 함수를 호출합니다. 요청 받은 값을 Dataframe에 저장
    return render_template("apply_photo.html")  # 사진 등록하는 HTML페이지로 넘어갑니다.
 
@app.route("/upload_done", methods=["POST"])  # 반드시 "POST" method로
def upload_done():
    uploaded_files = request.files["file"]  # 사용자에게 사진 파일을 업로드를 요청
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))  
    # 데이터베이스 모듈의 now_index()할수를 불러와서 사진이랑 정보를 인덱스로 대응시킵니다.
    return redirect(url_for("hello"))  # 처음 화면으로 돌아갑니다.

@app.route("/list")
def list():
    house_list = database.load_list()
    length = len(house_list)
    return render_template("list.html", house_list = house_list, length = length)  # list.html에 house_list, lengt라는 변수를 할당합니다.

@app.route("/house_info/<int:index>/")  # 데코레이터에서 index라는 int 값을 받을 수 있게 합니다.
def house_info(index): # 등록한 집 목록을 보기
    house_info = database.load_house(index)  # index는 Dataframe에서 save메소드의 index
    location = house_info["location"]
    cleaness = house_info["cleaness"]
    built_in = house_info["built_in"]
    photo = f"img/{index}.jpeg"
    return render_template("house_info.html", location=location, cleaness = cleaness, built_in = built_in, photo= photo)
    # 등록된 house_info table HTML페이지로 넘어갑니다.
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port="5001")
    
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True )