"""
Base classes for automated red-team agents.

This is a lightweight, PyRIT-inspired structure:
- an Agent that proposes adversarial prompts
- a Target that represents the LLM we attack
- a Scorer that estimates how successful an attack was
"""

from abc import ABC, abstractmethod
from typing import List, Tuple


class TargetLLM(ABC):
    """Abstract LLM target – anything that takes text and returns text."""

    @abstractmethod
    def query(self, prompt: str) -> str:
        ...


class AttackScorer(ABC):
    """Scores whether a response looks like a successful attack."""

    @abstractmethod
    def score(self, response: str) -> float:
        ...


class RedTeamAgent(ABC):
    """Base class for red-team agents."""

    def __init__(self, target: TargetLLM, scorer: AttackScorer, max_iters: int = 5):
        self.target = target
        self.scorer = scorer
        self.max_iters = max_iters

    @abstractmethod
    def run_attack(self, initial_prompt: str) -> List[Tuple[str, str, float]]:
        """
        Returns a list of (prompt, response, score) for each iteration.
        """
        ...
