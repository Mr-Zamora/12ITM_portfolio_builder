#!/usr/bin/env python3
"""
Test script for the Interactive Questionnaire.

This script tests the basic functionality of the InteractiveQuestionnaire class
with the new project structure.
"""

import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.absolute()))

from app.interactive_questionnaire import InteractiveQuestionnaire

def test_questionnaire_initialization():
    """Test that the questionnaire initializes correctly."""
    print("Testing questionnaire initialization...")
    questionnaire = InteractiveQuestionnaire()
    assert questionnaire is not None
    print("[OK] Questionnaire initialized successfully")

def test_question_loading():
    """Test that questions are loaded correctly."""
    print("\nTesting question loading...")
    questionnaire = InteractiveQuestionnaire()
    assert hasattr(questionnaire, 'questions')
    assert len(questionnaire.questions) > 0
    print(f"[OK] Loaded {len(questionnaire.questions)} questions")

def test_responses_saving():
    """Test that responses can be saved."""
    print("\nTesting response saving...")
    test_responses = {
        "project_title": "Test Project",
        "project_description": "A test project description",
        "project_goals": "Test goals",
        "timeline": "Test timeline"
    }
    
    questionnaire = InteractiveQuestionnaire()
    questionnaire.responses = test_responses
    
    # This will save to a temporary file
    questionnaire.save_responses()
    assert questionnaire.responses_path.exists()
    print(f"[OK] Responses saved to {questionnaire.responses_path}")
    
    # Clean up
    questionnaire.responses_path.unlink()

if __name__ == "__main__":
    print("Running tests...\n")
    test_questionnaire_initialization()
    test_question_loading()
    test_responses_saving()
    print("\n[SUCCESS] All tests passed!")
