import random
from string import digits

"""
۱-همه کدهای ملی ۱۰ رقمی هستند.
۲-کدهای ملی که همه ارقام آنها مثل هم باشند معتبر نیستند.
روش کار: دهمین رقم شماره ملی را ( از سمت چپ ) به عنوان A در نظر می گیریم.
یک مقدار B در نظر می گیریم و آن را برابر با =
(اولین رقم * ۱۰) + ( دومین رقم * ۹ ) + ( سومین رقم * ۸ ) + ( چهارمین رقم * ۷ ) + ( پنجمین رقم * ۶) + ( ششمین رقم * ۵ ) + ( هفتمین رقم * ۴ ) + ( هشتمین رقم * ۳ ) + ( نهمین رقم * ۲ )قرار می دهیم.
مقدار C را برابر با = B – (B/11)*11 قرار می دهیم.
اگر مقدار C برابر با صفر باشد و مقدار A برابر C باشد کد ملی صحیح است.
اگر مقدار C برابر با ۱ باشد و مقدار A برابر با ۱ باشد کد ملی صحیح است.
اگر مقدار C بزرگتر از ۱ باشد و مقدار A برابر با ۱۱ – C باشد کد ملی صحیح است.
"""

class NationalCode:
    @staticmethod
    def is_valid(code):
        for i in code:
            if i not in digits:
                return False
        if len(code) != 10 or code in [str(i)*10 for i in range(10)]:
            return False
        numArray = [int(ch) for ch in code]
        a = numArray[9]
        b = (numArray[0] * 10) + (numArray[1] * 9) + (numArray[2] * 8) + (numArray[3] * 7) + (numArray[4] * 6) + (numArray[5] * 5) + (numArray[6] * 4) + \
            (numArray[7] * 3) + (numArray[8] * 2)
        c = b - (b//11) * 11
        if (c == 0 and a == c) or (c == 1 and a == 1) or (c > 1 and a == abs(c - 11)):
            return True
        else:
            return False
    
    @staticmethod
    def random_m1():
        while True:
            random_code = ''
            for _ in range(10):
                random_code += random.choice(digits)
            if NationalCode.is_valid(random_code):
                return random_code
    
    @staticmethod
    def random_between_m1(num1, num2):
        while True:
            code = random.randint(num1, num2)
            if NationalCode.is_valid(str(code)):
                return code
