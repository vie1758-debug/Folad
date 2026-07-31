"""
Folad — NIS Grenada Assistant
A Streamlit app built from the ECCU GAP Camp 2026 chatbot exercises.

Deploy on Streamlit Community Cloud:
1. Push this file + requirements.txt to your GitHub repo (root, or note the
   subfolder path when you deploy).
2. On https://share.streamlit.io, click "New app", pick the repo/branch,
   and set "Main file path" to app.py.
3. (Optional) In the app's Settings -> Secrets, add:
       OPENAI_API_KEY = "sk-..."
   if you want real AI replies instead of the built-in stub.
"""

import streamlit as st

# ---------------------------------------------------------------------
# PAGE CONFIG — must be the first Streamlit call in the script
# ---------------------------------------------------------------------
st.set_page_config(page_title="Folad — NIS Grenada Assistant", page_icon="🤖", layout="centered")

BOT_NAME = "Folad"

# =====================================================================
# 🎨 UX DESIGNER: Register tones (Day 3 / Day 7)
# =====================================================================
tones = {
    "anxious": lambda t: f"{t} 💛",
    "warm": lambda t: f"{t} 💛",
    "formal": lambda t: f"Dear user — {t}",
    "professional": lambda t: f"Dear user — {t}",
    "urgent": lambda t: f"{t.upper()} ⚡",
    "bereaved": lambda t: f"{t}",  # gentleness comes from the wording itself, not styling
}

# =====================================================================
# 🗣️ Jargon translator (Day 4 / Day 5)
# =====================================================================
jargon_to_plain = {
    "Maternity": "financial support for having a child as a mother",
    "Survivors": "insurance benefits granted to those who lost a family member",
    "Reciprocal": "an agreement that lets your work contributions count across CARICOM countries",
    "Invalidity": "an insurance benefit for those unable to work due to illness, injury, or disability",
}

def translate(msg: str) -> str:
    words = msg.split()
    return " ".join(jargon_to_plain.get(w.strip(",."), w) for w in words)

# =====================================================================
# 🗺️ Territory rulebook (Day 4 / Day 5)
# =====================================================================
territory_rulebook = {
    "Mothers": {"currency": "XCD", "escalate_to": "Maternity Benefits desk"},
    "Widows": {"currency": "XCD", "escalate_to": "Survivors Benefits desk"},
    "General": {"currency": "XCD", "escalate_to": "General Enquiries desk"},
}

def get_rules(segment: str) -> dict:
    return territory_rulebook.get(segment, {"currency": "XCD", "escalate_to": "a human agent"})

# =====================================================================
# 🛡️ A.R.T. classifier — Authority, Register, Territory (Day 5)
# =====================================================================
GRIEF_WORDS = {"passed away", "died", "funeral", "loss", "mourning"}
URGENT_WORDS = {"now", "asap", "urgent", "emergency", "today"}
FORMAL_WORDS = {"regarding", "hereby", "kindly", "please advise"}
CASE_SPECIFIC_PHRASES = {"my case", "my claim", "my status", "am i eligible", "my payment"}

def classify_register(msg: str) -> str:
    m = msg.lower()
    if any(w in m for w in GRIEF_WORDS):
        return "bereaved"
    if any(w in m for w in URGENT_WORDS):
        return "urgent"
    if any(w in m for w in FORMAL_WORDS):
        return "professional"
    return "warm"

def is_case_specific(msg: str) -> bool:
    m = msg.lower()
    return any(p in m for p in CASE_SPECIFIC_PHRASES)

def classify_and_route(id_verified: bool, segment: str, message: str) -> str:
    # Authority check: never answer case-specific questions without verified ID
    if is_case_specific(message) and not id_verified:
        return "ESCALATING — this needs a verified human agent to check your specific case."

    register = classify_register(message)
    rules = get_rules(segment)
    plain = translate(message)
    tone_fn = tones.get(register, lambda t: t)

    reply_core = f"Understood: {plain}. (Local desk: {rules['escalate_to']})"
    if register == "bereaved":
        reply_core = f"I'm so sorry for your loss. {reply_core}"

    return tone_fn(reply_core)

# =====================================================================
# 🤖 Optional AI backend (Day 8) — falls back to a stub if no API key
# =====================================================================
def llm_call(system_prompt: str, user_msg: str) -> str:
    api_key = st.secrets.get("OPENAI_API_KEY", None)
    if not api_key:
        return None  # signal: no key configured, use the rule-based reply instead
    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.4,
        )
        return r.choices[0].message.content
    except Exception as e:
        return f"[API error — falling back to rule-based reply] {e}"

SYSTEM_PROMPT = (
    f"You are {BOT_NAME}, an NIS Grenada assistant helping people with simple "
    "insurance questions (maternity, survivors, invalidity benefits). "
    "Never quote specific prices or guarantee contract terms. "
    "Always escalate case-specific questions to a human agent. "
    "Be warm, clear, and use plain language, not jargon."
)

# =====================================================================
# 🚀 STREAMLIT UI — this replaces the old input()/while-True loop
# =====================================================================
st.title(f"🤖 {BOT_NAME}")
st.caption("NIS Grenada Assistant — demo built from the ECCU GAP Camp exercises")

with st.sidebar:
    st.header("User context")
    id_verified = st.checkbox("ID verified", value=True)
    segment = st.selectbox("Segment", list(territory_rulebook.keys()))
    use_ai = st.checkbox("Use AI backend if available", value=True)
    st.caption("Set OPENAI_API_KEY in Secrets to enable real AI replies.")

# Keep chat history across reruns using session_state (Streamlit's replacement
# for a blocking while-True loop)
if "history" not in st.session_state:
    st.session_state.history = []

for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

user_msg = st.chat_input("How can I help you today?")

if user_msg:
    st.session_state.history.append(("user", user_msg))
    with st.chat_message("user"):
        st.write(user_msg)

    reply = None
    if use_ai:
        reply = llm_call(SYSTEM_PROMPT, user_msg)

    if not reply:  # no AI key, or AI call skipped -> rule-based A.R.T. reply
        reply = classify_and_route(id_verified, segment, user_msg)

    st.session_state.history.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.write(reply)
