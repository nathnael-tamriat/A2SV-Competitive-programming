class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1)+ len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                multiplication = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                result[i+j]+= multiplication
                result[i + j + 1] += result[i+j] // 10
                result[i + j] = result[i+j] % 10
        if len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return"".join(map(str,result[::-1]))