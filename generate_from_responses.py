#!/usr/bin/env python3
"""
Simple script to generate a statement from existing responses without interactive input.
"""

import json
from pathlib import Path
from app.utils.generate_statement_prompt import generate_prompt
from app.utils.gemini_utils import configure_gemini, generate_statement
from app.app_config import RESPONSES_DIR, GENERATED_DIR

def generate_from_file(responses_file='student_responses.json'):
    """Generate a statement from an existing responses file."""
    # Find the responses file
    responses_path = RESPONSES_DIR / responses_file
    if not responses_path.exists():
        # Try looking in the root directory for backward compatibility
        responses_path = Path(__file__).parent / responses_file
        if not responses_path.exists():
            print(f"Error: Could not find responses file {responses_file}")
            return
    
    print(f"Loading responses from {responses_path}")
    
    # Load the responses
    try:
        with open(responses_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Check if it's the new format with metadata
        if isinstance(data, dict) and 'responses' in data:
            responses = data['responses']
            student_id = data.get('student_id', 'unknown')
        else:
            # Assume it's the old format (just a dict of responses)
            responses = data
            student_id = 'unknown'
        
        print(f"Loaded {len(responses)} responses for student {student_id}")
        
        # Generate the prompt
        print("\nGenerating prompt...")
        prompt = generate_prompt(responses)
        
        # Generate the statement
        print("\nGenerating statement using Gemini API...")
        statement = generate_statement(prompt)
        
        # Save the generated statement
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Create output directory
        output_dir = GENERATED_DIR / student_id
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f'statement_of_intent_{timestamp}.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(statement.text)
        
        print(f"\nStatement generated and saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("NESA Stage 6 IT Multimedia - Statement Generator")
    print("-" * 50)
    
    # Use the default student_responses.json file
    generate_from_file('student_responses.json')
