import streamlit as st
from google import genai

# Setup the page layout
st.set_page_config(page_title="Andromeda Ad Angle Generator", page_icon="🎥", layout="centered")

st.title("🎥 Andromeda Ad Angle Generator")
st.write("Generate 10 conceptually diverse video hooks optimized for Meta's Andromeda algorithm.")

# Securely grab the API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

# The UI Inputs
product_name = st.text_input("Product Name (e.g., CGS Authentic Gold Necklace)")
product_details = st.text_area("Product Details & Offer (e.g., 18k gold, pawnable, 50% off via Messenger)")

# The hidden system prompt
system_instruction = """
You are an elite Meta Ads Creative Director. When given a product and offer, generate 10 DISTINCT video ad angles. 
Each must have a different psychological approach (e.g., emotional, logical, visual).
For each angle provide:
1. Angle Name
2. Visual Hook (First 3 seconds): Highly detailed, hyper-realistic cinematic layout instructions. 
3. Voiceover / On-Screen Text script.
4. Call to Action: Explicitly direct users to click the button below for automated messaging.
CRITICAL CONSTRAINTS: 
- ALWAYS emphasize "Cash on Delivery" and "Free Shipping".
- NEVER use "Buy 1 Take 1". 
- Do NOT generate actual video files, only text mockups.
"""

if st.button("Generate 10 Ad Angles"):
    if not product_name:
        st.warning("Please enter a product name.")
    else:
        with st.spinner("Analyzing algorithm and generating angles..."):
            prompt = f"System Instructions: {system_instruction}\n\nProduct Name: {product_name}\nDetails & Offer: {product_details}"
            
            # Call the free Gemini AI model using the new SDK
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            
            st.success("Angles Generated!")
            st.markdown(response.text)
