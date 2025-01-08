import streamlit as st
from scrabe import create_custom_hacker_news, combine_links, combine_subtext


# Set the page configuration (title, layout)
st.set_page_config(page_title="Hacker News", layout="wide")

# Custom styles to improve the appearance
st.markdown("""
    <style>
        .header { 
            font-size: 40px;
            color: #ff6600;
            font-weight: bold;
        }
        .subheader {
            font-size: 24px;
            color: #2c3e50;
            font-weight: bold;
        }
        .news-item {
            background-color: #f4f4f4;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .news-link {
            font-size: 16px;
            color: #2980b9;
        }
        .news-link:hover {
            text-decoration: underline;
        }
        .button-style {
            background-color: #ff6600;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="header">Hacker News</div>', unsafe_allow_html=True)

# Instructions for users
st.write("""
Welcome to the **Hacker News** feed. Below are the latest stories from Hacker News.
You can click on the links to read more about each article.
""")

# Fetch and display the news
list_news = create_custom_hacker_news(
    combine_links('https://news.ycombinator.com/news?p='),
    combine_subtext('https://news.ycombinator.com/news?p='))

for new in list_news:
    with st.container():
        # News item container with styling
        st.markdown(f'<div class="news-item">', unsafe_allow_html=True)

        # Display title with a bold subheader
        st.markdown(f'<div class="subheader">{new["title"]}</div>',
                    unsafe_allow_html=True)

        # Display the link as a clickable text with custom style
        st.markdown(
            f'<a href="{new["link"]}" class="news-link" target="_blank">Read more</a>',
            unsafe_allow_html=True)

        # Add a button that links to the news article for an added touch
        st.markdown(
            f'<a href="{new["link"]}" target="_blank"><button class="button-style">Go to Article</button></a>',
            unsafe_allow_html=True)

        st.markdown('</div>',
                    unsafe_allow_html=True)  # Close the news item container
