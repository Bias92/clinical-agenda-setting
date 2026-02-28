"""
LLM client wrapper for OpenAI API calls.
Supports GPT-3.5 Turbo (paper's primary model).
"""

import os
from openai import OpenAI


class LLMClient:
    """Wrapper for OpenAI API calls with conversation history management."""

    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0.0):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY 환경변수가 설정되지 않았습니다.\n"
                "터미널에서 실행: export OPENAI_API_KEY='sk-your-key'"
            )
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature

    def single_call(
        self, system_prompt: str, user_prompt: str, max_tokens: int = 1024
    ) -> str:
        """단일 호출: system prompt + user prompt → response"""
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content.strip()

    def conversation_call(
        self, messages: list[dict], max_tokens: int = 512
    ) -> str:
        """대화형 호출: 메시지 히스토리 전체를 전달"""
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=max_tokens,
            messages=messages,
        )
        return response.choices[0].message.content.strip()
