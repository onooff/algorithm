import requests
import json

url = 'https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/'
# problem2_day-1.json


def go(problem='1', day='1'):
    global url
    file_name = 'problem'+problem+'_day-'+day+'.json'
    response = requests.get(
        url=url+file_name)
    # print(response, response.text)
    return response


p = '2'
size = 60
board = [[[0, 0, 0] for j in range(size)] for i in range(size)]
for d in ['1', '2', '3']:
    ret = go(p, d)
    ret_parsed = json.loads(ret.text)
    max_val = 0
    for r in ret_parsed:
        # print(r, len(ret_parsed[r]))
        for call in ret_parsed[r]:
            start_point = call[0]
            end_point = call[1]
            use_time = call[2]
            board[size-1-(start_point % size)][start_point//size][0] += 1
            board[size-1-(end_point % size)][end_point//size][1] += 1
            board[size-1-(end_point % size)][end_point//size][2] = board[size-1-(end_point %
                                                                                 size)][end_point//size][1]-board[size-1-(start_point % size)][start_point//size][0]
            max_val = max(
                max_val, board[size-1-(start_point % size)][start_point//size][0])
    print(max_val)

    for i in range(size):
        for j in range(size):
            print(board[i][j][0], end=' ')
    print()
