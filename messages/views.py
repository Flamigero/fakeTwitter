"""Messages views"""

# Django
from django.shortcuts import render, redirect

# Models
from .models import Message

def feed(request):
    

    tweets = Message.objects.raw("""
        select id, text, user_id, retweet_id from twitter_messages_message where retweet_id IS NULL
        union
        select t.id, m.text, t.user_id, t.retweet_id from twitter_messages_message t inner join twitter_messages_message m on t.retweet_id = m.id
    """)

    return render(request, 'feed.html', {
        'tweets': tweets
    })