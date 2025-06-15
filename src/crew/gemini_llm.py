from crewai.llms.base_llm import BaseLLM
from typing import Any, Dict, List, Optional, Union
import requests
import os

class GeminiLLM(BaseLLM):
    def __init__(self, model: str, api_key: str, temperature: Optional[float] = None):
        super().__init__(model=model, temperature=temperature)
        self.api_key = api_key
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    def call(
        self,
        messages: Union[str, List[Dict[str, str]]],
        tools: Optional[List[dict]] = None,
        callbacks: Optional[List[Any]] = None,
        available_functions: Optional[Dict[str, Any]] = None,
    ) -> Union[str, Any]:
        # Support both string and list of dicts
        if isinstance(messages, str):
            contents = [{"role": "user", "parts": [{"text": messages}]}]
        else:
            contents = [{"role": "user", "parts": [{"text": m["content"]}]} for m in messages]
        payload = {
            "contents": contents
        }
        response = requests.post(
            self.endpoint + f"?key={self.api_key}",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]

    def supports_function_calling(self) -> bool:
        return False

    def get_context_window_size(self) -> int:
        return 8192
