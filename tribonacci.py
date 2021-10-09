def tribonacci(signature, n):
    if n<4:
        return signature
    return tribonacci(signature.append(sum(signature[-1:-4:-1])),n-1)
    #your code here
