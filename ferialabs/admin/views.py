import tempfile

from flask import Response, request, send_file
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.template import EndpointLinkRowAction
from werkzeug.exceptions import HTTPException

from ferialabs.admin import basic_auth
from ferialabs.application import flask_application
from ferialabs.db import db_session, models


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                response="You could not be authenticated. Please refresh the page.",
                status=401,
                headers={"WWW-Authenticate": 'Basic realm="Login Required"'},
            ),
        )


class BasicHTTPAuthMixin:
    """
    Basic HTTP Auth Mixin
    Implements HTTP Basic Auth in 2 methods that are used by `Flask-Admin` views:
    `is_accessible`, `inaccessible_callback`
    """

    @staticmethod
    def is_accessible() -> bool:
        """
        Authorize the user request by HTTP Basic Auth rule. Throw an AuthException if the request wasn't
        authorized
        :return: True if the request was authorized
        """
        auth_obj = basic_auth.get_auth()
        password = basic_auth.get_auth_password(auth_obj)

        if not basic_auth.authenticate(auth_obj, password):
            raise AuthException("Not authenticated.")

        return True



class FerialabsAdminIndexView(BasicHTTPAuthMixin, AdminIndexView):
    """
    Index Page for the project Admin dashboard.
    Inherits a Basic HTTP protection rule from `BasicHTTPAuthMixin`
    """

class FerialabsAdminModelView(BasicHTTPAuthMixin, ModelView):
    """
    Model View class for Admin Dashboard.
    Inherits a Basic HTTP protection rule from `BasicHTTPAuthMixin`
    """


class PortfolioProjectAdminView(FerialabsAdminModelView):
    pass


admin = Admin(
    flask_application,
    name="Feria Labs Website Admin",
    template_mode="bootstrap3",
    index_view=FerialabsAdminIndexView(url="/"),
)
admin.add_view(PortfolioProjectAdminView(models.Project, db_session, name="Portfolio Project"))

