# -*- coding: utf-8 -*-
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from forms import SearchForm
from arduino.arduinoMorse import ArduinoMorse

def encode(request):
    text=""
    morse=[]
    if request.method == 'GET':         
        form = SearchForm(request.GET) 
        if form.is_valid():
            text = form.cleaned_data['text']
            arduino=ArduinoMorse(text)
            arduino.start()
            for x in text :
                if x=='a' or x=='A':
                    morse.append('.-')
                elif x=='b' or x=='B':
                    morse.append('-...')
                elif x=='c' or x=='C':
                    morse.append('-.-.')
                elif x=='d' or x=='D':
                    morse.append('-..')
                elif x=='e' or x=='E':
                    morse.append('.')
                elif x=='f' or x=='F':
                   morse.append('..-.')
                elif x=='g' or x=='G':
                    morse.append('--.')
                elif x=='h' or x=='H':
                    morse.append('....')
                elif x=='i' or x=='I':
                    morse.append('..')
                elif x=='j' or x=='J':
                    morse.append('.---')
                elif x=='k' or x=='K':
                    morse.append('-.-')
                elif x=='l' or x=='L':
                    morse.append('.-..')
                elif x=='m' or x=='M':
                    morse.append('--')
                elif x=='n' or x=='N':
                    morse.append('-.')
#                elif x=='ñ' or x=='Ñ':
#                    morse.append('--.--')
                elif x=='o' or x=='O':
                    morse.append('---')     
                elif x=='p' or x=='P':
                    morse.append('.--.')
                elif x=='q' or x=='Q':
                    morse.append('--.--')
                elif x=='r' or x=='R':
                    morse.append('.-.')
                elif x=='s' or x=='S':
                    morse.append('...')
                elif x=='t' or x=='T':
                    morse.append('-')
                elif x=='u' or x=='U':
                    morse.append('..-')
                elif x=='v' or x=='V':
                    morse.append('...-')
                elif x=='w' or x=='W':
                    morse.append('.--')
                elif x=='x' or x=='X':
                    morse.append('-..-')
                elif x=='y' or x=='Y':
                    morse.append('-.--')
                elif x=='z' or x=='Z':
                    morse.append('--..')
                elif x=='0':
                    morse.append('-----')
                elif x=='1':
                    morse.append('.----')
                elif x=='2':
                    morse.append('..---')
                elif x=='3':
                    morse.append('...--')
                elif x=='4':
                    morse.append('....-')
                elif x=='5':
                    morse.append('.....')
                elif x=='6':
                    morse.append('-....')
                elif x=='7':
                    morse.append('--...')
                elif x=='8':
                    morse.append('---..')                
                elif x=='9':
                    morse.append('----.')
                elif x=='.':
                    morse.append('.-.-.-')
                elif x==',':
                    morse.append('--..--')
                elif x=='?':
                    morse.append('..--..')
                elif x=='"':
                    morse.append('.-..-.')
                elif x==' ':
                    morse.append(' ')          
        else:
            queryset = []
    form = SearchForm() 
    return render_to_response("arduino/index.html", {'form': form, "text": text, "morse": morse})
    
