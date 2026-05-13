import streamlit as st
import streamlit.components.v1 as com
import time
# python -m streamlit run movies.py 
st.sidebar.title("🎬 Movie Explorer")
st.sidebar.title("Top 10 Indian Movies🎬")
st.sidebar.header("Choose Your Favourite Movie")
x=st.sidebar.selectbox("Select a movie", ["Dangal", "3 Idiots", "PK", "Bajrangi Bhaijaan","Baahubali 2: The Conclusion","Dhurandhar: The Revenge","Pushpa 2: The Rule","RRR","KGF: Chapter 2","Kalki 2898 AD"])
video_links = {
    "Dangal": ["https://youtu.be/x_7YlGv9u1g?si=HmFsh2ra9X81t-pJ","https://youtu.be/XuIVa_K59QE?si=CfYjlk6yZJCSaePH","https://youtu.be/91ZI3IrojMU?si=jQK48vivkm8sm4j6"],
    "3 Idiots": ["https://youtu.be/DKzBmRRdPXo?si=BpiT4BLj_FyqIGsc","https://youtu.be/lbCRtrrMvSw?si=-vh8CrUaIqI22Icw"],
    "PK": ["https://youtu.be/SOXWc32k4zA?si=7uSfji1qoxztwH0U","https://youtu.be/WsjRWM0EhvM?si=Ix5mYCCj_CzD2AnZ"],
    "Bajrangi Bhaijaan": ["https://youtu.be/4nwAra0mz_Q?si=mHUvCc6T8gWbXa6X","https://youtu.be/1j02gw87ln0?si=mAGwIasOtjrft2H4","https://youtu.be/Oz_ZJhcOX1E?si=ApZcP1UAbOoUjVBj"],
    "Baahubali 2: The Conclusion": ["https://youtu.be/G62HrubdD6o?si=DUfSAzCcVrhOm54R","https://youtu.be/X4hEii_WRPA?si=1tWhIhjSzRw-X06w"],
    "Dhurandhar: The Revenge": ["https://youtu.be/NHk7scrb_9I?si=Jj6AGA9x-tRJAMnP","https://youtu.be/CN0lNff-zm0?si=U8KjHq13LGEcDZRR"],
    "Pushpa 2: The Rule": ["https://youtu.be/1kVK0MZlbI4?si=hBinm5fyENMDzsiU","https://youtu.be/0DVAM48BhQU?si=VlEN4SGX3Z5lfwGW","https://youtu.be/MhIulWFPcpg?si=9MeRh3dEZkvCEI2T"],
    "RRR": ["https://youtu.be/GY4BgdUSpbE?si=JFuyYvL4czmGLUEj","https://youtu.be/sAzlWScHTc4?si=OzVSkdEexthumasJ"],
    "KGF: Chapter 2": ["https://youtu.be/JKa05nyUmuQ?si=eiwP6GAo8D4W_Y6M","https://youtu.be/PWaPCqeCfeY?si=1lbkGBHTLWRsfAy9"],
    "Kalki 2898 AD": ["https://youtu.be/aninoDcPWo4?si=sITMn3MTCwioFl81","https://youtu.be/QYJupzlZX4s?si=Iv4Bh-F8XRBkfK2x","https://youtu.be/kQDd1AhGIHk?si=KeZEMzbp36pxNER5"]
}
song_links = {
    "Dangal": ["https://open.spotify.com/embed/track/47ZCCeeC5PaMYN4meEAz44?si=a76a88c279c74990",
                "https://open.spotify.com/embed/track/69Zx9ptG9bB7nNQz7b5itz?si=aaace4011f394978",
                "https://open.spotify.com/embed/track/5Ry67OqwCxKbswCxcPHcg9?si=be9531fc40a94e52",
                "https://open.spotify.com/embed/track/7w5Je2ouh5Zxp5nfaGitvy?si=c4b2a77ac47a4a65",
                "https://open.spotify.com/embed/track/1J85Qi47YYQ76PQ57O9Fjh?si=a68f69b14d8f4996",
                "https://open.spotify.com/embed/track/12eA8kd2uD1zoN4jdtbYn4?si=c07c3124ebea4363",
                "https://open.spotify.com/embed/track/4OUD1GNh40ELde8ThTYsym?si=2a4be2bdf8434514"],
    "3 Idiots": ["https://open.spotify.com/embed/track/4sZDyON3hp3bB9Y8uayqvT?si=33cdd1efcbfd4de7",
                "https://open.spotify.com/embed/track/2OvedmlIy9jzXJ0lsLSN9w?si=eab06039ae5941e6",
                "https://open.spotify.com/embed/track/5cOu9ymkebFkMiFLQueO1n?si=c7d3e8019be1471d",
                "https://open.spotify.com/embed/track/1w6XiTEJCIILDTV2wyP6fT?si=5c890bebe71541af",
                "https://open.spotify.com/embed/track/19SF5nItZDNoGKFq6uoPNB?si=5a01fb9688784863"],
    "PK": ["https://open.spotify.com/embed/track/5YUZpKW1nRVtxsy3sN6q1g?si=fd160a2126554a85",
            "https://open.spotify.com/embed/track/0q8g9felKNWRG6lBxQ7FX6?si=17e75f8588f94a7b",
            "https://open.spotify.com/embed/track/0NbsId64Ern8x1fThsnSdG?si=b03fb8e58d8541a9",
            "https://open.spotify.com/embed/track/0bYDMpQ94LnF38FiOlc8K9?si=2f4860be24e1429d",
            "https://open.spotify.com/embed/track/6QXOeVS0RuwbMrI4ud2Lud?si=d415063bd3764d55",
            "https://open.spotify.com/embed/track/64uIY06wOtU9o8r3c1rx1x?si=9235f5c5968b4ae0",
            "https://open.spotify.com/embed/track/383Joat1pE0yLpjQmbMrJQ?si=d5d6b80290804b91"],
    "Bajrangi Bhaijaan": ["https://open.spotify.com/embed/track/0Zz7AEZfBKP2U7sO0WJKER?si=caf63945c8f04070",
                        "https://open.spotify.com/embed/track/3aaiAWCet6sbfOfLSn3g7i?si=0946eef783af4674",
                        "https://open.spotify.com/embed/track/52qnHAlqWpo3kgEteAPjRf?si=d3b8669d049f4e4d",
                        "https://open.spotify.com/embed/track/1vmQPVE7vbgSZ12C8MlKX8?si=3233033ce9e64bd1",
                        "https://open.spotify.com/embed/track/1DUoaxHClMTqzTZCTcF61z?si=d3b99a14587043dc",
                        "https://open.spotify.com/embed/track/6TGX01ExmdHyOG72fqUU3Q?si=d54e37eb4c074839",
                        "https://open.spotify.com/embed/track/7txLCGOXyDlDXTjtR1Sk4v?si=233433e8cbac4ee8"],
    "Baahubali 2: The Conclusion": ["https://open.spotify.com/embed/track/2S3KDCaxzKx8fvHatpnANw?si=9f29de98c2b24db3",
                                    "https://open.spotify.com/embed/track/6PS5jdC3iUx1pnMB6pyBnX?si=32bd95d5d81e4e1e",
                                    "https://open.spotify.com/embed/track/5iVyx2WMd7lwkWeXIs6cid?si=bbf0b6eea3704344",
                                    "https://open.spotify.com/embed/track/6Dzrw3MQFXeAGnJrfDUYun?si=07dc0b7109ec407b",
                                    "https://open.spotify.com/embed/track/1khRXKcOsjsChxKf3zsgg3?si=2a77aba676a445f2"],
    "Dhurandhar: The Revenge": ["https://open.spotify.com/embed/track/2SeUci6OXx1ztZiFiDIyX5?si=659496b06fb94f97",
                                "https://open.spotify.com/embed/track/6cYWjvAPGJrb6ZOJn1URn2?si=86e41a6297484aa2",
                                "https://open.spotify.com/embed/track/0bdA7CMrqT1qJVwwhw2Yn4?si=b11255da031045f3",
                                "https://open.spotify.com/embed/track/06y0NcmJ1VuTyAQkHnwko0?si=673a8450ace54720",
                                "https://open.spotify.com/embed/track/4Ec2TXBQ5NMXuXfFBDkE1A?si=de4dfa373b43412b",
                                "https://open.spotify.com/embed/track/1qJiRzRlmNrzYBsMdVPqT2?si=4432557b545045ba",
                                "https://open.spotify.com/embed/track/1i6Uk2tHzDbWgxhlEayzYb?si=f8da6bd6ea0a477e",
                                "https://open.spotify.com/embed/track/3rnQfyFzUNdWKtdwUypWo5?si=67d48b0184174a00",
                                "https://open.spotify.com/embed/track/6za0VNkFezXamgUjJi1nMx?si=38b821708bc54e99",
                                "https://open.spotify.com/embed/track/66jbypfLRHYRB3UwqklrYI?si=0cf701afbb20456a",
                                "https://open.spotify.com/embed/track/5gysl1k9QxPSM604I8G3uk?si=15dabb122cfd4ec3",
                                "https://open.spotify.com/embed/track/6iMasiFzpQt3Y8c9EnITCP?si=1c366a077f344a81",
                                "https://open.spotify.com/embed/track/6NPUftix9Z6nbo8Seg3yle?si=4de53d22668647d3",
                                "https://open.spotify.com/embed/track/4QAhkj55nfiPtYyqkooIzu?si=38a2e1281da34583"],
    "Pushpa 2: The Rule": ["https://open.spotify.com/embed/track/1o0bFBGkxgxCnu6mg2YrP1?si=2a15d0ff6fdb4bf2",
                            "https://open.spotify.com/embed/track/2ZDOzySC2g3YF1p26TPzBt?si=cd6ec5a56a8a4e19",
                            "https://open.spotify.com/embed/track/44hBx9rDmlkHlm3ZJZFzvT?si=f5d7dd4522514de7",
                            "https://open.spotify.com/embed/track/0Tvybk3jWj7usdP3LALmHI?si=2d0dc65589d54a95",
                            "https://open.spotify.com/embed/track/5oSKZvm7Pn1J8CennbbBWr?si=ea8a721de4234529"],
    "RRR": ["https://open.spotify.com/embed/track/208sMwgVcaFt2mT79Df1KG?si=86a4181e89c3438a",
            "https://open.spotify.com/embed/track/2OsAjPo5sDkTgaRMx6fRHg?si=382ce44a930741d7",
            "https://open.spotify.com/embed/track/31fXnOzbWufydBV2MTRfJi?si=0ff1233cee004166",
            "https://open.spotify.com/embed/track/3aUfD75nYgejjhXNv0nfFO?si=a22cd69a94fb46a3",
            "https://open.spotify.com/embed/track/7G8LfMpY6TGN9dbZ9m0Jdd?si=063e24d15bd648d0",
            "https://open.spotify.com/embed/track/7lp9Rj8QzgiQz4j4cNflPZ?si=b66cc270e95b4640",
            "https://open.spotify.com/embed/track/3Kv659H6czvQ7uvPHza3Es?si=cac3a4f2d3e44b2e"],
    "KGF: Chapter 2": ["https://open.spotify.com/embed/track/45GXsEdPxpFLnqQMPR2Cyy?si=c74a50fc02914766",
                    "https://open.spotify.com/embed/track/3jOHvaeBCCtvK7u1ueTLGI?si=6466ad3bea024321",
                    "https://open.spotify.com/embed/track/1DaF1xu2qeaxYOK0TeycKP?si=8eec0979a3974692",
                    "https://open.spotify.com/embed/track/1XOCtdeIjy7eIIPsYFGXzZ?si=90613b6995f04f7b",
                    "https://open.spotify.com/embed/track/5B9BTcqyMXfZCFaSsKIpDH?si=063a09aa58e24805"],
    "Kalki 2898 AD": ["https://open.spotify.com/embed/track/73qEZ1uDm4V2jq9EeXWM8G?si=214f5b7a9eb1465e",
                    "https://open.spotify.com/embed/track/3z8DnKyVl4TVZHT2KOHHpw?si=77916a6cb33a45bd",
                    "https://open.spotify.com/embed/track/5rLTwoukwaXRbdE84nSMNO?si=c681ce52ee384fad",
                    "https://open.spotify.com/embed/track/27hRZl3YfW9PGEWozrMFKF?si=d5cf7969991c4ab6",
                    "https://open.spotify.com/embed/track/01oul2Pto2wf1fYRupqAnh?si=98f6d43a0a194f13",
                    "https://open.spotify.com/embed/track/2zDXJrQbQW00vj3z7WX0h4?si=2fdca3efdb734cf6"]
}
image_links = {
    "Dangal": ["https://static.okko.tv/images/v4/80a200a0-cbd5-4bf3-b7f9-81c8e5ad00c9",
                "https://flxt.tmsimg.com/assets/p13537054_v_h10_ab.jpg"],
    "3 Idiots": ["http://smotreshka.server-img.lfstrm.tv/image/aHR0cHM6Ly9jbXMuc21vdHJlc2hrYS50di9hcmNoaXZlLWltZy9zdGF0aWMvbWVkaWEvYTEvZDIvYTFkMjFhZDViMjllMDVkYzMyM2VlY2Y3MjZkM2UwZmE=",
                    "https://www.alaraby.co.uk/sites/default/files/media/images/8FFA01C6-142C-42CF-809F-8318803333D7.png"],
    "PK": ["https://i.pinimg.com/originals/f1/48/72/f14872b5698749e1e7a4ff3cb4a17b88.jpg",
            "https://saichintala.com/wp-content/uploads/2014/12/pk-aamir-khan-2nd-movie-poster-wallpaper.jpg"],
    "Bajrangi Bhaijaan": ["https://avatars.mds.yandex.net/get-kinopoisk-image/1946459/9e8e4177-0e4c-4181-93f2-3b85d21b0da3/1920x",
                    "https://s.yimg.com/ny/api/res/1.2/ghV3.H2JknMTb6XwRb_oXw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk2MDtjZj13ZWJw/https://media.zenfs.com/en-us/homerun/deadline.com/3a81d10941c6a637c6a4af7a34fdbe71"],
    "Baahubali 2: The Conclusion": ["https://is3-ssl.mzstatic.com/image/thumb/Video114/v4/fe/a5/d6/fea5d6a1-5053-5c1a-3bf7-d1af044eceea/1246063720-WW-AMP_SF.lsr/1200x675.jpg",
                    "https://i.ytimg.com/vi/EzRPk74m5P0/maxresdefault.jpg"],
    "Dhurandhar: The Revenge": ["https://staticimg.amarujala.com/assets/images/2026/03/20/thharathhara-2_12eac9c7238d95a8bd4fdfaf7b3fab20.jpeg?q=80",
                    "https://images.financialexpressdigital.com/2026/03/Dhurandhar-2_20260331012830.jpg"],
    "Pushpa 2: The Rule": ["https://image.tmdb.org/t/p/original/7jGItf7idJsBm9QTNoTNTU3KiGe.jpg",
                    "https://www.game-ost.ru/static/covers_soundtracks/1/2/1249512_773157.jpg"],
    "RRR": ["https://static.okko.tv/images/v4/90d584b1-cdba-46ba-b48e-45877b702de1?presetId=4000&amp;width=1200&amp;height=630&amp;scale=1&amp;quality=80",
                    "https://img.haarets.co.il/bs/00000182-1133-d5f6-abe3-1bbbe9a70000/5b/af/06225d494f93ae9780440ebf5935/47789311.JPG?precrop=14235",
                    "https://cdn.vox-cdn.com/uploads/chorus_image/image/71744359/RRR_Still_2.0.jpg"],
    "KGF: Chapter 2": ["https://i.ytimg.com/vi/g16LqkE9JMI/maxresdefault.jpg",
                    "https://m.media-amazon.com/images/M/MV5BMmVlZWYwYTUtZDBlNi00MWE4LWE5ZjctYzMxYTMxMDAxYWY0XkEyXkFqcGc@._V1_.jpg"],
    "Kalki 2898 AD": ["https://images.ottplay.com/images/kalki-2898-ad-official-poster-1719582068.jpg",
                    "https://cdn.gulte.com/wp-content/uploads/2024/06/Kalki-2898-AD-release-trailer-1-scaled.jpeg"]
}
ratings = {
                "Dangal": {"IMDb": "8.4/10", "Rotten Tomatoes": "88%", "Metacritic": "77/100"},
                "3 Idiots": {"IMDb": "8.4/10", "Rotten Tomatoes": "86%", "Metacritic": "67/100"},
                "PK": {"IMDb": "8.1/10", "Rotten Tomatoes": "76%", "Metacritic": "51/100"},
                "Bajrangi Bhaijaan": {"IMDb": "8.0/10", "Rotten Tomatoes": "85%", "Metacritic": "64/100"},
                "Baahubali 2: The Conclusion": {"IMDb": "8.2/10", "Rotten Tomatoes": "90%", "Metacritic": "61/100"},
                "Pushpa 2: The Rule": {"IMDb": "7.4/10", "Rotten Tomatoes": "76%", "Metacritic": "63/100"},
                "RRR": {"IMDb": "7.8/10", "Rotten Tomatoes": "95%", "Metacritic": "83/100"},
                "KGF: Chapter 2": {"IMDb": "8.3/10", "Rotten Tomatoes": "83%", "Metacritic": "60/100"},
                "Kalki 2898 AD": {"IMDb": "TBD", "Rotten Tomatoes": "TBD", "Metacritic": "TBD"},
                "Dhurandhar: The Revenge": {"IMDb": "No", "Rotten Tomatoes": "No", "Metacritic": "No"},
            }
