import tweepy
from pymongo import MongoClient
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from PIL.PngImagePlugin import PngInfo
import textwrap
import sys
from random import choice

client = MongoClient('mongodb://USER:PWD@IP:PORT')
db = client.database

# If you want run by command ligne less Database
#param = sys.argv[1]

#list_tables = ["python", "javascript", "reactjs", "flask", "django" ]

# if take all tag
""" tables = list(db.list_tag.find({}, {"tag": 1}))

for t in tables:
    list_tables.append(t["tag"]) """

# Shake the list
param = choice(list_tables)




try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

def get_question(table):

    try:
        question = list(db[table].find({"twitter": None, "publishext": 1},{"question":0}).limit(1))
        
    except Exception as e:
        print(f'Error  : {e}')

    for q in question:
        dataset = q
    
    return dataset

# create the wallpaper
def get_wallpaper(language, question, slug):

    metadata = PngInfo()
    metadata.add_text("Website", "https://xxxxxxxxx.xx")
    metadata.add_text("link", f'https://xxxxxxxxxxxx.xxxxxx/a/{language}/{slug}')
    # image_width
    image = Image.new('RGB', (800, 400), color=(55, 71, 79))
    font = ImageFont.truetype("Ubuntu-Regular.ttf", 40)
    font2 = ImageFont.truetype("Ubuntu-Regular.ttf", 30)
    language = f'{language.capitalize()} : '
    text1 = question
    text2  = "xxxxxxxxxxxxxxxxxxxxxx"
    text_color = (200, 200, 200)
    language_start_height = 30
    text_start_height = 100
    text2_start_height = 340
    draw_text_on_image(image, language, text1, text2, font, font2, text_color, language_start_height, text_start_height, text2_start_height)
    image.save('created_image.png', pnginfo=metadata)

# Apply text on wallpaper
def draw_text_on_image(image, language, text, text2, font, font2, text_color, language_start_height, text_start_height, text2_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    l_text = language_start_height
    y_text = text_start_height
    y_text2 = text2_start_height

    linesl = textwrap.wrap(language, width=40)    
    for line in linesl:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 6, l_text),line, font=font, fill=text_color)
        y_text += line_height

    lines = textwrap.wrap(text, width=40)    
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),line, font=font, fill=text_color)
        y_text += line_height

    lines2 = textwrap.wrap(text2, width=40)    
    for line in lines2:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 0.76, y_text2),line, font=font2, fill=text_color)
        y_text2 += line_height

#
# Main Function
#
def main(param):
    twitter_auth_keys = {
        "consumer_key"        : "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "consumer_secret"     : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "access_token"        : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "access_token_secret" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }

    q_t = param+"_question"

    g_question = get_question(q_t)
    
    # create the liste of tag
    tag = ''
    for t in  g_question["tags"]:
        tag +=  str(f'#{t} - ')

    tag = tag[:-2]

    print(f'{g_question["language"].capitalize()}: {g_question["title"]} - {tag}' )
    message = f'{g_question["language"].capitalize()}: {g_question["title"]} - {tag} - Answer link : https://xxxxxxxxxxxx.xx/x/{g_question["language"]}/{g_question["slug"]}'
    
    #Create the poster
    get_wallpaper(g_question["language"], g_question["title"], g_question["slug"])


    #### Auth tiwtter

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)


    # Upload image
    media = api.media_upload("created_image.png")

    # Post tweet with image
    tweet = message
    api.update_status(status=tweet, media_ids=[media.media_id])

    # If update database
    #db[q_t].update_one({"id": g_question["id"]},{"$set": {"twitter": 1 }})

# auto launch 
if __name__ == "__main__":
    main(param)