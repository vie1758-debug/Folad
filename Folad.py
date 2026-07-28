# DAY 1=====




# =====================================================================
# MINIPROJECT: TEAM-BUILT CHATBOT GREETING
# =====================================================================

# ---------------------------------------------------------------------
# 🎨 UX DESIGNER (Feelings Advocate)
# Role: Focuses on how the user feels when interacting with the app.
# ---------------------------------------------------------------------

BOT_NAME = "Folad"
DEFAULT_REGISTER = "warm"        

VALID_MOODS = ("anxious", "formal", "urgent", "warm")
user_name = input("What is your name? ").strip() or "friend"
mood = input("How are you feeling? (anxious / formal / urgent / warm): ").strip().lower()

if not mood:
    mood = DEFAULT_REGISTER
if mood not in VALID_MOODS:
   mood = DEFAULT_REGISTER
   
# ---------------------------------------------------------------------
# 📋 PRODUCT OWNER (Client's Voice)
# Role: Ensures the app gets the necessary data from the user.
# ---------------------------------------------------------------------


# SAFETY NET: If the user just presses Enter without typing anything, 
# this keeps the program from breaking or looking blank by giving a default name.
         


# ---------------------------------------------------------------------
# 🛠️ SYSTEMS DEVELOPER (Builder)
# Role: Writes the logic and functions that make the app work.
# ---------------------------------------------------------------------

# DEFINE A FUNCTION: This creates a reusable block of code named 'greet'.
# It takes three arguments (inputs): the bot's name, the user's name, and the tone/register.
def greet(bot, user, register):
    if register == "warm":
        return f"Hello, my dear {user}! I'm {bot}, here to help!"
    elif register == "formal":
        return f"Good day {user}. I am {bot}. How may I assist?"
    elif register == "anxious":
        return f"Hi {user}, I'm {bot}. Don't worry—I'm here to guide you step by step."
    elif register == "urgent":
        return f"{user} — {bot} here. Let's act quickly."
    else:
        return f"Hello {user}, I am {bot}."

# RUN THE BOT: Calls the function using our active variables and prints the result to the screen.
while True:
    user_input = input("How can I help you today? (type 'exit' to quit): ").lower().strip()

    if user_input == "exit":
        print(f"Goodbye {user_name}! Stay safe.")
        break
    elif "register" in user_input:
        print("You can register at the nearest NIS office.")
    elif "payment" in user_input:
        print("Payments can be made online or at authorized centers.")
    elif "benefit" in user_input:
        print("NIS offers maternity, invalidity, and survivor benefits.")
    elif "help" in user_input:
        print("I'm here to assist you with NIS services.")
    else:
        print("Sorry, I didn’t understand that. Can you rephrase?")




# DAY 2




# ---------------------------------------------------------------------
# =====================================================
#   ECCU GAP Camp 2026 · WEEK 1 · DAY 2 SKELETON
#   Design — The Wardrobe (register switch)
# =====================================================

# 🤖 STEP 1: Give your bot a cool name! Replace the text in quotes.
BOT_NAME = "Folad"


# --- 📋 PRODUCT OWNER ROLE ---
# This "mini-machine" (function) checks if the mood entered is one we actually support.
# It acts like a bouncer at a club door.
def is_valid_mood(m):
    # It checks if the mood is in our approved list: anxious, formal, or urgent.
    # If yes, it returns True. If not, it returns False.
    return m in ("anxious", "formal", "urgent")

# A simple True/False flag. We'll use this later in Week 1, Day 4!
is_eligible = True   

# --- 💻 SYSTEMS DEVELOPER ROLE ---
# This function is the "brain" that chooses which tone to reply with based on the mood.
def speak(mood):
    if not is_valid_mood(mood):
        return f"[{BOT_NAME}] I'll default to formal — I didn't catch the mood."
    
    if mood == "anxious":
        return "I'm here for you. Let's go step by step."
    elif mood == "formal":
        return "How may I assist you today?"
    else:  # urgent
        return "Please act quickly and follow instructions."

# --- 🚀 RUNNING THE PROGRAM ---
# 1. Ask the user for their name. If they just hit enter, default to "friend".
# (.strip() cleans up accidental extra spaces the user might type).

# 2. Ask the user how they are feeling and make it lowercase so spelling matches our code.


# 3. Print the greeting and the bot's custom response!
print(f"Hi {user_name} — this is {BOT_NAME}.")
print(speak(mood))




#DAY 3





