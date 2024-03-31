from rest_framework_simplejwt.tokens import RefreshToken


def get_user_slug(instance):
    return (
        f"{instance.first_name}-{instance.last_name}-{str(instance.uid).split('-')[0]}"
    )


def get_user_address_slug(instance):
    return f"{instance.country.lower()}-{str(instance.uid).split('-')[0]}"


def get_user_media_path_prefix(instance, filename):
    return f"media/users/{instance.id}-{instance.slug}/{filename}"


def get_token(user):
    """
    @user take the user instance.
    @response -> return refresh token and access token.
    """
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token)
