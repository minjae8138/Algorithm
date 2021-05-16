record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    answer = []
    db = {}

    # new_record 생성 -> 띄어쓰기 기준으로 스플릿
    new_record = []
    for re in record:
        re = re.split(" ")
        new_record.append(re)

    # db에 아이디와 닉네임 업데이트
    for new in new_record:
        if new[0] == "Enter":
            db[new[1]] = new[2]
        else:
            if new[0] == "Change":
                db[new[1]] = new[2]
    # print(db)
    # 결과 형식에 맞게 바꿔서 answer에 추가
    for new in new_record:
        if new[0] == "Enter":
            answer.append(db[new[1]] + "님이 들어왔습니다.")
        elif new[0] == "Leave":
            answer.append(db[new[1]] + "님이 나갔습니다.")

    # print(answer)
    return answer

print(solution(record))