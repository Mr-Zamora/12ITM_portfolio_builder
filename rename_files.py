#!/usr/bin/env python3
"""
Script to rename existing response and statement files to follow the snake_case naming convention.
"""

import json
import os
import re
from pathlib import Path

def to_snake_case(text):
    """Convert text to snake_case."""
    if not text:
        return "untitled_project"
        
    # Convert to lowercase
    snake = text.lower()
    # Replace spaces and special characters with underscores
    snake = ''.join(c if c.isalnum() else '_' for c in snake)
    # Replace multiple underscores with a single one
    while '__' in snake:
        snake = snake.replace('__', '_')
    # Remove leading/trailing underscores
    snake = snake.strip('_')
    
    return snake

def rename_response_files():
    """Rename response files to follow the snake_case naming convention."""
    responses_dir = Path("app/data/responses")
    
    if not responses_dir.exists():
        print(f"Directory {responses_dir} does not exist.")
        return
    
    # Get all JSON files in the responses directory
    response_files = list(responses_dir.glob("*.json"))
    
    if not response_files:
        print("No response files found.")
        return
    
    print(f"Found {len(response_files)} response files.")
    
    for file_path in response_files:
        # Skip already renamed files
        if not file_path.name.startswith("responses_"):
            continue
            
        try:
            # Load the JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract project title and student ID
            project_title = None
            student_id = None
            
            if isinstance(data, dict):
                if 'project_title' in data:
                    project_title = data['project_title']
                elif 'responses' in data and 'q1' in data['responses']:
                    project_title = data['responses']['q1']
                
                if 'student_id' in data:
                    student_id = data['student_id']
            
            # If no project title found, try to extract from filename
            if not project_title:
                # Extract student_id from filename (responses_XXXXXXXX.json)
                match = re.search(r'responses_(.+)\.json', file_path.name)
                if match:
                    student_id = match.group(1)
                    
                    # Check if there's a statement file with this student_id to get the title
                    generated_dir = Path("app/data/generated") / student_id
                    if generated_dir.exists():
                        statement_files = list(generated_dir.glob("*.md"))
                        if statement_files:
                            # Try to extract title from the first line of the statement file
                            with open(statement_files[0], 'r', encoding='utf-8') as f:
                                first_line = f.readline().strip()
                                if first_line.startswith("# Statement of Intent:"):
                                    project_title = first_line[len("# Statement of Intent:"):].strip()
            
            # If still no project title, use a default
            if not project_title:
                print(f"Could not determine project title for {file_path.name}, using 'untitled_project'")
                project_title = "Untitled Project"
                
            # If no student ID, extract from filename
            if not student_id:
                match = re.search(r'responses_(.+)\.json', file_path.name)
                if match:
                    student_id = match.group(1)
                else:
                    print(f"Could not determine student ID for {file_path.name}, skipping")
                    continue
            
            # Convert project title to snake_case
            snake_title = to_snake_case(project_title)
            
            # Create new filename
            new_filename = f"{snake_title}_{student_id}.json"
            new_path = file_path.parent / new_filename
            
            # Update the file content with project_title if not present
            if 'project_title' not in data and isinstance(data, dict):
                data['project_title'] = project_title
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
            
            # Rename the file
            if new_path != file_path:
                print(f"Renaming {file_path.name} to {new_filename}")
                os.rename(file_path, new_path)
            else:
                print(f"File {file_path.name} already has the correct name")
                
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")

def rename_statement_files():
    """Rename statement files to follow the snake_case naming convention."""
    generated_dir = Path("app/data/generated")
    
    if not generated_dir.exists():
        print(f"Directory {generated_dir} does not exist.")
        return
    
    # Get all student directories
    student_dirs = [d for d in generated_dir.iterdir() if d.is_dir()]
    
    if not student_dirs:
        print("No student directories found.")
        return
    
    print(f"Found {len(student_dirs)} student directories.")
    
    for student_dir in student_dirs:
        # Get all statement files in the student directory
        statement_files = list(student_dir.glob("statement_of_intent_*.md"))
        
        if not statement_files:
            print(f"No statement files found in {student_dir.name}.")
            continue
        
        print(f"Found {len(statement_files)} statement files in {student_dir.name}.")
        
        for file_path in statement_files:
            try:
                # Extract timestamp from filename
                match = re.search(r'statement_of_intent_(.+)\.md', file_path.name)
                if not match:
                    print(f"Could not extract timestamp from {file_path.name}, skipping")
                    continue
                    
                timestamp = match.group(1)
                
                # Try to determine project title from file content
                project_title = None
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith("# Statement of Intent:"):
                        project_title = first_line[len("# Statement of Intent:"):].strip()
                
                # If no project title found, check if there's a response file for this student
                if not project_title:
                    responses_dir = Path("app/data/responses")
                    response_files = list(responses_dir.glob(f"*_{student_dir.name}.json"))
                    if response_files:
                        with open(response_files[0], 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if isinstance(data, dict):
                                if 'project_title' in data:
                                    project_title = data['project_title']
                                elif 'responses' in data and 'q1' in data['responses']:
                                    project_title = data['responses']['q1']
                
                # If still no project title, use a default
                if not project_title:
                    print(f"Could not determine project title for {file_path.name}, using 'untitled_project'")
                    project_title = "Untitled Project"
                
                # Convert project title to snake_case
                snake_title = to_snake_case(project_title)
                
                # Create new filename
                new_filename = f"{snake_title}_statement_of_intent_{timestamp}.md"
                new_path = file_path.parent / new_filename
                
                # Rename the file
                if new_path != file_path:
                    print(f"Renaming {file_path.name} to {new_filename}")
                    os.rename(file_path, new_path)
                else:
                    print(f"File {file_path.name} already has the correct name")
                    
            except Exception as e:
                print(f"Error processing {file_path.name}: {str(e)}")

if __name__ == "__main__":
    print("Renaming response files...")
    rename_response_files()
    
    print("\nRenaming statement files...")
    rename_statement_files()
    
    print("\nDone!")
