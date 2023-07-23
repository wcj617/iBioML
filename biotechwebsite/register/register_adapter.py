from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class RegisterInvitationAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        # invitation_accepted = request.session.get('invitation_accepted', False)
        # # pdb.set_trace()
        # if invitation_accepted is True:
        #     return True
        # else:
        # domain-expert1@gmail.com
        # www.localhost.com/signup?token=askdjflskjjn12387iush8123123d&email=domain-expert1@gmail.com
        # token = get_token_param(request.url)
        # email = validate_token(token)

        # A (app) <- POST /monitoring/<uuid> {fraud detected} HTTP (subscriber pattern) B (monitoring) fraud login 
         # C
        return True
