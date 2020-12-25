import streamlit as st
from functions import reversed
from functions import comple



def main():

    st.title("Reverse Complement Calculator")
    st.header("This web app calculates the **_reverse_**, **_complement_**, or **_reverse-complement_** of your DNA sequence")
    input_text = st.text_area("")

    olmayanlar = ["B","D","E","F","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","U","Ü","V","Y","Z","X",".",",",";",":","1","2","3","4","5","6","7","8","9","0","-","_","?","=",")","(","/","&","%","+","^","'","!","é",">","£","#","$","½","§","{"]
    option = st.selectbox("Choose the action", ("Reverse", "Complement", "Reverse-Complement"))



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