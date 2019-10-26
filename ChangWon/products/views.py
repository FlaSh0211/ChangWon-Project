from django.shortcuts import render
from django.core.mail import EmailMessage # 메일 객체 생성시 필요함 - 2019-10-26 남승철 추가

# Create your views here.
# product들의 리스트를 보여주는 페이지입니다 - 김영환
def main(request):
    # products = Product.objects.all() --> 심세은님 부탁드립니다. 
    context = {"error":True, "title":"Chang-Won"}
    
    return render(request, 'products/index.html', context)


# 2019-10-26 남승철 추가
def sendEmail(request):                     # 문의 사항 이메일 보내기 db에 등록
    who = request.POST.get("who_request")   # 문의자 이름 or id
    content = request.POST.get("content")   # 문의 내용

    # 메일 보내기
    emailcontent = EmailMessage() 	                    # 이메일 객체 생성
    emailcontent.subject = who                          # 보낸이
    emailcontent.body =  content	                    # 내용
    emailcontent.from_email = '000@gmail.com'           # 발신지
    emailcontent.to = ['000@gmail.com'] 			    # 목적지
    emailcontent.send() 

    #게시판에 등록
    blog = Blog(
        who = who, 
        content = content
    )

    return redirect('main')