import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Import necessary libraries
from streamlit_lottie import st_lottie  
import json
import os

# Set page configuration
st.set_page_config(page_title="Personality Tests", layout="wide")

# Main title
st.title('Personality Tests 🧠')

# Ensure user is logged in
if 'user_email' not in st.session_state:
    st.warning('Please log in first')
    st.stop()
else:
    user_email = st.session_state['user_email']

# File path to Lottie animation
lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/personality.json"
# Function to load Lottie animation
def load_lottiefile(filepath: str):
    """Loads a Lottie animation from a JSON file."""
    if not os.path.exists(filepath):
        st.error(f"Error: File not found - {filepath}")
        return None
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile(lottie_path)

# Layout: Chat on the left, Animation on the right
col1, col2 = st.columns([2, 1])  # Adjust ratio for better alignment

with col1:
     # Initialize session state variables if they don't exist
 if 'current_test' not in st.session_state:
    st.session_state['current_test'] = None
 if 'test_results' not in st.session_state:
    st.session_state['test_results'] = {}
 if 'questions_answered' not in st.session_state:
    st.session_state['questions_answered'] = 0
 if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

# Test definitions
def mbti_test():
    questions = [
        {"question": "At a party, you:", 
         "options": ["Interact with many, including strangers", "Interact with a few people you know"]},
        {"question": "You tend to be more:", 
         "options": ["Realistic than speculative", "Speculative than realistic"]},
        {"question": "Which is worse:", 
         "options": ["Having your head in the clouds", "Being in a rut"]},
        {"question": "You are more impressed by:", 
         "options": ["Principles", "Emotions"]},
        {"question": "You are more drawn toward the:", 
         "options": ["Convincing", "Touching"]},
        {"question": "You prefer to work:", 
         "options": ["To deadlines", "Just whenever"]},
        {"question": "You tend to choose:", 
         "options": ["Rather carefully", "Somewhat impulsively"]},
        {"question": "At parties do you:", 
         "options": ["Stay late, with increasing energy", "Leave early with decreased energy"]},
        {"question": "You are more attracted to:", 
         "options": ["Sensible people", "Imaginative people"]},
        {"question": "You are more interested in:", 
         "options": ["What is actual", "What is possible"]},
        {"question": "In judging others, you are more swayed by:", 
         "options": ["Laws than circumstances", "Circumstances than laws"]},
        {"question": "In approaching others, is your inclination to be somewhat:", 
         "options": ["Objective", "Personal"]},
        {"question": "You are more:", 
         "options": ["Punctual", "Leisurely"]},
        {"question": "It bothers you more having things:", 
         "options": ["Incomplete", "Completed"]},
        {"question": "In your social groups, you generally:", 
         "options": ["Keep up-to-date on others' happenings", "Get behind on the news"]},
        {"question": "When solving a problem, you would rather:", 
         "options": ["Apply a standard solution", "Look for a new solution"]},
        {"question": "You prefer writers who:", 
         "options": ["Say what they mean", "Use metaphors and symbolism"]},
        {"question": "You more often prefer:", 
         "options": ["The final and unalterable statement", "The tentative and preliminary statement"]},
        {"question": "You find it easier to:", 
         "options": ["Put others to good use", "Identify with others"]},
        {"question": "You would rather be considered:", 
         "options": ["A practical person", "An ingenious person"]}
    ]
    
    dimensions = [
        {"name": "Extraversion (E) vs. Introversion (I)", "questions": [0, 7, 14], "options": [0, 1]},
        {"name": "Sensing (S) vs. Intuition (N)", "questions": [1, 8, 9, 15, 16, 19], "options": [0, 1]},
        {"name": "Thinking (T) vs. Feeling (F)", "questions": [3, 4, 10, 11, 18], "options": [0, 1]},
        {"name": "Judging (J) vs. Perceiving (P)", "questions": [5, 6, 12, 13, 17], "options": [0, 1]}
    ]
    
    return questions, dimensions