# =====================================================
#   ECCU GAP Camp 2026 · WEEK 1 · DAY 3 SKELETON
#   Prototype — Functions as reusable skills
# =====================================================

# 🤖 Change this to your bot's actual name!
BOT_NAME = "Folad"

# --- 🎨 UX DESIGNER ROLE: Tone Modifiers ---
# These functions act like filters (like a voice changer). 
# You pass text into them, and they return it styled in a specific mood.

def warm(text):    
    return f"{text} 💛"               # Adds a comforting heart emoji to the end.

def formal(text):  
    return f"Dear user — {text}"      # Makes it sound super polite and official.

def urgent(text):  
    return f"{text.upper()} ⚡"       # Smashes the text into ALL CAPS and adds lightning!


# --- 📋 PRODUCT OWNER ROLE: Data Organizers ---
# These are helper functions to clean up whatever messy text the user types in.

def clean_name(raw): 
    # .strip() removes accidental spaces at the start/end.
    # .title() automatically capitalizes the first letter of their name (e.g., "alex" becomes "Alex").
    # If they type nothing, it defaults to "friend".
    return raw.strip().title() or "friend"

def is_missing(field): 
    # Checks if the user just hit Enter without typing anything. 
    # Returns True if it's empty, False if there is text.
    return field.strip() == ""


# --- 💻 SYSTEMS DEVELOPER ROLE: The Logic Center ---
# This is where the magic happens. We are going to treat functions like variables!

def decide_tone(mood):
    # This function looks at the mood and hands back the *actual voice filter function* 
    # from the UX Designer section above. Notice there are no parenthesis () after warm, urgent, or formal!
    if mood == "anxious": return warm
    if mood == "urgent":  return urgent
    return formal                     # If it's anything else (or "formal"), use the formal filter.

def compose_reply(mood, body):
    # 1. Ask 'decide_tone' to give us the correct voice changer function.
    tone_fn = decide_tone(mood)
    
    # 2. Use that function (tone_fn) on our message body to style it.
    return tone_fn(body)


# --- 🚀 RUNNING THE APP ---


# 2. Ask for the mood. Lowercase it, and default to "formal" if they leave it blan

# 3. Create the base message we want to send.
body = f"Hi {user_name}, {BOT_NAME} here — how can I help today?"

# 4. Pass the mood and the message into our composer, and print the beautifully styled result!
print(compose_reply(mood, body))





# DAY 4





# =====================================================
#   ECCU GAP Camp 2026 · WEEK 1 · DAY 4 SKELETON
#   Refine — Plain Language & Territory
# =====================================================

# 🤖 Don't forget to replace this with your bot's name!
BOT_NAME = "Folad"

# --- 🎨 UX DESIGNER ROLE: Jargon Buster ---
# This dictionary works like a translator. It swaps out confusing corporate 
# words (jargon) for simple words that real humans actually use.
# Example: "synergy" -> "working together"
jargon_to_plain = {
    "Maternity Benefits": "Pros for having a child as a mother.",
    "Survivors Benefits": "Gaining the insurance benefits of a decesed family member.",
    "Reciprocal Agreement": "Allows regular workers' achievements and contributions in CARICOM countries are recognized across all countries.",
    "Invalidty Benefit": "An insurance benefit granted to those with the inability to work, whether because of illness, injury or disability",
}

def translate(msg):
    # 1. Take a whole sentence and chop it up into individual words.
    words = msg.split()
    
    # 2. Look up each word in our dictionary. If it's a jargon word, swap it. 
    # If it's a normal word, just keep it as-is! Then glue them back into a sentence.
    return " ".join(jargon_to_plain.get(w, w) for w in words)


# --- 💻 SYSTEMS DEVELOPER ROLE: The Checklist Runner ---
# A list of specific requirements or tasks your bot needs to check off.
requirements = ["Quick responses to user questions or statements", "Correct info in relations to topics", "Proper knowlegde output based on user needs"]

def check_all(reqs):
    # This loop goes through your checklist one item at a time.
    for r in reqs:
        # If the item isn't blank, print a checkmark. If it is blank, print an X!
        print("✓", r) if r != "" else print("✗ missing:", r)


# --- 📋 PRODUCT OWNER ROLE: Regional Rulebook ---
# A database mapping different business segments/islands to their specific rules. 
# It keeps track of the local currency (XCD) and who to alert if things get too complicated.
territory_rulebook = {
    "Mothers": {"currency": "XCD", "escalate_to": "Maternity Benefits"},
    "Widows": {"currency": "XCD", "escalate_to": "Survivors Benefits"},
}

