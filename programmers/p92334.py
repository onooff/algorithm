def solution(id_list, report, k):
    reporter_dict = {x: set() for x in id_list}
    reportee_dict = {x: set() for x in id_list}
    for r in report:
        reporter, reportee = r.split()
        reporter_dict[reporter].add(reportee)
        reportee_dict[reportee].add(reporter)

    banned = set()
    for reportee in reportee_dict:
        if len(reportee_dict[reportee]) >= k:
            banned.add(reportee)

    answer = list()
    for reporter in id_list:
        answer.append(0)
        for reportee in reporter_dict[reporter]:
            if reportee in banned:
                answer[-1] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
