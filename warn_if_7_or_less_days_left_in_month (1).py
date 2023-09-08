import datetime
import calendar

def warn_if_7_or_less_days_left_in_month():
    # Hole das aktuelle Datum und die Zeit
    today = datetime.date.today()

    #hiermit habe ich getestet, ob die Code funktioniert, wenn der Tag 27 wäre
    #today = today.replace(day=27)

    # Berechne den letzten Tag des Monats
    #monthrange(year,month) returns der Wochentag des ersten Tages des Monats und die Anzahl der Tage im Monat zurück,
    # [1] weil ich nur die Anzahl der Tage im Monat brauche
    last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])
    #print(last_day_of_month)

    # Berechne die Anzahl der Tage bis zum letzten Tag des Monats
    days_left_in_month = (last_day_of_month - today).days
    #print(days_left_in_month)

    # Wenn es 7 oder weniger Tage bis zum letzten Tag des Monats sind, gib einen Warnhinweis aus
    if days_left_in_month <= 7:
       return True
    else:
        return False


