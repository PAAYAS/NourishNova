<div>
<h1 align="center">NourishNova</h1>
  <h4>Empowering you to make nutritious choices</h4>
</div>

## 🌟 Inspiration:
The inspiration behind NourishNova stems from the pressing issue of student food insecurity. Recognizing the need for innovative solutions to address this challenge, the project aims to utilize technology to connect students with resources and revamp campus dining. By creating sustainable food assistance programs, NourishNova seeks to empower college and university students to find affordable and nutritious meals, ensuring their well-being and academic success.

## 💡 What it does:
NourishNova is a comprehensive nutrition app specifically designed to tackle student food insecurity. It leverages technology to connect students with affordable and nutritious meal options on campus. The app serves as a hub for accessing information about available resources, such as food pantries, meal discounts, and community programs. By providing a centralized platform, NourishNova helps students make informed choices and access the support they need to overcome food insecurity.

## 🔧 How we built it:
NourishNova was built using a combination of technologies and methodologies. The backend utilizes the FastAPI framework, enabling the development of fast and efficient web APIs. The frontend is designed with Streamlit, an open-source app framework in Python, providing an intuitive and user-friendly interface for students. Additionally, extensive research and collaboration with campus dining services and community organizations were conducted to gather accurate and up-to-date information on available resources.

#### Dataset:
I used Food.com kaggle dataset Data with over 500,000 recipes and 1,400,000 reviews from Food.com. Visit this [kaggle](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews?select=recipes.csv) link for more details.

#### Backend Developement:

The application is built using the FastAPI framework, which allows for the creation of fast and efficient web APIs. When a user makes a request to the API (user data,nutrition data...) the model is used to generate a list of recommended food similar/suitable to his request (data) which are then returned to the user via the API.

#### Frontend Developement:

The application's front-end is made with Streamlit. Streamlit is an open source app framework in Python language. It helps to create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. For our case the front-end is composed of three web pages. The main page is Hello.py which is a welcoming page used to introduce you to my project. The side bar on the left allows the user to navigate too the automatic diet recommendation page and the custom food recommendation page. In the diet recommendation page the user can fill information about his age,weight,height.. and gets a diet recommendation based on his information. Besides, the custom food recommendation allows the user to specify more his food preferency using nutritional values.

#### Technologies:
The project is created with:
* Python: 3.10.8
* fastapi 0.88.0
* uvicorn 0.20.0
* scikit-learn 1.1.3
* Pandas: 1.5.1
* Streamlit: 1.16.0
* streamlit-echarts 1.24.1
* Numpy: 1.21.5
* beautifulsoup4 4.11.1

![](https://img.icons8.com/color/48/null/python--v1.png)![](https://img.icons8.com/color/48/null/numpy.png)![](Assets/streamlit-icon-48x48.png)![](Assets/fastapi.ico)![](Assets/scikit-learn.ico) ![](https://img.icons8.com/color/48/null/pandas.png)

## 🚀 Challenges we ran into:
During the development process, several challenges were encountered, including:
- Gathering comprehensive and up-to-date information about available resources across various campuses and communities.
- Ensuring the accuracy and reliability of the data presented on the platform.
- Addressing the complex logistics of connecting students with local food assistance programs and discounts.

## 🏆 Accomplishments that we're proud of:
Throughout the development of NourishNova, several accomplishments were achieved, including:
- Building a user-friendly app interface that provides easy access to information and resources.
- Establishing partnerships with campus dining services and community organizations to ensure the availability of accurate and relevant data.
- Creating a platform that can potentially transform the way students access and benefit from food assistance programs.

## 🎓 What we learned:
The development process of NourishNova provided valuable insights and learnings, such as:
- Understanding the importance of leveraging technology to address social issues like student food insecurity.
- Recognizing the significance of collaboration with campus stakeholders and community organizations to ensure the success and sustainability of the platform.
- Gaining knowledge about the complexities of logistics and data management involved in creating a comprehensive resource hub.

## 🔜 What's next for NourishNova:
The future of NourishNova holds promising opportunities, including:
- Expanding the platform to include additional campuses and communities, catering to a larger student population.
- Integrating features for real-time updates on available resources and meal options.
- Exploring partnerships with local businesses to provide exclusive discounts and promotions for students.
- Collecting feedback from users and continuously improving the platform to meet the evolving needs of students.

Overall, NourishNova aims to bring about positive change in addressing student food insecurity by utilizing technology and fostering collaboration among campus stakeholders and community organizations. With its user-friendly interface and comprehensive resource hub, NourishNova is poised to make a significant impact in ensuring affordable and nutritious meals for college and university students.

## Setup

### Run it locally
#### Clone the repo
```
$ git clone https://github.com/PAAYAS/NourishNova.git
```
Go to Streamlit_Frontend directory and run:
```
$ python -m streamlit run NourishNova.py
```
Go to FastAPI_Backend directory and run:
```
$ python -m uvicorn main:app
```
Then open http://localhost:8501 and enjoy :smiley:.
