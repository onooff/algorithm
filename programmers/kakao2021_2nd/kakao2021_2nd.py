import requests
import json

url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'


def start(problem='1'):
    global url
    header = {'X-Auth-Token': '521c713a42c3e2b1abd6dd6f454e9f44',
              'Content-Type': 'application/json'}
    data = {'problem': problem}
    response = requests.post(
        url=url+'/start', data=json.dumps(data), headers=header)
    # print(response, response.text)
    return response


def locations(key='key'):
    global url
    header = {'Authorization': key,
              'Content-Type': 'application/json'}
    response = requests.get(
        url=url+'/locations', headers=header)
    # print(response, response.text)
    return response


def trucks(key='key'):
    global url
    header = {'Authorization': key,
              'Content-Type': 'application/json'}
    response = requests.get(
        url=url+'/trucks', headers=header)
    # print(response, response.text)
    return response


def simulate(key='key', commands=list()):
    global url
    header = {'Authorization': key,
              'Content-Type': 'application/json'}
    data = {'commands': commands}
    response = requests.put(
        url=url+'/simulate', data=json.dumps(data), headers=header)
    # print(response, response.text)
    return response


def score(key='key'):
    global url
    header = {'Authorization': key,
              'Content-Type': 'application/json'}
    response = requests.get(
        url=url+'/score', headers=header)
    # print(response, response.text)
    return response


for problem in ['1', '2']:
    # for problem in ['1']:
    start_ret = start(problem)
    start_ret_parsed = json.loads(start_ret.text)
    key = start_ret_parsed['auth_key']

    locations_ret = locations(key)
    locations_ret_parsed = json.loads(locations_ret.text)
    trucks_ret = trucks(key)
    trucks_ret_parsed = json.loads(trucks_ret.text)

    l = locations_ret_parsed['locations']
    t = trucks_ret_parsed['trucks']

    status = ''
    while status != 'finished':
        simulate_ret = simulate(
            # key, [{"truck_id": 0, "command": [2, 5, 4, 1, 6]}])
            key, [{"truck_id": 0, "command": []}])
        simulate_ret_parsed = json.loads(simulate_ret.text)
        print(simulate_ret_parsed)
        status = simulate_ret_parsed['status']
    score_ret = score(key)
    print(score_ret.text)

'''

'''


l = [[0 for i in range(10)] for j in range(10)]
