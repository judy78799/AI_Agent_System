import requests
import streamlit as st

st.title("Agent 테스트 화면")

query = st.text_input("질문을 입력하세요")

if st.button("질문하기"):
    if not query.strip():
        st.warning("질문을 입력해주세요.")
    else:
        response = requests.post(
            "http://localhost:8000/api/ask",
            params={"query": query},
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()

        st.subheader("답변")
        st.write(data.get("answer"))

        st.subheader("상태")
        st.json(data)
