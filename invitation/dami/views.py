from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import User

def main(request):
    return render(request, 'user/UserMain.html')

# 로그인 화면
def user_login(request):
    # 이미 로그인한 경우
    if request.user.is_authenticated:
        if request.user.profile.Type == 'admin':
            return redirect('main:admin_main')  # admin_main.html로 리다이렉트
        else:
            return redirect('main:UserMain')
    else:
        form = LoginForm(data=request.POST or None)
        if request.method == "POST":
            # 입력정보가 유효한 경우 각 필드 정보 가져옴
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # 위 정보로 사용자 인증(authenticate 사용하여 superuser로 로그인 가능)
                user = authenticate(request, username=username, password=password)

                # 로그인이 성공한 경우
                if user is not None:
                    login(request, user)  # 로그인 처리 및 세션에 사용자 정보 저장

                    if user.profile.Type == 'admin':
                        return redirect('main:admin_main')  # admin_main 페이지로 리다이렉트
                    else:
                        return redirect('main:UserMain')  # main 페이지로 리다이렉트

        return render(request, 'registration/login.html', {'form': form})  # 폼을 템플릿으로 전달
    
# 회원가입 화면
def register(request):
    error_message = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        User_Name = request.POST.get('User_Name')
        if User.objects.filter(username=User_Name).exists():
            error_message = "이미 존재하는 아이디입니다."
        elif form.is_valid():
            
            Password = form.cleaned_data['Password']
            Password_Check = form.cleaned_data['Password_Check']
            
            # 비밀번호 일치 여부를 확인
            if Password == Password_Check:
                # 새로운 유저를 생성
                user = User.objects.create_user(username=User_Name, password=Password)
                
                # 유저를 로그인 상태로 만들기 전에 인증(authenticate)이 필요
                user = authenticate(request, username=User_Name, password=Password)

                # 유저를 로그인 상태로 만듦
                if user:
                    login(request, user)  # 이제 두 개의 인수를 사용하면서 올바르게 로그인 처리
                    return redirect('main:login')
            else:
                form.add_error('Password_Check', '비밀번호가 일치하지 않습니다.')       
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form, 'error_message': error_message})

# 관리자 홈
def admin_main(request):
    return render(request, 'admin/admin_main.html')

# 유저관리 페이지
def admin_user_list(request):
    user_list = User.objects.all().order_by('id') # 아이디를 오름차순으로 정렬
    return render(request, 'admin/admin_user_list.html', {'user_list': user_list})

# 유저삭제
def admin_user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('main:admin_user_list')
    
    # GET 요청에 대한 처리 (페이지를 보여줄 때)
    return render(request, 'admin/admin_user_delete.html', {'user': user})

# 유저수정
def admin_user_modify(request, user_id):
    if request.method == 'POST':
        try:
            # POST 요청을 받으면 폼에서 입력한 회원 정보를 저장합니다.
            user = User.objects.get(pk=user_id)
            user.set_password(request.POST['password'])  # 비밀번호 변경
            user.username = request.POST['username']      # 이름 변경
            # 다른 필드도 유사하게 처리하실 수 있습니다.
            user.save()
            return redirect('main:admin_user_list')  # 수정 후 유저 목록 페이지로 리디렉션
        except User.DoesNotExist:
            # 해당 ID의 회원이 존재하지 않을 경우 예외 처리
            pass

    return render(request, 'admin/admin_user_modify.html', {'user': User.objects.get(pk=user_id)})

###############test_code
def view_User_type(request):
    if request.user.is_authenticated:
        # 현재 로그인한 사용자의 UserProfile 모델 인스턴스를 가져옵니다.
        User = User.objects.get(user=request.user)
        
        # UserProfile 모델의 type 값을 가져와서 출력합니다.
        user_type = User.Type
        
        return render(request, 'User_type.html', {'user_type': user_type})
    else:
        return render(request, 'User_type.html', {'user_type': '사용자가 로그인하지 않았습니다.'})