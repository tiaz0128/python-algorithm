import pytest
from collections import defaultdict


@pytest.mark.parametrize(
    "args",
    [
        (
            ["muzi", "ryan", "frodo", "neo"],
            [
                "muzi frodo",
                "muzi frodo",
                "ryan muzi",
                "ryan muzi",
                "ryan muzi",
                "frodo muzi",
                "frodo ryan",
                "neo muzi",
            ],
            2,
        ),
        (
            ["joy", "brad", "alessandro", "conan", "david"],
            [
                "alessandro brad",
                "alessandro joy",
                "alessandro conan",
                "david alessandro",
                "alessandro david",
            ],
            4,
        ),
        (["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"], 0),
    ],
)
def test_most_presented_gift(args):
    *inputs, expected = args

    result = solution(*inputs)

    assert expected == result


def solution(friends, gifts):
    # 기록이 있다면 더 많이 준 사람이 하나 받음

    gift_degree = defaultdict(int)
    gift_record = defaultdict(dict)

    for name in friends:
        gift_record[name].update({friend: 0 for friend in friends if name != friend})

        for gift in gifts:
            sender, recipient = gift.split(" ")

            if sender == name:
                gift_record[name][recipient] += 1
                gift_degree[name] += 1
            elif recipient == name:
                gift_record[name][sender] -= 1
                gift_degree[name] -= 1

    point = []
    for name in friends:
        cnt = 0
        for friend, v in gift_record[name].items():
            if v > 0:
                cnt += 1
            elif v == 0 and gift_degree[name] > gift_degree[friend]:
                cnt += 1

        point.append(cnt)

    # 주고받은 기록이 없거나, 같은 경우
    # 선물 지수가 큰 사람이 받음
    # - (친구들에게 준 선물 - 받은 선물)
    # - 선물 지수도 같으면 선물을 주고 받지 않음

    # 선물을 가장 많이 받은 친구가 받은 선물 수

    return max(point)
