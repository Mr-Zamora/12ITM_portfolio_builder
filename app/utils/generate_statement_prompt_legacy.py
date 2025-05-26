"""
Statement of Intent Prompt Generator for NESA Stage 6 IT Multimedia

This script generates a prompt for the Gemini API to create a Statement of Intent
document based on student responses.
"""

import json
from pathlib import Path

def load_schema(schema_file='statement_intent_schema.json'):
    """Load the JSON schema file."""
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file '{schema_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in schema file '{schema_file}'.")
        exit(1)

def generate_prompt(student_responses):
    """Generate a prompt for the Gemini API following the NESA Statement of Intent structure."""
    schema = load_schema()
    
    # Build the prompt
    prompt_parts = [
        "# Statement of Intent Generation",
        "\n## Instructions for AI Assistant",
        "You are an expert in NESA Stage 6 Industrial Technology Multimedia. "
        "Your task is to generate a comprehensive Statement of Intent document "
        "based on the student's responses below. Follow these guidelines:",
        "1. Use the exact section structure and numbering from the template",
        "2. Maintain an academic and professional tone",
        "3. Include all relevant details from the student's responses",
        "4. Keep placeholders in square brackets if information is missing",
        "5. Format the output in Markdown with proper headings",
        "\n## Student Responses",
        json.dumps(student_responses, indent=2),
        "\n## Template Structure",
        "Use the following exact structure for the Statement of Intent:",
        "\n# Statement of Intent: [Project Title]",
        "\n## 1.1 Introduction: Defining the Project and its Purpose",
        "For my Industrial Technology Multimedia Major Project, I aim to design, develop, and produce "
        "[specific multimedia product type] titled '[Project Title]'.",
        "\nThis project is driven by the need to address [specific problem/opportunity].",
        "\nMy project will specifically focus on [core content/subject matter] by primarily utilising "
        "[main multimedia forms/technologies].",
        "\n## 1.2 Rationale: Why This Project? Why This Approach?",
        "The decision to undertake this project is motivated by [personal interest/connection].",
        "\nFurthermore, I believe that a [product type] is the most effective medium because [justification].",
        "\nThis project provides a significant opportunity to explore and develop high-level skills in "
        "[2-3 specific techniques/processes], aligning with industry practices in [industry sector].",
        "\n## 1.3 Target Audience: Who is this Project For, and Why?",
        "The primary target audience for this project is [specific demographic].",
        "\nThis audience was selected because [justification with reference to research/insights].",
        "\nI anticipate that this audience will have [relevant characteristics], which will directly "
        "influence the design and functionality of the project.",
        "\n## 1.4 Project Goals and Objectives",
        "The overarching goal of this project is to [main purpose/impact]. To achieve this, the project has "
        "the following specific objectives:",
        "\n### Objective 1: [Specific, measurable objective]",
        "### Objective 2: [Specific, measurable objective]",
        "### Objective 3: [Specific, measurable objective]",
        "\n## 1.5 Technical Implementation",
        "The project will be developed using the following technologies and methodologies:",
        "- [Technology 1]: [Purpose/justification]",
        "- [Technology 2]: [Purpose/justification]",
        "- [Technology 3]: [Purpose/justification]",
        "\n## 1.6 Timeline and Milestones",
        "The deadline for my project is around Week 3, Term 3, however, it has been advised that I complete my project by Week 2 to allocate enough study time for trials. This will give me roughly forty-two weeks to complete my entire project.",
        "\nThe project will follow this timeline:",
        "- **Term 4 (Weeks 1-10)**: [Initial research, concept development, and planning phase]",
        "- **Summer Break**: [Continued skill development and preliminary prototyping]",
        "- **Term 1 (Weeks 1-10)**: [Core development phase - implementation of primary features and technologies]",
        "- **Term 2 (Weeks 1-10)**: [Asset creation, integration, and initial testing]",
        "- **Term 3 (Weeks 1-2)**: [Final refinement, comprehensive testing, and project completion]",
        "\n## 1.7 Expected Outcomes and Success Criteria",
        "The final product must be:",
        "1. [Success criterion 1]",
        "2. [Success criterion 2]",
        "3. [Success criterion 3]",
        "\n## Additional Guidelines",
        "- Maintain the exact heading structure shown above",
        "- Use formal, academic language throughout",
        "- Ensure all sections flow logically from one to the next",
        "- Include specific details from the student's responses where available",
        "- Keep placeholders in square brackets if information is missing",
        "- Format all technical terms and software names in code ticks (e.g., `HTML5`)",
        "- Ensure the document is well-structured and easy to read"
    ]
    
    return "\n".join(prompt_parts)

def get_example_responses():
    """Return example student responses for testing."""
    return {
        "project_title": "Interactive Learning Platform for Physics Concepts",
        "project_type": "Interactive Website",
        "problem_opportunity": "Students struggle with visualizing physics concepts.",
        "target_audience": "Year 11-12 Physics students",
        "technologies": ["HTML/CSS/JavaScript", "Python", "Three.js"],
        "learning_goals": "Master web development and physics visualization techniques.",
        "timeline": "3 months development with bi-weekly milestones.",
        "milestones": "Complete design, implement core features, user testing.",
        "challenges": "Balancing educational content with engaging design."
    }

if __name__ == "__main__":
    # Example usage
    example_responses = get_example_responses()
    prompt = generate_prompt(example_responses)
    print("Generated Prompt:")
    print("-" * 50)
    print(prompt)
