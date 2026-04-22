from abc import ABC, abstractmethod

class AIPlatform(ABC):
    @abstractmethod
    def chat(self, propmt: str)-> str:
        pass