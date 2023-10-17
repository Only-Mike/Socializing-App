import streamlit as st
import random

# Lists for truth and dare challenges

# MAKE CHALLENGES INTO A LIST OF DICTIONARIES FOR GENDER AND PERSONALIZED CHOICES
truth_challenges = [
    "What is your biggest fear?",
    "Have you ever cheated on a test?",
    "What is the most embarrassing thing that has ever happened to you?",
    "What is your most treasured possession?",
    "Tell us about your first crush."
]

dare_challenges = [
    "Do 10 push-ups.",
    "Speak in an accent for the next 3 rounds.",
    "Dance with no music for 1 minute.",
    "Imitate a celebrity of your choice.",
    "Call a friend and sing 'Happy Birthday' to them, regardless of their actual birthday."
]

never_have_i_ever_challenges = [
    "Never have I ever been to a concert.",
    "Never have I ever been to a foreign country.",
    "Never have I ever been to a wedding.",
    "Never have I ever been to a funeral.",
]
# Lists to keep track of used challenges and players
used_truth_challenges = []
used_dare_challenges = []
used_never_have_i_ever_challenges = []
player_names = []

# Function to get a unique random challenge
def get_unique_random_challenge():
    choice = random.choice(["Truth", "Dare", "never_have_i_ever"])
    challenge = None
    
    if choice == "Truth":
        available_truth_challenges = [ch for ch in truth_challenges if ch not in used_truth_challenges]
        
        if not available_truth_challenges:
            used_truth_challenges.clear()
            available_truth_challenges = truth_challenges.copy()
        
        challenge = random.choice(available_truth_challenges)
        used_truth_challenges.append(challenge)
        
    elif choice == "Dare":
        available_dare_challenges = [ch for ch in dare_challenges if ch not in used_dare_challenges]
        
        if not available_dare_challenges:
            used_dare_challenges.clear()
            available_dare_challenges = dare_challenges.copy()
        
        challenge = random.choice(available_dare_challenges)
        used_dare_challenges.append(challenge)

    else:
        available_never_have_i_ever_challenges = [ch for ch in never_have_i_ever_challenges if ch not in used_never_have_i_ever_challenges]
        
        if not available_never_have_i_ever_challenges:
            used_never_have_i_ever_challenges.clear()
            available_never_have_i_ever_challenges = never_have_i_ever_challenges.copy()
        
        challenge = random.choice(available_never_have_i_ever_challenges)
        used_never_have_i_ever_challenges.append(challenge)
        
    return f"{choice}: {challenge}"

# Streamlit app
st.title("Truth or Dare Generator")

# Add player names individually
new_player = st.text_input("Enter a player name:")
if new_player:
    if st.button("Add Player"):
        player_names.append(new_player)
        st.success(f"Added {new_player}")

# Show list of added players
if player_names:
    st.write("List of Players:")
    for player in player_names:
        st.write(player)

# Generate Truth or Dare
if player_names:
    if st.button("Generate Truth or Dare"):
        selected_player = random.choice(player_names)
        challenge = get_unique_random_challenge()
        st.write(f"{selected_player}, {challenge}")
