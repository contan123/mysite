from .models import Comment
from .forms import CommentForm
from django.http import JsonResponse

def submit_comment(request):
    comment_form = CommentForm(request.POST,user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['comment_object']
        comment.save()

        data = {}
        data['status'] = 'SUCCESS'
        data['avatar'] = comment.user.get_avatar()
        data['username'] = comment.user.get_nickname()
        data['comment_time'] = comment.created_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text'] = comment.text
    else:
        data = {}
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())

    return JsonResponse(data)