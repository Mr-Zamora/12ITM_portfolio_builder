"""
NESA Stage 6 IT Multimedia Portfolio Builder

This package provides tools for students to create and manage their IT Multimedia portfolios
for the NESA Stage 6 curriculum.
"""

__version__ = "0.1.0"

# Import key components for easier access
from .interactive_questionnaire import InteractiveQuestionnaire

# Define what gets imported with 'from app import *'
__all__ = ['InteractiveQuestionnaire']
