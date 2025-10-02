from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined FAQs
faq_data = {
    "What is your return policy?": "You can return any item within 30 days for a full refund.",
    "How long does shipping take?": "Shipping typically takes 5-7 business days.",
    "Do you offer customer support?": "Yes, our customer support is available 24/7.",
    "What payment methods do you accept?": "We accept all major credit cards and PayPal.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email."
}

@app.route('/faq', methods=['POST'])
def faq():
    user_query = request.json.get('query')
    response = "I'm sorry, I don't have an answer for that."

    # Check if the user's query matches any FAQ
    for question, answer in faq_data.items():
        if user_query.lower() in question.lower():
            response = answer
            break
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
