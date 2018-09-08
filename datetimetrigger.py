import sys
import calendar
import datetime

year = datetime.date.today().year
month = 11
if len(sys.argv) > 1:
    try:
        year = int(sys.argv[-1])
    except ValueError:
        pass

last_sat = max(week[-2] for week in calendar.monthcalendar(year, month))
print('{}-{}-{:2}'.format(year, calendar.month_abbr[month], last_sat))
print("last_sat")
print(last_sat)

agm_date = datetime.datetime(year, month, last_sat, 19, 0, 0, 0)
print("AGM Date:" + str(agm_date))

voting_conclusion = agm_date - datetime.timedelta(hours=19, minutes=1)
print("voting_conclusion:"+str(voting_conclusion))

voting_last_chance = agm_date - datetime.timedelta(days=5)
print("voting_last_chance:"+str(voting_last_chance))

agm_notice = agm_date - datetime.timedelta(days=17)
print("agm_notice:" + str(agm_notice))

voting_commences = agm_date - datetime.timedelta(days=30)
print("voting_commences:" + str(voting_commences))

voting_notice = voting_commences - datetime.timedelta(days=17)
print("voting_notice:"+str(voting_notice))

candidate_call = voting_notice - datetime.timedelta(days=30)
print("candidate_call:"+str(candidate_call))

ro_call = candidate_call - datetime.timedelta(days=30)
print("ro_call:"+str(ro_call))

while True:
    now = datetime.datetime.now()
    if now == ro_call:
        print("Trigger RO Call")
        print("Tweet to @GeekZoneBot: I have issued the RO call!")

    if now == candidate_call:
        print("Trigger Candidate Call")
        print("Tweet to @GeekZoneBot: I have issued the Candidate Call!")

    if now == voting_notice:
        print("Trigger Voting Notice")
        print("Tweet to @GeekZoneBot: I have issued the Voting Notice!")

    if now == voting_commences:
        print("Trigger Voting Commences")
        print("Tweet to @GeekZoneBot: I have issued the Voting Commencement Notice!")

    if now == agm_notice:
        print("Trigger AGM Notice")
        print("Tweet to @GeekZoneBot: I have issued the AGM Notice!")

    if now == voting_last_chance:
        print("Trigger Voting Last Chance")
        print("Tweet to @GeekZoneBot: I have issued the Voting Last Chance Notice!")

    if now == voting_conclusion:
        print("Trigger Voting Conclusion")
        print("Tweet to @GeekZoneBot: I have issued the Voting Conclusion Notice!")

    if now == agm_date:
        print("Trigger AGM Start")
        print("Tweet to @GeekZoneBot: I have issued the AGM Start Notice!")
