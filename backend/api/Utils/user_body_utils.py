

from accounts.models import User, BodyInfoRecord, UserBodyInfo


def save_userbody(user, validated_data, week_diet):
    user = user[0]
    user = User.objects.filter(id=user.id).first()
    is_record = UserBodyInfo    .objects.filter(user=user).all()

    if len(is_record) > 0:
        userbodyinfo = UserBodyInfo.objects.filter(user=user).first()
        userbodyinfo.age=validated_data['age']
        userbodyinfo.weight=validated_data['weight']
        userbodyinfo.height=validated_data['height']
        userbodyinfo.gender=validated_data['gender']
        userbodyinfo.general=validated_data['general_activity']
        userbodyinfo.excise=validated_data['excise_activity']

        userbodyinfo.save()
    else:
        userbodyinfo = UserBodyInfo.objects.create(
            user=user,
            age=validated_data['age'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            gender=validated_data['gender'],
            general=validated_data['general_activity'],
            excise=validated_data['excise_activity'],
        )

    record = BodyInfoRecord.objects.create(
        user = user,
        age=validated_data['age'],
        weight=validated_data['weight'],
        height=validated_data['height'],
        gender=validated_data['gender'],
        general=validated_data['general_activity'],
        excise=validated_data['excise_activity'],
        week_diet= week_diet
    )
    return userbodyinfo, record