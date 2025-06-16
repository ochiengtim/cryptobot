 # chatbot.py

from crypto_data import crypto_db

bot_name = "CryptoBuddy"
bot_intro = "🌱 Hey there, I’m CryptoBuddy! Let’s find you a green and growing crypto. Type 'exit' to leave."

def get_user_input():
    return input("You: ").lower()

def respond_to_query(query):
    if "sustainable" in query:
        recommended = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌿 Invest in {recommended}! It’s eco-friendly and has long-term potential."

    elif "trending" in query or "rising" in query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"📈 These cryptos are trending up: {', '.join(trending)}."

    elif "most sustainable" in query:
        top = sorted(crypto_db.items(), key=lambda item: item[1]["sustainability_score"], reverse=True)[0][0]
        return f"🌍 {top} is the most sustainable crypto right now!"

    elif "long-term" in query or "growth" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"🚀 {coin} is rising and sustainable! A great long-term choice."
        return "🤷 No perfect match for long-term growth right now."

    elif "profit" in query or "profitable" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"💰 {coin} is profitable with rising prices and high market cap."
        return "📉 Hmm, none seem highly profitable right now."

    elif "recommend" in query or "should i buy" in query:
        recommendations = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                recommendations.append(coin)
        if recommendations:
            return f"🧠 Consider these: {', '.join(recommendations)}"
        return "😕 Nothing meets all the good conditions right now."

    else:
        return "❓ I didn't get that. Ask me about 'sustainable' or 'profitable' cryptos!"

def disclaimer():
    print("⚠️ Disclaimer: Crypto is risky. Always do your own research (DYOR).")

def chat():
    print(f"{bot_name}: {bot_intro}")
    disclaimer()
    while True:
        user_query = get_user_input()
        if user_query in ["exit", "quit", "bye"]:
            print(f"{bot_name}: 👋 Take care and stay green!")
            break
        response = respond_to_query(user_query)
        print(f"{bot_name}: {response}")

# Start chat
if __name__ == "__main__":
    chat()

