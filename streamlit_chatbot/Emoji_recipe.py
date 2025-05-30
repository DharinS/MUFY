import streamlit as st

# 🍽️ Expanded Recipes
def get_recipe(emoji):
    recipes = {
        # Meals
        '🍕': {
            'name': 'Pizza',
            'ingredients': ['1 pizza dough', '1/2 cup tomato sauce', '1 cup shredded mozzarella', 'Toppings of your choice'],
            'steps': ['Preheat oven to 220°C (425°F).', 'Spread tomato sauce on the dough.', 'Add cheese and toppings.', 'Bake for 15–20 minutes until golden.'],
            'instructions': "Roll out dough, add sauce and toppings, then bake until golden and bubbling."
        },
        '🌮': {
            'name': 'Tacos',
            'ingredients': ['Taco shells', 'Cooked ground beef or beans', 'Shredded cheese', 'Lettuce, salsa, sour cream'],
            'steps': ['Heat taco shells.', 'Fill with meat or beans.', 'Top with cheese, lettuce, salsa.', 'Add sour cream.'],
            'instructions': "Prepare filling, load tacos, and serve with toppings."
        },
        '🍔': {
            'name': 'Cheeseburger',
            'ingredients': ['1 bun', '1 beef patty', '1 slice cheese', 'Lettuce, tomato', 'Ketchup, mustard'],
            'steps': ['Grill patty.', 'Toast bun.', 'Assemble with cheese and toppings.'],
            'instructions': "Grill, stack, and serve hot."
        },
        '🍝': {
            'name': 'Spaghetti Bolognese',
            'ingredients': ['200g spaghetti', '100g ground beef', '1/2 cup tomato sauce', '1 garlic clove'],
            'steps': ['Boil spaghetti.', 'Cook beef with garlic.', 'Add sauce and simmer.', 'Serve over pasta.'],
            'instructions': "A hearty Italian classic with meat sauce."
        },
        '🍳': {
            'name': 'Fried Eggs',
            'ingredients': ['2 eggs', '1 tbsp butter', 'Salt & pepper'],
            'steps': ['Heat pan.', 'Crack eggs.', 'Cook until whites set.', 'Season and serve.'],
            'instructions': "Quick protein-packed breakfast."
        },
        '🍪': {
            'name': 'Cookies',
            'ingredients': ['1 cup butter', '1 cup sugar', '2 cups flour', '1 cup chocolate chips'],
            'steps': ['Mix dough.', 'Scoop onto tray.', 'Bake at 180°C (350°F) for 12 mins.', 'Cool and enjoy!'],
            'instructions': "Crispy edges, gooey center — classic treat!"
        },
        
        # Fruits
        '🍎': {
            'name': 'Apple Snack',
            'ingredients': ['1 fresh apple', 'Peanut butter or caramel (optional)'],
            'steps': ['Wash and slice apple.', 'Add dip if desired.'],
            'instructions': "A crisp and refreshing snack."
        },
        '🍌': {
            'name': 'Banana Smoothie',
            'ingredients': ['1 banana', '1 cup milk (or almond milk)', '1 tsp honey'],
            'steps': ['Blend all ingredients until smooth.', 'Serve chilled.'],
            'instructions': "A creamy, healthy smoothie in 2 minutes."
        },
        '🍉': {
            'name': 'Watermelon Cubes',
            'ingredients': ['1/4 watermelon'],
            'steps': ['Slice and cube watermelon.', 'Chill before serving.'],
            'instructions': "Perfect hydrating fruit snack."
        },
        '🍍': {
            'name': 'Pineapple Bites',
            'ingredients': ['1 fresh pineapple'],
            'steps': ['Peel and core pineapple.', 'Cut into bite-sized chunks.'],
            'instructions': "Sweet, juicy tropical treat."
        },
        '🥝': {
            'name': 'Kiwi Slices',
            'ingredients': ['2 ripe kiwis'],
            'steps': ['Peel skin.', 'Slice into rounds.'],
            'instructions': "Tangy and vitamin-rich fruit slices."
        },
        '🍓': {
            'name': 'Strawberry Delight',
            'ingredients': ['1 cup strawberries', '1 tbsp sugar or cream'],
            'steps': ['Rinse and trim stems.', 'Serve plain or with sugar/cream.'],
            'instructions': "Sweet, tart, and always refreshing."
        },
    }

    return recipes.get(emoji)

# 🌐 Streamlit UI
st.set_page_config(page_title="Emoji Recipe App 🍴", page_icon="🍽️")

st.title("🍴 Emoji Recipe Finder")
st.markdown("Type a food or fruit emoji to get a quick recipe or snack idea!")

emoji_input = st.text_input("🔍 Enter a food emoji (e.g., 🍕, 🍌, 🍓, 🍔):")

if emoji_input:
    recipe = get_recipe(emoji_input)
    
    if recipe:
        st.header(f"{emoji_input} {recipe['name']}")
        st.subheader("🛒 Ingredients")
        for item in recipe['ingredients']:
            st.write(f"- {item}")
        
        st.subheader("👨‍🍳 Steps")
        for i, step in enumerate(recipe['steps'], 1):
            st.write(f"{i}. {step}")
        
        st.subheader("📝 Full Instructions")
        st.write(recipe['instructions'])
    else:
        st.error("🙁 Sorry, no recipe found for that emoji.")

st.markdown("---")
st.markdown("✅ Try emojis like: 🍕 🌮 🍔 🍌 🍎 🍍 🍓 🥝 🍳")
emoji_input = st.selectbox(
    "🔍 Choose a food or fruit emoji:",
    options=list(get_recipe.__defaults__[0].keys())
)
