"""
Utility functions for interacting with the Gemini API.
"""
import google.generativeai as genai
from pathlib import Path
import json

def configure_gemini(api_key=None):
    """
    Configure the Gemini API with the provided API key.
    
    Args:
        api_key (str, optional): Gemini API key. If not provided, looks for GEMINI_API_KEY in app_config.py.
    """
    if not api_key:
        try:
            # First try to get from app_config.py
            import app_config
            api_key = getattr(app_config, 'GEMINI_API_KEY', None)
        except ImportError:
            # If that fails, try environment variables
            from dotenv import load_dotenv
            import os
            load_dotenv()
            api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("No API key found. Please set GEMINI_API_KEY in app_config.py or .env file.")
    
    genai.configure(api_key=api_key)

def generate_statement(prompt_text, model_name="gemini-1.5-flash"):
    """
    Generate content using the Gemini API.
    
    Args:
        prompt_text (str): The prompt to send to the model
        model_name (str, optional): Name of the Gemini model to use
        
    Returns:
        str: Generated content
    """
    try:
        # First try with the specified model (Gemini 2.5 Flash Preview)
        preferred_model = "gemini-2.5-flash-preview-05-20"
        
        try:
            # Try the preferred model first
            print(f"Trying model: {preferred_model}")
            model = genai.GenerativeModel(preferred_model)
            response = model.generate_content(prompt_text)
            print(f"Successfully used model: {preferred_model}")
            return response.text
        except Exception as e:
            print(f"Could not use preferred model: {e}")
            print("Falling back to alternative models...")
            
            # Get available models
            models = genai.list_models()
            available_models = [model.name for model in models]
            print(f"Available models: {available_models}")
            
            # Try other models in order of preference
            fallback_models = [
                "gemini-1.5-flash",
                "gemini-1.5-pro",
                "gemini-pro"
            ]
            
            for fallback in fallback_models:
                for available in available_models:
                    if fallback in available:
                        model_name = available
                        print(f"Using fallback model: {model_name}")
                        break
                if model_name:
                    break
        
        # Generate content
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        print(f"Error generating content: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check if your API key is valid")
        print("2. Make sure you have internet connectivity")
        print("3. Try using a different model name")
        raise

def save_generated_content(content, filename="generated_statement.md"):
    """
    Save the generated content to a file.
    
    Args:
        content (str): The content to save
        filename (str): Output filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Content saved to {filename}")

def load_student_responses(json_file):
    """
    Load student responses from a JSON file.
    
    Args:
        json_file (str): Path to JSON file with responses
        
    Returns:
        dict: Parsed JSON data
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading responses: {e}")
        raise

def validate_responses(responses, schema_file='statement_intent_schema.json'):
    """
    Validate student responses against the schema.
    
    Args:
        responses (dict): Student responses
        schema_file (str): Path to schema file
        
    Returns:
        tuple: (is_valid, list_of_errors)
    """
    try:
        # Load schema
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        
        errors = []
        
        # Check required fields
        for section in schema.get('sections', []):
            for field in section.get('fields', []):
                field_id = field.get('id')
                if field.get('required', False) and field_id not in responses:
                    errors.append(f"Missing required field: {field_id}")
        
        return (len(errors) == 0, errors)
        
    except Exception as e:
        return (False, [f"Validation error: {str(e)}"])
