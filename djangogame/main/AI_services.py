# 구글 api 중 멀티턴 챗 서비스 테스트
from django.conf import settings
from google import genai
from google.genai import types

file_path = ""

class GeminiChatService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.chat_sessions = {}
        
    def load_context_from_file(self, file_path):
        """서버의 파일에서 컨텍스트 읽기"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
            return None
    
    def get_or_create_chat(self, session_id):
        """채팅 세션 가져오기 또는 생성"""
        if session_id not in self.chat_sessions:
            self.chat_sessions[session_id] = self.client.chats.create(
                model='gemini-2.5-flash'
            )
        # 초기 히스토리 구성
        history = []
        if long_context:
            history.append({
                'role': 'user',
                'parts': [f"다음 정보를 기억해주세요:\n\n{long_context}"]
            })
            history.append({
                'role': 'model',
                'parts': ['네, 제공해주신 정보를 숙지했습니다. 이를 바탕으로 질문에 답변하겠습니다.']
            })
        chat = model.start_chat(history=history)
        self.chat_sessions[session_id] = {
            'model': model,
            'chat': chat,
            'files': files or []
        }
            
        return self.chat_sessions[session_id]['chat']
    
    def send_message(self, session_id, message):
        """메시지 전송"""
        chat = self.get_or_create_chat(session_id)
        response = chat.send_message(message)
        return response.text
    
    def get_history(self, session_id):
        """히스토리 조회"""
        if session_id in self.chat_sessions:
            chat = self.chat_sessions[session_id]['chat']
            return [
                {
                    'role': msg.role,
                    'content': msg.parts[0].text if hasattr(msg.parts[0], 'text') else str(msg.parts[0])
                }
                for msg in chat.history
            ]
        return []
    
    def clear_session(self, session_id):
        """세션 삭제"""
        if session_id in self.chat_sessions:
            del self.chat_sessions[session_id]
            return True
        return False

gemini_chat = GeminiChatService()