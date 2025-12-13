# https://leetcode.com/problems/coupon-code-validator/

def validateCoupons(code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
    codes = []
    
    for i in range(len(code)):
        if code[i] and all(j.isalnum() or j == "_" for j in code[i]):
            if businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]:
                if isActive[i]:
                    codes.append({
                        "code": code[i],
                        "businessLine": businessLine[i],
                    })
    
    return [i["code"] for i in sorted(codes, key=lambda k: (k["businessLine"], k["code"]))] # (11 ms)