import streamlit as st
import random


# NOTES:
# ADD A RESET BUTTON TO RESET THE USED CHALLENGES
# ADD POSIBILITY TO ADD NEW CHALLENGES
# ADD POSIBILITY TO ADD NEW CATEGORIES
# ADD POSIBILITY TO GIVE FEEDBACK ON CHALLENGES (THUMBS UP OR DOWN) AND YOU WONT GET THEM IN THE FUTURE 
# USE FEEDBACK TO RECOMMENDATION SYSTEM TO RECOMMEND CHALLENGES BASED ON WHAT YOU LIKE
# ADD POSIBILITY TO import/export challenges and players AND SEE WHO HAD WHAT QUESTIONS AND WHAT THEY LIKED

#Dictionaries for truth and dare challenges
truth_challenges = [
    #Social challenges
    {"question": "What is your biggest insecurity?", "category": "Social"},
    {"question": "What is your biggest regret?", "category": "Personal"},
    {"question": "What is your biggest fear?", "category": "Fear"},
    {"question": "Have you ever cheated on a test?", "category": "School"},
    {"question": "What is your most treasured possession?", "category": "Personal"},
    {"question": "What is your biggest pet peeve?", "category": "Social"},
    {"question": "What is your biggest regret?", "category": "Personal"},

    #Adult challenges
    {"question": "What is your biggest turn on?", "category": "Adult"},
    {"question": "What is your biggest turn off?", "category": "Adult"},
    {"question": "What is your biggest sexual fantasy?", "category": "Adult"},

    #Embarrassment challenges
    {"question": "What is the most embarrassing thing you've ever done?", "category": "Embarrassment"},
    {"question": "What is the most embarrassing thing your parents have caught you doing?", "category": "Embarrassment"},
    {"question": "What is the most embarrassing thing you've ever worn?", "category": "Embarrassment"},
    {"question": "What is the most embarrassing thing you've ever said?", "category": "Embarrassment"},
    {"question": "What is the most embarrassing thing you've ever posted on social media?", "category": "Embarrassment"},
    {"question": "What is the most embarrassing thing that has ever happened to you?", "category": "Embarrassment"},

    #Love challenges
    {"question": "Tell us about your first crush.", "category": "Love"},
    {"question": "Tell us about your first kiss.", "category": "Love"},
    {"question": "Tell us about your first love.", "category": "Love"},
    {"question": "Tell us about your first heartbreak.", "category": "Love"},
    {"question": "Tell us about your first date.", "category": "Love"},
    {"question": "Tell us about your first time.", "category": "Love"},
]   

dare_challenges = [
    #Physicalh challenges
    {"question": "Do 10 push-ups.", "category": "Physical"},
    {"question": "Dance with no music for 1 minute.", "category": "Physical"},
    {"question": "Do 10 squats.", "category": "Physical"},
    {"question": "Do 10 jumping jacks.", "category": "Physical"},
    {"question": "Do 10 burpees.", "category": "Physical"},
    {"question": "Do 10 lunges.", "category": "Physical"},
    {"question": "Do 10 crunches.", "category": "Physical"},
    {"question": "Do 10 pull-ups.", "category": "Physical"},
    {"question": "Do 10 leg raises.", "category": "Physical"},
    {"question":  "Make up a dance and perform it.", "category": "Physical"},

    #Physical touch challenges
    {"question": "Together with the person on your left and right, make scene from a movie within 2 minutes and perform it.", "category": "Physical Touch"},
    {"question": "Try to see if you can score the person in front of you - use physical touch and body language only.", "category": "Physical Touch"},
    {"question": "Try to see if you can score the person to your left - use physical touch and body language only.", "category": "Physical Touch"},
    {"question": "Try to see if you can score the person to your right - use physical touch and body language only.", "category": "Physical Touch"},
    {"question": "Make up a dance and dance with a person of your choice - but with the OPPOSITE gender (if possible).", "category": "Physical Touch"},

    #Imitation challenges
    {"question": "Imitate a celebrity of your choice.", "category": "Imitation"},
    {"question": "Imitate a family member of your choice.", "category": "Imitation"},
    {"question": "Imitate a friend of your choice.", "category": "Imitation"},
    {"question": "Imitate a teacher of your choice.", "category": "Imitation"},
    {"question": "Imitate a classmate of your choice.", "category": "Imitation"},
    {"question": "Imitate a stranger of your choice.", "category": "Imitation"},

    #adult challenges
    {"question": "Take a body shot off of someone.", "category": "Adult"},
    {"question": "Give someone a lap dance.", "category": "Adult"},
    {"question": "Take off your shirt.", "category": "Adult"},

    #Embarrassment challenges
    {"question": "Call a friend and sing 'Happy Birthday' to them, regardless of their actual birthday.", "category": "Embarrassment"},
    {"question": "Do your best impression of a baby being born.", "category": "Embarrassment"},
    {"question": "Speak in an accent for the next 3 rounds.", "category": "Embarrassment"},

    #Love challenges
    {"question": "Give someone a hug.", "category": "Love"},
    {"question": "Give someone a kiss.", "category": "Love"},
    {"question": "Call your crush (and say whatever you want - preferably the truth).", "category": "Love"},
    {"question": "Tell someone you love them.", "category": "Love"},
    {"question": "Tell someone you hate them.", "category": "Love"},
    {"question": "Tell someone you like them.", "category": "Love"},
    {"question": "Tell someone you have a crush on them.", "category": "Love"},

]


