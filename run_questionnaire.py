#!/usr/bin/env python3
"""
Simple script to run the Interactive Questionnaire directly.
"""

from app.interactive_questionnaire import InteractiveQuestionnaire

if __name__ == "__main__":
    print("NESA Stage 6 IT Multimedia - Statement of Intent Generator")
    print("-" * 50)
    print("Running the questionnaire directly...\n")
    
    # Create and run the questionnaire
    questionnaire = InteractiveQuestionnaire()
    questionnaire.run()
