from chatterbot import ChatBot
from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot("ChatBot")
app = Flask(__name__)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "How old are you?",
    "I don't have an age.",
    "What can you do?",
    "I can answer questions, provide information, and have conversations with you.",
    "What's the weather like today?",
    "I'm sorry, I don't have access to real-time weather information.",
    "What's the meaning of life?",
    "That's a difficult question. There are many different answers depending on who you ask.",
    "Do you like pizza?",
    "I don't have a physical body, so I can't eat pizza. But I know many people enjoy it!",
    "Can you tell me a joke?",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What's the capital of France?",
    "The capital of France is Paris.",
    "What's the largest animal on Earth?",
    "The largest animal on Earth is the blue whale.",
    "What's the most populous country in the world?",
    "The most populous country in the world is China.",
    "What's the tallest mountain in the world?",
    "The tallest mountain in the world is Mount Everest.",
    "What should I pack for a tropical vacation?",
    "Light clothing, sunscreen, sunglasses, hat, swimwear, and insect repellent.",
  
    "How can I find cheap flights?",
    "Use flight comparison websites, book in advance, and be flexible with dates.",
  
    "What is the best way to exchange currency?",
    "Use local ATMs, exchange at banks, or use currency exchange services.",
  
    "How do I keep my valuables safe while traveling?",
    "Use a money belt, lock your luggage, and store valuables in a hotel safe.",
  
    "What is the best way to travel around Europe?",
    "Train travel is popular and efficient; consider the Eurail pass.",
  
    "How do I choose the right travel insurance?",
    "Compare policies based on coverage, price, and customer reviews.",
  
    "What are some tips for traveling with kids?",
    "Pack snacks, bring entertainment, plan breaks, and choose kid-friendly accommodations.",
  
    "How can I avoid jet lag?",
    "Stay hydrated, adjust to the new time zone gradually, and get plenty of sleep before traveling.",
  
    "What is the best way to book accommodations?",
    "Use hotel booking websites, read reviews, and compare prices.",
  
    "How do I stay healthy while traveling?",
    "Drink bottled water, eat at reputable places, and wash your hands frequently.",
  
    "What is the best way to travel around Asia?",
    "Consider budget airlines, trains, and buses.",
  
    "How do I handle a lost passport while traveling?",
    "Report it to the local authorities and contact your embassy.",
  
    "What are some essential items for a long flight?",
    "Neck pillow, earplugs, eye mask, snacks, and a good book.",
  
    "How can I save money while traveling?",
    "Travel during off-peak seasons, use public transportation, and eat at local markets.",
  
    "What should I do in case of a medical emergency abroad?",
    "Contact local emergency services and inform your travel insurance provider.",
  
    "What is the best way to learn about local customs?",
    "Research beforehand, observe locals, and ask politely.",
  
    "How can I avoid tourist scams?",
    "Be cautious of overly friendly strangers, avoid unlicensed guides, and don't flash valuables.",
  
    "What are some tips for solo travelers?",
    "Stay in well-reviewed accommodations, stay connected with family, and trust your instincts.",
  
    "How do I choose the best travel backpack?",
    "Look for comfort, durability, size, and features like multiple compartments.",
  
    "What should I do if my flight is canceled?",
    "Contact the airline, inquire about rebooking options, and understand your rights.",
  
    "How do I use public transportation in a new city?",
    "Research routes and schedules, buy tickets in advance, and ask locals for help.",
  
    "What are the benefits of group tours?",
    "They offer convenience, safety, and the opportunity to meet new people.",
  
    "How can I find reliable travel information?",
    "Use reputable travel websites, guidebooks, and travel blogs.",
  
    "What is the best way to handle travel fatigue?",
    "Take regular breaks, stay hydrated, and get plenty of rest.",
  
    "How do I avoid overpacking?",
    "Make a packing list, choose versatile clothing, and pack only essentials.",
  
    "What are some tips for booking last-minute travel?",
    "Use last-minute deal websites, be flexible with your plans, and check multiple sources.",
  
    "How can I stay connected with family while traveling?",
    "Use international SIM cards, messaging apps, and Wi-Fi.",
  
    "What are some tips for traveling in a foreign language country?",
    "Learn basic phrases, use translation apps, and be patient.",
  
    "How do I navigate a foreign city?",
    "Use maps, GPS, and ask locals for directions.",
  
    "What is the best way to experience local culture?",
    "Attend local events, visit markets, and interact with residents.",
  
    "How do I choose the right travel credit card?",
    "Look for cards with travel rewards, no foreign transaction fees, and good customer service.",
  
    "What should I do if I miss my flight?",
    "Contact the airline immediately and ask about rebooking options.",
  
    "How can I make the most of a layover?",
    "Explore the airport, visit a lounge, or take a quick city tour if time allows.",
  
    "What are some tips for eco-friendly travel?",
    "Choose sustainable accommodations, minimize waste, and support local businesses.",
  
    "How do I prepare for a road trip?",
    "Plan your route, check your vehicle, and pack snacks and entertainment.",
  
    "What should I know about travel vaccinations?",
    "Consult with a healthcare provider, get recommended shots, and carry your vaccination record.",
  
    "How can I find good restaurants while traveling?",
    "Use review websites, ask locals, and explore food markets.",
  
    "What are some safety tips for hiking trips?",
     "Stay on marked trails, carry a map, and bring plenty of water and a first aid kit.",
  
    "How do I manage travel expenses?",
    "Set a budget, track your spending, and use travel-friendly banking options.",
  
    "What is the best way to handle language barriers?",
    "Use body language, translation apps, and learn key phrases.",
  
    "How do I plan a multi-city trip?",
    "Use multi-destination booking tools, plan your itinerary carefully, and consider travel times.",
  
    "What are some tips for traveling during peak seasons?",
    "Book in advance, be prepared for crowds, and visit popular sites early or late in the day.",
  
    "How can I ensure my hotel is safe?",
    "Check reviews, choose well-located properties, and use room locks.",
  
    "What should I do if I get sick while traveling?",
    "Visit a local clinic or hospital, use travel insurance, and rest as needed.",
  
    "How do I stay organized while traveling?",
    "Use packing cubes, keep important documents together, and use travel apps for itineraries.",
  
    "What are the advantages of using a travel agent?",
    "They offer expert advice, handle bookings, and provide support if issues arise.",
  
    "How do I avoid getting lost in a new place?",
    "Use maps, GPS, and stay aware of your surroundings.",
  
    "What are some tips for traveling on a budget?",
    "Stay in hostels, cook your own meals, and use public transportation.",
  
    "How can I make friends while traveling?",
    "Stay in social accommodations, join group activities, and be open to meeting new people.",
  
    "What should I know about tipping in different countries?",
    "Research local customs, carry small bills, and tip appropriately.",
  
    "How do I find hidden gems in a destination?",
    "Ask locals, explore beyond tourist areas, and use travel forums.",
  
    "What are some tips for beach vacations?",
    "Bring sunscreen, stay hydrated, and watch for safety flags.",
  
    "How do I handle travel delays?",
    "Stay calm, contact your airline, and have a backup plan.",
  
    "What should I do if I lose my luggage?",
    "Report it to the airline, keep receipts, and use travel insurance if needed.",
  
    "How do I choose the right travel guidebook?",
    "Look for recent editions, detailed maps, and comprehensive information.",
  
    "What are some tips for avoiding travel burnout?",
    "Take rest days, limit your itinerary, and enjoy downtime.",
  
    "How can I find the best travel deals?",
    "Sign up for newsletters, use deal websites, and book during sales.",
  
    "What should I consider when renting a car?",
    "Check insurance options, read rental agreements, and inspect the car before driving.",
  
    "How do I stay safe while traveling at night?",
    "Stick to well-lit areas, avoid isolated places, and travel with others if possible.",
  
    "What are some essential travel apps?",
    "Google Maps, TripAdvisor, Airbnb, and language translation apps.",
  
    "How do I deal with travel-related stress?",
    "Practice relaxation techniques, stay organized, and take breaks.",
  
    "What should I do if my travel plans change?",
    "Contact service providers, check cancellation policies, and rebook if necessary.",
  
    "How can I travel sustainably?",
    "Use eco-friendly transportation, support local businesses, and reduce waste.",
  
    "What are some tips for planning a trip itinerary?",
    "Prioritize must-see sites, allow for flexibility, and include rest time.",
  
    "How do I stay fit while traveling?",
    "Use hotel gyms, walk or bike around the city, and do bodyweight exercises.",
  
    "What should I know about travel etiquette?",
    "Respect local customs, dress appropriately, and be polite.",
  
    "How do I choose the best travel backpack?",
    "Look for durability, comfort, and the right size for your needs.",
  
    "What are some tips for traveling during the holidays?",
    "Book early, prepare for crowds, and enjoy local festivities.",
  
    "How do I handle homesickness while traveling?",
    "Stay in touch with loved ones, bring a comfort item, and stay busy with activities.",
  
    "What should I know about using travel rewards points?",
    "Understand the redemption process, look for blackout dates, and maximize value.",
  
    "What should I know about travel rewards points?",
    "Understand the redemption process, look for blackout dates, and maximize value.",
  
    "How can I stay cool in hot climates?",
    "Wear light clothing, stay hydrated, and avoid the sun during peak hours.",
  
    "What are some tips for cultural immersion in India?",
    "Learn about regional customs and traditions, participate in local festivals, and try authentic Indian cuisine.",
  
    "What are some must-try dishes in India?",
    "Biryani: fragrant rice dish with spices and meat/vegetables; Dosa: thin, crispy crepe served with chutney and sambar; Chaat: savory snacks like pani puri, bhel puri, and aloo tikki; Tandoori: marinated meats/vegetables cooked in a clay oven.",
  
    "How do I experience Indian street food safely?",
    "Choose busy stalls with high turnover, ensure food is freshly prepared and cooked thoroughly, and avoid tap water or ice in drinks.",
  
     "What are some cultural experiences in India?",
    "Attend festivals like Diwali (Festival of Lights) and Holi (Festival of Colors), visit historical sites such as the Taj Mahal and Jaipur's forts, explore traditional arts like Bharatanatyam (classical dance) and Kathak (storytelling through dance).",
  
    "How can I navigate India's diverse cultural norms?",
    "Respect local customs such as removing shoes before entering homes or temples, covering shoulders and legs in religious sites, and greeting with a 'namaste' (palms together, slight bow).",
  
    "What should I know about Indian hospitality?",
    "Expect warm welcomes and generous hospitality from locals; it's customary to offer guests food and refreshments.",
  
    "How do I respect religious sites in India?",
    "Follow dress codes (cover shoulders, no shorts), remove shoes before entering temples, and be mindful of photography restrictions.",
  
    "What are some traditional arts and crafts to explore in India?",
    "Textiles: sarees, silk weaving; Handicrafts: pottery, metalwork, woodcarving; Performing Arts: classical dance, music like sitar and tabla; Folk Art: Madhubani paintings, Warli art.",
  
    "How do I explore Indian spirituality?",
    "Visit spiritual centers like Varanasi (for Ganga Aarti), Rishikesh (yoga and meditation), and temples dedicated to various gods and goddesses.",
  
    "What are some eco-friendly travel options in India?",
    "Choose eco-friendly accommodations, support sustainable tour operators, and participate in community-based tourism initiatives.",
  
    "How can I learn basic Hindi phrases for travel?",
    "Learn greetings (namaste), thank you (dhanyavaad), and basic questions (kya hai? - What is this?) to facilitate interactions with locals.",
  
    "What should I know about Indian festivals?",
    "They often involve music, dance, and elaborate rituals; popular festivals include Diwali, Holi, Eid, and Christmas celebrated with local flavors.",
  
    "How can I explore India's wildlife responsibly?",
    "Visit national parks and wildlife reserves known for tiger safaris (like Ranthambore), elephant sanctuaries (like Jaipur), and birdwatching sites (like Bharatpur).",
  
    "What are some etiquette tips for dining in India?",
    "Wash hands before and after meals, eat with your right hand (traditionally), and try to finish what's served as a sign of respect.",
  
    "How can I experience India's diverse music traditions?",
    "Attend classical concerts (Carnatic or Hindustani), folk music performances, and Bollywood music shows in major cities.",
  
    "What are some iconic landmarks to visit in India?",
    "Taj Mahal (Agra), Red Fort (Delhi), Amber Fort (Jaipur), Gateway of India (Mumbai), and Meenakshi Temple (Madurai).",
  
    "How do I shop responsibly in India?",
    "Support local artisans at craft markets, bargain respectfully, and avoid purchasing items made from endangered species or cultural artifacts without proper certification."

]


trainer = ListTrainer(chatbot)
trainer.train(conversation)
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(chatbot.get_response(userText))


app.run(debug=True)
