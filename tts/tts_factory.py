from .tts_interface import TTSInterface
from typing import Type


class TTSFactory:
    @staticmethod
    def get_tts_engine(engine_type, **kwargs) -> Type[TTSInterface]:
        if engine_type == "AzureTTS":
            from .azureTTS import TTSEngine as AzureTTSEngine
            return AzureTTSEngine(kwargs.get("api_key"), kwargs.get("region"), kwargs.get("voice"))
        elif engine_type == "barkTTS":
            from .barkTTS import TTSEngine as BarkTTSEngine
            return BarkTTSEngine(kwargs.get("voice"))
        elif engine_type == "edgeTTS":
            from .edgeTTS import TTSEngine as EdgeTTSEngine
            return EdgeTTSEngine(kwargs.get("voice"))
        elif engine_type == "pyttsx3TTS":
            from .pyttsx3TTS import TTSEngine as Pyttsx3TTSEngine
            return Pyttsx3TTSEngine()
        elif engine_type == "cosyvoiceTTS":
            from .cosyvoiceTTS import TTSEngine as CosyvoiceTTSEngine
            return CosyvoiceTTSEngine(
                client_url=kwargs.get("client_url"),
                mode_checkbox_group=kwargs.get("mode_checkbox_group"),
                sft_dropdown=kwargs.get("sft_dropdown"),
                prompt_text=kwargs.get("prompt_text"),
                prompt_wav_upload_url=kwargs.get("prompt_wav_upload_url"),
                prompt_wav_record_url=kwargs.get("prompt_wav_record_url"),
                instruct_text=kwargs.get("instruct_text"),
                seed=kwargs.get("seed"),
                api_name=kwargs.get("api_name"),
            )
        elif engine_type == "meloTTS":
            from .meloTTS import TTSEngine as MeloTTSEngine
            return MeloTTSEngine(
                speaker=kwargs.get("speaker"),
                language=kwargs.get("language"),
                device=kwargs.get("device"),
                speed=kwargs.get("speed"),
            )
        else:
            raise ValueError(f"Unknown TTS engine type: {engine_type}")

# Example usage:
# tts_engine = TTSFactory.get_tts_engine("azure", api_key="your_api_key", region="your_region", voice="your_voice")
# tts_engine.speak("Hello world")