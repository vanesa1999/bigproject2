from rest_framework import serializers
from datetime import timedelta, tzinfo
from django.contrib.auth.models import User
from .models import Punonjes, Departament, Departament_per_punonjes, DitePushimi, Lejet, Pozicionet
from rest_framework.status import HTTP_404_NOT_FOUND
from datetime import datetime

def IsWeekend(day1, day2):
    delta1 = timedelta(days=1)
    dayt = 0
    while day2 >= day1:
        if (day2.isoweekday() == 6):
            dayt += 1
            print(day2)
        if (day2.isoweekday() == 7):
            dayt += 1
            print(day2)
        day2 = day2 - delta1
        print(dayt)
    return dayt


def llogaritoret(ora1, ora2, days):
    if days >= 1:
        if 10 <= ora1 <= 18:
            if 10 <= ora2 <= 18:
                if ora2 >= ora1:
                    totali = days * 8 + (ora2 - ora1)
                else:
                    totali = days * 8 + (ora1 - ora2)
            else:
                totali = days * 8 + (18 - ora1)
        elif ora1 < 10:
            if 10 <= ora2 <= 18:
                totali = days * 8 + (ora2 - 10)
            elif ora2 < 10:
                if ora2 >= ora1:
                    totali = days * 8
                else:
                    totali = (days + 1) * 8
            elif ora2 > 18:
                totali = (days + 1) * 8
        elif ora1 > 18:
            if 10 <= ora2 <= 18:
                totali = days * 8 + (ora2 - 10)
            elif ora2 < 10:
                totali = days * 8
            elif ora2 > 18:
                if ora2 >= ora1:
                    totali = days * 8
                else:
                    totali = (days + 1) * 8


    else:
        if ora2 >= ora1:
            if 10 <= ora1 <= 18:
                if 10 <= ora2 <= 18:
                    totali = ora2 - ora1
                elif ora2 > 18:
                    ora2 = 18
                    totali = ora2 - ora1
            elif ora1 < 10:
                if 10 <= ora2 <= 18:
                    ora1 = 10
                    totali = ora2 - ora1
                elif ora2 < 10:
                    totali = 0
                elif ora2 > 18:
                    ora2 = 18
                    ora1 = 10
                    totali = ora2 - ora1

            elif ora1 > 18:
                if ora2 > 18:
                    totali = 0
                else:
                    totali = 0
    return totali


class RrogaField(serializers.ReadOnlyField):
    def to_representation(self, value):
        pu = value.punonjes
        aa = Lejet.objects.filter(punonjes=pu, statusi='Pranuar', lloji_i_lejes='Leje e papaguar')
        print(aa)
        ta = 0
        now = datetime.now()
        for la in aa:
            if la.fillimi.month == now.month:
                if la.mbarimi.month == now.month:
                    tota = 0
                    ba = la.fillimi
                    ea = la.mbarimi
                    deltaa = ea - ba
                    daysa = deltaa.days
                    pushimet = IsWeekend(ba, ea)
                    tota = llogaritoret(ba.hour, ea.hour, daysa) - 8 * pushimet
                    ta += tota
                else:
                    tota = 0
                    ea = la.mbarimi
                    daysa = 31 - ba.day
                    ba = datetime(year=ba.year, month= ba.month+1 if ba.month != 12 else 1, day=1)
                    pushimet = IsWeekend(ba, ea)
                    tota = llogaritoret(24, ea.hour, daysa)
                    ta += tota
            else:
                if la.mbarimi.month == now.month:
                    tota = 0
                    ea = la.mbarimi
                    daysa = ea.day
                    tota = llogaritoret(0, ea.hour, daysa)
                    ta += tota
                else:
                    return

        rroga = ((176 - ta) / 176) * 100
        return ("Rroga juaj ne % per kete muaj", rroga, "%")



class OretField(serializers.ReadOnlyField):
    def to_representation(self, value):
        delta = value.mbarimi - value.fillimi
        days = delta.days
        n = IsWeekend(value.fillimi, value.mbarimi)
        ora1 = value.fillimi.hour
        ora2 = value.mbarimi.hour
        totali = llogaritoret(ora1, ora2, days) - n * 8

        return ("numri i diteve pushim gjate lejes:", n, "totali i oreve te punes pushim:", totali)

