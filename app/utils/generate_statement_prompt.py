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
    with enhanced instructions to ensure Band 6 quality, a "community college student" voice,
    and Australian spelling.
    """
    schema = load_schema() # Schema loaded but not directly used in this prompt's construction

    # Build the prompt
    prompt_parts = [
        "# NESA Stage 6 Industrial Technology Multimedia - Statement of Intent Generation",
        "\n## Instructions for AI Assistant (Band 6 Enhancement & Style Adaptation Protocol)",
        "You are an expert AI Assistant specializing in the NESA Stage 6 Industrial Technology Multimedia Major Project. Your core task is to generate a comprehensive, academically rigorous, and **Band 6-level Statement of Intent** document based on the student's provided responses. **Crucially, you must transform, elevate, and elaborate on the student's input to meet Band 6 standards, AND adapt the language style as specified.**",

        "\n**Follow these strict guidelines for Band 6 quality, writing style, and spelling:**",
        "1.  **Content Elevation (Band 6):** If a student's response is vague, generic, or lacks sufficient detail/justification for a Band 6, **you must rephrase, expand, and add the necessary academic depth and logical connections.** For example:",
        "    *   **'Problem/Opportunity':** Reframe niche preferences into demonstrable user needs or genuine opportunities for innovation.",
        "    *   **'Justification':** Clearly articulate the 'why' behind choices, linking them to project goals, audience needs, and industry relevance.",
        "    *   **'Objectives':** Translate commercial/marketing goals (e.g., 'Steam launch,' 'YouTube views') into specific, *product-centric*, and *measurable* academic objectives related to user experience, learning outcomes, or technical demonstration.",
        "    *   **'Characteristics/Criteria':** Convert subjective desires into actionable design principles or measurable evaluation points.",
        "2.  **Language Style Adaptation (Highly Technical Year 12 Student / Community College Voice):**",
        "    *   **Vocabulary:** Use direct, clear, and slightly less formal vocabulary. Replace overly academic/complex words (e.g., 'encompass', 'meticulously', 'mitigate', 'discerning', 'propensity', 'efficacy', 'necessitate') with simpler, more common synonyms (e.g., 'include', 'carefully', 'reduce', 'good', 'tendency', 'effectiveness', 'require').",
        "    *   **Sentence Structure:** Opt for more direct and concise sentence structures. Break down long, complex sentences into shorter, more manageable ones. Prioritise active voice.",
        "    *   **Tone:** Maintain an enthusiastic, confident, and professional tone, reflective of a student passionate about their technical work, but without excessive formality. The language should be highly articulate and clear, but sound like a capable Year 12 student writing a project brief, not a university essay.",
        "    *   **Technical Terminology:** **Crucially, technical terms, software, and hardware names should remain precise and be formatted consistently (e.g., `Python`, `Adobe After Effects`, `Raspberry Pi`). Do NOT simplify technical jargon or compromise accuracy.** The student is highly skilled technically.",
        "3.  **Australian Spelling Conventions:** Consistently use Australian English spelling (e.g., '-ise' instead of '-ize', 'colour' instead of 'color', 'favourite' instead of 'favorite', 'programme' instead of 'program' for a show/event, but 'program' for software code).",
        "4.  **Specificity and Detail:** Elaborate on broad statements, adding concrete examples or explanations where appropriate, but explaining them in the adapted style.",
        "5.  **Logical Coherence:** Ensure all sections flow logically and build upon each other. Explicitly connect the problem statement to the project's solution, objectives, and success criteria, maintaining smooth transitions in the adapted style.",
        "6.  **Adherence to Structure:** Strictly follow the provided section structure and numbering.",
        "7.  **Placeholders:** If information is genuinely missing and cannot be reasonably inferred or elevated to Band 6 standard, keep the bracketed placeholder `[ ]` as a prompt for future student input.",
        "8.  **Formatting:** Use Markdown for headings and emphasis (bolding).",

        "\n## Student Responses (for reference and transformation)",
        json.dumps(student_responses, indent=2), # Displays student's raw input to the AI

        "\n## Band 6 Statement of Intent Template (to be populated, elevated, and styled by AI)",
        "\n# Statement of Intent: [Project Title - *Incorporate student's project title (e.g., `q1`)*]",

        "\n## 1.1 Introduction: Defining the Project and its Purpose",
        "For my Industrial Technology Multimedia Major Project, I'm going to design, build, and make [specific multimedia product type - *Use `q2`. Elevate if generic, e.g., 'a highly interactive web-based simulation' instead of just 'website'. Adapt language.*] titled '[Project Title - *From `q1`*]'.",
        "\nThis project is mostly happening because I've noticed [specific problem/opportunity - *Use `q3`. **CRITICAL**: Rephrase student input to reflect a genuine user need, a gap in knowledge/resources, or a significant societal/creative opportunity, not a niche preference or personal whim. Adapt language to be more direct and less academic.*].",
        "\nMy project will specifically focus on [core content/subject matter - *Use `q5`. Elaborate on the core theme, narrative, or gameplay focus beyond just listing techniques. E.g., 'the exploration of non-Euclidean geometry through interactive puzzle design'. Adapt language.*] by primarily using [main multimedia forms/technologies - *Use `q4`. List specific software/languages and justify their relevance to the project's aims. Keep technical terms precise but adapt surrounding language.*].",

        "\n## 1.2 Rationale: Why This Project? Why This Approach?",
        "I decided to make this project because I'm really into [personal interest/connection - *Use `q5` and any other relevant student input. Connect personal passion to the project's academic or industry relevance. Adapt language.*]. This project fits right in with what I want to do in the [industry sector - *Use `q8`. Be specific, e.g., 'digital game development,' 'interactive educational media'. Adapt language.*] industry.",
        "\nI also really believe that [product type - *From `q2`*] is the best way to do this project because [justification - *Use `q6`. **Elevate**: Explain *why* this specific medium (e.g., a game, a website, an animation) uniquely addresses the identified problem/opportunity and engages the target audience, leveraging its specific characteristics (e.g., interactivity, immersion, visual storytelling, accessibility). Avoid vague statements like 'it's suitable'. Adapt language to be more direct.*].",
        "\nThis project is a huge chance for me to learn and get really good at [2-3 specific techniques/processes - *Use `q7`. Be specific and demonstrate ambition, e.g., 'advanced character rigging and inverse kinematics,' 'real-time shader development,' 'complex database integration for dynamic content delivery'. Adapt language.*], which are all skills used a lot in today's [industry sector - *From `q8`*] industry.",

        "\n## 1.3 Target Audience: Who is this Project For, and Why?",
        "The main people I'm making '[Project Title - *From `q1`*]' for are [specific demographic - *Use `q10`. Be precise, e.g., 'Year 9-10 Science students studying ecosystems,' 'Independent game enthusiasts aged 25-45 who appreciate narrative-driven puzzle games'. Adapt language.*].",
        "\nI picked this group because [justification with reference to research/insights - *Use `q9`. **Elevate**: Avoid stereotypes or generalisations. Base justification on identified needs, learning gaps, market analysis, or specific psychological insights relevant to their engagement with multimedia. Adapt language to be more direct.*].",
        "\nI expect this audience to [relevant characteristics - *Use `q10`, `q11`. **Transform**: Convert subjective desires into actionable user characteristics influencing design (e.g., 'a high level of digital literacy and access to mobile devices,' 'a preference for immersive narratives over competitive gameplay,' 'a desire for challenging mental stimulation'). Adapt language.*], which will directly change how I design the game, how it feels to play, and what it does, so it works well for them.",

        "\n## 1.4 Project Goals and Objectives",
        "The main goal of this project is to [main purpose/impact - *Use `q11`. **Elevate**: Reframe vague desires (e.g., 'feel young') into concrete, measurable impacts or benefits for the user, aligning with the project's core problem/opportunity. E.g., 'provide an innovative platform for conceptual understanding,' 'deliver a deeply engaging interactive narrative experience'. Adapt language.*]. To do this, here are my clear and important goals:",
        "\n- **Objective 1 (User Experience/Learning Outcome):** [Specific, measurable objective - *Use `q15`. **CRITICAL Transformation**: If student input is a commercial goal (e.g., 'launch on Steam'), rephrase it to describe what the *user will achieve or experience within the product*. E.g., 'Enable users to successfully complete all three core levels of the game, demonstrating mastery of its unique puzzle mechanics,' or 'Help players clearly understand complex scientific principles through interactive visualisations.' Adapt language.*]",
        "\n- **Objective 2 (Engagement/Aesthetics/Technical Aspect):** [Specific, measurable objective - *Use `q16` or other relevant input. Focus on the project's inherent qualities. E.g., 'Make the game look good with a consistent [visual style, e.g., cyberpunk aesthetic] and [auditory design, e.g., atmospheric soundscape] to make it more immersive and fun,' or 'Make sure the controls are easy to use so players can move around and interact without problems.' Adapt language.*]",
        "\n- **Objective 3 (Skill Demonstration/Problem-Solving):** [Specific, measurable objective - *Use `q14` or `q7`. This objective should highlight a key technical or creative challenge. E.g., 'Successfully build advanced [skill, e.g., procedural generation algorithms] to make content that feels fresh every time you play,' or 'Show off great [skill, e.g., character animation] that makes characters feel real and expressive.' Adapt language.*]",

        "\n## 1.5 Project Parameters, Scope, and Constraints",
        "The final thing I'm making will be a [product type - *From `q2`*], delivered as [specific format(s) and key technical parameters - *E.g., 'an HTML5 web application for desktop browsers,' 'an MP4 video file (about X minutes, 1920x1080 resolution),' 'a standalone program for Windows.' Adapt language.*].",
        "\nThe game will have [3-5 key components/features defining boundaries - *List concrete features that will be included, e.g., 'three distinct game levels,' 'an interactive quiz part,' 'custom character models and animations for the main characters.' Adapt language.*]. To make sure I can finish the project on time, I won't be adding things like [briefly mention 1-2 explicitly excluded items to manage scope, e.g., 'multiplayer functionality,' 'a lot of spoken dialogue,' 'player accounts'] to the final game.",
        "\nHere are the main limitations and challenges I expect to face while making this:",
        "-   **Time:** The biggest challenge is the time I have for the HSC course, which is about forty-two weeks. This means I really need to manage my time strictly and stick to the detailed plan I've set up. (This is static; student doesn't need to input for it).",
        "-   **Skills & Knowledge:** To do this well, I need to get good at [1-2 specific advanced skills needed - *Use `q19`, `q20`. E.g., 'advanced Python coding for game logic,' 'tricky 3D modelling work in Blender'*]. I'll learn these skills from [mention specific learning methods, e.g., 'online tutorials (like Udemy, Skillshare),' 'advice from people in the industry,' 'a lot of practice making smaller test projects'. Adapt language.*].",
        "-   **Resources & Equipment:** I need access to certain software (`{json.dumps(student_responses.get('q4', ''))}` if available, otherwise specify. E.g., `Adobe Creative Suite`, `Unity`, `Blender`) and hardware ([e.g., 'a good computer for making art,' 'a drawing tablet']). I'll have to carefully handle things like [mention specific resource constraints from `q21`, `q22`, e.g., 'making the game run fast on the Raspberry Pi's limited power,' 'making sure all the game's art and sound look and feel consistent, even with limited time and software']. I'll manage this by testing and fixing bugs a lot. (Adapt language).",
        "-   **Technical Complexity:** Making tricky features, like [specific complex technical aspect from `q22` or inferred, e.g., 'getting dynamic collision detection to work for different shapes,' 'building a smart enemy AI system,' 'making cool real-time fire effects'], will be a big technical challenge. This means I need to plan really well, test things often, and fix bugs carefully. (Adapt language).",

        "\n## 1.6 Timeline and Milestones",
        "The deadline for my project is around Week 3, Term 3. But I've been told it's smart to finish by Week 2 to have enough time for trials. This gives me about forty-two weeks to do everything.",
        "\nHere's my plan for the project:",
        "-   **Term 4 (Weeks 1-10):** First up is research, getting my ideas together, and detailed planning. This includes studying the game industry, writing down my early designs, and setting up my tech. (Adapt language).",
        "-   **Summer Break:** I'll keep working on my skills and start building early versions of the game. I'll focus on getting better at coding, animation, and making the main game parts work. (Adapt language).",
        "-   **Term 1 (Weeks 1-10):** This is where most of the building happens. I'll put in the main features, connect my tech (like Flask with the front-end, and getting the server running), and set up the main game loops or content. (Adapt language).",
        "-   **Term 2 (Weeks 1-10):** I'll create and add all the art, sound, and animations. Then, I'll do lots of testing to make sure everything works and find any bugs. (Adapt language).",
        "-   **Term 3 (Weeks 1-2):** Final polish, more testing, and finishing up the project. This means getting everything ready for the final presentation, writing up all the detailed documentation for my folio, and a final quality check. (Adapt language).",

        "\n## 1.7 Expected Outcomes and Success Criteria",
        "I'll judge if '[Project Title - *From `q1`*]' is successful based on how well it meets my goals and how good the final game and my folio are. Here are my specific success checks:",
        f"1.  **Goals Met & Player Impact:** The game needs to clearly meet its main goals (from Section 1.4), especially in [reiterate key user outcome from objectives, e.g., 'getting players hooked on unique mechanics,' 'how well they understand game objectives']. I'll check this by [how it will be measured - *Use `q23`, `q24`. **Transform**: Focus on internal, academic validation methods like 'organised player feedback sessions,' 'watching how players interact with the game,' 'tracking how many levels they finish,' all written down in my folio.*]. (Adapt language).",
        f"2.  **Tech Quality & Looks/Sounds:** The finished game needs to show that I'm really good at [technical skills from `q27`, e.g., 'coding efficiently,' 'making smooth animations,' 'rendering graphics well'], and it should have a strong [aesthetic style from `q17`, e.g., 'nostalgic retro video arcade look'] and great sound. I'll prove this with [how it will be shown - e.g., 'test reports showing good performance and few bugs,' 'a clear plan in my folio for how the game looks and sounds consistently,' 'getting positive feedback from my teachers and classmates on the art and tech.']. (Adapt language).",
        f"3.  **Audience Fit & Improvement:** The game needs to be right for, easy to use for, and fun for its audience ([target audience from `q10`]). I'll keep checking and improving this by [how it will be assessed - *Use `q25`. **Transform**: Focus on 'getting feedback from players regularly,' 'advice from teachers and people in the game industry,' 'checking it against my detailed design plans in my folio,' so the game really connects with its players.*]. (Adapt language).",

        "\n## 1.8 Opportunities",
        "When '[Project Title - *From `q1`*]' is done, it'll be a really important part of my portfolio. It'll show off my advanced skills in [2-3 key skill areas demonstrated - *Use `q28` and other relevant skill mentions. E.g., 'making interactive games,' 'full-stack web development,' 'tricky 2D/3D animation,' 'making good user interfaces'*]. This big project will be super helpful for applying to college or jobs in [relevant industry/field - *Use `q8` and `q28`. E.g., 'digital media,' 'game development'*]. Plus, I'll get good at [valuable process learned - e.g., 'managing a big creative project from start to finish,' 'using feedback to make it better,' 'solving tough tech problems when things get stressful'], which will be really useful later on. (Adapt language)."
    ]

    return "\n".join(prompt_parts)

# --- Student Responses (This will be loaded from student_responses.json in your app) ---
# For local testing, we'll keep the problematic responses to show the enhancement effect.
def get_mock_student_responses():
    """Returns mock student responses, simulating input from student_responses.json."""
    return {
        "q1": "Monkey Magic Video Game",
        "q2": "Video Game",
        "q3": "There are not monkeys with magic video games available", # Poor input
        "q4": "Flask, HTML, CSS, jinja, javascript, hosted on a raspberry pi server with joystick controls and keypad controls",
        "q5": "Retro gaming, 2d and 3d graphics, vfx, animation and coding", # Mixed input
        "q6": "it's suitable for my target market of young adults and gen x people", # Poor input
        "q7": "animation, sound design, graphics, 2d and 3d animation, concept sketchets, coding",
        "q8": "animation, multimedia, vfx, game development",
        "q9": "They have money to spend, they like nostalgia and have more time than other age groups to explore deep multilevel game play", # Poor input
        "q10": "young adults and Gen X people", # Demographic
        "q11": "feel young and relevant, feel in touch with the youth, relive old memories of their youth", # Poor input
        "q12": "coolness factor, aura", # Unused in enhanced template
        "q13": "nostalgic, fun, nerdiness", # Unused in enhanced template
        "q14": "coding, vfx, animation, graphics", # Skill for Objective 3
        "q15": "minimum viable product (MVP), launch in steam platform, youtube views and trailer", # Poor input for Objective 1
        "q16": "steam platform, youtube, online, deployed in raspberry pi server", # Poor input for Objective 2
        "q17": "nostalgic, sound design, retro arcade vibes", # Success Criterion 1 raw
        "q18": "monetization", # Unused
        "q19": "learn coding, improve in2d and 3d animation", # Skills for Constraints
        "q20": "coding and animation", # Skill for Constraints (redundant)
        "q21": "raspberry pi server", # Resource for Constraints
        "q22": "sound design and animation", # Challenge for Constraints
        "q23": "launch in steam platform, many youtube views and reviews and comments", # External validation (for Success Criterion 1)
        "q24": "steam reviews and youtube views and comments", # External validation (for Success Criterion 2)
        "q25": "i will get industry professionals to review and offer feedback", # External validation (for Success Criterion 3)
        "q26": "nostalgic reto video arcade vibe", # Success Criterion (redundant with q17)
        "q27": "coding, animation, graphics, wit and humour", # Success Criterion (attributes)
        "q28": "multimedia, motion graphics, game development" # Opportunities
    }

if __name__ == "__main__":
    mock_responses = get_mock_student_responses()
    prompt = generate_prompt(mock_responses)
    print("Generated AI Prompt:")
    print("=" * 70)
    print(prompt)
    print("=" * 70)
    print("\nIMPORTANT: The AI will now take these instructions and the student's raw input, then generate a Band 6 Statement of Intent with the specified 'community college student' voice and Australian spelling.")