# Securely grab the API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
from google import genai
client = genai.Client(api_key=api_key)

# ... (keep your UI inputs and system_instruction the same) ...

if st.button("Generate 10 Ad Angles"):
    if not product_name:
        st.warning("Please enter a product name.")
    else:
        with st.spinner("Analyzing algorithm and generating angles..."):
            prompt = f"System Instructions: {system_instruction}\n\nProduct Name: {product_name}\nDetails & Offer: {product_details}"
            
            # Call the new updated client
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            
            st.success("Angles Generated!")
            st.markdown(response.text)
