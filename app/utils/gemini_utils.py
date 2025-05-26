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
        api_key (str, optional): Gemini API key. If not provided, looks for GEMINI_API_KEY in environment variables.
    """
    if not api_key:
        # Load from environment variables first
        from dotenv import load_dotenv
        import os
        import sys
        from pathlib import Path
        
        # Try to load from .env file in project root
        project_root = Path(__file__).parent.parent.parent
        load_dotenv(project_root / '.env')
        
        # Check for environment variable
        api_key = os.getenv('GEMINI_API_KEY')
        
        # If still no API key, check if we're in development mode
        if not api_key:
            # Look for the API key in the .env file directly as a last resort
            env_path = project_root / '.env'
            if env_path.exists():
                with open(env_path, 'r') as f:
                    for line in f:
                        if line.startswith('GEMINI_API_KEY='):
                            api_key = line.strip().split('=', 1)[1].strip().strip('"').strip("'")
                            print(f"Loaded API key from .env file")
                            break
        
        if not api_key:
            raise ValueError("No API key found. Please set GEMINI_API_KEY in .env file.")
            
    # Configure the Gemini API
    print(f"Configuring Gemini API with key: {api_key[:5]}...{api_key[-4:]}")
    
    genai.configure(api_key=api_key)

def generate_statement(prompt_text, model_name="gemini-1.5-flash", api_key=None):
    """
    Generate content using the Gemini API.
    
    Args:
        prompt_text (str): The prompt to send to the model
        model_name (str, optional): Name of the Gemini model to use
        api_key (str, optional): Gemini API key. If not provided, will be loaded from environment
        
    Returns:
        str: Generated content
    """
    # Configure Gemini with API key
    configure_gemini(api_key)
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
