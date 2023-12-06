from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 추가하려는 사용자 컬럼들을 정의합니다.
    user_id = models.CharField(max_length=20, unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # 실제로는 비밀번호를 해싱하여 저장해야 합니다.
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name
    
# 모델 파일 작성 방법 가이드
# # 모델로부터 모든 데이터를 조회
# all_data = MyModel.objects.all()

# # 특정 조건으로 데이터 조회
# filtered_data = MyModel.objects.filter(name="John")

# # 데이터 생성
# new_data = MyModel(name="Alice", age=30, email="alice@example.com")
# new_data.save()

# # 데이터 수정
# record = MyModel.objects.get(id=1)
# record.name = "Updated Name"
# record.save()

# # 데이터 삭제
# record = MyModel.objects.get(id=1)
# record.delete()