class RaportField(serializers.ReadOnlyField):
    def to_representation(self, value):
        startday = value.fillimi
        endday = value.mbarimi
        delta = endday - startday
        days = delta.days
        n = IsWeekend(value.fillimi, value.mbarimi)
        totali1 = 0
        pz = Pozicionet.objects.get(pozicioni='Punonjes Departamenti')
        d = Departament.objects.get(punonjes=value.punonjes)
        pt = Punonjes.objects.filter(pozicioni=pz, statusi='Aktiv', departamenti=d)
        b = Lejet.objects.filter(statusi='Pranuar', punonjes__in=pt)
        for x in b:
            if startday <= x.fillimi < endday:
                if x.mbarimi <= endday:
                    fillimi = x.fillimi
                    mbarimi = x.mbarimi
                    delta = mbarimi - fillimi
                    days = delta.days
                    # seconds= delta.seconds
                    ora1 = fillimi.hour
                    ora2 = mbarimi.hour
                    pushimet = IsWeekend(fillimi, mbarimi)
                    totali = llogaritoret(ora1, ora2, days) - 8 * pushimet
                    print("la", pushimet, totali)
                elif x.mbarimi > endday:
                    fillimi = x.fillimi
                    mbarimi = endday
                    delta = mbarimi - fillimi
                    days = delta.days
                    ora1 = fillimi.hour
                    ora2 = mbarimi.hour
                    pushimet = IsWeekend(fillimi, mbarimi)
                    totali = llogaritoret(ora1, ora2, days) - 8 * pushimet
                    print("lo", totali)
            elif startday <= x.mbarimi < endday:
                if x.mbarimi <= endday:
                    fillimi = startday
                    mbarimi = x.mbarimi
                    delta = mbarimi - fillimi
                    days = delta.days
                    # seconds= delta.seconds
                    ora1 = fillimi.hour
                    ora2 = mbarimi.hour
                    pushimet = IsWeekend(fillimi, mbarimi)
                    totali = llogaritoret(ora1, ora2, days) - 8 * pushimet
                    print("la", pushimet, totali)
                elif x.mbarimi > endday:
                    fillimi = startday
                    mbarimi = endday
                    delta = mbarimi - fillimi
                    days = delta.days
                    ora1 = fillimi.hour
                    ora2 = mbarimi.hour
                    pushimet = IsWeekend(fillimi, mbarimi)
                    totali = llogaritoret(ora1, ora2, days) - 8 * pushimet
                    print("lo", totali)

            totali1 += totali
            print(totali1)

        tot = llogaritoret(startday.hour, endday.hour, days)
        p = pt.count()
        totall = (tot- 8*n) * p - totali1
        pu = value.punonjes
        aa = Lejet.objects.filter(punonjes=pu, statusi='Pranuar', lloji_i_lejes='Leje e paguar')
        ta = 0
        for la in aa:
            tota = 0
            ba = la.fillimi
            ea = la.mbarimi
            deltaa = ea - ba
            daysa = deltaa.days
            tota = llogaritoret(ba.hour, ea.hour, daysa)- 8*n
            ta += tota
        return ("totali i oreve leje te marra nga gjithe punonjesit gjate periudhes:", totali1,
                "totali i oreve aktive te punes per periudhen e lejes:", totall,
                'totali i oreve lejeve te paguara te marra nga punonjesi', ta)


class PunonjesHrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punonjes
        fields = "__all__"


class DepartamentHrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'


class DepartamentPerPunonjesSerializer(serializers.ModelSerializer):
    titulli = serializers.SerializerMethodField('get_titulli_from_departament')
    pergjegjesi = serializers.SerializerMethodField('get_pergjegjesi_from_departament')

    class Meta:
        model = Departament_per_punonjes
        fields = ['punonjes', 'info', 'titulli', 'pergjegjesi']

    def get_titulli_from_departament(self, departament_per_punonjes):
        titulli = departament_per_punonjes.info.titulli
        return titulli

    def get_pergjegjesi_from_departament(self, departament_per_punonjes):
        pergjegjesi = departament_per_punonjes.info.pergjegjesi.__str__()
        return pergjegjesi

class UserHrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'id']

class DitePushimiHrSerializer(serializers.ModelSerializer):
    class Meta:
        model = DitePushimi
        fields = '__all__'

class LejetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lejet
        fields = ['data_e_kerkeses', 'lloji_i_lejes', 'fillimi', 'mbarimi', 'arsyetimi']

class LejetViewSerializer(serializers.ModelSerializer):
    rroga = RrogaField(source='*')

    class Meta:
        model = Lejet
        fields = ['rroga', 'id', 'data_e_kerkeses', 'lloji_i_lejes', 'fillimi', 'mbarimi', 'statusi', 'arsyetimi',
                  'punonjes']


class LejetHrViewSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Lejet
        fields = '__all__'


class LejetHrViewSerializer(serializers.ModelSerializer):
    oret = OretField(source='*')
    raport = RaportField(source='*')

    class Meta:
        model = Lejet
        fields = ['data_e_kerkeses', 'raport', 'lloji_i_lejes', 'fillimi', 'mbarimi', 'punonjes', 'id', 'statusi',
                  'oret', 'arsyetimi', ]
        extra_kwargs = {'data_e_kerkeses': {'read_only': True},
                        'lloji_i_lejes': {'read_only': True},
                        'fillimi': {'read_only': True},
                        'mbarimi': {'read_only': True},
                        'punonjes': {'read_only': True},
                        'id': {'read_only': True},
                        }




