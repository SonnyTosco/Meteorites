from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/dashboard'] = 'Users#dashboard'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/main'] = 'Users#main'
routes['POST']['/login_user'] = 'Users#login_user'
routes['POST']['/register_user'] = 'Users#register_user'

routes['GET']['/events/join'] = 'Events#join'
routes['GET']['/events/unjoin'] = 'Events#unjoin'
routes['GET']['/events/view'] = 'Events#view'

routes['POST']['/posts/add_post'] = 'Posts#add_post'
routes['POST']['/posts/delete_post'] = 'Posts#delete_post'
