import streamlit as st
from db_connection import db_connection
from streamlit_lottie import st_lottie
import json
import os

 #Function to load Lottie animation
def load_lottiefile(filepath: str):
    if not os.path.exists(filepath):
        st.error(f"Error: File not found - {filepath}")
        return None
    with open(filepath, "r") as f:
        return json.load(f)

# Page configuration
st.set_page_config(
    page_title="Mental Health Companion",
    layout="wide"
)
st.title("Resources :computer:")
# Ensure user is logged in
if 'user_email' not in st.session_state:
    st.warning('Please log in first')
    st.stop()
else:
    user_email = st.session_state['user_email']

# Load animation and image
lottie_yoga = load_lottiefile("/home/thania/Downloads/Joshi/Joshi/anime/yogadog.json")  
yoga_image = "/home/thania/Downloads/stretching.jpeg" 

# Create columns for title and visuals
col1, col2, col3 = st.columns([2, 1, 1])

# Add title in the first column
with col1:
    st.markdown("Your personal guide to mindfulness, yoga, and mental wellness")

# Add image in the second column
with col2:
    st.image(yoga_image, width=200)

# Add animation in the third column
with col3:
    st_lottie(lottie_yoga, height=200, key="yoga_animation")
# Navigation
tab1, tab2, tab3 = st.tabs(["Yoga", "Meditation", "Articles"])