# Lists to keep track of used challenges and players
used_truth_challenges = []
used_dare_challenges = []
player_names = []

# Initialize session_state if it hasn't been initialized
if 'player_data' not in st.session_state:
    st.session_state.player_data = {}

# Function to get a unique random challenge
def get_unique_random_challenge(player_name):
    excluded_categories = st.session_state.player_data[player_name]['excluded_categories']
    choice = random.choice(["Truth", "Dare"])
    challenge = None

    # Filter out challenges from excluded categories
    available_truth_challenges = [ch for ch in truth_challenges if ch not in used_truth_challenges and ch['category'] not in excluded_categories]
    available_dare_challenges = [ch for ch in dare_challenges if ch not in used_dare_challenges and ch['category'] not in excluded_categories]

    if choice == "Truth":
        # If no challenges are left, clear the used list and reset
        if not available_truth_challenges:
            used_truth_challenges.clear()
            available_truth_challenges = [ch for ch in truth_challenges if ch['category'] not in excluded_categories]

        challenge = random.choice(available_truth_challenges)
        used_truth_challenges.append(challenge)
        
    elif choice == "Dare":
        # If no challenges are left, clear the used list and reset
        if not available_dare_challenges:
            used_dare_challenges.clear()
            available_dare_challenges = [ch for ch in dare_challenges if ch['category'] not in excluded_categories]

        challenge = random.choice(available_dare_challenges)
        used_dare_challenges.append(challenge)
        
    return {"choice": choice, "question": challenge['question'], "category": challenge['category']}


def main():
    st.title("Truth or Dare Generator")

    # All categories
    all_categories = list(set(ch['category'] for ch in truth_challenges + dare_challenges))

    # Add player names individually
    new_player = st.text_input("Enter a player name:", key="new_player_input")  # Unique key added here
    if new_player:
        excluded_categories_for_new_player = st.multiselect("Select categories to exclude for this player", all_categories)
        if st.button("Add Player"):
            st.session_state.player_data[new_player] = {'excluded_categories': excluded_categories_for_new_player}
            st.success(f"Added {new_player}")

    # Delete players
    if st.session_state.player_data:
        player_to_delete = st.selectbox("Select a player to delete", list(st.session_state.player_data.keys()))
        if st.button("Delete Player"):
            del st.session_state.player_data[player_to_delete]
            st.success(f"Deleted {player_to_delete}")

    # Show list of added players
    if st.session_state.player_data:
        st.write("List of Players:")
        for player in st.session_state.player_data.keys():
            st.write(player)

    # Generate Truth or Dare
    if st.session_state.player_data:
        if st.button("Generate Truth or Dare"):
            selected_player = random.choice(list(st.session_state.player_data.keys()))
            challenge = get_unique_random_challenge(selected_player)
            st.write(f"{selected_player}, {challenge}")

    # Display excluded categories for each player in the sidebar
    if st.session_state.player_data:
        st.sidebar.title("Excluded Categories for Each Player:")
        for player, data in st.session_state.player_data.items():
            st.sidebar.write(f"{player}: {', '.join(data['excluded_categories']) if data['excluded_categories'] else 'None'}")

# Run the app
if __name__ == "__main__":
    main()
