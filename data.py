import pandas as pd

data = {
    "comment": [
        # Praise (13)
        "Amazing animation, I loved it!",
        "You guys rock!",
        "Beautiful design!",
        "Top-notch work!",
        "Superb effort, well done!",
        "Absolutely brilliant!",
        "Visuals are fantastic!",
        "Great attention to detail!",
        "That blew my mind!",
        "Perfect execution!",
        "This is next-level!",
        "Really impressed!",
        "So creative!",

        # Support (13)
        "Keep up the good work!",
        "You're improving a lot, keep going.",
        "Don't give up!",
        "I see potential in your work.",
        "Keep pushing, you'll get better!",
        "You're doing great!",
        "Looking forward to more from you.",
        "Never stop creating!",
        "We believe in you!",
        "Go for it!",
        "Take your time, we’ll wait!",
        "Progress over perfection.",
        "This is just the beginning!",

        # Constructive Criticism (13)
        "The idea is good, but execution needs improvement.",
        "Audio was not great but loved the visuals.",
        "Maybe try using less text next time.",
        "Timing felt a bit off.",
        "I liked it, but pacing could be improved.",
        "Try smoother transitions.",
        "Sound mix could be cleaner.",
        "Consider shortening the intro.",
        "Color grading needs a bit of work.",
        "Could use a better voiceover.",
        "Too much going on, simplify it.",
        "Would be better with background music.",
        "Some parts felt repetitive.",

        # Hate/Abuse (13)
        "This is trash content.",
        "Shut this down!",
        "You're terrible at this.",
        "Who even asked for this?",
        "Total garbage.",
        "Please stop making videos.",
        "Worst thing I’ve seen.",
        "Just quit already.",
        "Completely talentless.",
        "Can't believe I wasted my time.",
        "This sucks so much.",
        "No skill, no effort.",
        "So cringe, get a life.",

        # Threat (10)
        "I’ll report this if I see it again.",
        "This better be your last post like this.",
        "You’ll regret uploading this.",
        "I’ll shut your page down.",
        "Stop or there will be consequences.",
        "I’m blocking and reporting you.",
        "Next time, I’m emailing the platform.",
        "Prepare for backlash.",
        "You’re crossing the line.",
        "I’ll hack your account if you don’t stop.",

        # Emotional (13)
        "This reminded me of my childhood days.",
        "I’m in tears, this touched me deeply.",
        "So many memories flooding back!",
        "This made me smile after a rough day.",
        "I connected with this emotionally.",
        "Took me back to simpler times.",
        "What a comforting piece of art.",
        "This made me think of my mom.",
        "Such a warm feeling watching this.",
        "This healed a part of me.",
        "Brought tears to my eyes.",
        "Incredible emotional depth.",
        "Felt every second of this.",

        # Irrelevant/Spam (13)
        "Buy cheap followers at xyz.com",
        "Follow me for more followers!",
        "Click my bio to get rich!",
        "Promo codes available at my site!",
        "DM me for collab!",
        "Check my latest post for secrets!",
        "Earn money fast now!",
        "Get 10k followers today!",
        "Spammy content alert!",
        "Visit xyz.biz for surprise!",
        "Win free iPhones, just follow!",
        "Subscribe to my channel now!",
        "Don’t miss this crypto tip!",

        # Question/Suggestion (12)
        "Can you make a video on meditation?",
        "What tools did you use for this?",
        "Could you do a behind-the-scenes?",
        "Can you explain the concept more?",
        "Would love to see a part 2!",
        "Have you thought of animating X?",
        "Can you cover topic Y next?",
        "Will you do a tutorial on this?",
        "Would be great if you added subtitles.",
        "Can this be done in black & white?",
        "Can you do this for mobile users too?",
        "Suggestion: add captions for clarity."
    ],
    "label": [
        *["Praise"] * 13,
        *["Support"] * 13,
        *["Constructive Criticism"] * 13,
        *["Hate/Abuse"] * 13,
        *["Threat"] * 10,
        *["Emotional"] * 13,
        *["Irrelevant/Spam"] * 13,
        *["Question/Suggestion"] * 12,
    ]
}

df = pd.DataFrame(data)
df.to_csv("data/raw_comments.csv", index=False)
print("✅ Full dataset of 100 comments saved at data/raw_comments.csv")
