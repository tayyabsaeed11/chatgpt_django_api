# chatgpt_django_api
A REST API that enables user registration/login and access to OpenAI's ChatGPT API with daily usage limits for free users.

# Features

- JWT Authentication**: Secure user registration and login system
- Usage Tracking**: Free users get 5 requests/day with automatic daily reset
- Premium Support**: Option to upgrade for unlimited access (premium flag implementation)
- API Monitoring**: Tracks last request time and remaining quota
- Rate Limiting**: Automatic quota enforcement with informative error messages

#Create Virtual Environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

#Install Dependencies:
pip install -r requirements.txt

#Environment Setup:
DJANGO_SECRET_KEY=secret-key-here
OPENAI_API_KEY=openai-api-key-here

#Required Packages:
asgiref==3.8.1
certifi==2025.4.26
charset-normalizer==3.4.2
Django==5.2
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
idna==3.10
PyJWT==2.9.0
python-dotenv==1.1.0
requests==2.32.3
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.4.0


#API Endpoints:
User Registration
 path('register/', RegisterView.as_view(), name='register'),
 ![0](https://github.com/user-attachments/assets/b676a6b5-d0c9-4591-889e-855f01b44e11)

User Login:
path('login/', LoginView.as_view(), name='token_obtain_pair'),
![1](https://github.com/user-attachments/assets/80be7bb8-1234-4107-be65-038df1ff47e2)

ChatGPT Request:
path('chat/', ChatView.as_view(), name='chat'),
![5](https://github.com/user-attachments/assets/d1fdd50d-f11d-4d13-8faa-a3cab84c4f52)
![6](https://github.com/user-attachments/assets/e46ef2f6-2310-41c4-a831-3087c177056d)

#Environment Variables
Variable	Description
DJANGO_SECRET_KEY	Secret key for Django application
OPENAI_API_KEY	OpenAI API key for ChatGPT access

Important Notes
Keep .env file secure and never commit it to version control
Free tier users get 5 requests per 24-hour period
System automatically resets quotas at midnight UTC






