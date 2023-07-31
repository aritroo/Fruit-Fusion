import streamlit as st
from main import FruityviceConnection



api_connection = FruityviceConnection(connection_name="fruityvice")

def main():
    
    """
    The main function to run the recipe information web app.

    This function sets up the Streamlit app, connects to the Fruityvice API,
    and handles user interactions to fetch and display recipe data.
    """

    st.title("Fruit Fusion")
    st.write("Your One-Stop Fruitopia: Juicy Facts at Your Fingertips!")

    fruit_input = st.text_input("Enter Your fruit name")

    if st.button("Get Info"):
        try:
            data = api_connection.query(fruit_input)
            display_data(data)
        except Exception as e:
            st.error(f"Error Occured {e}")


def display_data(fruit_data):

    st.write(f"# Provided information for {fruit_data['name']}")
    st.write(f"# Family : {fruit_data['family']}")
    st.write(f"# Genus : {fruit_data['genus']}")

    with st.expander("Nutritions"):
        try:
            st.title(f"Nutritions Content in {fruit_data['name']}")
            st.write(f"Calories : {fruit_data['calories']} cal")
            st.write(f"Fat : {fruit_data['fat']}g")
            st.write(f"Sugar : {fruit_data['sugar']}g")
            st.write(f"Carbohydrates : {fruit_data['carbohydrates']}g")
            st.write(f"Protein : {fruit_data['protein']}g")
            
        except Exception as e:
            st.markdown(f"#none")
        
    

if __name__ == "__main__":
    main()