def ocean_test():
    questions = [
        {"question": "I am someone who is always full of new ideas.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I am quick to understand new things.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I have high appreciation for art, culture and literature.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I have interest in abstract ideas.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I have good organizing and planning skills.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I easily get started on tasks and follow a schedule.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I pay attention to details.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I complete tasks thoroughly.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I enjoy being the center of attention.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I start conversations with new people easily.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I talk to many different people at parties.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I feel comfortable around people.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I sympathize with others' feelings.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I take time out for others.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I feel others' emotions.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I make people feel at ease.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I get stressed out easily.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I worry about things.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I am easily disturbed.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]},
        {"question": "I change my mood a lot.", 
         "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]}
    ]
    
    dimensions = [
        {"name": "Openness", "questions": [0, 1, 2, 3], "scoring": "direct"},
        {"name": "Conscientiousness", "questions": [4, 5, 6, 7], "scoring": "direct"},
        {"name": "Extraversion", "questions": [8, 9, 10, 11], "scoring": "direct"},
        {"name": "Agreeableness", "questions": [12, 13, 14, 15], "scoring": "direct"},
        {"name": "Neuroticism", "questions": [16, 17, 18, 19], "scoring": "direct"}
    ]
    
    return questions, dimensions

def disc_test():
    questions = [
        {"question": "Which of the following best describes your approach to work?", 
         "options": ["Taking charge and aiming for quick results", 
                    "Motivating others and maintaining a positive atmosphere", 
                    "Focusing on teamwork and supporting others", 
                    "Ensuring accuracy and following processes"]},
        {"question": "How do you handle deadlines?", 
         "options": ["I push to meet them ahead of time", 
                    "I use them as motivation to keep energy high", 
                    "I plan carefully to meet them without stress", 
                    "I double-check details to ensure everything is correct"]},
        {"question": "What is your leadership style?", 
         "options": ["Direct and results-focused", 
                    "Inspiring and enthusiastic", 
                    "Supportive and team-oriented", 
                    "Analytical and systematic"]},
        {"question": "How do you communicate ideas?", 
         "options": ["Directly and to the point", 
                    "Enthusiastically with stories and examples", 
                    "Diplomatically with consideration for others", 
                    "Precisely with accurate details"]},
        {"question": "When working on a project, what's most important to you?", 
         "options": ["Getting results quickly", 
                    "Making the process enjoyable", 
                    "Ensuring everyone works well together", 
                    "Following the correct procedures"]},
        {"question": "How do you make decisions?", 
         "options": ["Quickly, based on what will get results", 
                    "Based on what will be most popular", 
                    "Carefully, considering how it affects others", 
                    "Methodically, analyzing all the facts"]},
        {"question": "What motivates you at work?", 
         "options": ["Challenges and achievements", 
                    "Recognition and social interaction", 
                    "Stability and helping others", 
                    "Quality and accuracy"]},
        {"question": "How do you respond to change?", 
         "options": ["I embrace it as an opportunity", 
                    "I get excited about new possibilities", 
                    "I prefer gradual, well-explained changes", 
                    "I want to understand the reasons and details"]},
        {"question": "What's your preferred work environment?", 
         "options": ["Fast-paced with autonomy", 
                    "Social and collaborative", 
                    "Harmonious and supportive", 
                    "Structured and organized"]},
        {"question": "How do you handle conflict?", 
         "options": ["I address it directly and move on", 
                    "I try to keep things positive and smooth it over", 
                    "I seek compromise and harmony", 
                    "I analyze the situation logically"]},
        {"question": "What's your biggest strength?", 
         "options": ["Getting results", 
                    "Inspiring others", 
                    "Being reliable", 
                    "Ensuring accuracy"]},
        {"question": "What do others notice about you first?", 
         "options": ["My confidence and directness", 
                    "My enthusiasm and friendliness", 
                    "My patience and supportiveness", 
                    "My attention to detail"]},
        {"question": "How do you prefer to receive feedback?", 
         "options": ["Direct and to the point", 
                    "Positive and encouraging", 
                    "Gentle and constructive", 
                    "Detailed and specific"]},
        {"question": "What's your approach to problem-solving?", 
         "options": ["Find the quickest, most effective solution", 
                    "Brainstorm creative ideas with others", 
                    "Consider how solutions affect everyone involved", 
                    "Analyze the problem methodically"]},
        {"question": "How do you respond to stress?", 
         "options": ["Become more controlling and decisive", 
                    "Talk it out and seek social support", 
                    "Withdraw to process and maintain calm", 
                    "Focus on details and analysis"]},
        {"question": "What's your biggest fear at work?", 
         "options": ["Losing control or being taken advantage of", 
                    "Being rejected or ignored", 
                    "Sudden changes or conflict", 
                    "Being wrong or criticized"]},
        {"question": "How do you view rules?", 
         "options": ["Guidelines that can be bent to get results", 
                    "Helpful but flexibility is important", 
                    "Important for maintaining harmony", 
                    "Essential and should be followed"]},
        {"question": "What's your ideal role in a team?", 
         "options": ["Leader who drives action", 
                    "Motivator who generates enthusiasm", 
                    "Mediator who ensures cooperation", 
                    "Analyst who ensures quality"]},
        {"question": "How do you approach new projects?", 
         "options": ["Jump in and figure it out as I go", 
                    "Get others excited and involved", 
                    "Establish a steady, collaborative approach", 
                    "Create a detailed plan before starting"]},
        {"question": "What energizes you?", 
         "options": ["Challenges and competition", 
                    "Social activities and recognition", 
                    "Stable relationships and helping others", 
                    "Solving complex problems"]}
    ]
    
    dimensions = [
        {"name": "Dominance (D)", "questions": range(20), "options": [0]},
        {"name": "Influence (I)", "questions": range(20), "options": [1]},
        {"name": "Steadiness (S)", "questions": range(20), "options": [2]},
        {"name": "Conscientiousness (C)", "questions": range(20), "options": [3]}
    ]
    
    return questions, dimensions

# Function to calculate MBTI results
def calculate_mbti_results(answers, dimensions):
    results = {}
    for dim in dimensions:
        score_a = 0
        score_b = 0
        for q_idx in dim["questions"]:
            if q_idx in answers:
                if answers[q_idx] == dim["options"][0]:
                    score_a += 1
                elif answers[q_idx] == dim["options"][1]:
                    score_b += 1
        
        # Determine which side of the dimension is stronger
        if score_a > score_b:
            if dim["name"] == "Extraversion (E) vs. Introversion (I)":
                results["E/I"] = "E"
            elif dim["name"] == "Sensing (S) vs. Intuition (N)":
                results["S/N"] = "S"
            elif dim["name"] == "Thinking (T) vs. Feeling (F)":
                results["T/F"] = "T"
            elif dim["name"] == "Judging (J) vs. Perceiving (P)":
                results["J/P"] = "J"
        else:
            if dim["name"] == "Extraversion (E) vs. Introversion (I)":
                results["E/I"] = "I"
            elif dim["name"] == "Sensing (S) vs. Intuition (N)":
                results["S/N"] = "N"
            elif dim["name"] == "Thinking (T) vs. Feeling (F)":
                results["T/F"] = "F"
            elif dim["name"] == "Judging (J) vs. Perceiving (P)":
                results["J/P"] = "P"
    
    personality_type = results["E/I"] + results["S/N"] + results["T/F"] + results["J/P"]
    return personality_type

# Function to calculate OCEAN results
def calculate_ocean_results(answers):
    dimension_scores = {
        "Openness": 0,
        "Conscientiousness": 0,
        "Extraversion": 0,
        "Agreeableness": 0,
        "Neuroticism": 0
    }
    
    # Map numeric indices directly to scores (0=Strongly Disagree, 4=Strongly Agree)
    # So the values are 1, 2, 3, 4, 5 respectively
    numeric_values = [1, 2, 3, 4, 5]
    
    # Calculate scores for each dimension
    for i in range(4):
        if i in answers:
            dimension_scores["Openness"] += numeric_values[answers[i]]
    
    for i in range(4, 8):
        if i in answers:
            dimension_scores["Conscientiousness"] += numeric_values[answers[i]]
    
    for i in range(8, 12):
        if i in answers:
            dimension_scores["Extraversion"] += numeric_values[answers[i]]
    
    for i in range(12, 16):
        if i in answers:
            dimension_scores["Agreeableness"] += numeric_values[answers[i]]
    
    for i in range(16, 20):
        if i in answers:
            dimension_scores["Neuroticism"] += numeric_values[answers[i]]
    
    # Convert raw scores to percentages
    max_score_per_dimension = 20  # 4 questions × 5 points max
    for dim in dimension_scores:
        dimension_scores[dim] = (dimension_scores[dim] / max_score_per_dimension) * 100
    
    return dimension_scores



  

# Function to calculate DISC results
def calculate_disc_results(answers):
    disc_scores = {
        "Dominance (D)": 0,
        "Influence (I)": 0,
        "Steadiness (S)": 0,
        "Conscientiousness (C)": 0
    }
    
    for q_idx, answer in answers.items():
        if answer == 0:
            disc_scores["Dominance (D)"] += 1
        elif answer == 1:
            disc_scores["Influence (I)"] += 1
        elif answer == 2:
            disc_scores["Steadiness (S)"] += 1
        elif answer == 3:
            disc_scores["Conscientiousness (C)"] += 1
    
    # Convert to percentages
    total = sum(disc_scores.values())
    if total > 0:
        for key in disc_scores:
            disc_scores[key] = (disc_scores[key] / total) * 100
    
    return disc_scores

# Function to display personality descriptions
def get_mbti_description(personality_type):
    descriptions = {
        "ISTJ": "The Inspector - Practical, fact-minded, reliable, and responsible. You value traditions and loyalty, and are organized and methodical in your approach to life.",
        "ISFJ": "The Protector - Quiet, friendly, and conscientious. You're committed to meeting obligations and putting others' needs before your own.",
        "INFJ": "The Counselor - Idealistic, principled, and sensitive. You seek meaning and connection in ideas, relationships, and material possessions.",
        "INTJ": "The Mastermind - Independent, analytical, and determined. You have high standards and a natural desire to develop innovative solutions to problems.",
        "ISTP": "The Craftsman - Tolerant, flexible, and observant. You're interested in how and why things work and excel at hands-on problem-solving.",
        "ISFP": "The Composer - Quiet, friendly, and sensitive. You enjoy the present moment and what's going on around you, and value personal freedom.",
        "INFP": "The Healer - Idealistic, loyal, and curious. You seek authenticity and want to help others fulfill their potential.",
        "INTP": "The Architect - Logical, original, and creative thinker. You seek to develop logical explanations for everything that interests you.",
        "ESTP": "The Dynamo - Energetic, action-oriented, and pragmatic. You focus on immediate results and bring a practical approach to situations.",
        "ESFP": "The Performer - Outgoing, friendly, and spontaneous. You enjoy working with others and bringing energy to social situations.",
        "ENFP": "The Champion - Enthusiastic, creative, and sociable. You see life as full of possibilities and can connect seemingly unrelated ideas.",
        "ENTP": "The Visionary - Quick, ingenious, and outspoken. You enjoy intellectual challenges and see connections between disparate ideas.",
        "ESTJ": "The Supervisor - Practical, realistic, and decisive. You value tradition, security, and clear hierarchies.",
        "ESFJ": "The Provider - Warm-hearted, conscientious, and cooperative. You value harmony and work to establish it in your environment.",
        "ENFJ": "The Teacher - Warm, empathetic, and responsible. You're attuned to others' needs and help others fulfill their potential.",
        "ENTJ": "The Commander - Frank, decisive, and strategic planner. You see inefficiency and have a drive to organize people and processes."
    }
    
    if personality_type in descriptions:
        return descriptions[personality_type]
    else:
        return "Invalid personality type"

def get_ocean_description(scores):
    descriptions = {}
    
    # Openness descriptions
    if scores["Openness"] >= 75:
        descriptions["Openness"] = "You are extremely open to new experiences. You have a vivid imagination, appreciate art and beauty, and are willing to try new things. You tend to be intellectually curious and often think about abstract concepts."
    elif scores["Openness"] >= 50:
        descriptions["Openness"] = "You are moderately open to new experiences. You balance practical thinking with appreciation for creative ideas and are somewhat willing to explore new concepts."
    else:
        descriptions["Openness"] = "You prefer familiarity and tradition over novelty. You tend to be practical, conventional, and focused on concrete rather than abstract thinking."
    
    # Conscientiousness descriptions
    if scores["Conscientiousness"] >= 75:
        descriptions["Conscientiousness"] = "You are highly conscientious. You're organized, reliable, and methodical. You plan ahead, work diligently toward goals, and pay close attention to details."
    elif scores["Conscientiousness"] >= 50:
        descriptions["Conscientiousness"] = "You are moderately conscientious. You balance organization with flexibility and generally follow through on commitments while allowing some room for spontaneity."
    else:
        descriptions["Conscientiousness"] = "You tend to be more flexible and spontaneous rather than organized. You may prefer to improvise rather than make detailed plans and might occasionally procrastinate."
    
    # Extraversion descriptions
    if scores["Extraversion"] >= 75:
        descriptions["Extraversion"] = "You are highly extraverted. You're outgoing, energetic, and draw energy from social interactions. You enjoy being the center of attention and meeting new people."
    elif scores["Extraversion"] >= 50:
        descriptions["Extraversion"] = "You are moderately extraverted. You enjoy social situations but also value your alone time. You can be outgoing when needed but don't always seek the spotlight."
    else:
        descriptions["Extraversion"] = "You tend toward introversion. You prefer deeper one-on-one connections over large social gatherings and need time alone to recharge your energy."
    
    # Agreeableness descriptions
    if scores["Agreeableness"] >= 75:
        descriptions["Agreeableness"] = "You are highly agreeable. You're compassionate, cooperative, and prioritize getting along with others. You tend to trust people and avoid conflict."
    elif scores["Agreeableness"] >= 50:
        descriptions["Agreeableness"] = "You are moderately agreeable. You generally care about others' feelings but can stand your ground when necessary. You balance cooperation with healthy skepticism."
    else:
        descriptions["Agreeableness"] = "You tend to be more straightforward and challenging in your interactions. You may prioritize truth over tact and are willing to engage in conflict when necessary."
    
    # Neuroticism descriptions
    if scores["Neuroticism"] >= 75:
        descriptions["Neuroticism"] = "You experience emotions intensely and may be more sensitive to stress. You tend to worry about things and may experience mood fluctuations more frequently."
    elif scores["Neuroticism"] >= 50:
        descriptions["Neuroticism"] = "You have a moderate emotional reactivity. You experience normal ups and downs but generally maintain emotional stability in most situations."
    else:
        descriptions["Neuroticism"] = "You are emotionally stable and resilient. You remain calm under pressure, rarely worry, and recover quickly from stressful events."
    
    return descriptions

def get_disc_description(scores):
    # Find primary and secondary styles
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_scores[0][0]
    secondary = sorted_scores[1][0]
    
    descriptions = {
        "Dominance (D)": "You are direct, decisive, and results-oriented. You focus on accomplishing goals, overcoming obstacles, and taking charge. You value competence and aren't afraid of challenges.",
        "Influence (I)": "You are enthusiastic, optimistic, and people-oriented. You enjoy social interactions, are persuasive, and motivate others. You value recognition and tend to be expressive.",
        "Steadiness (S)": "You are patient, supportive, and relationship-oriented. You prefer cooperation, stability, and helping others. You value loyalty and are a dependable team player.",
        "Conscientiousness (C)": "You are analytical, systematic, and quality-oriented. You focus on accuracy, maintaining standards, and logical analysis. You value expertise and careful planning."
    }
    
    combined_description = f"Your primary style is {primary}: {descriptions[primary]}\n\nYour secondary style is {secondary}: {descriptions[secondary]}\n\n"
    
    # Add combination insight
    if primary == "Dominance (D)" and secondary == "Influence (I)":
        combined_description += "With high D and I, you're a persuasive leader who inspires action. You're results-oriented but also care about bringing people along with your vision."
    elif primary == "Dominance (D)" and secondary == "Steadiness (S)":
        combined_description += "With high D and S, you're a determined yet patient leader. You push for results while maintaining stability and supporting your team."
    elif primary == "Dominance (D)" and secondary == "Conscientiousness (C)":
        combined_description += "With high D and C, you're a strategic achiever. You drive for results while ensuring quality and accuracy in all you do."
    elif primary == "Influence (I)" and secondary == "Dominance (D)":
        combined_description += "With high I and D, you're a charismatic motivator. You inspire others while maintaining focus on goals and results."
    elif primary == "Influence (I)" and secondary == "Steadiness (S)":
        combined_description += "With high I and S, you're a supportive encourager. You connect well with others and create harmonious, positive environments."
    elif primary == "Influence (I)" and secondary == "Conscientiousness (C)":
        combined_description += "With high I and C, you're a detailed communicator. You express ideas enthusiastically while maintaining accuracy and quality."
    elif primary == "Steadiness (S)" and secondary == "Dominance (D)":
        combined_description += "With high S and D, you're a determined supporter. You maintain stability while pursuing goals with quiet determination."
    elif primary == "Steadiness (S)" and secondary == "Influence (I)":
        combined_description += "With high S and I, you're a friendly collaborator. You build strong relationships and create positive team environments."
    elif primary == "Steadiness (S)" and secondary == "Conscientiousness (C)":
        combined_description += "With high S and C, you're a reliable analyst. You provide consistent support while ensuring accuracy and quality in your work."
    elif primary == "Conscientiousness (C)" and secondary == "Dominance (D)":
        combined_description += "With high C and D, you're a critical thinker. You analyze situations thoroughly and take decisive action based on your findings."
    elif primary == "Conscientiousness (C)" and secondary == "Influence (I)":
        combined_description += "With high C and I, you're a precise communicator. You share detailed information in an engaging way."
    elif primary == "Conscientiousness (C)" and secondary == "Steadiness (S)":
        combined_description += "With high C and S, you're a methodical supporter. You provide reliable, high-quality work while maintaining a steady, supportive approach."
    
    return combined_description
# Inject CSS for rounded images
st.markdown(
    """
    <style>
    .round-image {
        width: 150px; /* Adjust the size of the image */
        height: 150px; /* Ensure it remains square */
        border-radius: 50%; /* Makes the image round */
        object-fit: cover; /* Ensures the image scales properly */
        margin-bottom: 10px; /* Adds some spacing below the image */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Main app logic
if st.session_state['current_test'] is None:
    st.write("Select a personality test to begin:")
    
    
        #MBTI Test Section
    st.subheader("MBTI Personality Test")
    st.write("""
    The MBTI (Myers-Briggs Type Indicator) test helps you discover your psychological preferences in how you perceive the world and make decisions.
    It is based on Carl Jung's theory of psychological types.
    The test categorizes individuals into 16 personality types based on four dichotomies: Extraversion/Introversion, Sensing/Intuition, Thinking/Feeling, and Judging/Perceiving.
    This test is widely used for personal development, career guidance, and improving interpersonal relationships.
    Take this test to understand your personality type and how it influences your behavior.
    """)
    st.image("/home/thania/Downloads/Set of MBTI person types_ Socionics mbti. Personality test. Mind behavior concept. Flat vector illustration",width=200 )
    if st.button("Start MBTI Test", key="start_mbti"):
            st.session_state['current_test'] = "MBTI Personality Test"
            st.session_state['questions_answered'] = 0
            st.session_state['answers'] = {}
            st.rerun()
    
        #Big Five (OCEAN) Test Section
    st.subheader("Big Five (OCEAN)")
    st.write("""
    The Big Five personality test measures five broad dimensions of personality: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.
    It is one of the most scientifically validated models of personality.
    This test helps you understand how you score on each dimension and what it means for your behavior and preferences.
    Use this test to gain insights into your personality traits and how they affect your interactions with others.
    """)
    st.image("/home/thania/Downloads/The Big 5 OCEAN Traits Explained - Personality Quizzes.jpeg",width=200)
    if st.button("Start OCEAN Test", key="start_ocean"):
            st.session_state['current_test'] = "Big Five (OCEAN)"
            st.session_state['questions_answered'] = 0
            st.session_state['answers'] = {}
            st.rerun()
    
        #DISC Assessment Section 
    st.subheader("DISC Assessment")
    st.write("""
    The DISC assessment identifies your behavioral style in terms of Dominance, Influence, Steadiness, and Conscientiousness.
    It is a powerful tool used in workplace settings to improve communication, teamwork, and leadership.
    This test helps you understand how you approach tasks, interact with others, and respond to challenges.
    Take this test to learn more about your behavioral tendencies and how to leverage them effectively.
    """)
    st.image("/home/thania/Downloads/DiSC Personality Test Guide.jpeg", width=200)
    if st.button("Start DISC Test", key="start_disc"):
            st.session_state['current_test'] = "DISC Assessment"
            st.session_state['questions_answered'] = 0
            st.session_state['answers'] = {}
            st.rerun()
else:
    # Get the appropriate test
    if st.session_state['current_test'] == "MBTI Personality Test":
        questions, dimensions = mbti_test()
        result_calculator = calculate_mbti_results
        result_interpreter = get_mbti_description
    elif st.session_state['current_test'] == "Big Five (OCEAN)":
        questions, dimensions = ocean_test()
        result_calculator = calculate_ocean_results
        result_interpreter = get_ocean_description
    elif st.session_state['current_test'] == "DISC Assessment":
        questions, dimensions = disc_test()
        result_calculator = calculate_disc_results
        result_interpreter = get_disc_description
    
    # Add a back button at the top
    if st.button("← Back to Test Selection"):
        st.session_state['current_test'] = None
        st.session_state['questions_answered'] = 0
        st.session_state['answers'] = {}
        st.rerun()
        
    # Display progress
    total_questions = len(questions)
    progress = st.session_state['questions_answered'] / total_questions
    st.progress(progress)
    st.write(f"Question {st.session_state['questions_answered'] + 1} of {total_questions}")
    
    # Display current question if not all questions are answered
    if st.session_state['questions_answered'] < total_questions:
        current_q = questions[st.session_state['questions_answered']]
        st.subheader(current_q["question"])
        
        # Create radio buttons for options
        option_labels = current_q["options"]
        selected_option = st.radio("Select your answer:", options=range(len(option_labels)), 
                                  format_func=lambda x: option_labels[x], key=f"q_{st.session_state['questions_answered']}")
        
        if st.button("Next"):
            # Save the answer
            st.session_state['answers'][st.session_state['questions_answered']] = selected_option
            st.session_state['questions_answered'] += 1
           # st.experimental_rerun()
    
    # Show results when all questions are answered
    else:
        st.subheader("Your Results")
        
        # Calculate results
        if st.session_state['current_test'] == "MBTI Personality Test":
            result = result_calculator(st.session_state['answers'], dimensions)
            st.session_state['test_results'][st.session_state['current_test']] = result
            
            st.write(f"Your personality type is: **{result}**")
            st.write(result_interpreter(result))
            
            # Display MBTI chart
            st.subheader("Your MBTI Dimensions")
            for dim in dimensions:
                score_a = 0
                score_b = 0
                for q_idx in dim["questions"]:
                    if q_idx in st.session_state['answers']:
                        if st.session_state['answers'][q_idx] == dim["options"][0]:
                            score_a += 1
                        elif st.session_state['answers'][q_idx] == dim["options"][1]:
                            score_b += 1
                
                total = score_a + score_b
                if total > 0:
                    pct_a = (score_a / total) * 100
                    pct_b = (score_b / total) * 100
                    
                    dim_name = dim["name"]
                    dim_parts = dim_name.split(" vs. ")
                    
                    st.write(f"**{dim_name}**")
                    st.write(f"{dim_parts[0]}: {pct_a:.0f}% | {dim_parts[1]}: {pct_b:.0f}%")
                    st.progress(pct_a/100)
        
        elif st.session_state['current_test'] == "Big Five (OCEAN)":
            result = result_calculator(st.session_state['answers'])
            st.session_state['test_results'][st.session_state['current_test']] = result
            
            # Create radar chart for OCEAN
            labels = list(result.keys())
            values = list(result.values())
            
            fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
            angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
            angles += angles[:1]  # Close the loop
            
            values += values[:1]  # Close the loop
            
            ax.plot(angles, values, linewidth=2, linestyle='solid')
            ax.fill(angles, values, alpha=0.25)
            
            ax.set_theta_offset(3.14159 / 2)
            ax.set_theta_direction(-1)
            
            plt.xticks(angles[:-1], labels)
            ax.set_rlabel_position(0)
            plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="grey", size=8)
            plt.ylim(0, 100)
            
            st.pyplot(fig)
            
            # Display descriptions
            descriptions = result_interpreter(result)
            for dim, desc in descriptions.items():
                st.subheader(dim)
                st.write(f"Score: {result[dim]:.1f}%")
                st.write(desc)
        
        elif st.session_state['current_test'] == "DISC Assessment":
            result = result_calculator(st.session_state['answers'])
            st.session_state['test_results'][st.session_state['current_test']] = result
            
            # Create bar chart for DISC
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(result.keys(), result.values(), color=['#FF5733', '#33FF57', '#3357FF', '#F3FF33'])
            
            ax.set_ylabel('Percentage')
            ax.set_title('Your DISC Profile')
            ax.set_ylim(0, 100)
            
            # Add percentage labels on top of bars
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height:.1f}%',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')
            
            st.pyplot(fig)
            
            # Display description
            st.subheader("Your DISC Profile Interpretation")
            st.write(result_interpreter(result))
        
        # Option to retake or try another test
        if st.button("Retake Test"):
            st.session_state['questions_answered'] = 0
            st.session_state['answers'] = {}
            #st.experimental_rerun()
        
        if st.button("Try Another Test"):
            st.session_state['current_test'] = None
            st.session_state['questions_answered'] = 0
            st.session_state['answers'] = {}
            #st.experimental_rerun()

with col2:
    if lottie_coding:
        st_lottie(
            lottie_coding,
            speed=1,
            loop=True,
            height=250,  # Adjust height
            width=250,   # Adjust width
            quality="high",
            key="lottie_sidebar",
        )


