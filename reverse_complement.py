import streamlit as st
from functions import *




def main():

    st.title("Reverse Complement Calculator")
    st.header("This web app calculates the **_reverse_**, **_complement_**, or **_reverse-complement_** of your DNA sequence")
    input_text = st.text_area("")

    option = st.selectbox("Choose the action", ("Reverse", "Complement", "Reverse-Complement"))

    if validateSeq(input_text) == False:
        st.warning("Please check your DNA Seq !")

    else:
        if option == "Reverse":


            ters = reversed(input_text)
            st.text("")
            st.write("**_Reverse_** of your sequence: {0} ".format(ters))
        
            
        elif option == "Complement":
            try:
                tamamla = comple(input_text)
                st.text("")
                st.write("**_Complement_** of your sequence: {0} ".format(tamamla))
            except:
                st.warning("There is a problem in DNA sequence. Please check it out (:")


        elif option == "Reverse-Complement":
            try:
                sonuc = reversed(input_text)
                cevap = comple(sonuc)
                st.text("")
                st.write("**_Reverse Complement_** of your sequence: {0} ".format(cevap))
            except:
                st.warning("There is a problem in DNA sequence. Please check it out (:")
        




if __name__ == "__main__":
    main()