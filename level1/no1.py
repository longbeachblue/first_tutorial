def solution(d, budget):
    answer = 0
    for a in d :
        while(budget>0):
            budget=budget-d[a]
            answer=answer+1
    return answer


def main():
    d=[]
    a = input()
    d.appent(a)
    d.sort()
    budget = input()
    solution(d,budget)