def solution(citations):
    citations.sort(reverse=True)
    for citation in citations:
        if citation <= citations.index(citation):
            answer = citations.index(citation)
            break
        else :
            answer = len(citations)
    return answer

# 100 50 10 와 같이 h가 인덱스보다 항상 큰 경우를 생각해낼 것