import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data directories
DATA_DIR = BASE_DIR / 'app' / 'data'
STUDENTS_DIR = DATA_DIR / 'students'
RESPONSES_DIR = DATA_DIR / 'responses'
GENERATED_DIR = DATA_DIR / 'generated'
TEMPLATES_DIR = BASE_DIR / 'app' / 'templates'
STATIC_DIR = BASE_DIR / 'app' / 'static'

# Ensure directories exist
os.makedirs(STUDENTS_DIR, exist_ok=True)
os.makedirs(RESPONSES_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# File paths
STUDENT_RESPONSES_FILE = RESPONSES_DIR / 'student_responses.json'
STATEMENT_SCHEMA = DATA_DIR / 'statement_intent_schema.json'

# Create a symbolic link for backward compatibility
if not (BASE_DIR / 'statement_intent_schema.json').exists() and STATEMENT_SCHEMA.exists():
    try:
        import os
        os.symlink(STATEMENT_SCHEMA, BASE_DIR / 'statement_intent_schema.json')
    except (OSError, AttributeError):
        pass  # Symlink creation not supported or not needed

# Template files
STATEMENT_TEMPLATE = TEMPLATES_DIR / 'statement_template.md'
STAGE_TEMPLATE = TEMPLATES_DIR / 'stage_template.md'

# Default template content
DEFAULT_STATEMENT_TEMPLATE = """# Statement of Intent: {student_name}

## Project Title
{project_title}

## Project Description
{project_description}

## Project Goals
{project_goals}

## Timeline
{timeline}
"""

DEFAULT_STAGE_TEMPLATE = """# {stage_title}

## Progress Update
{progress_update}

## Challenges Faced
{challenges}

## Next Steps
{next_steps}
"""

# Create default templates if they don't exist
if not STATEMENT_TEMPLATE.exists():
    with open(STATEMENT_TEMPLATE, 'w', encoding='utf-8') as f:
        f.write(DEFAULT_STATEMENT_TEMPLATE)

if not os.path.exists(STAGE_TEMPLATE):
    with open(STAGE_TEMPLATE, 'w', encoding='utf-8') as f:
        f.write(DEFAULT_STAGE_TEMPLATE)
