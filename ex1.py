import csv
from io import TextIOWrapper
from zipfile import ZipFile

MAX_LINES = 10000

# opens file for olympics table.
# CHANGE!
team_outfile = open("team.csv", 'w', )
team_outwriter = csv.writer(team_outfile, delimiter=",", quoting=csv.QUOTE_NONE)
game_outfile = open("game.csv", 'w', )
game_outwriter = csv.writer(game_outfile, delimiter=",", quoting=csv.QUOTE_NONE)
event_outfile = open("event.csv", 'w', )
event_outwriter = csv.writer(event_outfile, delimiter=",", quoting=csv.QUOTE_NONE)
medal_outfile = open("medal.csv", 'w', )
medal_outwriter = csv.writer(medal_outfile, delimiter=",", quoting=csv.QUOTE_NONE)
athlete_outfile = open("athlete.csv", 'w', )
athlete_outwriter = csv.writer(athlete_outfile, delimiter=",", quoting=csv.QUOTE_NONE)
plays_outfile = open("plays.csv", 'w', )
plays_outwriter = csv.writer(plays_outfile, delimiter=",", quoting=csv.QUOTE_NONE)
athletes = set()
teams = set()
games = set()
events = set()
medals = set()
all_rows = set()

# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    counter = 0
    with ZipFile('athlete_events.csv.zip') as zf:
        with zf.open('athlete_events.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',','') for v in row]
                row = [v.replace("'",'') for v in row]
                row = [v.replace('"','') for v in row]
                row = [v if v != 'NA' else "" for v in row]
                # in 'Sailing', the medal winning rules are different than the rest of olympic games, so they are discarded.
                if row[12] == "Sailing":
                    continue
                # In all years but 1956 summer, olympic games took place in only one city. we clean this fringe case out of the data.
                if row[9] == '1956' and row[11] == 'Stockholm':
                    continue
                # This country is associated with two different noc values, and is discarded.
                if row[6] == 'Union des Socits Franais de Sports Athletiques':
                    continue
                process_row(row)
                counter += 1
                if counter == MAX_LINES:
                    break
        plays_outfile.close()
        athlete_outfile.close()
        medal_outfile.close()
        event_outfile.close()
        game_outfile.close()
        team_outfile.close()


# process_row should splits row into the different csv table files
# CHANGE!!!
def process_row(row):
    if row[0] == "ID":
        team_outwriter.writerow([row[6], row[7]])
        game_outwriter.writerow([row[8], row[9], row[10], row[11]])
        event_outwriter.writerow([row[13], row[12]])
        medal_outwriter.writerow([row[14]])
        plays_outwriter.writerow([row[0], row[6], row[8], row[13], row[3], row[4], row[5], row[14]])  # add row to plays
        athlete_outwriter.writerow([row[0], row[6], row[8], row[1], row[2]])
        return
    if tuple(row) not in all_rows:  # check for duplicate rows
        all_rows.add(tuple(row))
    else:
        return
    if not (row[0], row[6], row[8], row[1], row[2]) in athletes:  # check for duplicate athlete row
        athletes.add((row[0], row[6], row[8], row[1], row[2]))
        athlete_outwriter.writerow([row[0], row[6], row[8], row[1], row[2]])
    if not (row[6], row[7]) in teams:  # check for duplicate team row
        teams.add((row[6], row[7]))
        team_outwriter.writerow([row[6], row[7]])
    if not (row[8], row[9], row[10], row[11]) in games:  # check for duplicate game row
        games.add((row[8], row[9], row[10], row[11]))
        game_outwriter.writerow([row[8], row[9], row[10], row[11]])
    if (row[13], row[12]) not in events:  # check for duplicate event row
        events.add((row[13], row[12]))
        event_outwriter.writerow([row[13], row[12]])
    if not (row[14]) in medals and row[14] != '':  # check for duplicate medal row
        medals.add((row[14]))
        medal_outwriter.writerow([row[14]])
    plays_outwriter.writerow([row[0], row[6], row[8], row[13], row[3], row[4], row[5], row[14]])  # add row to plays


# return the list of all tables
# CHANGE!!!
def get_names():
    return ["team", "game", "event", "medal", "athlete", "plays"]


if __name__ == "__main__":
    process_file()



