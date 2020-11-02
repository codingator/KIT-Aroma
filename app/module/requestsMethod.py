import requests
import json

def web_request(method_name, url, dict_data, is_urlencoded=True):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    method_name = method_name.upper() # 메소드이름을 대문자로 바꾼다 
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')
        
    if method_name == 'GET': # GET방식인 경우
        response = requests.get(url=url, params=dict_data)
    elif method_name == 'POST': # POST방식인 경우
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers={'Content-Type': 'application/json'})
    
    dict_meta = {'status_code':response.status_code, 'ok':response.ok, 'encoding':response.encoding, 'Content-Type': response.headers['Content-Type']}
    if 'json' in str(response.headers['Content-Type']): # JSON 형태인 경우
        return {**dict_meta, **response.json()}
    else: # 문자열 형태인 경우
        return {**dict_meta, **{'text':response.text}}

# # POST방식 호출 테스트('Content-Type': 'application/x-www-form-urlencoded')
# url  = 'http://teamaroma.pythonanywhere.com/con/data' # 접속할 사이트주소 또는 IP주소를 입력한다 
# data = {'method': 'SELECT', 'table': []}          # 요청할 데이터
# response = web_request(method_name='POST', url=url, dict_data=data)

# # print(response)
# if response['ok'] == True:
#     print(response)

#     # 성공 응답 시 액션
# else:
#     pass
#     # 실패 응답 시 액션
