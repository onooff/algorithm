def solution(word='', pages=''):
    urls = dict()
    links = dict()
    word = word.lower()
    for p in pages:
        p = p.lower()
        sp = p.split('<')
        url = ''
        point = 0
        link = list()
        body_flag = False
        for pp in sp:
            if body_flag:
                if pp.startswith("/body>"):
                    break
                elif pp.startswith("a href"):
                    link.append(pp.split("https://")[1].split("\"")[0])
                else:
                    start = 0
                    for i in range(len(pp)):
                        if not pp[i].isalpha():
                            chk = pp[start:i]
                            if chk == word:
                                point += 1
                            start = i+1
            elif pp.startswith("meta property"):
                url = pp.split("https://")[1].split("\"")[0]
                # print(url)
            elif pp.startswith("body"):
                body_flag = True
                start = 0
                for i in range(len(pp)):
                    if not pp[i].isalpha():
                        chk = pp[start:i]
                        if chk == word:
                            point += 1
                        start = i+1
        # print(url, point, links)
        urls.setdefault(url, 0)
        urls[url] += point
        for l in link:
            links.setdefault(l, 0)
            links[l] += point/len(link)

    answer = 0
    best_point = 0
    i = 0
    for u in urls:
        k = 0
        if u in links:
            k = links[u]
        chk = urls[u]+k
        if best_point < chk:
            best_point = chk
            answer = i
        i += 1
    return answer


print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
               ))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
                        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
