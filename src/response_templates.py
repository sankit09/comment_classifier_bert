RESPONSE_TEMPLATES = {
    "Praise": "Thanks so much for your kind words! 🙌",
    "Support": "We appreciate your support and encouragement. ❤️",
    "Constructive Criticism": "Thank you for the honest feedback! We'll work to improve. 💡",
    "Hate/Abuse": "We’re here to foster respectful conversations. Your feedback has been noted.",
    "Threat": "This type of comment is serious. Our team has been alerted. 🚨",
    "Emotional": "We’re touched that this resonated with you. Thank you for sharing. 🤗",
    "Irrelevant/Spam": "Thanks for your interest! However, we ask users to avoid off-topic promotions.",
    "Question/Suggestion": "Great question/suggestion! We’ll pass it to the team. 💭"
}

def generate_response(category):
    return RESPONSE_TEMPLATES.get(category, "Thank you for your comment!")
