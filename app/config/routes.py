from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/dashboard'] = 'Users#dashboard'
routes['GET']['/logout'] = 'Users#logout'
routes['POST']['/login_user'] = 'Users#login_user'
routes['POST']['/register_user'] = 'Users#register_user'

routes['GET']['/events/join'] = 'Events#join'
routes['GET']['/events/leave'] = 'Events#leave'

routes['POST']['/posts/add_post'] = 'Posts#add_post'
routes['POST']['/posts/delete_post'] = 'Posts#delete_post'
