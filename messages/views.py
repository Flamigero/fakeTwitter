"""Messages views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator

# Models
from .models import Message

# Forms
from messages.forms import TweetForm

@method_decorator(login_required, name='dispatch')
class Feed(View):
    template_name = 'feed.html'
    tweetsQuery = """
            select id, text, user_id, retweet_id from twitter_messages_message where retweet_id IS NULL
            union
            select t.id, m.text, t.user_id, t.retweet_id from twitter_messages_message t inner join twitter_messages_message m on t.retweet_id = m.id
        """

    def get(self, request):
        tweets = Message.objects.raw(self.tweetsQuery)
        return render(request, self.template_name, {
            'tweets': tweets
        })

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()

        tweets = Message.objects.raw(self.tweetsQuery)
        return render(request, self.template_name, {
            'tweets': tweets
        })