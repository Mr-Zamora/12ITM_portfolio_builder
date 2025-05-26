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
    
    # Import random for variety features
    import random

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
        "    *   **Individual Voice:** Create a UNIQUE voice for each student. Some students might use more slang or colloquialisms, others might be more formal. Some might use shorter sentences, others longer ones. Some might be more enthusiastic, others more matter-of-fact. Vary paragraph lengths and sentence structures significantly between different statements.",
        "    *   **Authentic Variations:** Include occasional 'authentic' elements like a personal anecdote, a specific example from the student's experience, or a unique perspective on their project. Make each statement feel genuinely individual.",
        "    *   **Structural Diversity:** Don't always follow the exact same pattern in each section. Sometimes lead with examples, other times with principles. Sometimes use lists, other times use paragraphs. Vary how information is presented.",
        "    *   **Project-Specific Language:** Adapt vocabulary and phrasing to match the type of project. Game projects might use more action-oriented language, educational projects more supportive language, technical projects more precise language.",
        "    *   **Confidence Variation:** Some students should sound very confident about their skills and project, others slightly more tentative or reflective. This creates authentic diversity in voice.",
        "    *   **Section Organization:** Don't always present information in the same order within sections. Sometimes start with the 'what', other times with the 'why'. Create natural variation in how ideas flow.",
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
        "/* RANDOMLY SELECT ONE OF THESE OPENING STYLES FOR THE FIRST PARAGRAPH */",
        "STYLE 1: For my Industrial Technology Multimedia Major Project, I'm going to design, build, and make [specific multimedia product type - *Use `q2`. Elevate if generic, e.g., 'a highly interactive web-based simulation' instead of just 'website'. Adapt language.*] titled '[Project Title - *From `q1`*]'.",
        "STYLE 2: My name is [student name - make up a realistic name], and I'm creating [specific multimedia product type - *Use `q2`. Elevate if generic*] called '[Project Title - *From `q1`*]' for my Industrial Technology Multimedia Major Project. This is something I'm really excited about.",
        "STYLE 3: '[Project Title - *From `q1`*]' is a [specific multimedia product type - *Use `q2`. Elevate if generic*] that I'm developing as my Industrial Technology Multimedia Major Project. It represents my passion for [relevant field from `q4` or `q5`].",
        "STYLE 4: Have you ever wondered [question related to the problem/opportunity in `q3`]? That's exactly what my Industrial Technology Multimedia Major Project '[Project Title - *From `q1`*]' aims to address through [specific multimedia product type - *Use `q2`. Elevate if generic*].",
        
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE PROBLEM/OPPORTUNITY PARAGRAPH */",
        "STYLE 1: This project is mostly happening because I've noticed [specific problem/opportunity - *Use `q3`. **CRITICAL**: Rephrase student input to reflect a genuine user need, a gap in knowledge/resources, or a significant societal/creative opportunity, not a niche preference or personal whim. Adapt language to be more direct and less academic.*].",
        "STYLE 2: What really pushed me to create this was [specific problem/opportunity - *Use `q3`*]. I kept seeing this issue come up, and I thought, 'Someone should really do something about this.' So I decided that someone would be me.",
        "STYLE 3: The main reason behind this project is simple: [specific problem/opportunity - *Use `q3`*]. It's something I've experienced personally, and I know many others have too.",
        "STYLE 4: I started working on this after realizing [specific problem/opportunity - *Use `q3`*]. It's a problem that doesn't get enough attention, but it affects [relevant group] in significant ways.",
        
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE FOCUS/TECHNOLOGIES PARAGRAPH */",
        "STYLE 1: My project will specifically focus on [core content/subject matter - *Use `q5`. Elaborate on the core theme, narrative, or gameplay focus beyond just listing techniques. E.g., 'the exploration of non-Euclidean geometry through interactive puzzle design'. Adapt language.*] by primarily using [main multimedia forms/technologies - *Use `q4`. List specific software/languages and justify their relevance to the project's aims. Keep technical terms precise but adapt surrounding language.*].",
        "STYLE 2: To bring this vision to life, I'll be diving deep into [core content/subject matter - *Use `q5`*]. The technical side will involve [main multimedia forms/technologies - *Use `q4`*], which I've chosen because [brief justification related to project goals].",
        "STYLE 3: At its heart, this project explores [core content/subject matter - *Use `q5`*]. I'll be using [main multimedia forms/technologies - *Use `q4`*] to create something that's both technically impressive and meaningful to users.",
        "STYLE 4: The core of '[Project Title - *From `q1`*]' is all about [core content/subject matter - *Use `q5`*]. For the technical implementation, I've selected [main multimedia forms/technologies - *Use `q4`*] because these tools give me the flexibility and power I need for what I'm trying to achieve.",

        "\n## 1.2 Rationale: Why This Project? Why This Approach?",
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE PERSONAL CONNECTION PARAGRAPH */",
        "STYLE 1: I decided to make this project because I'm really into [personal interest/connection - *Use `q5` and any other relevant student input. Connect personal passion to the project's academic or industry relevance. Adapt language.*]. This project fits right in with what I want to do in the [industry sector - *Use `q8`. Be specific, e.g., 'digital game development,' 'interactive educational media'. Adapt language.*] industry.",
        "STYLE 2: This project is personal for me. [Brief personal anecdote related to `q5` - create a short, authentic-sounding story]. That experience showed me how important this kind of work is, and it's pushed me toward the [industry sector - *Use `q8`*] field.",
        "STYLE 3: My passion for [personal interest/connection - *Use `q5`*] is what drives this project. I've always been fascinated by [aspect of the project], and I see this as my first real step toward a career in [industry sector - *Use `q8`*].",
        "STYLE 4: When I think about why I'm doing this project, it comes down to two things: my interest in [personal interest/connection - *Use `q5`*] and my goal to work in [industry sector - *Use `q8`*] after I finish school.",
        
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE MEDIUM JUSTIFICATION PARAGRAPH */",
        "STYLE 1: I also really believe that [product type - *From `q2`*] is the best way to do this project because [justification - *Use `q6`. **Elevate**: Explain *why* this specific medium (e.g., a game, a website, an animation) uniquely addresses the identified problem/opportunity and engages the target audience, leveraging its specific characteristics (e.g., interactivity, immersion, visual storytelling, accessibility). Avoid vague statements like 'it's suitable'. Adapt language to be more direct.*].",
        "STYLE 2: Why [product type - *From `q2`*] and not something else? Simply put, [justification - *Use `q6`*]. No other format would allow the same level of [key benefit, e.g., 'engagement', 'clarity', 'emotional impact'].",
        "STYLE 3: The decision to create a [product type - *From `q2`*] wasn't random. I chose this format specifically because [justification - *Use `q6`*]. This approach lets me [key benefit] in a way that [alternative approach] simply couldn't.",
        "STYLE 4: A [product type - *From `q2`*] is perfect for what I'm trying to achieve. Here's why: [justification - *Use `q6`*]. This format gives me the tools to [key benefit] while still keeping the project manageable within my timeframe and resources.",
        
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE SKILLS PARAGRAPH */",
        "STYLE 1: This project is a huge chance for me to learn and get really good at [2-3 specific techniques/processes - *Use `q7`. Be specific and demonstrate ambition, e.g., 'advanced character rigging and inverse kinematics,' 'real-time shader development,' 'complex database integration for dynamic content delivery'. Adapt language.*], which are all skills used a lot in today's [industry sector - *From `q8`*] industry.",
        "STYLE 2: On the technical side, I'm looking forward to developing my skills in [2-3 specific techniques/processes - *Use `q7`*]. These aren't just random techniques – they're highly valued in the [industry sector - *From `q8`*] industry, which is where I hope to work someday.",
        "STYLE 3: I'll be pushing myself to master [2-3 specific techniques/processes - *Use `q7`*] throughout this project. I've done some basic work with these before, but this is my chance to really level up and create something that shows what I can do. These skills are exactly what employers in [industry sector - *From `q8`*] are looking for.",
        "STYLE 4: The technical challenges of this project will help me grow in some important areas: [2-3 specific techniques/processes - *Use `q7`*]. I've researched what skills are most valuable in the [industry sector - *From `q8`*] industry, and these are definitely at the top of the list.",

        "\n## 1.3 Target Audience: Who is this Project For, and Why?",
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE AUDIENCE IDENTIFICATION PARAGRAPH */",
        "STYLE 1: The main people I'm making '[Project Title - *From `q1`*]' for are [specific demographic - *Use `q10`. Be precise, e.g., 'Year 9-10 Science students studying ecosystems,' 'Independent game enthusiasts aged 25-45 who appreciate narrative-driven puzzle games'. Adapt language.*].",
        "STYLE 2: I've designed '[Project Title - *From `q1`*]' specifically with [specific demographic - *Use `q10`*] in mind. They're my primary audience, though others might find it useful too.",
        "STYLE 3: When I think about who will use '[Project Title - *From `q1`*]', I'm mainly focusing on [specific demographic - *Use `q10`*]. This is a group I understand well and feel I can create something valuable for.",
        "STYLE 4: '[Project Title - *From `q1`*]' targets [specific demographic - *Use `q10`*]. I chose this audience carefully after considering who would benefit most from what I'm creating.",
        
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE AUDIENCE JUSTIFICATION PARAGRAPH */",
        "STYLE 1: I picked this group because [justification with reference to research/insights - *Use `q9`. **Elevate**: Avoid stereotypes or generalisations. Base justification on identified needs, learning gaps, market analysis, or specific psychological insights relevant to their engagement with multimedia. Adapt language to be more direct.*].",
        "STYLE 2: There are several reasons why I'm focusing on this particular audience. Most importantly, [justification - *Use `q9`*]. I've observed this firsthand and believe my project can make a real difference here.",
        "STYLE 3: My research into this audience revealed that [justification - *Use `q9`*]. This insight was eye-opening and helped me shape the entire direction of my project.",
        "STYLE 4: Why this specific audience? Because [justification - *Use `q9`*]. Understanding their unique needs has been crucial in developing something that will genuinely resonate with them.",
        
        "/* RANDOMLY SELECT ONE OF THESE STYLES FOR THE AUDIENCE CHARACTERISTICS PARAGRAPH */",
        "STYLE 1: I expect this audience to [relevant characteristics - *Use `q10`, `q11`. **Transform**: Convert subjective desires into actionable user characteristics influencing design (e.g., 'a high level of digital literacy and access to mobile devices,' 'a preference for immersive narratives over competitive gameplay,' 'a desire for challenging mental stimulation'). Adapt language.*], which will directly change how I design the game, how it feels to play, and what it does, so it works well for them.",
        "STYLE 2: Understanding my audience's characteristics is crucial. They tend to [relevant characteristics - *Use `q10`, `q11`*], and I've designed every aspect of my project with these traits in mind.",
        "STYLE 3: The specific needs and preferences of my audience include [relevant characteristics - *Use `q10`, `q11`*]. These insights aren't just interesting – they're guiding my design decisions at every step.",
        "STYLE 4: What makes this audience unique? For one thing, they [relevant characteristics - *Use `q10`, `q11`*]. I'm constantly referring back to these characteristics as I develop my project to ensure it meets their specific needs.",

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
        f"-   **Resources & Equipment:** I need access to certain software (`{student_responses.get('q4', '')}` if available, otherwise specify. E.g., `Adobe Creative Suite`, `Unity`, `Blender`) and hardware ([e.g., 'a good computer for making art,' 'a drawing tablet']). I'll have to carefully handle things like [mention specific resource constraints from `q21`, `q22`, e.g., 'making the game run fast on the Raspberry Pi's limited power,' 'making sure all the game's art and sound look and feel consistent, even with limited time and software']. I'll manage this by testing and fixing bugs a lot. (Adapt language).",
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
        "1.  **Goals Met & Player Impact:** The game needs to clearly meet its main goals (from Section 1.4), especially in [reiterate key user outcome from objectives, e.g., 'getting players hooked on unique mechanics,' 'how well they understand game objectives']. I'll check this by [how it will be measured - *Use `q23`, `q24`. **Transform**: Focus on internal, academic validation methods like 'organised player feedback sessions,' 'watching how players interact with the game,' 'tracking how many levels they finish,' all written down in my folio.*]. (Adapt language).",
        "2.  **Tech Quality & Looks/Sounds:** The finished game needs to show that I'm really good at [technical skills from `q27`, e.g., 'coding efficiently,' 'making smooth animations,' 'rendering graphics well'], and it should have a strong [aesthetic style from `q17`, e.g., 'nostalgic retro video arcade look'] and great sound. I'll prove this with [how it will be shown - e.g., 'test reports showing good performance and few bugs,' 'a clear plan in my folio for how the game looks and sounds consistently,' 'getting positive feedback from my teachers and classmates on the art and tech.']. (Adapt language).",
        "3.  **Audience Fit & Improvement:** The game needs to be right for, easy to use for, and fun for its audience ([target audience from `q10`]). I'll keep checking and improving this by [how it will be assessed - *Use `q25`. **Transform**: Focus on 'getting feedback from players regularly,' 'advice from teachers and people in the game industry,' 'checking it against my detailed design plans in my folio,' so the game really connects with its players.*]. (Adapt language).",

        "\n## 1.8 Opportunities",
        "When '[Project Title - *From `q1`*]' is done, it'll be a really important part of my portfolio. It'll show off my advanced skills in [2-3 key skill areas demonstrated - *Use `q28` and other relevant skill mentions. E.g., 'making interactive games,' 'full-stack web development,' 'tricky 2D/3D animation,' 'making good user interfaces'*]. This big project will be super helpful for applying to college or jobs in [relevant industry/field - *Use `q8` and `q28`. E.g., 'digital media,' 'game development'*]. Plus, I'll get good at [valuable process learned - e.g., 'managing a big creative project from start to finish,' 'using feedback to make it better,' 'solving tough tech problems when things get stressful'], which will be really useful later on. (Adapt language)."
    ]

    # Add variety instructions at the end
    variety_instructions = [
        "\n## CRITICAL VARIETY INSTRUCTIONS",
        "To ensure each Statement of Intent feels like original student work:",
        "1. **REQUIRED: For each section, RANDOMLY SELECT ONE of the provided style options (STYLE 1, STYLE 2, etc.).** Do not use the same style for all sections. Mix them up to create a unique document.",
        "2. **REQUIRED: Create a unique student persona** for each statement. Give them distinctive traits like:",
        "   - A specific confidence level (very confident, somewhat tentative, balanced)",
        "   - A distinctive writing style (more technical, more emotional, more analytical)",
        "   - Unique speech patterns (short sentences, complex sentences, use of questions, use of examples)",
        "   - Different vocabulary preferences (simple, advanced, field-specific)",
        "3. **REQUIRED: Vary paragraph structures** - Some students use topic sentences followed by details, others build to their main point, others use compare/contrast structures.",
        "4. **REQUIRED: Include at least one authentic personal element** - a brief anecdote, a specific example from their experience, or a unique perspective.",
        "5. **REQUIRED: Adjust language based on project type** - use different vocabulary and tone for games vs. educational tools vs. websites.",
        "6. **REQUIRED: Include occasional 'authentic variations'** - some minor repetition of key points, varying levels of formality between sections, or natural transitions.",
        "7. **REQUIRED: Vary formatting approaches** - some students might use more bullet points, others more paragraphs, some more headings.",
        "8. **REQUIRED: Use different evidence types** - some students might cite statistics, others personal observations, others industry trends.",
        "9. **REQUIRED: Create different emotional tones** - some students more enthusiastic, others more analytical, others more reflective.",
        "10. **CRITICAL: REMOVE ALL STYLE MARKERS like 'STYLE 1:', 'STYLE 2:' etc. from your final output. These are just selection guides for you.**",
        "11. **CRITICAL: DO NOT use phrases like 'This project is mostly happening because...' or any other template phrases verbatim. Rewrite them in your own unique style.**"
    ]
    
    # Add randomization instructions
    randomization_instructions = [
        "\n## RANDOMIZATION REQUIREMENTS",
        "To create truly unique statements, you MUST use randomization in your approach:",
        "1. For EACH SECTION, randomly select ONE of the provided style options (STYLE 1, STYLE 2, etc.).",
        "2. Randomly determine the student's overall voice characteristics (confidence level, formality, sentence structure preferences).",
        "3. Randomly decide whether to include more personal anecdotes or more objective analysis.",
        "4. Randomly vary paragraph lengths throughout the document - mix very short (1-2 sentences) with medium and longer paragraphs.",
        "5. Randomly select different transition phrases between sections and ideas - never use the same transitions in different statements.",
        "6. IMPORTANT: Create a completely different 'feel' for each statement - if one is enthusiastic and personal, make another more measured and analytical."
    ]
    
    # Add the variety and randomization instructions to the prompt
    prompt_parts.extend(variety_instructions)
    prompt_parts.extend(randomization_instructions)
    
    # Add final reminder to avoid template language
    prompt_parts.append("\n## FINAL CRITICAL REMINDER")
    prompt_parts.append("NEVER use the exact same phrases, sentence structures, or paragraph organization between different statements. Each statement must feel like it was written by a completely different student with their own unique voice, style, and approach.")
    prompt_parts.append("REMEMBER: Markers will immediately recognize template language. Your goal is to make each statement feel genuinely original while maintaining Band 6 quality.")
    
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