"""
Interactive Questionnaire for Statement of Intent

This script guides students through answering questions for their Statement of Intent,
collecting responses, and generating the final document using the Gemini API.
"""

import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path
from generate_statement_prompt import generate_prompt
from gemini_utils import configure_gemini, generate_statement

class InteractiveQuestionnaire:
    def __init__(self):
        self.responses: Dict[str, Any] = {}
        self.questions: List[Dict] = []
        self.current_question_index = 0
        self.script_dir = Path(__file__).parent.absolute()
        self.responses_path = self.script_dir / 'student_responses.json'
        self.load_questions()

    def load_questions(self):
        """Load questions from the schema file and question file."""
        try:
            # Get the directory of the current script
            script_dir = Path(__file__).parent.absolute()
            
            # Load schema for structure
            schema_path = script_dir / 'statement_intent_schema.json'
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
                
            # Load questions from markdown file
            questions_path = script_dir / 'QS_STATEMENT_OF_INTENT.md'
            with open(questions_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse questions from markdown
            self.parse_questions(content)
            
            if not self.questions:
                print("Warning: No questions were parsed from the file.")
                
        except FileNotFoundError as e:
            print(f"Error: {e.filename} not found.")
            print(f"Current directory: {os.getcwd()}")
            print(f"Script directory: {script_dir}")
            exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in schema file.")
            exit(1)

    def parse_questions(self, content: str):
        """Parse questions from markdown content."""
        # Simple approach: Look for lines with question marks
        lines = content.split('\n')
        current_section = "Introduction"
        question_count = 0
        
        for i, line in enumerate(lines):
            # Check for section headers
            if line.startswith('## '):
                current_section = line.replace('## ', '').strip()
                continue
                
            # Look for questions (lines with **What, **How, etc.)
            if '**' in line and '?' in line and any(q in line for q in ['What', 'How', 'Why', 'Describe']):
                question_text = line.strip().replace('**', '')
                question_count += 1
                
                # Get the title from the previous ### line if available
                title = ""
                for j in range(i-1, max(0, i-10), -1):
                    if lines[j].startswith('### '):
                        title = lines[j].replace('### ', '').strip()
                        break
                
                if not title:
                    title = f"Question {question_count}"
                
                # Create question object
                question = {
                    'section': current_section,
                    'title': title,
                    'text': question_text,
                    'id': f"q{question_count}",
                    'required': True
                }
                
                self.questions.append(question)
        
        # If no questions were found, add some default questions
        if not self.questions:
            print("No questions found in the markdown file. Adding default questions.")
            default_questions = [
                {
                    'section': 'Introduction',
                    'title': 'Project Title',
                    'text': 'What is the proposed title of your Industrial Technology Multimedia Major Project?',
                    'id': 'q1',
                    'required': True
                },
                {
                    'section': 'Introduction',
                    'title': 'Project Type',
                    'text': 'What is the specific type of multimedia product you intend to create?',
                    'id': 'q2',
                    'required': True
                },
                {
                    'section': 'Introduction',
                    'title': 'Problem/Opportunity',
                    'text': 'What specific problem, opportunity, or need does your project aim to address?',
                    'id': 'q3',
                    'required': True
                },
                {
                    'section': 'Target Audience',
                    'title': 'Audience',
                    'text': 'Who is the primary target audience for your project?',
                    'id': 'q4',
                    'required': True
                },
                {
                    'section': 'Implementation',
                    'title': 'Technologies',
                    'text': 'What are the primary multimedia technologies you plan to use?',
                    'id': 'q5',
                    'required': True
                }
            ]
            self.questions.extend(default_questions)

    def display_question(self, question: Dict):
        """Display the current question and navigation options."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{question['section']}")
        print("=" * len(question['section']))
        print(f"\n{question['text']}")
        
        # Show if question has been answered
        question_id = question['id']
        if question_id in self.responses:
            print("\nCurrent response:")
            print("-" * 15)
            print(self.responses[question_id])
            print("-" * 15)
        
        # Show navigation
        print("\n" + "-" * 50)
        print("Options:")
        print("1. Answer this question")
        print("2. Skip this question")
        if self.current_question_index > 0:
            print("3. Previous question")
        if self.current_question_index < len(self.questions) - 1:
            print("4. Next question")
        print("5. Save and generate statement")
        print("6. Save responses without generating")
        print("7. Exit without saving")
        print("-" * 50)

    def get_user_input(self, question: Dict) -> str:
        """Get and validate user input for the current question."""
        print(f"\n{question['text']}")
        print("\nEnter your response below (or press Enter to skip)")
        print("You can use multiple lines. Type 'DONE' on a new line when finished.")
        print("> ", end='')
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
            if not lines:  # First line
                print("> ", end='')
        
        return "\n".join(lines).strip()

    def save_responses(self):
        """Save responses without generating the statement."""
        if not self.responses:
            print("No responses to save.")
            return False
        
        with open(self.responses_path, 'w', encoding='utf-8') as f:
            json.dump(self.responses, f, indent=2)
        
        print(f"\nResponses saved to {self.responses_path}")
        return True

    def run(self):
        """Run the interactive questionnaire."""
        # Check if we have any questions
        if not self.questions:
            print("\nError: No questions available. Cannot continue.")
            return
            
        while True:
            # Make sure we don't go out of bounds
            if self.current_question_index >= len(self.questions):
                self.current_question_index = len(self.questions) - 1
            elif self.current_question_index < 0:
                self.current_question_index = 0
                
            question = self.questions[self.current_question_index]
            self.display_question(question)
            
            # Get user choice
            choices = ["1", "2"]
            if self.current_question_index > 0:
                choices.append("3")
            if self.current_question_index < len(self.questions) - 1:
                choices.append("4")
            choices.extend(["5", "6", "7"])
            
            while True:
                choice = input("\nChoose an option: ").strip()
                if choice in choices:
                    break
                print("Invalid choice. Please try again.")
            
            # Handle choice
            if choice == "1":  # Answer
                response = self.get_user_input(question)
                if response:
                    self.responses[question['id']] = response
                self.current_question_index += 1
            elif choice == "2":  # Skip
                self.current_question_index += 1
            elif choice == "3" and "3" in choices:  # Previous
                self.current_question_index = max(0, self.current_question_index - 1)
            elif choice == "4" and "4" in choices:  # Next
                self.current_question_index += 1
            elif choice == "5":  # Save and generate
                self.save_and_generate()
                return
            elif choice == "6":  # Save without generating
                if self.save_responses():
                    print("\nResponses saved. You can continue later by running this program again.")
                    return
            elif choice == "7":  # Exit
                print("\nExiting without saving. Your progress will be lost.")
                return
            
            # Wrap around if needed
            if self.current_question_index >= len(self.questions):
                self.current_question_index = 0
    
    def save_and_generate(self):
        """Save responses and generate the statement of intent."""
        if not self.responses:
            print("No responses to save. Exiting.")
            return
        
        # Save responses
        with open(self.responses_path, 'w', encoding='utf-8') as f:
            json.dump(self.responses, f, indent=2)
        
        print(f"\nResponses saved to {self.responses_path}")
        print("\nGenerating your Statement of Intent...")
        
        try:
            # Configure Gemini
            try:
                configure_gemini()
            except ValueError as e:
                print(f"\nError configuring Gemini API: {str(e)}")
                print("Please check your API key in app_config.py or .env file.")
                return
            except ImportError as e:
                print(f"\nError importing Gemini API: {str(e)}")
                print("Please install the required packages: pip install google-generativeai python-dotenv")
                return
            
            # Generate the prompt
            try:
                prompt = generate_prompt(self.responses)
            except Exception as e:
                print(f"\nError generating prompt: {str(e)}")
                return
            
            # Generate the statement
            try:
                statement = generate_statement(prompt)
            except Exception as e:
                print(f"\nError from Gemini API: {str(e)}")
                print("This might be due to API rate limits, invalid API key, or network issues.")
                return
            
            # Create a timestamped filename to avoid overwriting previous versions
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'statement_of_intent_{timestamp}.md'
            statement_path = self.script_dir / filename
            
            # Save the generated statement
            with open(statement_path, 'w', encoding='utf-8') as f:
                f.write(statement)
            
            print("\n" + "="*50)
            print("Your Statement of Intent has been generated!")
            print(f"File saved as: {statement_path}")
            print("="*50)
            
            # Show the complete generated document
            print("\nComplete Generated Statement of Intent:")
            print("-" * 50)
            try:
                with open(statement_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(content)
                print("-" * 50)
            except Exception as e:
                print(f"\nCould not display preview: {str(e)}")
            
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}")
            print("Please check your configuration and try again.")

    def load_saved_responses(self):
        """Load previously saved responses if they exist."""
        if self.responses_path.exists():
            try:
                with open(self.responses_path, 'r', encoding='utf-8') as f:
                    self.responses = json.load(f)
                print(f"\nLoaded {len(self.responses)} saved responses from {self.responses_path}")
                return True
            except json.JSONDecodeError:
                print(f"\nError: Invalid JSON in {self.responses_path}")
            except Exception as e:
                print(f"\nError loading responses: {str(e)}")
        return False

if __name__ == "__main__":
    print("NESA Stage 6 IT Multimedia - Statement of Intent Generator")
    print("-" * 50)
    print("This tool will guide you through creating your Statement of Intent.")
    print("You can navigate between questions and save your progress.\n")
    
    try:
        questionnaire = InteractiveQuestionnaire()
        
        # Check for existing responses
        responses_exist = questionnaire.responses_path.exists()
        
        if responses_exist:
            print(f"\nFound existing responses at {questionnaire.responses_path}")
            print("Would you like to:")
            print("1. Load existing responses and continue")
            print("2. Start fresh (existing responses will be overwritten when you save)")
            print("3. Exit")
            
            while True:
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice == "1":
                    questionnaire.load_saved_responses()
                    break
                elif choice == "2":
                    print("\nStarting with fresh responses.")
                    break
                elif choice == "3":
                    print("\nExiting program.")
                    exit(0)
                else:
                    print("Invalid choice. Please try again.")
        
        questionnaire.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {str(e)}")
        print("Please report this issue with the details above.")
    finally:
        print("\nThank you for using the Statement of Intent Generator!")
