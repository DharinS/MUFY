import streamlit as st
import random

# 🍽️ Global Recipes Dictionary
recipes = {
    # Meals
    '🍕': {
        'category': 'Meals',
        'name': 'Pizza',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg',
        'ingredients': ['1 pizza dough', '1/2 cup tomato sauce', '1 cup shredded mozzarella', 'Toppings of your choice'],
        'steps': ['Preheat oven to 220°C (425°F).', 'Spread tomato sauce on the dough.', 'Add cheese and toppings.', 'Bake for 15–20 minutes until golden.'],
        'instructions': "Roll out dough, add sauce and toppings, then bake until golden and bubbling.",
        'time': '30 mins',
        'difficulty': 'Easy',
        'calories': '500 kcal'
    },
    '🌮': {
        'category': 'Meals',
        'name': 'Tacos',
        'image_url': 'https://malaysia.images.search.yahoo.com/search/images;_ylt=AwrKBPV4IjdoKQIANiPjPwx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=jpj+of+a+taco&fr2=piv-web&fr=mcafee-malaysia#id=0&iurl=https%3A%2F%2Fimages3.alphacoders.com%2F248%2F248457.jpg&action=click',
        'ingredients': ['Taco shells', 'Cooked ground beef or beans', 'Shredded cheese', 'Lettuce, salsa, sour cream'],
        'steps': ['Heat taco shells.', 'Fill with meat or beans.', 'Top with cheese, lettuce, salsa.', 'Add sour cream.'],
        'instructions': "Prepare filling, load tacos, and serve with toppings.",
        'time': '20 mins',
        'difficulty': 'Easy',
        'calories': '350 kcal'
    },
    '🍔': {
        'category': 'Meals',
        'name': 'Cheeseburger',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/RedDot_Burger.jpg',
        'ingredients': ['1 bun', '1 beef patty', '1 slice cheese', 'Lettuce, tomato', 'Ketchup, mustard'],
        'steps': ['Grill patty.', 'Toast bun.', 'Assemble with cheese and toppings.'],
        'instructions': "Grill, stack, and serve hot.",
        'time': '25 mins',
        'difficulty': 'Medium',
        'calories': '600 kcal'
    },
    '🍜': {
        'category': 'Meals',
        'name': 'Char Kway Teow',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Char_kway_teow.jpg',
        'ingredients': ['Flat rice noodles', 'Prawns', 'Chinese sausage', 'Bean sprouts', 'Eggs', 'Chives', 'Soy sauce', 'Chili paste'],
        'steps': ['Heat oil in a wok.', 'Add prawns and sausage, stir-fry.', 'Add eggs and scramble.', 'Toss in noodles, soy sauce, and chili.', 'Add bean sprouts and chives, stir-fry quickly.'],
        'instructions': "Use high heat and stir-fry quickly for the perfect smoky Char Kway Teow.",
        'time': '25 mins',
        'difficulty': 'Hard',
        'calories': '700 kcal'
    },
    '🍛': {
        'category': 'Meals',
        'name': 'Nasi Lemak',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Nasi_Lemak_Malaysia.jpg',
        'ingredients': ['Coconut rice', 'Fried anchovies', 'Boiled egg', 'Sambal', 'Cucumber slices', 'Peanuts'],
        'steps': ['Cook rice in coconut milk.', 'Prepare sambal and fry anchovies.', 'Plate with egg, cucumber, and peanuts.'],
        'instructions': "A Malaysian national dish. Spicy, creamy, and balanced.",
        'time': '45 mins',
        'difficulty': 'Medium',
        'calories': '650 kcal'
    },
    '🍢': {
        'category': 'Meals',
        'name': 'Satay Skewers',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/08/Satay.JPG',
        'ingredients': ['Chicken or beef', 'Satay marinade', 'Peanut sauce', 'Skewers'],
        'steps': ['Marinate meat.', 'Thread onto skewers.', 'Grill until charred.', 'Serve with peanut sauce.'],
        'instructions': "Sweet and savory skewers perfect with spicy peanut sauce.",
        'time': '35 mins',
        'difficulty': 'Medium',
        'calories': '450 kcal'
    },

    # Fruits
    '🍎': {
        'category': 'Fruits',
        'name': 'Apple Snack',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg',
        'ingredients': ['1 fresh apple', 'Peanut butter or caramel (optional)'],
        'steps': ['Wash and slice apple.', 'Add dip if desired.'],
        'instructions': "A crisp and refreshing snack.",
        'time': '5 mins',
        'difficulty': 'Very Easy',
        'calories': '95 kcal'
    },
    '🍌': {
        'category': 'Fruits',
        'name': 'Banana Smoothie',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana_Smoothie.jpg',
        'ingredients': ['1 banana', '1 cup milk (or almond milk)', '1 tsp honey'],
        'steps': ['Blend all ingredients until smooth.', 'Serve chilled.'],
        'instructions': "A creamy, healthy smoothie in 2 minutes.",
        'time': '2 mins',
        'difficulty': 'Very Easy',
        'calories': '120 kcal'
    },
    '🍓': {
        'category': 'Fruits',
        'name': 'Strawberry Delight',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/29/PerfectStrawberry.jpg',
        'ingredients': ['1 cup strawberries', '1 tbsp sugar or cream'],
        'steps': ['Rinse and trim stems.', 'Serve plain or with sugar/cream.'],
        'instructions': "Sweet, tart, and always refreshing.",
        'time': '5 mins',
        'difficulty': 'Easy',
        'calories': '50 kcal'
    }
}

def get_recipe(emoji):
    return recipes.get(emoji)

# 🌐 Streamlit UI
st.set_page_config(page_title="Emoji Recipe App 🍴", page_icon="🍽️")

st.title("🍽️ Emoji Recipe Finder")
st.markdown("Choose or type a food emoji to get a quick recipe or snack idea!")

# ⬇️ Category Filter
category = st.radio("Filter by category:", ["All", "Meals", "Fruits"])

# 🔍 Filter recipe list based on category
if category == "All":
    filtered_recipes = recipes
else:
    filtered_recipes = {k: v for k, v in recipes.items() if v['category'] == category}

# 😃 Emoji Selection
use_text_input = st.checkbox("Prefer to type emoji instead")

if use_text_input:
    emoji_input = st.text_input("🖊️ Enter emoji:").strip()
else:
    emoji_input = st.selectbox("Choose an emoji:", list(filtered_recipes.keys()))

# 🎲 Random Recipe Button
if st.button("🎲 Surprise Me!"):
    emoji_input = random.choice(list(filtered_recipes.keys()))
    st.success(f"Randomly selected: {emoji_input}")

# 🍝 Display Recipe
recipe = get_recipe(emoji_input)
if recipe:
    st.header(f"{emoji_input} {recipe['name']}")

    if 'image_url' in recipe:
       st.image(recipe['image_url'], use_container_width=True)


    st.markdown(f"**⏱️ Time**: {recipe['time']} | **🔥 Difficulty**: {recipe['difficulty']} | **🍽️ Calories**: {recipe['calories']}")

    st.subheader("🛒 Ingredients")
    for item in recipe['ingredients']:
        st.write(f"- {item}")

    st.subheader("👨‍🍳 Steps")
    for i, step in enumerate(recipe['steps'], 1):
        st.write(f"{i}. {step}")

    st.subheader("📝 Instructions")
    st.write(recipe['instructions'])
elif emoji_input:
    st.error("🙁 Sorry, no recipe found for that emoji.")