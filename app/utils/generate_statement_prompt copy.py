"""
Statement of Intent Prompt Generator for NESA Stage 6 IT Multimedia

This script generates a prompt for the Gemini API to create a Statement of Intent
document based on student responses.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

# Import app_config for file paths
from app.app_config import STATEMENT_SCHEMA

def load_schema(schema_file=None):
    """Load the JSON schema file.
    
    Args:
        schema_file: Optional path to schema file. If None, uses the path from app_config.
    """
    if schema_file is None:
        schema_file = STATEMENT_SCHEMA
        
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file '{schema_file}' not found.")
        # Try the old location as a fallback
        old_path = Path(__file__).parent.parent.parent / 'statement_intent_schema.json'
        if old_path.exists():
            print(f"Using fallback schema file at {old_path}")
            with open(old_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in schema file '{schema_file}'.")
        exit(1)

def generate_prompt(student_responses):
    """
    Generate a prompt for the Gemini API following the NESA Statement of Intent structure,
    with enhanced instructions to ensure Band 6 quality, even with poor student input.
    """
    schema = load_schema() # Schema loaded but not directly used in this prompt's construction

    # Build the prompt
    prompt_parts = [
        "# NESA Stage 6 Industrial Technology Multimedia - Statement of Intent Generation",
        "\n## Instructions for AI Assistant (Band 6 Enhancement Protocol)",
        "You are an expert AI Assistant specializing in the NESA Stage 6 Industrial Technology Multimedia Major Project. Your core task is to generate a comprehensive, academically rigorous, and **Band 6-level Statement of Intent** document based on the student's provided responses. **Crucially, you must not just insert text; you must transform, elevate, and elaborate on the student's input to meet Band 6 standards.**",
        "\n**Follow these strict guidelines for Band 6 quality:**",
        "1.  **Maintain Academic Tone & Formal Language:** Ensure the language is sophisticated, precise, and professional throughout. Avoid colloquialisms or informal phrasing.",
        "2.  **Transform and Elevate Content:** If a student's response is vague, generic, or lacks sufficient detail/justification for a Band 6, **you must rephrase, expand, and add the necessary academic depth and logical connections.** For example:",
        "    * **Problem/Opportunity:** If input is a niche preference, reframe it into a demonstrable user need, a gap in existing resources, or a genuine opportunity for innovation.",
        "    * **Justification:** Clearly articulate the 'why' behind choices, linking them to project goals, audience needs, and industry relevance.",
        "    * **Objectives:** Translate commercial/marketing goals (e.g., 'Steam launch,' 'YouTube views') into specific, *product-centric*, and *measurable* academic objectives related to user experience, learning outcomes, or technical demonstration.",
        "    * **Characteristics/Criteria:** Convert subjective desires into actionable design principles or measurable evaluation points."
        "3.  **Ensure Specificity and Detail:** Elaborate on broad statements, adding concrete examples or explanations where appropriate.",
        "4.  **Logical Coherence:** Ensure all sections flow logically and build upon each other. Explicitly connect the problem statement to the project's solution, objectives, and success criteria.",
        "5.  **Adhere to Structure:** Use the exact section structure, numbering, and headings provided in the template below.",
        "6.  **Placeholders:** If information is genuinely missing and cannot be reasonably inferred or elevated to Band 6 standard, keep the bracketed placeholder `[ ]` as a prompt for future student input.",
        "7.  **Formatting:** Format all technical terms, software, and hardware names in code ticks (e.g., `Python`, `Adobe After Effects`, `Raspberry Pi`).",

        "\n## Student Responses (for reference and transformation)",
        json.dumps(student_responses, indent=2), # Displays student's raw input to the AI

        "\n## Band 6 Statement of Intent Template (to be populated and elevated by AI)",
        "\n# Statement of Intent: [Project Title - *Incorporate student's project title (e.g., `q1`)*]",

        "\n## 1.1 Introduction: Defining the Project and its Purpose",
        "For my Industrial Technology Multimedia Major Project, I intend to design, develop, and produce a [specific multimedia product type - *Use `q2`. Elevate if generic, e.g., 'a highly interactive web-based simulation' instead of just 'website'*] titled '[Project Title - *From `q1`*]'.",
        "\nThis project is primarily driven by the need to address [specific problem/opportunity - *Use `q3`. **CRITICAL**: Rephrase student input to reflect a genuine user need, a gap in knowledge/resources, or a significant societal/creative opportunity, not a niche preference or personal whim. Ensure academic justification.*].",
        "\nMy project will specifically focus on [core content/subject matter - *Use `q5`. Elaborate on the core theme, narrative, or gameplay focus beyond just listing techniques. E.g., 'the exploration of non-Euclidean geometry through interactive puzzle design'*] by primarily utilising [main multimedia forms/technologies - *Use `q4`. List specific software/languages and justify their relevance to the project's aims*].",

        "\n## 1.2 Rationale: Why This Project? Why This Approach?",
        "The decision to undertake this project is deeply motivated by [personal interest/connection - *Use `q5` and any other relevant student input. Connect personal passion to the project's academic or industry relevance*]. This pursuit aligns with aspirations within the [industry sector - *Use `q8`. Be specific, e.g., 'digital game development,' 'interactive educational media'*] industry sector.",
        "\nFurthermore, I firmly believe that a [product type - *From `q2`*] is the most effective medium for this project because [justification - *Use `q6`. **Elevate**: Explain *why* this specific medium (e.g., a game, a website, an animation) uniquely addresses the identified problem/opportunity and engages the target audience, leveraging its specific characteristics (e.g., interactivity, immersion, visual storytelling, accessibility). Avoid vague statements like 'it's suitable'.*].",
        "\nThis project provides a significant opportunity to explore and develop high-level skills in [2-3 specific techniques/processes - *Use `q7`. Be specific and demonstrate ambition, e.g., 'advanced character rigging and inverse kinematics,' 'real-time shader development,' 'complex database integration for dynamic content delivery'*], directly aligning with contemporary industry practices in [industry sector - *From `q8`*].",

        "\n## 1.3 Target Audience: Who is this Project For, and Why?",
        "The primary target audience for '[Project Title - *From `q1`*]' is [specific demographic - *Use `q10`. Be precise, e.g., 'Year 9-10 Science students studying ecosystems,' 'Independent game enthusiasts aged 25-45 who appreciate narrative-driven puzzle games'*].",
        "\nThis audience was meticulously selected because [justification with reference to research/insights - *Use `q9`. **Elevate**: Avoid stereotypes or generalisations. Base justification on identified needs, learning gaps, market analysis, or specific psychological insights relevant to their engagement with multimedia. E.g., 'existing resources fail to cater to their visual learning styles,' 'this demographic actively seeks emotionally resonant gaming experiences'*].",
        "\nI anticipate that this audience will exhibit [relevant characteristics - *Use `q10`, `q11`. **Transform**: Convert subjective desires into actionable user characteristics influencing design (e.g., 'a high level of digital literacy and access to mobile devices,' 'a preference for immersive narratives over competitive gameplay,' 'a desire for challenging mental stimulation').*], which will directly influence the design, user experience, and functionality of the project to ensure optimal engagement and efficacy.",

        "\n## 1.4 Project Goals and Objectives",
        "The overarching goal of this project is to [main purpose/impact - *Use `q11`. **Elevate**: Reframe vague desires (e.g., 'feel young') into concrete, measurable impacts or benefits for the user, aligning with the project's core problem/opportunity. E.g., 'provide an innovative platform for conceptual understanding,' 'deliver a deeply engaging interactive narrative experience'*]. To achieve this, the project has the following specific, measurable, and academically relevant objectives:",
        "\n- **Objective 1 (User Experience/Learning Outcome):** [Specific, measurable objective - *Use `q15`. **CRITICAL Transformation**: If student input is a commercial goal (e.g., 'launch on Steam'), rephrase it to describe what the *user will achieve or experience within the product*. E.g., 'Enable users to successfully complete all three core levels of the game, demonstrating mastery of its unique puzzle mechanics,' or 'Facilitate clear comprehension of complex scientific principles through interactive visualizations.'*]",
        "\n- **Objective 2 (Engagement/Aesthetics/Technical Aspect):** [Specific, measurable objective - *Use `q16` or other relevant input. Focus on the project's inherent qualities. E.g., 'Achieve a consistent and compelling [visual style, e.g., cyberpunk aesthetic] and [auditory design, e.g., atmospheric soundscape] that enhances immersion and narrative delivery,' or 'Ensure robust and intuitive user interface design allowing seamless navigation and interaction.'*]",
        "\n- **Objective 3 (Skill Demonstration/Problem-Solving):** [Specific, measurable objective - *Use `q14` or `q7`. This objective should highlight a key technical or creative challenge. E.g., 'Successfully implement advanced [skill, e.g., procedural generation algorithms] to create dynamic and replayable content,' or 'Demonstrate sophisticated [skill, e.g., character animation] that conveys distinct personality and emotional depth.'*]",

        "\n## 1.5 Project Parameters, Scope, and Constraints",
        "The final output of this project will be a [product type - *From `q2`*], delivered as [specific format(s) and key technical parameters - *E.g., 'an HTML5 web application optimized for desktop browsers,' 'an MP4 video file (approx. X minutes, 1920x1080 resolution),' 'a standalone executable for Windows.'*].",
        "\nThe project's scope will encompass [3-5 key components/features defining boundaries - *List concrete features that will be included, e.g., 'three distinct game levels,' 'an interactive quiz module,' 'custom character models and animations for key figures.'*]. To maintain feasibility within the project timeline, elements such as [briefly mention 1-2 explicitly excluded items to manage scope, e.g., 'multiplayer functionality,' 'extensive voice acting,' 'dynamic user accounts'] will be excluded from the final product.",
        "\nKey constraints and challenges anticipated during development include:",
        "-   **Time:** The most significant constraint is the finite timeline of the HSC course, approximately forty-two weeks, necessitating rigorous time management and adherence to the detailed schedule outlined below. (This is static; student doesn't need to input for it).",
        "-   **Skills & Knowledge:** Successful execution requires developing proficiency in [1-2 specific advanced skills needed - *Use `q19`, `q20`. E.g., 'advanced Python scripting for game logic,' 'complex 3D modeling workflows in Blender'*]. Strategies for acquiring these skills will include [mention specific learning methods, e.g., 'dedicated online tutorials (Udemy/Skillshare),' 'mentorship from industry professionals,' 'extensive practice with small prototype projects'*].",
        "-   **Resources & Equipment:** Access to required software (`{tech_details_raw.replace('`', '')}` if available, otherwise specify. E.g., `Adobe Creative Suite`, `Unity`, `Blender`) and hardware ([e.g., 'a powerful rendering workstation,' 'a drawing tablet']) is essential. Potential limitations regarding [mention specific resource constraints from `q21`, `q22`, e.g., 'limited access to high-end rendering machines,' 'dependency on school-provided software licenses'] will be meticulously managed.",
        "-   **Technical Complexity:** Implementing features such as [specific complex technical aspect from `q22` or inferred, e.g., 'dynamic collision detection for complex geometries,' 'an adaptive AI system for enemy behavior,' 'real-time particle effects for magical spells'] presents a significant technical challenge that will necessitate thorough planning, iterative prototyping, and robust debugging processes.",

        "\n## 1.6 Timeline and Milestones",
        "The deadline for my project is around Week 3, Term 3, however, it has been advised that I complete my project by Week 2 to allocate enough study time for trials. This will give me roughly forty-two weeks to complete my entire project.",
        "\nThe project will follow this structured timeline:",
        "-   **Term 4 (Weeks 1-10)**: Initial research, concept development, and detailed planning phase, encompassing comprehensive industry study, preliminary design documentation, and initial technology setup and familiarization.",
        "-   **Summer Break**: Dedicated skill development and preliminary prototyping, focusing on refining core technical proficiencies (e.g., coding, animation techniques) and building fundamental gameplay mechanics or interactive elements.",
        "-   **Term 1 (Weeks 1-10)**: Core development phase, involving the implementation of primary features, integration of key technologies (e.g., Flask with front-end components, server deployment), and the establishment of foundational game loops or content structures.",
        "-   **Term 2 (Weeks 1-10)**: Asset creation, comprehensive integration, and initial rigorous testing, encompassing the development of detailed graphics, sound design, intricate animation sequences, and extensive playtesting for functionality, usability, and bug identification.",
        "-   **Term 3 (Weeks 1-2)**: Final refinement, comprehensive testing, and project completion, leading to the preparation for final presentation, extensive documentation for the management folio, and final quality assurance.",

        "\n## 1.7 Expected Outcomes and Success Criteria",
        "The success of '[Project Title - *From `q1`*]' will be rigorously evaluated against its effectiveness in meeting the stated objectives and the overall quality of the final product and supporting documentation. Specific criteria for success include:",
        "1.  **Objective Achievement & User Impact:** The project must demonstrably achieve its primary objectives (as outlined in Section 1.4), particularly in terms of [reiterate key user outcome from objectives, e.g., 'player engagement with unique mechanics,' 'comprehension of complex concepts']. This will be measured through [how it will be measured - *Use `q23`, `q24`. **Transform**: Focus on internal, academic validation methods like 'structured user testing feedback,' 'pre/post-testing questionnaires for learning outcomes,' 'observational analysis of user interaction,' rather than commercial metrics.*].",
        "2.  **Technical Excellence & Aesthetic Cohesion:** The final product must exhibit a high level of technical proficiency in [technical skills from `q27`, e.g., 'coding efficiency,' 'animation fluidity,' 'graphics rendering quality'], and present a cohesive [aesthetic style from `q17`, e.g., 'nostalgic retro video arcade aesthetic'] and sound design. This will be evidenced by [how it will be shown - e.g., 'documented testing reports demonstrating smooth performance,' 'consistent visual and auditory design principles detailed in the folio,' 'positive critical review from peers/mentors on execution.']",
        "3.  **Audience Appropriateness & Refinement:** The project must be highly relevant, accessible, and engaging for its defined target audience ([target audience from `q10`]). This will be continually assessed and refined through [how it will be assessed - *Use `q25`. **Transform**: Focus on 'iterative user feedback cycles,' 'expert critique from mentors,' 'formal evaluation against design specifications documented in the folio,' rather than just 'industry professionals reviewing'.*].",

        "\n## 1.8 Opportunities",
        "Upon successful completion, '[Project Title - *From `q1`*]' will serve as a significant piece for my personal portfolio, showcasing my advanced skills in [2-3 key skill areas demonstrated - *Use `q28` and other relevant skill mentions. E.g., 'interactive game design,' 'complex 2D/3D animation pipelines,' 'full-stack web development with dynamic content handling'*]. This comprehensive project will be invaluable for supporting applications for further education or career opportunities in the [relevant industry/field - *Use `q8` and `q28`. E.g., 'digital media,' 'game development,' 'interactive design'*] sectors. Furthermore, the project provides valuable experience in [valuable process learned - e.g., 'managing a large-scale creative project,' 'iterative design based on rigorous feedback,' 'problem-solving complex technical challenges under pressure'], which is highly transferable to future endeavours. (Note: Adherence to copyright and licensing will determine public dissemination)."
    ]

    return "\n".join(prompt_parts)

# --- Student Responses (This will be loaded from student_responses.json in your app) ---
# For local testing, we'll keep the problematic responses to show the enhancement effect.
# def get_mock_student_responses():
#     """Returns mock student responses, simulating input from student_responses.json."""
#     return {
#         "q1": "Monkey Magic Video Game",
#         "q2": "Video Game",
#         "q3": "There are not monkeys with magic video games available", # Poor input
#         "q4": "Flask, HTML, CSS, jinja, javascript, hosted on a raspberry pi server with joystick controls and keypad controls",
#         "q5": "Retro gaming, 2d and 3d graphics, vfx, animation and coding", # Mixed input
#         "q6": "it's suitable for my target market of young adults and gen x people", # Poor input
#         "q7": "animation, sound design, graphics, 2d and 3d animation, concept sketchets, coding",
#         "q8": "animation, multimedia, vfx, game development",
#         "q9": "They have money to spend, they like nostalgia and have more time than other age groups to explore deep multilevel game play", # Poor input
#         "q10": "young adults and Gen X people", # Demographic
#         "q11": "feel young and relevant, feel in touch with the youth, relive old memories of their youth", # Poor input
#         "q12": "coolness factor, aura", # Unused in enhanced template
#         "q13": "nostalgic, fun, nerdiness", # Unused in enhanced template
#         "q14": "coding, vfx, animation, graphics", # Skill for Objective 3
#         "q15": "minimum viable product (MVP), launch in steam platform, youtube views and trailer", # Poor input for Objective 1
#         "q16": "steam platform, youtube, online, deployed in raspberry pi server", # Poor input for Objective 2
#         "q17": "nostalgic, sound design, retro arcade vibes", # Success Criterion 1 raw
#         "q18": "monetization", # Unused
#         "q19": "learn coding, improve in2d and 3d animation", # Skills for Constraints
#         "q20": "coding and animation", # Skill for Constraints (redundant)
#         "q21": "raspberry pi server", # Resource for Constraints
#         "q22": "sound design and animation", # Challenge for Constraints
#         "q23": "launch in steam platform, many youtube views and reviews and comments", # External validation (for Success Criterion 1)
#         "q24": "steam reviews and youtube views and comments", # External validation (for Success Criterion 2)
#         "q25": "i will get industry professionals to review and offer feedback", # External validation (for Success Criterion 3)
#         "q26": "nostalgic reto video arcade vibe", # Success Criterion (redundant with q17)
#         "q27": "coding, animation, graphics, wit and humour", # Success Criterion (attributes)
#         "q28": "multimedia, motion graphics, game development" # Opportunities
#     }

if __name__ == "__main__":
    # In your actual app, student_responses would be loaded from student_responses.json
    # For demonstration, we use the mock responses.
    mock_responses = get_mock_student_responses()
    prompt = generate_prompt(mock_responses)
    print("Generated AI Prompt:")
    print("=" * 70)
    print(prompt)
    print("=" * 70)
    print("\nIMPORTANT: The Band 6 quality depends on the AI's ability to interpret and enhance these instructions. The student's raw input (as seen under 'Student Responses') will be transformed into the higher-level language and justifications expected in the 'Generated Statement of Intent' section.")
