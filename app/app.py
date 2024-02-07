import streamlit as st
from backend import load_data, get_cocktail_recommendations,generate_wordcloud,generate_waffle

st.set_page_config(
    page_title="Streamlit App",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
    initial_sidebar_state="auto"
)
# Page 1
def page1():
    st.title("Dashboard")
    st.write("The following visualizations are the main insights that were gleamed in the project.")
    data = load_data()
    
    # Create a sidebar for user input
    st.sidebar.header('User Input')
    category_options = ['All'] + list(data['strCategory'].unique())
    category = st.sidebar.selectbox('Select Drink Category', category_options)
    alcoholic_options = ['All'] +  list(data['strAlcoholic'].unique())
    alcoholic = st.sidebar.selectbox('Select Drink Type ', alcoholic_options)
    glass_options = ['All'] + list(data['strGlass'].unique())
    glass_type = st.sidebar.selectbox('Select Glass Type', glass_options)

    # Validate the selected combination before filtering the data
    valid_combination = True
    if category != 'All' and category not in data['strCategory'].unique():
        st.error("Invalid selection for drink category. Please choose a valid category.")
        valid_combination = False
    if alcoholic != 'All' and alcoholic not in data['strAlcoholic'].unique():
        st.error("Invalid selection for alcoholic or non-alcoholic. Please choose a valid option.")
        valid_combination = False
    if glass_type != 'All' and glass_type  not in data['strGlass'].unique():
        st.error("Invalid selection for glass type. Please choose a valid option.")
        valid_combination = False

    # Filter the data based on user input if the combination is valid
    if valid_combination:
        filtered_data = data
        if category != 'All':
            filtered_data = filtered_data[filtered_data['strCategory'] == category]
        if alcoholic != 'All':
            filtered_data = filtered_data[filtered_data['strAlcoholic'] == alcoholic]
        if glass_type != 'All':
            filtered_data = filtered_data[filtered_data['strGlass'] == glass_type]

        # Display visualizations only if filtered data is not empty
        if not filtered_data.empty:
           st.header('Word Cloud')
           wordcloud_image = generate_wordcloud(filtered_data)
           st.image(wordcloud_image, use_column_width=True)
    
        else:
            st.warning("No data available for the selected criteria. Please adjust your selection.")
        
    st.header('Waffle Chart')
    waffle_image  = generate_waffle(data)
    st.image(waffle_image, use_column_width=True)   
# Page 2
def page2():
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
    pages = ["Dashboard", "Recommender"]
    choice = st.sidebar.selectbox("Go to", pages)

    if choice == "Dashboard":
        page1()
    elif choice == "Recommender":
        page2()

if __name__ == "__main__":
    main()
