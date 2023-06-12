

from accounts.models import BodyInfoRecord, UserBodyInfo


def save_userbody(user, validated_data):
    if user is not None:
        userbodyinfo = UserBodyInfo.objects.filter(user=user).update(
            user=user,
            age=validated_data['age'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            gender=validated_data['gender'],
            general=validated_data['general_activity'],
            activity=validated_data['excise_activity'],
        )
        BodyInfoRecord.objects.create(
            user = user,
            age=validated_data['age'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            gender=validated_data['gender'],
            general=validated_data['general_activity'],
            activity=validated_data['excise_activity'],
        )
    else:
        userbodyinfo = UserBodyInfo.objects.create(
            user=user,
            age=validated_data['age'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            gender=validated_data['gender'],
            general=validated_data['general_activity'],
            activity=validated_data['excise_activity'],
        )

    return userbodyinfo