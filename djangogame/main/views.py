from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import main.services

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


# 구글 api 멀티턴 챗 테스트
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .AI_services import gemini_chat

ai_text_path = '/static/text/test_text.txt'

def chat_page(request):
    """채팅 페이지 렌더링"""
    return render(request, 'chat_test.html')

@csrf_exempt
def chat_message(request):
    """채팅 메시지 처리"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
            message = data.get('message')
            system_instruction = data.get('system_instruction')
            use_context_file = data.get('use_context_file', False)  # 컨텍스트 파일 사용 여부
            
            if not session_id or not message:
                return JsonResponse({
                    'error': 'session_id와 message가 필요합니다.'
                }, status=400)
                
            # 서버의 미리 준비된 파일에서 컨텍스트 로드
            long_context = None
            if use_context_file:
                context_file_path = ai_text_path # 준비된 파일 path
                long_context = gemini_chat.load_context_from_file(context_file_path)
            
            response = gemini_chat.send_message(
                session_id=session_id,
                message=message,
                system_instruction=system_instruction,
                long_context=long_context
            )
            
            return JsonResponse({
                'success': True,
                'session_id': session_id,
                'response': response
            })
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'POST 요청만 가능합니다.'}, status=405)

@csrf_exempt
def get_chat_history(request):
    """채팅 히스토리 조회"""
    session_id = request.GET.get('session_id')
    
    if not session_id:
        return JsonResponse({'error': 'session_id가 필요합니다.'}, status=400)
    
    history = gemini_chat.get_history(session_id)
    
    return JsonResponse({
        'session_id': session_id,
        'history': history
    })

@csrf_exempt
def clear_chat(request):
    """채팅 초기화"""
    if request.method == 'POST':
        data = json.loads(request.body)
        session_id = data.get('session_id')
        
        if not session_id:
            return JsonResponse({'error': 'session_id가 필요합니다.'}, status=400)
        
        success = gemini_chat.clear_session(session_id)
        
        return JsonResponse({
            'success': success,
            'message': '채팅이 초기화되었습니다.' if success else '세션을 찾을 수 없습니다.'
        })
    
    return JsonResponse({'error': 'POST 요청만 가능합니다.'}, status=405)