Info = {
        "Dangal": {
            "year": "2016",
            "genre": "Biography, Sports, Drama",
            "director": "Nitesh Tiwari",
            "cast": "Aamir Khan, Fatima Sana Shaikh, Sanya Malhotra",
            "desc": """Dangal is a biographical sports drama based on the life of Mahavir Singh Phogat, 
                    a former wrestler who dreams of winning a gold medal for India. Unable to achieve his dream himself, 
                     he trains his daughters Geeta and Babita against societal norms to become world-class wrestlers. 
                   the film showcases their struggles, discipline, and journey from a small village to international success.""",
            "highlight": "Based on real-life Phogat family story. One of India's highest-grossing films.",
        },

        "3 Idiots": {
            "year": "2009",
            "genre": "Comedy, Drama",
            "director": "Rajkumar Hirani",
            "cast": "Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor",
            "desc": """3 Idiots follows the journey of three engineering students at a prestigious college. 
                    Through humor and emotional storytelling, the film criticizes the rigid education system and emphasizes 
                    learning with passion instead of pressure. Rancho, the central character, inspires his friends to think differently 
                    and follow their dreams.""",
            "highlight": "Iconic film on education system with strong social message.",
        },

        "PK": {
            "year": "2014",
            "genre": "Comedy, Drama, Sci-Fi",
            "director": "Rajkumar Hirani",
            "cast": "Aamir Khan, Anushka Sharma, Sanjay Dutt",
            "desc": """PK tells the story of an alien who lands on Earth and loses his communication device. 
                        While trying to retrieve it, he questions human beliefs, traditions, and religious practices. 
                        His innocent perspective exposes contradictions in society and promotes critical thinking.""",
            "highlight": "Unique concept blending satire with social commentary.",
        },

        "Bajrangi Bhaijaan": {
            "year": "2015",
            "genre": "Drama, Adventure",
            "director": "Kabir Khan",
            "cast": "Salman Khan, Kareena Kapoor, Nawazuddin Siddiqui",
            "desc": """The story revolves around Pavan, a kind-hearted man who embarks on a journey to reunite 
                        a mute Pakistani girl with her family. Crossing borders and facing numerous challenges, the film delivers 
                        a strong message of humanity, love, and unity beyond religion and nationality.""",
            "highlight": "Emotionally powerful cross-border story loved worldwide.",
        },

        "Baahubali 2: The Conclusion": {
            "year": "2017",
            "genre": "Action, Drama, Epic",
            "director": "S. S. Rajamouli",
            "cast": "Prabhas, Rana Daggubati, Anushka Shetty",
            "desc": """The film concludes the Baahubali saga, revealing why Katappa killed Baahubali. 
                        It follows Mahendra Baahubali as he avenges his father and defeats Bhallaladeva to reclaim the throne. 
                        Known for its grand visuals, storytelling, and action sequences, it set new benchmarks in Indian cinema.""",
            "highlight": "Historic blockbuster with massive VFX and storytelling scale.",
        },

        "RRR": {
            "year": "2022",
            "genre": "Action, Drama",
            "director": "S. S. Rajamouli",
            "cast": "Ram Charan, Jr NTR, Alia Bhatt",
            "desc": """RRR is a fictional story inspired by two Indian revolutionaries. 
                    It portrays their friendship, struggles, and fight against British colonial rule. 
                    The film combines intense action, emotional depth, and spectacular visuals.""",
            "highlight": "Oscar-winning song 'Naatu Naatu' gained global recognition.",
        },

        "KGF: Chapter 2": {
            "year": "2022",
            "genre": "Action, Crime",
            "director": "Prashanth Neel",
            "cast": "Yash, Sanjay Dutt, Raveena Tandon",
            "desc": """KGF Chapter 2 continues Rocky’s rise to power in the Kolar Gold Fields. 
                    As he becomes a feared leader, new enemies emerge including Adheera. 
                    The film focuses on power, ambition, and survival in a violent empire.""",
            "highlight": "Mass-action film with strong fan following.",
        },

        "Pushpa 2: The Rule": {
            "year": "2024",
            "genre": "Action, Thriller",
            "director": "Sukumar",
            "cast": "Allu Arjun, Rashmika Mandanna",
            "desc": """Pushpa 2 continues the story of Pushpa Raj as he strengthens his smuggling empire. 
                        Facing police forces and rivals, he evolves from a laborer to a powerful syndicate leader. 
                        The film focuses on dominance, survival, and rebellion.""",
            "highlight": "Highly anticipated sequel with massive hype.",
        },

        "Kalki 2898 AD": {
            "year": "2024",
            "genre": "Sci-Fi, Action",
            "director": "Nag Ashwin",
            "cast": "Prabhas, Deepika Padukone, Amitabh Bachchan",
            "desc": """Set in a futuristic world, Kalki 2898 AD explores a dystopian society where humanity is on the brink 
                    of collapse. The story revolves around a savior figure destined to restore balance and fight powerful forces.""",
            "highlight": "One of India’s biggest sci-fi projects.",
        },

        "Dhurandhar: The Revenge": {
            "year": "Unknown",
            "genre": "Action",
            "director": "Unknown",
            "cast": "Unknown",
            "desc": """No verified information available. This entry may not correspond to a real or confirmed film. 
                    Please verify the data source before using it in production.""",
            "highlight": "Data not reliable.",
        }
    }

