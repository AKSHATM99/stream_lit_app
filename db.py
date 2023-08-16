import psycopg2
import streamlit as st

conn = psycopg2.connect(host="dpg-cje7b6ocfp5c73bflmjg-a.singapore-postgres.render.com", dbname="aiverse_db",
user="aiverse_app", password="lFsZNXGIDS4rZaI1BrdEb8xG4JDOQsGJ", port=5432)

cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS users (
#             user_name VARCHAR(50) PRIMARY KEY,
#             password VARCHAR(50),
#             country VARCHAR(50)
# );
# """)

def verify(user_name, password):
    cur.execute("""SELECT COUNT(COUNTRY) FROM users WHERE user_name = %(user_name)s AND password = %(password)s;""",
                {'user_name': user_name, 'password': password})
    for i in cur:
        if i[0]==1:
            st.session_state['logged_in'] = 'Yes'
            return st.warning("Logged In Successfully")
        else:
            return st.warning("User Account Not Found. Please Sign Up .......")


def insert(user_name, password, country):
    cur.execute("""
    INSERT INTO users (user_name, password, country) VALUES (%s, %s, %s);
    """,(user_name, password, country))
    conn.commit()
    return st.warning("Signed up Successfully....")

# cur.close()
# conn.close()
# st.experimental_rerun()