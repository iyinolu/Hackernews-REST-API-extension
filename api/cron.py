import os
from django.conf import settings
import requests
import pyrebase
from api.models import Story, Comments


def fetch_hn_data():
    config = {
        "databaseURL": os.environ.get('DATABASE_URL', default=""),
        "apiKey": "",
        "authDomain": "",
        "storageBucket": ""
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    top_stories = db.child("topstories").get().val()

    if isinstance(top_stories, list):
        print('---- STORY -----')
        for storyId in top_stories:
            story = dict(db.child("item").child(str(storyId)).get().val())
            storyData = {
                "type": story["type"],
                "url": story["url"] if "url" in story.keys() else "",
                "title": story["title"] if "title" in story.keys() else "",
                "text": story["text"] if "text" in story.keys() else "",
                "id": story["id"] if "id" in story.keys() else ""
            }

            storyObject, status  = Story.objects.get_or_create(**storyData)

            print(storyObject)
            print('---- COMMENT -----')
            if status:
                try:
                    for commentId in story["kids"]:
                        comment = dict(db.child("item").child(
                            str(commentId)).get().val())

                        commentData = {
                            "story": storyObject,
                            "text": comment["text"] if "text" in comment.keys() else "",
                            "id": comment["id"] if "id" in comment.keys() else ""
                        }
                        
                        commentObj = Comments.objects.get_or_create(**commentData)[0]
                        print(commentObj)
                        print("")
                except KeyError:
                    pass
            else:
                break

        print("%---------End Of Story----------%")
        print("")
        print("")
        print("")
        print("")
