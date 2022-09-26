import logging
import pyrebase
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import register_events
from api.models import Story, Comments
from decouple import config
from django.conf import settings

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

def fetch_HN_data():
    firebase_config = {
        "databaseURL": config('HN_DATABASE_URL'),
        "apiKey": "",
        "authDomain": "",
        "storageBucket": ""
    }
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    top_stories = db.child("topstories").get().val()

    if isinstance(top_stories, list):
        for storyId in top_stories:
            story = dict(db.child("item").child(str(storyId)).get().val())
            storyData = {
                "type": story["type"],
                "url": story["url"] if "url" in story.keys() else "",
                "title": story["title"] if "title" in story.keys() else "",
                "text": story["text"] if "text" in story.keys() else "",
                "storyId": story["id"] if "id" in story.keys() else ""
            }

            storyObject, status  = Story.objects.get_or_create(**storyData)

            if status:
                try:
                    for commentId in story["kids"]:
                        comment = dict(db.child("item").child(
                            str(commentId)).get().val())

                        commentData = {
                            "story": storyObject,
                            "text": comment["text"] if "text" in comment.keys() else "",
                            "commentId": comment["id"] if "id" in comment.keys() else ""
                        }
                        
                        Comments.objects.get_or_create(**commentData)[0]
                except KeyError:
                    pass
            else:
                # Break data fetching when an exiting story ID has been previously created.
                # Assuming that the returned data from firebase has a consistent ordering,
                # with lastest data at the start of the returned array [top_stories].
                break


def start():
    if settings.DEBUG:
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    scheduler.add_job(fetch_HN_data, trigger=CronTrigger(minute="*/5"), id="sync_test", replace_existing=True)

    register_events(scheduler)

    scheduler.start()