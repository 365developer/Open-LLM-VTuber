from llm.llm_interface import LLMInterface
from llm.ollama import LLM as OllamaLLM
from llm.memGPT import LLM as MemGPTLLM
from typing import Type

import yaml
import os
# load configurations
def load_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(dir_path, "memgpt_config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
config = load_config()
def get_config(key, default=None):
    return config.get(key, default)

class LLMFactory:
    @staticmethod
    def create_llm(llm_provider, **kwargs) -> Type[LLMInterface]:

        if llm_provider == "ollama":
            return OllamaLLM(
                system=kwargs.get("SYSTEM_PROMPT"),
                base_url=kwargs.get("BASE_URL"),
                model=kwargs.get("MODEL"),
                llm_api_key=kwargs.get("LLM_API_KEY"),
                project_id=kwargs.get("PROJECT_ID"),
                organization_id=kwargs.get("ORGANIZATION_ID"),
                verbose=kwargs.get("VERBOSE", False)

            )
        elif llm_provider == "memgpt":
            return MemGPTLLM(
                base_url=kwargs.get("BASE_URL"),
                server_admin_token=kwargs.get("ADMIN_TOKEN"),
                agent_id=kwargs.get("AGENT_ID"),
                verbose=kwargs.get("VERBOSE", False)
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}")

# 使用工廠創建 LLM 實例
# llm_instance = LLMFactory.create_llm("ollama", **config_dict)