def get_rules(segment):
    # Look up the territory rules. If we've never heard of this segment before, 
    # default to a generic backup rule so the system doesn't crash.
    return territory_rulebook.get(segment, {"currency": "XCD", "escalate_to": "human agent"})


# --- 🛠️ SCRUM MASTER ROLE: Testing Everything Out ---
# This simulates a test run to make sure all components of the bot are working smoothly.

# Test 1: See if the translation dictionary clears up a messy sentence
sample = "I need help with my Maternity Benefits today."
print("plain :", translate(sample))

# Test 2: Look up specific regional rules for Segment A
print("rules :", get_rules("Maternity Benefits"))

# Test 3: Run the automated checklist to see what requirements are done
check_all(requirements)




# DAY 5




# =====================================================
#   ECCU GAP Camp 2026 · WEEK 1 · DAY 5 SKELETON
#   Integrate — A.R.T. classify_and_route()
#   Integrates Day 1–4 modules. Runs unchanged.
# =====================================================

# This helps us declare what kind of data we expect (like a safety net for code!)
from typing import Optional

# -----------------------------------------------------
# 🎨 UX DESIGNER: Mood & Emoji Palette
# This section adds some personality! Depending on how the user 
# is feeling, it customizes how the bot replies to them.
# -----------------------------------------------------
tones = {
    "anxious": lambda t: f"{t} 💛",          # Adds a comforting heart emoji
    "formal":  lambda t: f"Dear user — {t}",   # Adds a polite greeting
    "urgent":  lambda t: f"{t.upper()} ⚡",    # Makes it UPPERCASE with a lightning bolt
}

# -----------------------------------------------------
# 🗣️ UX DESIGNER + PRODUCT OWNER: The Jargon Translator
# Nobody likes confusing corporate speak! This function acts like 
# Google Translate, swapping out heavy jargon for simple words.
# -----------------------------------------------------
jargon_to_plain = {"Maternity Benefits": "Pros for having a child as a mother."}

def translate(msg): 
    # Loops through the message word-by-word and swaps jargon for plain English
    return " ".join(jargon_to_plain.get(w, w) for w in msg.split())

# -----------------------------------------------------
# 🗺️ PRODUCT OWNER: The Territory Rulebook
# Maps users to the correct local support helpdesk based on where they are.
# -----------------------------------------------------
territory_rulebook = {
    "Insurance Prices": {"escalate_to": "Human Agent"},
    "Mothers": {"escalate_to": "Maternity Benefits"},
}

def get_territory(segment): 
    # Looks up the user's area in our rulebook map
    return territory_rulebook.get(segment)

# -----------------------------------------------------
# 🛡️ SCRUM MASTER: The "A.R.T." Security System
# These three functions act like security guards checking IDs 
# at a concert gate. We check Authority, Register (mood), and Territory!
# -----------------------------------------------------

# 1. Authority Check: Is this user logged in and verified?
def check_authority(user): 
    return "ok" if user.get("id_verified") else None

# 2. Register Check: Does the user's mood match one of our emojis?
def check_register(user):
    mood = user.get("mood")
    return mood if mood in tones else None

# 3. Territory Check: Do we know which region this user belongs to?
def check_territory(user): 
    return get_territory(user.get("segment"))

# -----------------------------------------------------
# 🚀 SYSTEMS DEVELOPER: The Master Controller
# This is the brain of our app. It puts Days 1–4 together.
# It checks the security guards, translates the text, and routes the user.
# -----------------------------------------------------
def classify_and_route(user, message):
    # Step 1: Run our three security checks (A.R.T.)
    a = check_authority(user)
    r = check_register(user)
    t = check_territory(user)
    
    # Step 2: If ANY of the three checks fail (return None), wave the red flag!
    if not (a and r and t):
        return "ESCALATING — will send you to a human agent shortly."
    
    # Step 3: If checks pass, translate the user's message to plain text
    plain = translate(message)
    
    # Step 4: Add the mood formatting and give them the final answer!
    return tones[r](f"Understood: {plain}. (Local desk: {t['escalate_to']})")

# -----------------------------------------------------
# 🎮 TEST ZONE: Let's try it out!
# -----------------------------------------------------
# Here is a fake user we are creating to test our code:
demo_user = {"id_verified": True, "mood": "anxious", "segment": "TODO_segment_A"}

# Let's see what the bot says when this user asks a question!
print(classify_and_route(demo_user, "I need help with my Maternity Benefits today."))





