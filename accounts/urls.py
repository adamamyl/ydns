##
# YDNS Core
#
# Copyright (c) 2015 Christian Jurk <commx@commx.ws>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##

from django.conf.urls import patterns, include, url
from .views import (ActivationView, FacebookSignInView, GithubSignInView, GoogleSignInView, LoginView, LoginOtpView,
                    LogoutView, ResetPasswordView, ResetPasswordUpdateView, SetLanguageView, SignupView,
                    TwitterSignInView)

urlpatterns = patterns('',
    url(r'^activate$', ActivationView.as_view(), name='activate'),
    url(r'^signup$', SignupView.as_view(), name='signup'),
    url(r'^login/otp$', LoginOtpView.as_view(), name='login_otp'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^oauth/facebook$', FacebookSignInView.as_view(), name='facebook_sign_in'),
    url(r'^oauth/github$', GithubSignInView.as_view(), name='github_sign_in'),
    url(r'^oauth/google$', GoogleSignInView.as_view(), name='google_sign_in'),
    url(r'^oauth/twitter$', TwitterSignInView.as_view(), name='twitter_sign_in'),
    url(r'^reset-password/update$', ResetPasswordUpdateView.as_view(), name='reset_password_update'),
    url(r'^reset-password$', ResetPasswordView.as_view(), name='reset_password'),
    url(r'^set-language/(?P<lc>[\w-]{2,5})$', SetLanguageView.as_view(), name='set_language'),
    url(r'^settings/', include('accounts.settings.urls', namespace='settings')),
)