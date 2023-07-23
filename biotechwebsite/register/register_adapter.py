from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import pdb


class RegisterInvitationAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        # invitation_accepted = request.session.get('invitation_accepted', False)
        # # pdb.set_trace()
        # if invitation_accepted is True:
        #     return True
        # else:
        return False
