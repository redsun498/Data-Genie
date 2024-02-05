import streamlit as st
from backend import load_data, get_cocktail_recommendations

st.set_page_config(
    page_title="Streamlit App",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
    initial_sidebar_state="auto"
)
# Page 1
def page1():
    st.title("Dashboard")
    st.write("Welcome to Page 1!")
    data = load_data()

# Page 2
def page2():
    st.title("Visualization")
    st.write("Welcome to Page 2!")
    data = load_data()
    

# Page 3
def page3():
    data = load_data()
    st.title("Cocktail Recommender")
    cocktail_name = st.text_input("Enter the name of a cocktail to get recommendations based on ingredients:")
    cocktail_name = cocktail_name.lower()
  
    if cocktail_name != "":
        ingredient_recommendations = get_cocktail_recommendations(data, cocktail_name)

        if len(ingredient_recommendations) > 0:
            st.write("Recommended cocktails based on ingredients:")
            cocktail_index = data[data['strDrink'].str.lower() == cocktail_name].index
            st.write("Ingredients: " + data['ingredients_combined'][cocktail_index[0]])
            for recommendation in ingredient_recommendations:
                st.write(recommendation)
        else:
            st.write("Cocktail not found!")


# Navigation
def main():
    st.sidebar.title("Navigation")
    pages = ["Homepage", "Dashboard", "Recommender"]
    choice = st.sidebar.selectbox("Go to", pages)

    if choice == "Homepage":
        page1()
    elif choice == "Dashboard":
        page2()
    elif choice == "Recommender":
        page3()

if __name__ == "__main__":
    main()