# Yoga Tab
with tab1:
    st.header("Yoga Resources")
    
    # Video section
    st.subheader("Yoga Videos")
    yoga_videos = [
        {
            "title": "Morning Yoga Routine",
            "description": "Start your day with this energizing yoga flow to wake up your body and mind.",
            "url": "https://www.youtube.com/embed/UEEsdXn8oG8"
        },
        {
            "title": "Yoga for Stress Relief",
            "description": "Relieve tension and anxiety with this calming practice focused on deep stretches.",
            "url": "https://www.youtube.com/embed/hJbRpHZr_d0"
        },
        {
            "title": "Bedtime Yoga for Better Sleep",
            "description": "Wind down with gentle movements to prepare your body and mind for restful sleep.",
            "url": "https://www.youtube.com/embed/v7SN-d4qXx0"
        }
    ]
    
    # Create columns for videos
    video_cols = st.columns(3)
    
    for i, video in enumerate(yoga_videos):
        with video_cols[i % 3]:
            st.markdown(f"**{video['title']}**")
            st.markdown(video['description'])
            st.video(video["url"])
   
    # Articles section
    st.subheader("Yoga Articles")

    # Initialize session state for content visibility if not present
    if 'show_yoga_poses' not in st.session_state:
        st.session_state.show_yoga_poses = False
    if 'show_science' not in st.session_state:
        st.session_state.show_science = False

    # Toggle functions
    def toggle_yoga_poses():
        st.session_state.show_yoga_poses = not st.session_state.show_yoga_poses

    def toggle_science():
        st.session_state.show_science = not st.session_state.show_science
    # Buttons for article selection
    col1, col2 = st.columns(2)
    with col1:
        st.button("Yoga Poses for Anxiety and Depression", on_click=toggle_yoga_poses)
    with col2:
        st.button("The Science Behind Yoga", on_click=toggle_science)

    # Create a separate section below with expanders
    st.markdown("---")
    st.header("Selected Article")

    # Display content based on state in expanders
    if st.session_state.show_yoga_poses:
        with st.expander("Yoga Poses for Anxiety and Depression", expanded=True):
            # Main heading
            st.markdown("<h1>Yoga Poses for Anxiety and Depression</h1>", unsafe_allow_html=True)
            
            # Introduction
            st.markdown("When anxiety takes hold it can be difficult to find a way to refocus your mind. Thankfully relief from the symptoms of common mental health conditions is just one of the many benefits of yoga.")
            
            # Pose 1
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Butterfly-Pose.png")
            st.markdown("Butterfly Pose (Baddha Konasana)")
            
            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">1</span>
                </div>
                <h2>Butterfly (Baddha Konasana)</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("If you're looking for a relatively simple posture that grounds you in the moment when you're feeling anxious, then try this one!")
            
            st.markdown("By keeping your spine straight you're allowing tension to drain away. With a focus on your breathing, yogis feel the movement encourages internal reflection.")
            
            st.markdown("**Baddha konasana also encourages you to enter a meditative state, allowing you to enjoy all the health advantages of meditation.**")
            
            st.markdown("Plus it's powerful for your digestive health, making it the perfect yoga pose for weight loss.")
            
            # Pose 2
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Extended-Triangle-Pose.png")
            st.markdown("Extended Triangle Pose (Utthita Trikonasana)")
            
            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">2</span>
                </div>
                <h2>Extended Triangle (Utthita Trikonasana)</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("Experts recommend this simple asana as a yoga exercise for beginners, as it's seen as a pose that can help you cope better when life is tough.")
            
            st.markdown("**How does it work?**")
            
            st.markdown("Well it's thought that by tilting your body, you are equally distributing the energy flow, helping you feel calmer and more balanced.")
            
            st.markdown("Yoga Journal recommends including it as part of a sequence to train your brain to relax.")
            
            st.markdown("**Extended triangle is one of a number of asanas that are designed to access the parasympathetic nervous system.**")
            
            st.markdown("This part of your nervous system undoes the work of the sympathetic nervous system after a stressful situation. Slowing your heart rate and increasing your digestion.")
            
            # Pose 3
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Bridge-Pose.png")
            st.markdown("Bridge Pose (Setu Bandha Sarvangasana)")
            
            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">3</span>
                </div>
                <h2>Bridge Pose (Setu Bandha Sarvangasana)</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("This powerful inversion opens up space around your heart, creating more freedom for you to focus and think more clearly.")
            
            # Quote box
            st.markdown("""
            <div style="background-color:#1E1E1E;padding:20px;border-left:5px solid #3498DB;margin:20px 0;">
                <p style="font-style:italic;font-size:1.1em;color:#E0E0E0;">
                "Inversions are enormously beneficial to the nervous system. Having the head below the heart is soothing and cooling for the nervous system and is wonderful for toning down stress. Fresh, oxygenated blood is sent to the brain which can help manage anxiety, depression, and insomnia."
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Watch the video below for more information about how it should be practiced:")
            st.video("https://youtu.be/57jInRiLu7o")
            
            # Pose 4
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Half-Moon-Pose.png")
            st.markdown("Half Moon Pose (Ardha Chandrasana)")
            
            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">4</span>
                </div>
                <h2>Half Moon Pose (Ardha Chandrasana)</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("Half moon is named as such as it's said to resemble an Indian moon floating in the sky.")
            
            st.markdown("Though it's not easy, it has many advantages when it comes to using yoga to improve your mental health.")
            
            st.markdown("**It's a cooling one, encouraging a calm and soothing energy to enter your body and making you relax.**")
            
            st.markdown("Also, we have a tendency to slouch when we are low. This movement opens the whole front of your body, allowing you to enjoy the advantages of good posture and improved self-esteem.")
            
            # Pose 5
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Legs-Up-The-Wall-Pose.png")
            st.markdown("Legs-Up-The-Wall Pose (Viparita Karani)")
            
            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">5</span>
                </div>
                <h2>Legs-Up-The-Wall Pose (Viparita Karani)</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("When you need to calm a busy mind there aren't many postures as powerful as legs-up-the-wall.")
            
            st.markdown("There are two different variations, so choose the one that works for you.")
            
            st.markdown("**Firstly, the classic form of the pose:**")
            
            st.markdown("Renowned yogi Gail Boorstein Grossman explains in her book, Restorative Yoga for Life, how it can help you regain a sense of calm after a stressful day, making it ideal for anxious people.")
            
            st.markdown("**Secondly, there is the bolster variation:**")
            
            st.markdown("This is perfect if you want to be able to completely relax, as your lower back is supported with a bolster.")
            
            # Quote box
            st.markdown("""
            <div style="background-color:#252525;padding:20px;border-left:5px solid #00A8E8;margin:20px 0;">
                <p style="font-style:italic;font-size:1.1em;color:#E0E0E0;">
                "It is said that twenty minutes spent in this pose has the same beneficial effect on your nervous system as taking a nap."
                </p>
            </div>
            """, unsafe_allow_html=True)

            
            # Pose 6
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Childs-Pose.png")
            st.markdown("Child's Pose (Balasana)")
            
            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">6</span>
                </div>
                <h2>Child's Pose (Balasana)</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("Child's pose is a restful posture that can be sequenced between more challenging asanas.")
            
            st.markdown("It gently stretches your lower back, hips, thighs, knees, and ankles while relaxing your spine, shoulders, and neck.")
            
            st.markdown("**This pose is particularly beneficial for anxiety as it encourages you to turn inward and focus on your breath.**")
            
            # Pose 1 (originally Pose 7)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Seated-Forward-Bend.png")
            st.markdown("Seated Forward Bend (Paschimottanasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">7</span>
                </div>
                <h2>Seated Forward Bend (Paschimottanasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("We know yoga has a number of advantages for your mental health, thanks to its mindful movements. Seated forward bend is considered to be particularly good.")

            st.markdown("It gives the back of your body a full stretch, all the way from your heels to your neck.")

            st.markdown("**Research shows that it not only helps to relieve feelings of stress, but also deal with the associated symptoms such as tiredness and headaches.**")

            # Pose 2 (originally Pose 8)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Cow-Pose.png")
            st.markdown("Cow (Bitilasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">8</span>
                </div>
                <h2>Cow (Bitilasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("One of the pillars of yoga is breath.")

            st.markdown("There are a range of different techniques, each with their own effect on the body and emotions.")

            st.markdown("When you're suffering with low mood or uncontrollable worry it can be useful to connect to your breathing to feel calmer.")

            st.markdown("**This form encourages you to inhale and exhale, while awakening your spine.**")

            st.markdown("Robert Butera in his book, Yoga Therapy for Stress and Anxiety explains that the key is to connect your breath with your movement.")

            st.markdown("As you breathe deeper and deeper, the slower the motion becomes and the calmer you will be.")

            # Pose 3 (originally Pose 9)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Cat-Pose.png")
            st.markdown("Cat (Marjaryasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">9</span>
                </div>
                <h2>Cat (Marjaryasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("You typically practice by going between cat and cow to open up, then relax your back.")

            st.markdown("In Robert Butera's aforementioned book, Yoga Therapy for Stress and Anxiety, he explains the grounding qualities of the form:")

            st.markdown("The Cat Pose consists of relaxation of your back by taking on a posture of a cat… this movement allows us grounding as we begin to gently open up the back body and stimulate the core.")

            st.markdown("Watch the video below to see how to perform Cat/Cow Pose effectively:")
            st.video("https://www.youtube.com/watch?v=kqnua4rHVVA")

            # Pose 4 (originally Pose 10)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Standing-Forward-Fold.png")
            st.markdown("Standing Forward Bend (Uttanasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">10</span>
                </div>
                <h2>Standing Forward Bend (Uttanasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("You can enjoy many physical perks particularly for your neck and lower back with this one!")

            st.markdown("**However it is also shown to reduce stress, anxiety and depression.**")

            st.markdown("Celebrated yoga teacher, B. K. S Iyengar describes how, while practicing:")

            st.markdown("""
            <div style="background-color:#252525;padding:20px;border-left:5px solid #00A8E8;margin:20px 0;">
                <p style="font-style:italic;font-size:1.1em;color:#E0E0E0;">
                "The heartbeats slow down, and the spinal nerves rejuvenate. Any depression felt in the mind is removed if one holds the pose for two minutes or more."
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Pose 5 (originally Pose 11)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Camel-Pose.png")
            st.markdown("Camel (Ustrasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">11</span>
                </div>
                <h2>Camel (Ustrasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Ustrasana is a powerful yoga pose for back pain, however it's also seen as great for dealing with your emotions.")

            st.markdown("**Why?**")

            st.markdown("Well as the Yoga Business Academy explains, it's a great stress reliever, helping to lift you up (literally!) when you're feeling weighed down by your problems.")

            st.markdown("It also opens up the heart chakra, helping to release your emotions, with many people finding they start crying when practicing the exercise.")

            # Pose 6 (originally Pose 12)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Fish-Pose.png")
            st.markdown("Fish (Matsyasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">12</span>
                </div>
                <h2>Fish (Matsyasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Use this motion to release any pent up emotions, as it's also a heart opener.")

            st.markdown("Yogis explain how during the motion it's essential that you keep your breathing even to experience a sense of calm.")

            st.markdown("**They recommend practicing regularly to build confidence and to grow emotionally – getting through any problems that you encounter, swimmingly!**")

            # Pose 7 (originally Pose 13)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Staff-Pose.png")
            st.markdown("Staff (Dandasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">13</span>
                </div>
                <h2>Staff (Dandasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("One of the most popular reasons people start yoga is to cope with stress, according to the latest yoga statistics. Staff can be particularly useful.")

            st.markdown("**Yoga practitioners describe how practicing this posture regularly, can decrease stress hormones within your body.**")

            st.markdown("If you struggle with tiredness as a side effect of your disorder, the position is thought to give you a boost of energy.")

            st.markdown("Worries keeping you awake at night? There is evidence to show that dandasana is a great asana for sleep.")

            # Pose 8 (originally Pose 14)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Upward-Salute.png")
            st.markdown("Upward Salute (Urdhva Hastasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">14</span>
                </div>
                <h2>Upward Salute (Urdhva Hastasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Upward salute is often practiced as part of a Sun Salutation, a series of postures that encourage you to flow through moves while focusing on your breathing.")

            st.markdown("**It's great for anxiety as essentially the energy within your body can move freely.**")

            st.markdown("Yogis recommend holding the form for 30 seconds with your eyes closed to experience the full benefit.")

            st.markdown("Recognised as a self-esteem boosting asana, it can improve our sense of power and control.")

            # Pose 9 (originally Pose 15)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Tree-Pose.png")
            st.markdown("Tree (Vriksasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">15</span>
                </div>
                <h2>Tree (Vriksasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Tree is a balancing pose that requires your full concentration, which can be a welcome distraction.")

            st.markdown("**You feel strong and steady when you master the form, in turn becoming more in control of your emotions.**")

            st.markdown("Research into the impact of yoga for back pain looked at how a number of postures, including vriksasana, could help people with their condition.")

            st.markdown("Results showed that the postures helped to release serotonin, commonly known as the \"happy chemical\"!")


            # Pose 10 (originally Pose 16)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Dolphin-Pose.png")
            st.markdown("Dolphin Pose (Ardha Pincha Mayurasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">16</span>
                </div>
                <h2>Dolphin Pose (Ardha Pincha Mayurasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Dolphin has a number of different merits, including helping those with mild symptoms of depression.")

            st.markdown("**The shape means there's increased blood flow to the brain to improve awareness and concentration.**")

            st.markdown("Watch the video below from Yoga with Adriene to learn how to master the exercise:")
            st.video("https://youtu.be/6w4ZoSuBDCg")

            # Pose 11 (originally Pose 17)
            st.image("https://www.thegoodbody.com/wp-content/uploads/2020/03/Corpse-Pose.png")
            st.markdown("Corpse Pose (Savasana)")

            st.markdown("""
            <div style="display:flex;align-items:center">
                <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                    <span style="font-size:1.5em;">11</span>
                </div>
                <h2>Corpse Pose (Savasana)</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("Savasana is the final relaxation pose at the end of a yoga class, and it's essential for your mental health.")

            st.markdown("**Yoga teacher and author Cyndi Lee explains:**")

            st.markdown("""
            <div style="background-color:#1E1E1E;padding:20px;border-left:5px solid #00A8E8;margin:20px 0;">
                <p style="font-style:italic;font-size:1.1em;color:#E0E0E0;">
                "Savasana might look like a nap at the end of your yoga practice. But it's actually a fully conscious pose aimed at being awake, yet completely relaxed."
                </p>
            </div>
            """, unsafe_allow_html=True)


            st.markdown("It's a time to let go of any tension in your body and quiet your mind, allowing the benefits of your practice to fully integrate.")
    if st.session_state.show_science:
         with st.expander("Science behind Yoga", expanded=True):
            # Main heading
                st.markdown("<h1>Science behind Yoga</h1>", unsafe_allow_html=True)
                # Introduction
                st.markdown("""
                Yoga, an ancient practice originating in India over 5,000 years ago, has transcended cultural and geographical boundaries to become a global phenomenon. While traditionally viewed through a spiritual lens, modern science has begun to unravel the physiological and psychological mechanisms behind yoga's profound health benefits.
                """)
                
                
                # Physical Benefits section
                st.markdown("""
                <div style="display:flex;align-items:center">
                    <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                        <span style="font-size:1.5em;">1</span>
                    </div>
                    <h2>The Physical Benefits of Yoga</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### Flexibility and Strength")
                st.markdown("""
                One of the most immediate and noticeable benefits of yoga is improved flexibility. Regular practice helps to stretch and lengthen muscles, increasing the range of motion in joints. A study published in the International Journal of Yoga found that just 10 weeks of yoga practice significantly increased flexibility in athletic college students.
                
                Beyond flexibility, yoga builds strength through isometric contractions — holding poses that engage multiple muscle groups simultaneously. Unlike traditional strength training that often isolates specific muscles, yoga promotes functional strength that translates to everyday activities.
                """)
                
                st.markdown("### Cardiovascular Health")
                st.markdown("""
                Despite the common perception of yoga as a gentle practice, certain styles like Vinyasa or Ashtanga can offer a vigorous cardiovascular workout. Research published in the European Journal of Preventive Cardiology found that yoga can help reduce blood pressure, lower cholesterol levels, and decrease the risk of heart disease.
                
                **The mechanisms behind these benefits include:**
                
                * Reduced stress and inflammation
                * Improved autonomic nervous system function
                * Enhanced respiratory efficiency
                * Increased heart rate variability (a marker of cardiovascular health)
                """)
                
                st.markdown("### Pain Relief")
                st.markdown("""
                Chronic pain affects millions of people worldwide, often leading to reduced quality of life and dependence on medication. Studies have demonstrated the effectiveness of yoga as a complementary therapy in managing chronic pain conditions such as:
                
                * Lower back pain
                * Arthritis
                * Migraines
                * Fibromyalgia
                
                A meta-analysis published in the Journal of Pain Research concluded that yoga provides both short and long-term benefits for chronic pain management, with improvements in pain intensity, functional disability, and depression.
                """)
                
                
                
                st.markdown("""
                <div style="display:flex;align-items:center">
                    <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                        <span style="font-size:1.5em;">2</span>
                    </div>
                    <h2>Mental and Emotional Benefits</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### Stress Reduction")
                st.markdown("""
                One of the most well-documented benefits of yoga is its ability to reduce stress. Through the combination of physical postures, breath control, and meditation, yoga activates the parasympathetic nervous system, triggering the relaxation response.
                """)
                
                st.markdown("""
    <div style="background-color:#1E1E1E; padding:20px; border-left:5px solid #00a8e8; margin:20px 0;">
        <p style="font-style:italic; font-size:1.1em; color:#FFFFFF;">
        "Yoga practice can significantly reduce the secretion of cortisol, the primary stress hormone, 
        leading to a cascade of positive effects throughout the body and mind."
        </p>
    </div>
    """, unsafe_allow_html=True)

                st.markdown("### Improved Mood and Mental Health")
                st.markdown("""
                Regular yoga practice has been linked to reduced symptoms of depression and anxiety. The mindfulness aspect of yoga helps practitioners develop awareness of present-moment experiences, reducing rumination and worry.
                
                A study published in the Journal of Alternative and Complementary Medicine found that yoga increases levels of gamma-aminobutyric acid (GABA), a neurotransmitter that plays a crucial role in regulating mood. Low GABA levels are associated with anxiety and depression, suggesting that yoga's mood-enhancing effects may be partly due to its impact on brain chemistry.
                """)
                
                st.markdown("### Cognitive Function")
                st.markdown("""
                Emerging research suggests that yoga can enhance cognitive function, including:
                
                * Improved attention and concentration
                * Enhanced memory
                * Faster information processing
                * Better executive function
                
                These benefits may be particularly valuable for aging populations. A study published in the Journal of Alzheimer's Disease found that a 12-week yoga intervention improved visual-spatial memory, attention, and executive function in older adults with mild cognitive impairment.
                """)
                
                # File path to Lottie animation
                lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/yoga.json"

                lottie_coding = load_lottiefile(lottie_path)
                if lottie_coding:
                    st_lottie(
                        lottie_coding,
                        speed=1,
                        loop=True,
                        height=500,  # Adjust height
                        width=500,   # Adjust width
                        quality="high",
                        key="lottie_sidebar",
                    )
                
                st.markdown("""
                <div style="display:flex;align-items:center">
                    <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                        <span style="font-size:1.5em;">3</span>
                    </div>
                    <h2>The Role of Breath in Yoga</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                Central to yoga practice is pranayama, or breath control. The breath serves as a bridge between the body and mind, and conscious breathing techniques can influence both physical and mental states.
                
                **Scientific research has revealed several mechanisms through which pranayama affects health:**
                
                * **Autonomic Nervous System Regulation:** Deep, slow breathing activates the parasympathetic ("rest and digest") branch of the autonomic nervous system, counteracting the stress response.
                
                * **Improved Respiratory Function:** Regular practice of pranayama has been shown to increase vital capacity, improve oxygen saturation, and enhance overall respiratory efficiency.
                
                * **Stress Reduction:** Controlled breathing reduces cortisol levels and promotes a sense of calm and well-being.
                
                * **Enhanced Focus:** The concentration required for breath control serves as a form of meditation, training the mind to remain present and focused.
                """)
                
                # Conclusion
                st.markdown("""
                <div style="display:flex;align-items:center">
                    <div style="background-color:#00a8e8;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:15px;">
                        <span style="font-size:1.5em;">4</span>
                    </div>
                    <h2>Conclusion</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                The scientific evidence supporting yoga's health benefits continues to grow, validating what practitioners have known for thousands of years. As research methodologies become more sophisticated, we gain deeper insights into the mechanisms through which yoga promotes health and well-being.
                
                What makes yoga particularly valuable as a health intervention is its holistic nature. Unlike many modern medical approaches that target specific symptoms or systems, yoga addresses the whole person — physical, mental, and emotional.
                
                As healthcare continues to evolve toward more integrative approaches, yoga stands as a time-tested practice with scientifically validated benefits, offering a path to improved health that is accessible, affordable, and empowering.
                """)
                
                # Quote box
                st.markdown("""
    <div style="background-color:#1E1E1E; padding:20px; border-left:5px solid #00a8e8; margin:20px 0;">
        <p style="font-style:italic; font-size:1.1em; color:#FFFFFF;">
        "The science of yoga is, in fact, the science of living. It teaches us what our attitudes 
        should be toward life, toward our fellow human beings, toward all living things, 
        and toward the universe and its creator."
        </p>
    </div>
    """, unsafe_allow_html=True)
 

# Meditation Tab
with tab2:
    col1, col2 = st.columns([2, 1])

    lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/meditation.json"
    lottie_coding = load_lottiefile(lottie_path)

    # Add title in the first column
    with col1:
        st.header("Meditation Resources")
    # Add image in the second column
    with col2:
        if lottie_coding:
            st_lottie(
                lottie_coding,
                speed=1,
                loop=True,
                height=250,  # Adjust height
                width=250,   # Adjust width
                quality="high",
            )
        
    # Audio/podcast section
    st.subheader("Guided Meditations")
    
    meditation_audios = [
        {
            "title": "5-Minute Mindful Breathing",
            "description": "A quick meditation to center yourself during a busy day.",
            "duration": "5 minutes",
            "audio_url": "/home/thania/Downloads/WhatsApp Audio 2025-04-04 at 03.15.49.mpeg"
        },
        {
            "title": "Body Scan Meditation",
            "description": "Reduce physical tension with this progressive relaxation technique.",
            "duration": "15 minutes",
            "audio_url": "/home/thania/Downloads/15 Minute Guided Meditation for Mindfulness.mp3"
        },
        {
            "title": "Loving-Kindness Meditation",
            "description": "Cultivate compassion for yourself and others with this heart-opening practice.",
            "duration": "20 minutes",
            "audio_url": "/home/thania/Downloads/20 Minute Journey to Inner Peace & Deep Relaxation (Guided Meditation)_1.mp3"
        }
    ]
    
    for audio in meditation_audios:
        st.markdown(f"**{audio['title']}**")
        st.markdown(audio['description'])
        st.markdown(f"Duration: {audio['duration']}")
        # Placeholder for audio player
        st.audio(audio["audio_url"])
        st.markdown("---")
    
    # Video section for meditation
    st.subheader("Meditation Videos")
    
    meditation_videos = [
        {
            "title": "Introduction to Meditation",
            "description": "Learn the fundamentals of meditation practice with this beginner-friendly guide.",
            "url": "https://www.youtube.com/embed/inpok4MKVLM",
            "duration": "10 minutes"
        },
        {
            "title": "Guided Visualization for Anxiety",
            "description": "Use mental imagery to create a sense of calm and safety.",
            "url": "https://www.youtube.com/embed/O-6f5wQXSu8",
            "duration": "15 minutes"
        }
    ]
    
    video_cols = st.columns(2)
    
    for i, video in enumerate(meditation_videos):
        with video_cols[i % 2]:
            st.markdown(f"**{video['title']}**")
            st.markdown(video['description'])
            st.markdown(f"Duration: {video['duration']}")
            st.video(video["url"])

# Mental Health Resources Tab
with tab3:
    col1, col2 = st.columns([2, 1])

    lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/animation.json"
    lottie_coding = load_lottiefile(lottie_path)

    # Add title in the first column
    with col1:
        st.header("Mental Health Resources")
    # Add image in the second column
    with col2:
        if lottie_coding:
            st_lottie(
                lottie_coding,
                speed=1,
                loop=True,
                height=250,  # Adjust height
                width=250,   # Adjust width
                quality="high",
            )
    
    # Articles section
    st.subheader("Mental Health Articles")
    
    articles = [
        {
            "title": "Understanding Anxiety: Signs, Symptoms, and Coping Strategies",
            "description": "Learn to recognize anxiety and discover effective ways to manage it in daily life.",
            "url": "https://www.healthline.com/health/mental-health/how-to-cope-with-anxiety#coping-skills"
        },
        {
            "title": "The Connection Between Physical Exercise and Mental Health",
            "description": "How regular movement can improve mood, reduce stress, and boost cognitive function.",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S2212657022000162"
        },
        {
            "title": "Mindfulness in Everyday Life",
            "description": "Simple practices to incorporate mindfulness into your daily routine.",
            "url": "https://www.mindful.org/meditation/mindfulness-getting-started/"
        },
        {
            "title": "Healthy Sleep Habits for Better Mental Health",
            "description": "How quality sleep affects your psychological wellbeing and tips for improvement.",
            "url": "https://www.sleepfoundation.org/mental-health"
        }
    ]
    
    for article in articles:
        st.markdown(f"**{article['title']}**")
        st.markdown(article['description'])
        st.markdown(f"[Read Article]({article['url']})")
        st.markdown("---")
    
    # Crisis Resources section
    st.subheader("Crisis Resources")
    
    st.markdown("**Immediate Support Resources**")
    st.markdown("""
    If you're experiencing a mental health crisis or having thoughts of suicide, please reach out for help immediately:
    
    * National Suicide Prevention Lifeline: 988 or 1-800-273-8255
    * Crisis Text Line: Text HOME to 741741
    * Emergency Services: Call 911 or go to your nearest emergency room
    """)
