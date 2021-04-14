import csv

from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Cammand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
                reader = csv.DictReader(fp)
                data = list(reader)
                
        def boolstr(obj):
            if str(obj).lower == 'true':
                return True
            else:
                return False

        sqs = []
        for dict_ in data:
            print('Start Creating')
            sqs.append(Squirrel(
                Latitude=dict_['Y'], #Notice the sequence for exportation
                Longitude=dict_['X'],
                Unique_Squirrel_ID=dict_['Unique Squirrel ID'],
                Shift=dict_['Shift'],
                Date='-'.join([str(dict_['Date'])[4:8], str(dict_['Date'])[0:2], str(dict_['Date'])[2:4]]),
                Age=dict_['Age'] if str(dict_['Age'])!='nan' else 'Unknown',
                Primary_Fur_Color = dict_['Primary Fur Color'] if str(dict_['Primary Fur Color'])!='nan' else 'Unknown',
                Location = dict_['Location'] if str(dict_['Location'])!='nan' else 'Unknown',
                Specific_Location = str(dict_['Specific Location']),
                Running = boolstr(dict_['Running']),
                Chasing = boolstr(dict_['Chasing']),
                Climbing = boolstr(dict_['Climbing']),
                Eating = boolstr(dict_['Eating']),
                Foraging = boolstr(dict_['Foraging']),
                Other_Activities = str(dict_['Other Activities']),
                Kuks = boolstr(dict_['Kuks']),
                Quaas = boolstr(dict_['Quaas']),
                Moans = boolstr(dict_['Moans']),
                Tail_flags = boolstr(dict_['Tail flags']),
                Tail_twitches = boolstr(dict_['Tail twitches']),
                Approaches = boolstr(dict_['Approaches']),
                Indifferent = boolstr(dict_['Indifferent']),
                Runs_from = boolstr(dict_['Runs from'])))

        Squirrel.objects.bulk_create(sqs)
