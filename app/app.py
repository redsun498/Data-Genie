import streamlit as st
from backend import *

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

# Page 2
def page2():
    st.title("Visualizations")
    st.write("Welcome to Page 2!")

# Page 3
def page3():
    st.title("Cocktail Recomendator")
    cocktail_name = st.text_input("Enter the name of a cocktail to get recommendations based on ingredients:")
    cocktail_name = cocktail_name.lower()
    df = load_data()
    cocktail_index = df[df['strDrink'].str.lower() == cocktail_name].index
    if len(cocktail_index) > 0:
        cocktail_index = cocktail_index[0]
        ingredient_recommendations = get_cocktail_recommendations(cocktail_index)
        st.write("Cocktail:", cocktail_data['cocktail_name'][cocktail_index])
        st.write("Recommended cocktails based on ingredients:")
        for recommendation in ingredient_recommendations:
            st.write(recommendation)
    else:
       st.write("Cocktail not found!")


# Navigation
def main():
    st.sidebar.title("Navigation")
    pages = ["Page 1", "Page 2", "Page 3"]
    choice = st.sidebar.selectbox("Go to", pages)

    if choice == "Page 1":
        page1()
    elif choice == "Page 2":
        page2()
    elif choice == "Page 3":
        page3()

if __name__ == "__main__":
    main()




    



 Step 5: Display the results
if st.button("Get Recommendations"):
    cocktail_name = cocktail_name.lower()
    df = load_data()
    cocktail_index = df[df['strDrink'].str.lower() == cocktail_name].index
    if len(cocktail_index) > 0:
        cocktail_index = cocktail_index[0]
        ingredient_recommendations = get_cocktail_recommendations(cocktail_index)
        st.write("Cocktail:", cocktail_data['cocktail_name'][cocktail_index])
        st.write("Recommended cocktails based on ingredients:")
        for recommendation in ingredient_recommendations:
            st.write(recommendation)
    else:
       st.write("Cocktail not found!")