Wikip = {

    "Dangal": [
        {"name": "Aamir Khan", "role": "Mahavir Singh Phogat",
         "wiki": "https://en.wikipedia.org/wiki/Aamir_Khan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/6/65/Aamir_Khan_at_the_success_bash_of_Secret_Superstar.jpg"},

        {"name": "Sakshi Tanwar", "role": "Daya Kaur",
         "wiki": "https://en.wikipedia.org/wiki/Sakshi_Tanwar",
         "img": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Sakshi_Tanwar_graces_the_Ganesha_puja_at_Ekta_Kapoor%E2%80%99s_house_%2805%29_%28cropped%29.jpg"},

        {"name": "Fatima Sana Shaikh", "role": "Geeta Phogat",
         "wiki": "https://en.wikipedia.org/wiki/Fatima_Sana_Shaikh",
         "img": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Fatima_Sana_Shaikh_at_the_launch_of_Netflix_Slate_2025_%28cropped%29.jpg"},

        {"name": "Sanya Malhotra", "role": "Babita Kumari",
         "wiki": "https://en.wikipedia.org/wiki/Sanya_Malhotra",
         "img": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Sanya_Malhotra_at_the_launch_of_Netflix_Slate_2025_%28cropped%29.jpg"},

        {"name": "Zaira Wasim", "role": "Young Geeta",
         "wiki": "https://en.wikipedia.org/wiki/Zaira_Wasim",
         "img": "https://upload.wikimedia.org/wikipedia/commons/1/14/Zaira_Wasim_snapped_on_sets_of_Rajeev_Masand%E2%80%99s_show_%2804%29.jpg"},


        {"name": "Aparshakti Khurana", "role": "Omkar",
         "wiki": "https://en.wikipedia.org/wiki/Aparshakti_Khurana",
         "img": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Aparshakti_Khurana_at_Zee_Cine_Awards_2024.jpg"},

        {"name": "Girish Kulkarni", "role": "Coach Kadam",
         "wiki": "https://en.wikipedia.org/wiki/Girish_Kulkarni",
         "img": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Girish_Kulkarni_%28cropped%29.jpg"}
    ],

    "3 Idiots": [
        {"name": "Aamir Khan", "role": "Rancho",
         "wiki": "https://en.wikipedia.org/wiki/Aamir_Khan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/6/65/Aamir_Khan_at_the_success_bash_of_Secret_Superstar.jpg"},

        {"name": "R. Madhavan", "role": "Farhan",
         "wiki": "https://en.wikipedia.org/wiki/R._Madhavan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Madhavan_Saala_Khadoos_2_%28cropped%29.jpg"},

        {"name": "Sharman Joshi", "role": "Raju",
         "wiki": "https://en.wikipedia.org/wiki/Sharman_Joshi",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Sharman_Joshi_at_Trailer_launch_of_Hate_Story_3.jpg/500px-Sharman_Joshi_at_Trailer_launch_of_Hate_Story_3.jpg"},

        {"name": "Kareena Kapoor", "role": "Pia",
         "wiki": "https://en.wikipedia.org/wiki/Kareena_Kapoor_Khan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/2/29/Kareena_Kapoor_Khan_in_2023_%281%29_%28cropped%29.jpg"},

        {"name": "Boman Irani", "role": "Virus",
         "wiki": "https://en.wikipedia.org/wiki/Boman_Irani",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/IIFA_2017_Green_Carpet_%2836349841166%29_%28cropped%29.jpg/500px-IIFA_2017_Green_Carpet_%2836349841166%29_%28cropped%29.jpg"},

        {"name": "Omi Vaidya", "role": "Chatur",
         "wiki": "https://en.wikipedia.org/wiki/Omi_Vaidya",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Omi_Vaidya_1.jpg/500px-Omi_Vaidya_1.jpg"}
    ],

    "PK": [
        {"name": "Aamir Khan", "role": "PK",
         "wiki": "https://en.wikipedia.org/wiki/Aamir_Khan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/6/65/Aamir_Khan_at_the_success_bash_of_Secret_Superstar.jpg"},

        {"name": "Anushka Sharma", "role": "Jaggu",
         "wiki": "https://en.wikipedia.org/wiki/Anushka_Sharma",
         "img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Anushka_Sharma_promoting_Zero.jpg"},

        {"name": "Sanjay Dutt", "role": "Bhairon",
         "wiki": "https://en.wikipedia.org/wiki/Sanjay_Dutt",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Sanjay_dutt_department.jpg/500px-Sanjay_dutt_department.jpg"},

        {"name": "Saurabh Shukla", "role": "Tapasvi",
         "wiki": "https://en.wikipedia.org/wiki/Saurabh_Shukla",
         "img": "https://upload.wikimedia.org/wikipedia/commons/6/62/Saurabh_Shukla_graces_the_screening_of_Sonata.jpg"}
    ],

    "Bajrangi Bhaijaan": [
        {"name": "Salman Khan", "role": "Pavan",
         "wiki": "https://en.wikipedia.org/wiki/Salman_Khan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Salman_Khan_in_2023_%281%29_%28cropped%29.jpg/500px-Salman_Khan_in_2023_%281%29_%28cropped%29.jpg"},

        {"name": "Kareena Kapoor", "role": "Rasika",
         "wiki": "https://en.wikipedia.org/wiki/Kareena_Kapoor_Khan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/2/29/Kareena_Kapoor_Khan_in_2023_%281%29_%28cropped%29.jpg"},

        {"name": "Nawazuddin Siddiqui", "role": "Chand Nawab",
         "wiki": "https://en.wikipedia.org/wiki/Nawazuddin_Siddiqui",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Nawazuddin_Siddiqui_at_IFFK_2021_4_%28cropped%29.jpg/500px-Nawazuddin_Siddiqui_at_IFFK_2021_4_%28cropped%29.jpg"},

        {"name": "Harshaali Malhotra", "role": "Munni",
         "wiki": "https://en.wikipedia.org/wiki/Harshaali_Malhotra",
         "img": "https://upload.wikimedia.org/wikipedia/commons/6/60/Harshaali_Malhotra_at_the_premiere_of_Salaam_Venky_%28cropped%29.jpg"}
    ],
    "Baahubali 2: The Conclusion": [
            {"name": "Prabhas", "role": "Amarendra / Mahendra Baahubali",
            "wiki": "https://en.wikipedia.org/wiki/Prabhas",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Prabhas_by_Gage_Skidmore.jpg/500px-Prabhas_by_Gage_Skidmore.jpg"},

            {"name": "Rana Daggubati", "role": "Bhallaladeva",
            "wiki": "https://en.wikipedia.org/wiki/Rana_Daggubati",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Rana_Daggubati_by_Gage_Skidmore.jpg/500px-Rana_Daggubati_by_Gage_Skidmore.jpg"},

            {"name": "Anushka Shetty", "role": "Devasena",
            "wiki": "https://en.wikipedia.org/wiki/Anushka_Shetty",
            "img": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Anushka_at_the_trailer_launch_of_Baahubali_%28cropped%29.jpg"},

            {"name": "Ramya Krishnan", "role": "Sivagami",
            "wiki": "https://en.wikipedia.org/wiki/Ramya_Krishnan",
            "img": "https://upload.wikimedia.org/wikipedia/commons/4/42/Ramya_Krishnan.jpg"},

            {"name": "Sathyaraj", "role": "Katappa",
            "wiki": "https://en.wikipedia.org/wiki/Sathyaraj",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Sathiyaraj.JPG/500px-Sathiyaraj.JPG"},

            {"name": "Nassar", "role": "Bijjaladeva",
            "wiki": "https://en.wikipedia.org/wiki/Nassar_(actor)",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Nassar_at_Oru_Kadhai_Sollattumaa_Audio_Launch_%28cropped%29.jpg/500px-Nassar_at_Oru_Kadhai_Sollattumaa_Audio_Launch_%28cropped%29.jpg"},

            {"name": "Subbaraju", "role": "Kumara Varma",
            "wiki": "https://en.wikipedia.org/wiki/Subbaraju",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Subbarajuactor.jpg/500px-Subbarajuactor.jpg"},

            {"name": "Tamannaah Bhatia", "role": "Avantika",
            "wiki": "https://en.wikipedia.org/wiki/Tamannaah",
            "img": "https://upload.wikimedia.org/wikipedia/commons/6/60/Tamannaah_Bhatia_at_a_song_launch_from_the_film_Vedaa_%28cropped%29.jpg"},

            {"name": "Rohini", "role": "Sanga (Shivudu's mother)",
            "wiki": "https://en.wikipedia.org/wiki/Rohini_(actress)",
            "img": "https://upload.wikimedia.org/wikipedia/commons/4/48/Rohini_%28actress%29.jpg"},

    ],
   "Dhurandhar: The Revenge": [
        {"name": "Ranveer Singh", "role": "Lead Hero",
        "wiki": "https://en.wikipedia.org/wiki/Ranveer_Singh",
        "img": "https://upload.wikimedia.org/wikipedia/commons/3/32/Ranveer_Singh_in_2023_%281%29_%28cropped%29.jpg"},

        {"name": "Arjun Rampal", "role": "Main Villain",
        "wiki": "https://en.wikipedia.org/wiki/Arjun_Rampal",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Arjun_Rampal_is_the_new_Gillette_brand_ambassador.jpg/500px-Arjun_Rampal_is_the_new_Gillette_brand_ambassador.jpg"},

        {"name": "Sara Arjun", "role": "Heroine",
        "wiki": "https://en.wikipedia.org/wiki/Sara_Arjun",
        "img": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Photos-Sara-Arjun-from-Dhurandhar-The-Revenge-Cropped.jpg"},

        {"name": "Akshaye Khanna", "role": "Supporting Actor",
        "wiki": "https://en.wikipedia.org/wiki/Akshaye_Khanna",
        "img": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Akshaye_Khanna_at_the_launch_of_GUJCON_CRF_and_PRF.jpg"},

        {"name": "Sanjay Dutt", "role": "Police Officer",
        "wiki": "https://en.wikipedia.org/wiki/Sanjay_Dutt",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Sanjay_dutt_department.jpg/500px-Sanjay_dutt_department.jpg"},

        {"name": "Danish Pandor", "role": "Crime Boss",
        "wiki": "https://en.wikipedia.org/wiki/Danish_Pandor",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmLfrfVYZFXfBUe4DwG3E5RqluGZIIds1pJEEf6nzXhr-7poMYIL5ct7bPzqTXZ8L9cqtT6etg18m-xoLPiPy9o5cRxQ4HzYZt3gIEoaY1&s=10"},

        {"name": "R. Madhavan", "role": "Government Officer",
        "wiki": "https://en.wikipedia.org/wiki/R._Madhavan",
        "img": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Madhavan_Saala_Khadoos_2_%28cropped%29.jpg"}
],
    "Pushpa 2: The Rule": [
            {"name": "Allu Arjun", "role": "Pushpa Raj",
            "wiki": "https://en.wikipedia.org/wiki/Allu_Arjun",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Allu_Arjun_at_Pushpa_2_The_Rule_meet.jpg/500px-Allu_Arjun_at_Pushpa_2_The_Rule_meet.jpg"},

            {"name": "Rashmika Mandanna", "role": "Srivalli",
            "wiki": "https://en.wikipedia.org/wiki/Rashmika_Mandanna",
            "img": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Rashmika-Mandanna_at_the_music_launch_of_Chhaava_%28cropped%29.jpg"},

            {"name": "Fahadh Faasil", "role": "Bhanwar Singh Shekhawat",
            "wiki": "https://en.wikipedia.org/wiki/Fahadh_Faasil",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Fahadh_Faasil_2019.jpg/500px-Fahadh_Faasil_2019.jpg"},

            {"name": "Jagapathi Babu", "role": "Central Minister",
            "wiki": "https://en.wikipedia.org/wiki/Jagapathi_Babu",
            "img": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Jagapathi_Babu_at_62nd_Filmfare_awards_south.jpg"},

            {"name": "Sunil", "role": "Mangalam Srinu",
            "wiki": "https://en.wikipedia.org/wiki/Sunil_(actor)",
            "img": "https://upload.wikimedia.org/wikipedia/commons/5/50/Sunil_Telugu_Film_Actor.jpg"},

            {"name": "Anasuya Bharadwaj", "role": "Dakshayani",
            "wiki": "https://en.wikipedia.org/wiki/Anasuya_Bharadwaj",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Anasuya_Bharadwaj_at_Khiladi_pre_release_event_%281%29.jpg/500px-Anasuya_Bharadwaj_at_Khiladi_pre_release_event_%281%29.jpg"},

            {"name": "Dhananjaya", "role": "Jolly Reddy",
            "wiki": "https://en.wikipedia.org/wiki/Dhananjaya_(actor)",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Dhananjaya-profile.jpg/500px-Dhananjaya-profile.jpg"},

            {"name": "Ajay Ghosh", "role": "Konda Reddy",
            "wiki": "https://en.wikipedia.org/wiki/Ajay_Ghosh_(actor)",
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz1MR7cGQdgPoXi_mdWX424BqUC4rSOwYhHjfTDxKaJTsjuRqT83cOmzlz0YfhIX-kBHhY4KlN1kEaftaFMaABd70IQQ7K5llJOku_k43K&s=10"},

            {"name": "Rao Ramesh", "role": "MP Bhumireddy",
            "wiki": "https://en.wikipedia.org/wiki/Rao_Ramesh",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Rao_Ramesh_at_Mukunda_success_meet.jpg/500px-Rao_Ramesh_at_Mukunda_success_meet.jpg"},

        ],
    "RRR": [
        {"name": "Ram Charan", "role": "Alluri Sitarama Raju",
         "wiki": "https://en.wikipedia.org/wiki/Ram_Charan",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Ram_Charan_at_Game_Changer_trailer_launch.jpg/500px-Ram_Charan_at_Game_Changer_trailer_launch.jpg"},

        {"name": "Jr NTR", "role": "Komaram Bheem",
         "wiki": "https://en.wikipedia.org/wiki/N._T._Rama_Rao_Jr.",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/NTR_Jr._%282026%29.jpg/500px-NTR_Jr._%282026%29.jpg"},

        {"name": "Alia Bhatt", "role": "Sita",
         "wiki": "https://en.wikipedia.org/wiki/Alia_Bhatt",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Alia_Bhatt_at_Berlinale_2022_Ausschnitt.jpg/500px-Alia_Bhatt_at_Berlinale_2022_Ausschnitt.jpg"},

        {"name": "Ajay Devgn", "role": "Venkata Rama Raju",
         "wiki": "https://en.wikipedia.org/wiki/Ajay_Devgn",
         "img": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Ajay_Devgn_at_the_trailer_launch_of_Raid_2.jpg"}
    ],

    "KGF: Chapter 2": [
        {"name": "Yash", "role": "Rocky",
         "wiki": "https://en.wikipedia.org/wiki/Yash_(actor)",
         "img": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Yash%2C_Vishal%2C_Srinidhi_Shetty_at_the_%E2%80%98KGF%E2%80%99_Press_Meet_In_Chennai_%28cropped%29.jpg"},

        {"name": "Sanjay Dutt", "role": "Adheera",
         "wiki": "https://en.wikipedia.org/wiki/Sanjay_Dutt",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Sanjay_dutt_department.jpg/500px-Sanjay_dutt_department.jpg"},

        {"name": "Raveena Tandon", "role": "Ramika Sen",
         "wiki": "https://en.wikipedia.org/wiki/Raveena_Tandon",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Raveena_Tandon_at_IFFI_2021.jpg/500px-Raveena_Tandon_at_IFFI_2021.jpg"},

        {"name": "Srinidhi Shetty", "role": "Reena",
         "wiki": "https://en.wikipedia.org/wiki/Srinidhi_Shetty",
         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Srinidhi_Shetty_at_the_%E2%80%98KGF%E2%80%99_Press_Meet_In_Chennai_%28cropped%29.jpg/500px-Srinidhi_Shetty_at_the_%E2%80%98KGF%E2%80%99_Press_Meet_In_Chennai_%28cropped%29.jpg"}
    ],
    "Kalki 2898 AD": [
    {"name": "Prabhas", "role": "Bhairava",
     "wiki": "https://en.wikipedia.org/wiki/Prabhas",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Prabhas_by_Gage_Skidmore.jpg/500px-Prabhas_by_Gage_Skidmore.jpg"},

    {"name": "Deepika Padukone", "role": "SUM-80",
     "wiki": "https://en.wikipedia.org/wiki/Deepika_Padukone",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Deepika_Padukone_2025_%281%29.png/500px-Deepika_Padukone_2025_%281%29.png"},

    {"name": "Amitabh Bachchan", "role": "Ashwatthama",
     "wiki": "https://en.wikipedia.org/wiki/Amitabh_Bachchan",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Indian_actor_Amitabh_Bachchan.jpg/500px-Indian_actor_Amitabh_Bachchan.jpg"},

    {"name": "Kamal Haasan", "role": "Supreme Yaskin",
     "wiki": "https://en.wikipedia.org/wiki/Kamal_Haasan",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Kamal_Haasan_at_2023_San_Diego_Comic-Con_International_by_Gage_Skidmore%2C_005_%28cropped%29.jpg/500px-Kamal_Haasan_at_2023_San_Diego_Comic-Con_International_by_Gage_Skidmore%2C_005_%28cropped%29.jpg"},

    {"name": "Disha Patani", "role": "Roxie",
     "wiki": "https://en.wikipedia.org/wiki/Disha_Patani",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Disha_Patani_and_others_grace_the_premiere_of_Gustaakh_Ishq_02.jpg/500px-Disha_Patani_and_others_grace_the_premiere_of_Gustaakh_Ishq_02.jpg"},


    {"name": "Saswata Chatterjee", "role": "Commander Manas",
     "wiki": "https://en.wikipedia.org/wiki/Saswata_Chatterjee",
     "img": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Saswata_Chatterjee.webp"},

    {"name": "Brahmanandam", "role": "Rajyam (Rumored)",
     "wiki": "https://en.wikipedia.org/wiki/Brahmanandam",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Brahmanandam_at_ANR_Awards.png/500px-Brahmanandam_at_ANR_Awards.png"},

    {"name": "Rajendra Prasad", "role": "Supporting Role",
     "wiki": "https://en.wikipedia.org/wiki/Rajendra_Prasad_(actor)",
     "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Rajendra_Prasad.png/500px-Rajendra_Prasad.png"},

]
}
if st.sidebar.button("Submit"):
    st.header("You have selected : " + x)
    with st.spinner("Loading..."):
        time.sleep(2)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Trailer", "Songs", "Movie Poster","Ratings","About Movie"])
    with tab1:
        st.write("Trailers for " + x)
        for link in video_links.get(x, []):
            st.video(link)
    with tab2:
        st.write("Songs for " + x)
        st.write(f"🎵 Total Music In {x} : {len(song_links.get(x, []))}")
        for link in song_links.get(x, []):
            com.iframe(link, height=80)
    with tab3:

        st.write("Movie Posters for " + x)
        for link in image_links.get(x, []):
            st.image(link)
    with tab4:
        st.subheader(f"Ratings for {x}")
        rat = ratings.get(x, {})

        col1, col2, col3 = st.columns(3)
        col1.metric("IMDb ⭐", rat.get("IMDb", "N/A"))
        col2.metric("Rotten Tomatoes 🍅", rat.get("Rotten Tomatoes", "N/A"))
        col3.metric("Metacritic 🎯", rat.get("Metacritic", "N/A"))
    with tab5:
        st.subheader(f"About {x}")
        info = Info.get(x, {})

        st.write(f"🎬 Year: {info.get('year', 'N/A')}")
        st.write(f"🎭 Genre: {info.get('genre', 'N/A')}")
        st.write(f"🎬 Director: {info.get('director', 'N/A')}")
        st.write(f"⭐ Cast: {info.get('cast', 'N/A')}")
        st.write(f"🔗 Wikipedia Links:")

       
        for actor in Wikip.get(x, []):
            col1, col2 = st.columns([1,3])

            with col1:
                st.image(actor["img"])

            with col2:
                st.markdown(f"### [{actor['name']}]({actor['wiki']})")
                st.write(f"🎭 Role: {actor['role']}")

        st.markdown("---")
        st.write(info.get("desc", "No description"))

        st.markdown("---")
        st.success(info.get("highlight", ""))
    