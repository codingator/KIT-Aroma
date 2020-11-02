from flask import Flask, request, render_template, jsonify
from aroma.module import dbModule

app = Flask(__name__)

# Dashboard: Sensor, Public, admin, device,
# Razberry: user
# App: user

@app.route('/', methods=['GET'])
def index():
    db_class = dbModule.Database()

    sql = "show tables"
    result = db_class.executeAll(sql)

    return render_template('/test.html', result = result)

# There is translator in the module
@app.route('/con/data', methods=['GET', 'POST'])
def requireData():
    if request.method == 'POST':

        db_class = dbModule.Database()

        sql = ''

        post_method = request.form["method"]
        post_table = request.form["table"]

        # 예외처리 중복ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        # 삭제 기록?
        if post_method == 'INSERT' or post_method == 'UPDATE' or post_method == 'DELETE':
            ###########     INSERT     ############################################
            if post_method == 'INSERT':
                if post_table == 'user':
                    id = request.form["id"]
                    serialNum = request.form["serialNum"]
                    location = request.form["location"]
                    recipe = int(request.form["recipe"])
                    functionP = int(request.form["functionP"])
                    functionL = int(request.form["functionL"])
                    functionM = int(request.form["functionM"])
                    timeStamp = 'now()'
                    sql = "INSERT INTO user (id, serialNum, location, recipe, functionP, functionL, functionM, timeStamp) \
                        VALUE('%s','%s','%s', %d, %d, %d, %d, %s)" % (id, serialNum, location, recipe, functionP, functionL, functionM, timeStamp)
                elif post_table == 'recipe':
                    idx = ''
                    title = request.form["title"]
                    author = request.form["author"]
                    functionP = request.form["functionP"]
                    functionL = request.form["functionL"]
                    functionM = request.form["functionM"]
                    timeStamp = 'now()'
                    sql = "INSERT INTO recipe (title, author, functionP, functionL, functionM, timeStamp) \
                        VALUE('%s','%s', %d, %d, %d, %s)" % (title, author, functionP, functionL, functionM, timeStamp)
                elif post_table == 'perfume':
                    idx = ''
                    title = request.form["title"]
                    function = request.form["function"]
                    timeStamp = 'now()'
                    sql = "INSERT INTO perfume (title, function, timeStamp) \
                        VALUE('%s', %d, %s)" % (title, function, timeStamp)
                elif post_table == 'moodlight':
                    idx = ''
                    title = request.form["title"]
                    function = request.form["function"]
                    timeStamp = 'now()'
                    sql = "INSERT INTO moodLight (title, function, timeStamp) \
                        VALUE('%s', %d, %s)" % (title, function, timeStamp)
                elif post_table == 'music':
                    idx = ''
                    title = request.form["title"]
                    function = request.form["function"]
                    timeStamp = 'now()'
                    sql = "INSERT INTO music (title, function, timeStamp) \
                        VALUE('%s', %d, %s)" % (title, function, timeStamp)
                elif post_table == 'device':
                    idx = ''
                    serialNum = request.form["serialNum"]
                    timeStamp = 'now()'
                    sql = "INSERT INTO device (serialNum, timeStamp) \
                        VALUE('%s', %s)" % (serialNum, timeStamp)
                elif post_table == 'sensorData':
                    idx = ''
                    serialNum = request.form["serialNum"]
                    temperature = request.form["temperature"]
                    humedity = request.form["humedity"]
                    timeStamp = 'now()'
                    sql = "INSERT INTO sensorData (serialNum, temperature, humedity, timeStamp) \
                        VALUE('%s', %f, %f, %s)" % (serialNum, temperature, humedity, timeStamp)
                elif post_table == 'publicWeather':
                    local = request.form["local"]
                    weather = request.form["weather"]
                    perceivedTemperature = request.form["perceivedTemperature"]
                    humedity = request.form["humedity"]
                    windSpeed = request.form["windSpeed"]
                    dailyPrecipitation = request.form["dailyPrecipitation"]
                    sql = "INSERT INTO publicWeather (local, weather, perceivedTemperature, ,humedity, windSpeed, dailyPrecipitation) \
                        VALUE('%s', '%s', %f, %f, %f, %f)" % (local, weather, perceivedTemperature, humedity, windSpeed, dailyPrecipitation)
                elif post_table == 'admin':
                    id = request.form["id"]
                    password = request.form["password"]
                    sql = "INSERT INTO admin (id, password) \
                        VALUE('%s', '%s')" % (id, password)
            ###########     UPDATE     ############################################
            elif post_method == 'UPDATE':
                if post_table == 'user':
                    id = request.form["id"]
                    serialNum = request.form["serialNum"]
                    location = request.form["location"]
                    recipe = request.form["recipe"]
                    functionP = request.form["functionP"]
                    functionL = request.form["functionL"]
                    functionM = request.form["functionM"]
                    timeStamp = 'now()'
                    sql = "UPDATE user SET id = '%s', serialNum = '%s', location = '%s', recipe = %d, functionP = %d, functionL = %d, functionM = %d \
                            WHERE id = '%s'" % (id, serialNum, location, recipe, functionP, functionL, functionM, id)
                elif post_table == 'recipe':
                    idx = ''
                    title = request.form["title"]
                    author = request.form["author"]
                    functionP = request.form["functionP"]
                    functionL = request.form["functionL"]
                    functionM = request.form["functionM"]
                    timeStamp = 'now()'
                    sql = "UPDATE recipe SET title = '%s', functionP = %d, functionL = %d, functionM = %d \
                            WHERE idx = %d, author = '%s'" % (title, functionP, functionL, functionM, idx, author)
                elif post_table == 'perfume':
                    idx = ''
                    title = request.form["title"]
                    function = request.form["function"]
                    timeStamp = 'now()'
                    sql = "UPDATE perfume SET title = '%s', function = %d \
                            WHERE idx = %d" % (title, function, idx)
                elif post_table == 'moodlight':
                    idx = ''
                    title = request.form["title"]
                    function = request.form["function"]
                    timeStamp = 'now()'
                    sql = "UPDATE moodLight SET title = '%s', function = %d \
                            WHERE idx = %d" % (title, function, idx)
                elif post_table == 'music':
                    idx = ''
                    title = request.form["title"]
                    function = request.form["function"]
                    timeStamp = 'now()'
                    sql = "UPDATE music SET title = '%s', function = %d \
                            WHERE idx = %d" % (title, function, idx)
                elif post_table == 'device':
                    idx = ''
                    serialNum = request.form["serialNum"]
                    timeStamp = 'now()'
                    sql = "UPDATE device SET serialNum = '%s' \
                            WHERE idx = %d" % (serialNum, idx)
                elif post_table == 'sensorData':
                    idx = ''
                    serialNum = request.form["serialNum"]
                    temperature = request.form["temperature"]
                    humedity = request.form["humedity"]
                    timeStamp = 'now()'
                    sql = "UPDATE sensorData SET serialNum = '%s', temperature = %f, humedity = %f \
                            WHERE idx = '%s'" % (serialNum, temperature, humedity, idx)
                elif post_table == 'publicWeather':
                    local = request.form["local"]
                    weather = request.form["weather"]
                    perceivedTemperature = request.form["perceivedTemperature"]
                    humedity = request.form["humedity"]
                    windSpeed = request.form["windSpeed"]
                    dailyPrecipitation = request.form["dailyPrecipitation"]
                    sql = "UPDATE publicWeather SET weather = '%s', perceivedTemperature = %f, humedity = %f, windSpeed = %f, dailyPrecipitation = %f \
                            WHERE local = '%s'" % (weather, perceivedTemperature, humedity, windSpeed, dailyPrecipitation, local)
                elif post_table == 'admin':
                    id = request.form["id"]
                    password = request.form["password"]
                    sql = "UPDATE admin SET password = '%s' \
                            WHERE id = '%s'" % (password, id)
            ###########     DELETE     ############################################
            elif post_method == 'DELETE':
                if post_table == 'user':
                    id = request.form["id"]
                    sql = "DELETE FROM user WHERE id = '%s'" % (id)
                elif post_table == 'recipe':
                    idx = request.form["idx"]
                    author = request.form["author"]
                    sql = "DELETE FROM recipe WHERE idx = %d, author = '%s'" % (idx, author)
                elif post_table == 'perfume':
                    idx = request.form["idx"]
                    sql = "DELETE FROM perfume WHERE idx = %d" % (idx)
                elif post_table == 'moodlight':
                    idx = request.form["idx"]
                    sql = "DELETE FROM moodLight WHERE idx = %d" % (idx)
                elif post_table == 'music':
                    idx = request.form["idx"]
                    sql = "DELETE FROM music WHERE idx = %d" % (idx)
                elif post_table == 'device':
                    idx = request.form["idx"]
                    sql = "DELETE FROM device WHERE idx = %d" % (idx)
                elif post_table == 'sensorData':
                    idx = request.form["idx"]
                    sql = "DELETE FROM sensorData WHERE idx = %d" % (idx)
                elif post_table == 'publicWeather':
                    local = request.form["local"]
                    sql = "DELETE FROM publicWeather WHERE local = '%s'" % (local)
                elif post_table == 'admin':
                    id = request.form["id"]
                    password = request.form["password"]
                    sql = "DELETE FROM admin WHERE id = '%s'" % (id)

            db_class.execute(sql)
            db_class.commit()

            return post_method + ' ' + post_table + ' 정상 실행'

        else:
            if post_method == 'SELECT':

                result = {
                    'method' : '',
                    'table' : {
                        # 'user' : [],
                        # 'recipe' : [],
                        # 'perfume' : [],
                        # 'moodlight' : [],
                        # 'music' : [],
                        # 'device' : [],
                        # 'sensordata' : [],
                        # 'publicweather' : [],
                        # 'admin' : []
                    }
                }
                sql = "SELECT * FROM " + post_table
                sqlRes = db_class.executeAll(sql)

                result['method'] = post_method
                result['table'][post_table] = sqlRes


                # { method: ?,
                #     table: {
                #         ?: [ - ]
                #     }
                # }
                jsonify(result)

                return result
        # 테스트 후 데이터 리셋 -> 파일구조 변경 datatime

        return "확인할 수 없는 데이터 입니다. 전송된 데이터를 확인해 주세요."
    else:
        return "잘못 된 접근입니다."

@app.route('/testjson')
def testjson():
    return "data"

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db_class = dbModule.Database()

        id = request.form["id"]
        password = request.form["password"]

        sql = "SELECT * FROM admin WHERE id = '%s' AND password = '%s'" % (id, password)

        db_class.executeOne(sql)

        return "Login Access!"
    else:
        return "Please check your ID or Password."