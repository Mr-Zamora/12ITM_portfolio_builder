"""
Utility functions and helpers for the NESA Portfolio Builder.

This package contains various utility modules used throughout the application,
including AI integration, prompt generation, and other helper functions.
"""

from .gemini_utils import configure_gemini, generate_statement
from .generate_statement_prompt import generate_prompt

__all__ = ['configure_gemini', 'generate_statement', 'generate_prompt']
