from django.core.management.base import BaseCommand
  
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data.csv')

    def handle(self, *args, **options):
        colnames = [f.name for f in Squirrel._meta.fields]
        with open(options['squirrel_data.csv'], 'w') as fo:
            writer = csv.writer(fo)
            tup = ['Latitude',
                    'Longitude',
                    'Unique_Squirrel_ID',
                    'Shift',
                    'Date',
                    'Age',
                    'Primary_Fur_Color',
                    'Location',
                    'Specific_Location',
                    'Running',
                    'Chasing',
                    'Climbing',
                    'Eating',
                    'Foraging',
                    'Other_Activities',
                    'Kuks',
                    'Quaas',
                    'Moans',
                    'Tail_flags',
                    'Tail_twitches',
                    'Approaches',
                    'Indifferent',
                    'Runs_from'
                    ]
            writer.writerow(tup)

            for row in Squirrel.objects.all():
                rowOk = [getattr(row, field) for field in fields_list]
                writer.writerow(rowOk)
