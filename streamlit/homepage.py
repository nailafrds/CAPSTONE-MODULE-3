import streamlit as st
st.set_page_config(
    page_title = "Multiple App"
)
import streamlit.components.v1 as components
import streamlit as st

# HTML dan CSS untuk animasi teks muncul
appear_text_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #222;
            color: white;
            font-family: Arial, sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .appearing-text {
            font-size: 3rem;
            font-weight: bold;
            opacity: 0;
            animation: fadeIn 3s forwards;
        }

        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(50px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="appearing-text">
          SAUDI ARABIA USED CARS 
    </div>
</body>
</html>
"""

import base64
st.markdown(
    """<a href="https://syarah.com">
    <img src="data:image/png;base64,{}" max_container_windth=True">
    </a>""".format(base64.b64encode(open("header.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

#st.image('header.png','https',use_container_width=True)
st.markdown(appear_text_html, unsafe_allow_html=True)
st.text('''Welcome to Syarah - the leading e-commerce platform that is revolutionizing the way used cars are bought. Our used cars come with a 10 Days Trial, Money-back Guarantee. We provide a seamless and reliable car buying experience, backed by our unique Full Warranty Features, a 1 Year Warranty to ensure peace of mind for our customers. But that's not all - we also offer a wide selection of New cars.
At Syarah, we leave no stone unturned in ensuring %100 customer satisfaction.

We have established ourselves as a trusted name in the industry.
We take pride in our state-of-the-art refurbishment and logistic centers, spanning over 50,000 ㎡ in Riyadh City. Our in-house logistic arm facilitates over 20,000 drop-offs each year, ensuring efficient and reliable service. These accomplishments, coupled with a successful $20 million Series B round, demonstrate our unwavering commitment to providing an exceptional and trustworthy car buying experience. 

Join Syarah today and experience a new era in the car buying experience. Be a part of our mission to Shape the Future of Digital Automotive Commerce, and unlock extraordinary possibilities!''')

st.image('Syarah-series-C-A-B.png.webp',use_container_width=True)

