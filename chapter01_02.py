# 200222 08:38
# Numpy 09. 신주쿠 흥부부대찌개
import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 코드를 작성하세요.
won_array = revenue_in_yen * np.array(10.08)

# 정답 출력
print(won_array)

"""
과제해설
numpy array를 사용하면, 모든 데이터에 같은 숫자를 한 번에 곱해줄 수 있습니다.
먼저 주어진 리스트를 numpy array로 만듭니다.

yen_array = np.array(revenue_in_yen)
이제 이 numpy array에는 곱셈 연산을 적용할 수 있습니다.

won_array = yen_array * 10.08
won_array # 정답 출력
"""