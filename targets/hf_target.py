from transformers import pipeline
from .settings import DEFAULT_MODEL_NAME


class HFTarget:
    def __init__(self, model_name: str = DEFAULT_MODEL_NAME, max_new_tokens: int = 128):
        # force CPU, avoid CUDA / GPU issues
        self._pipe = pipeline(
            "text-generation",
            model=model_name,
            device=-1,          # CPU only
        )
        self.max_new_tokens = max_new_tokens

    def query(self, prompt: str) -> str:
        # 🔹 ΑΠΟΦΥΓΗ ΥΠΕΡΜΕΓΕΘΟΥΣ PROMPT
        # Κρατάμε μόνο τα τελευταία 500 χαρακτήρες (ή 800 αν θες)
        truncated_prompt = prompt[-500:]

        outputs = self._pipe(
            truncated_prompt,
            max_new_tokens=self.max_new_tokens,
        )
        out = outputs[0]["generated_text"]
        return out

