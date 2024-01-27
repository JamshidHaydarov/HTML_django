from django.shortcuts import render

def main_menu(request):
    print(str(request))
    first_person = {261: ('Alfred Alan', 'aalan@qmail.com', 'Stocks')}
    second_person = {227: ('Alison Smart', 'asmart@biztalk.com', ' Residential Property')}
    thirst_person = {246: ('Ally Emery', 'allye@easymail.com', 'Stocks')}
    fourth_person = {212: ('Andrew Phips', 'andyp@mycorp.com', 'Stocks')}
    fifth_person = {218: ('Ann Melan', 'ann melan@iinet.com', 'Residential Property')}
    sixth_person = {221: ('Alfred Alan', 'aalan@qmail.com', 'Stocks')}
    seventh_person = {243: ('Alfred Alan', 'aalan@qmail.com', 'Stocks')}
    eights_person = {232: ('Alfred Alan', 'aalan@qmail.com', 'Stocks')}
    nineth_person = {233: ('Alfred Alan', 'aalan@qmail.com', 'Stocks')}
    tenth_person = {241: ('Alfred Alan', 'aalan@qmail.com', 'Stocks')}

    return render(request=request, template_name='index.html', context={"first": first_person, "second": second_person, "thirst": thirst_person, "fourth": fourth_person, "fifth": fifth_person, "sixth": sixth_person, "seventh": seventh_person, "eight": eights_person, "nineth": nineth_person, "tenth": tenth_person})
