def avatar_url(request):
    if request.user.is_authenticated and hasattr(request.user, 'profesional') and request.user.profesional.avatar:
        return {'avatar_url': request.user.profesional.avatar.url}
    return {'avatar_url': None}
