#!/usr/bin/env python3
"""
Test script for the Gemini API integration.

This script tests that the API key is properly loaded and the Gemini API
can be successfully called.
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.utils.gemini_utils import configure_gemini, generate_statement

def test_api_key_loading():
    """Test that the API key is properly loaded."""
    print("Testing API key loading...")
    try:
        configure_gemini()
        print("[SUCCESS] API key loaded successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Error loading API key: {str(e)}")
        return False

def test_api_generation():
    """Test that the API can generate content."""
    print("\nTesting content generation...")
    try:
        response = generate_statement("Hello, write a short poem about coding.")
        print("\nGenerated content:")
        print("-" * 50)
        print(response.text)
        print("-" * 50)
        print("[SUCCESS] Content generated successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Error generating content: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Gemini API integration...\n")
    
    # Test API key loading
    if not test_api_key_loading():
        print("\nAPI key loading failed. Please check your .env file or environment variables.")
        sys.exit(1)
    
    # Test content generation
    if not test_api_generation():
        print("\nContent generation failed. Please check your API key and internet connection.")
        sys.exit(1)
    
    print("\n[SUCCESS] All tests passed!")