# Day 6; Sadly nothing in regards to the chatbot was done         









# Day 7




# =====================================================
# Eastern Caribbean Currency Union (ECCU) / Eastern Caribbean Central Bank (ECCB) 
# Generative AI & Python Summer Camp 2026 · WEEK 2 · DAY 7 SKELETON
#
# Prompt Engineering (Thoughtfully · Create · Really · Defined · Excellent · Inputs (TCRDEI)) + Axis 2 (Register)
# =====================================================

# User Experience (UX) DESIGNER (lead) — writes the register-specific system prompts (TCRDEI).
# SYSTEMS DEVELOPER (lead) — codes classify_register() — the Axis 2 router.
# PRODUCT OWNER (lead) — maps the Figma flow (visual, not in this file).

# TCRDEI mnemonic:
# T · Thoughtfully — Task: Bot Persona / Role / End-User Persona
# C · Create — Context: Environment / Pains / Ethical Considerations
# R · Really — References: few-shot examples of ideal dialogue
# D · Defined — Success: the exact expected "Gain"
# E · Excellent — Evaluate: check output vs. the Gain
# I · Inputs — Iterate: refine until it succeeds (ABI)

BOT_NAME = "Folad"

# --- SQUAD A (Prompt Engineers): TCRDEI-templated system prompts ---

PROMPT_TEMPLATE = """\
[T] You are {bot_name}, a {bot_role} serving {end_user_persona}.
[C] Context: {environment}. Known pains: {pains}. Ethical rule: {ethics}.
[R] Reference — example ideal response:
User: "{reference_user_line}"
Bot: "{reference_bot_line}"
[D] Success = the user feels "{expected_gain}".
[E] Before answering, check: does this satisfy [D]? If not, reroute.
[I] If the answer feels off, ask ONE clarifying question and iterate.
Register: {register}. Never break the central rule: the bot is the GPS; the human is the driver.
"""

def make_prompt(register: str, **kw) -> str:
    defaults = dict(
        bot_name=BOT_NAME,
        bot_role="NIS Grenadian bot, used as an assistant to deal with people's simple insurance claims.",
        end_user_persona="A Grenadian citizen who is trying to claim their insurance benefits",
        environment="Grenada, Eastern Caribbean",
        pains="Despair, Stress, Confusion, Anguish, Grief, Fear, Uncertainty, and Doubt.",
        ethics="You NEVER quote specific prices, guarantee contract terms, or discuss internal employee data. Instead say: 'Let me connect you with our sales team — they can build a custom quote for your needs.'",
        reference_user_line="My mother has sadly passed away but told me about a term called survivors benefits beforehand. What is it, and how do I claim it?",
        reference_bot_line="I'm so sorry to hear about your mother. Survivors Benefits are insurance benefits granted to those who have lost a family member. ",
        expected_gain="Warmth, Heard, Cared for, Peace of Mind and Clarity on the next step.",
        register=register,
    )
    defaults.update(kw)
    return PROMPT_TEMPLATE.format(**defaults)

PROMPT_LIBRARY = {
    "warm": make_prompt("warm"),
    "professional": make_prompt("professional"),
    "urgent": make_prompt("urgent"),
    # Care-first register (highest-emotional-risk) — condolences BEFORE information, always
    "bereaved": make_prompt("bereaved",
                            expected_gain="acknowledged first, then informed"),
}

# --- SQUAD B (Engineers): Axis 2 — classify_register ---------------

GRIEF_WORDS = {"passed away", "died", "funeral", "loss", "mourning"}
URGENT_WORDS = {"now", "asap", "urgent", "emergency", "today"}
FORMAL_WORDS = {"regarding", "hereby", "kindly", "please advise"}

def classify_register(msg: str) -> str:
    m = msg.lower()
    if any(w in m for w in GRIEF_WORDS): return "bereaved"
    if any(w in m for w in URGENT_WORDS): return "urgent"
    if any(w in m for w in FORMAL_WORDS): return "professional"
    return "warm"

def compose_system_prompt(msg: str) -> str:
    reg = classify_register(msg)
    return PROMPT_LIBRARY[reg]

# --- Demo -----------------------------------------------------------

if __name__ == "__main__":
    samples = [
        "My father passed away last month, how do I claim survivor benefits?",
        "I need to apply for a permit ASAP.",
        "Kindly advise on the eligibility rules.",
        "Hi, can you help me?",
    ]
    
    for s in samples:
        r = classify_register(s)
        print(f"[{r:>13}] {s}")

        
