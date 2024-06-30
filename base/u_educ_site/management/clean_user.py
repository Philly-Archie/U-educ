from apis.models import UserModel

class Command(BaseCommand): # type: ignore
    help = 'Remove users with no fullName value'

    def handle(self, *args, **kwargs):
        # Filter users where fullName is empty or null
        users_to_delete = UserModel.objects.filter(fullName__isnull=True) | UserModel.objects.filter(fullName='')
        
        # Delete the filtered users
        count, _ = users_to_delete.delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} users with no fullName value'))
