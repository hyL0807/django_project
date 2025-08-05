from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request,'index.html')

def page1(request):
    return render(request,'page1.html')

def page2(request):
    if request.method == 'POST':
        text_data = request.POST.get('text_data')
        return HttpResponse(f"입력된 텍스트 : {text_data}")
    else:
        return render(request,'page2.html')

#채팅 테스트
def page3(request):
    return render(request, 'page3.html')

@csrf_exempt
def process_message(request):
    """사용자 입력을 처리하고 응답 반환"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '').strip()
            
            if not user_input:
                return JsonResponse({'error': '메시지를 입력해주세요.'})
            
            # 입력값에 따른 응답 생성
            response = generate_response(user_input)
            
            return JsonResponse({
                'success': True,
                'user_message': user_input,
                'bot_response': response
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 요청 형식입니다.'})
        except Exception as e:
            return JsonResponse({'error': f'오류가 발생했습니다: {str(e)}'})
    
    return JsonResponse({'error': 'POST 요청만 허용됩니다.'})

def generate_response(user_input):
    """사용자 입력에 따른 응답 생성 로직"""
    user_input = user_input.lower()
    
    # 간단한 키워드 기반 응답 시스템
    responses = {
        '안녕': '안녕하세요! 무엇을 도와드릴까요?',
        'hello': 'Hello! How can I help you?',
        '날씨': '오늘 날씨가 궁금하시군요! 기상청 사이트를 확인해보시는 것을 추천드려요.',
        '시간': '현재 시간을 알고 싶으시군요. 브라우저에서 시간을 확인하실 수 있어요.',
        '도움': '무엇을 도와드릴까요? 궁금한 것이 있으면 언제든 물어보세요!',
        '감사': '천만에요! 도움이 되었다니 기쁘네요.',
        '바이': '안녕히 가세요! 좋은 하루 되세요.',
    }
    
    # 키워드 매칭
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    
    # 질문 형태 감지
    if '?' in user_input or '뭐' in user_input or '어떻게' in user_input:
        return f'"{user_input}"에 대한 질문이시군요! 더 구체적으로 말씀해 주시면 더 정확한 답변을 드릴 수 있어요.'
    
    # 기본 응답
    return f'"{user_input}"라고 말씀하셨군요. 흥미로운 이야기네요! 더 자세히 이야기해 주세요.'