from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/dashboard'] = 'Users#dashboard'
routes['GET']['/logout'] = 'Users#logout'
routes['POST']['/login_user'] = 'Users#login_user'
routes['POST']['/register_user'] = 'Users#register_user'

# Events
routes['GET']['/events/view'] = 'Events#view'
# routes['POST']['/events/<int:event_id>'] = 'Events#event'

# Messages
routes['POST']['/messages/delete/<int:user_id>/<int:message_id>'] = 'Messages#delete'
routes['POST']['/messages/post/<int:receiver_id>'] = 'Messages#post'

# Comments
routes['POST']['/comments/delete/<int:user_id>/<int:comment_id>'] = 'Comments#delete'
routes['POST']['/comments/post/<int:receiver_id>/<int:message_id>'] = 'Comments#post'