def solution(n, k):
    sheep = 12000 * n
    serv = n // 10
    drink = 2000 * (k - serv)
    
    answer = sheep + drink
    return answer