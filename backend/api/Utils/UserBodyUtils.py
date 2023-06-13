

from accounts.models import BodyInfoRecord, User, UserBodyInfo


def save_userbody(user_id, validated_data, week_diet):
    is_record = BodyInfoRecord.objects.filter(user__id=user_id).all()
    user = User.objects.filter(id=user_id).first()

    if len(is_record) > 0:
        userbodyinfo = UserBodyInfo.objects.filter(user=user).first()
        userbodyinfo.age=validated_data['age']
        userbodyinfo.weight=validated_data['weight']
        userbodyinfo.height=validated_data['height']
        userbodyinfo.gender=validated_data['gender']
        userbodyinfo.general=validated_data['general_activity']
        userbodyinfo.activity=validated_data['excise_activity']

        userbodyinfo.save()
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

    record = BodyInfoRecord.objects.create(
        user = user,
        age=validated_data['age'],
        weight=validated_data['weight'],
        height=validated_data['height'],
        gender=validated_data['gender'],
        general=validated_data['general_activity'],
        activity=validated_data['excise_activity'],
        week_diet= week_diet.id
    )
    return userbodyinfo, record