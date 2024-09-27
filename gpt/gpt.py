from dotenv import load_dotenv
import instaloader
import openai
import os

load_dotenv()

def parse_instagram(username):
    L = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(L.context, username)
    bio = profile.biography
    # profile_pic_url = profile.profile_pic_url
    posts_title = []

    for post in profile.get_posts():
        posts_title.append(post.caption)
        if len(posts_title) > 10:
            break
    return {
        'bio': bio,
        'posts_title': posts_title
    }

def generate_message(bio, posts_title):
    prompt = (f'Я аналізую профіль Instagram. Ось біографія: "{bio}.'
              f'Пости цього профілю: {posts_title}.'
              f'На основі цієї інформації згенеруй перше повідомлення для знайомства.'
              f'Повідомлення має бути природним і дружнім, з акцентом на персоналізацію.')

    client = openai.OpenAI(api_key=os.getenv('api_key'))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system", "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo"
    )
    return chat_completion.choices[0].message.content
