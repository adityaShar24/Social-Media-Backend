CONNECTED_TO_MONGODB = 'Connected to MongoDB'
CONNECTION_FAILED = 'Failed to connect to MongoDB'

HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400

USERNAME_MISSING_ERROR = 'username field should not be empty'
PASSWORD_MISSING_ERROR = 'password field should not be empty'
EXISITING_USERNAME_ERROR = 'username already exists, please enter a unique username'

USER_REGISTERED_MESSAGE = 'user {username} has been registered successfully!'
USER_NOT_EXISTS_ERROR = 'user {username} does not exists'

REGISTER_USER_ENDPOINT = 'auth_bp.register_user_wrapper'
LOGIN_USER_ENDPOINT = 'auth_bp.login_user_wrapper'

MAKE_REQUEST_ENDPOINT = 'request_bp.make_request_wrapper'
REMOVE_REQUEST_ENDPOINT = 'request_bp.remove_request_wrapper'

INVALID_PASSWORD_ERROR = 'Invalid password , please provide the correct one.'
USER_ID_MISSING_ERROR = 'userId field should not be empty'

POSTID_MISSING_ERROR = 'PostId cannot be empty'

REQUEST_SENT_MESSAGE = 'request sent successfully!'
REQUEST_DELETED_MESSAGE = "request deleted successfully"
REQUEST_ID_MISSING_ERROR = "No request with from current Id"
REQUEST_ACCEPTED_MESSAGE = "request has been accepted!"
REJECT_REQUEST_MESSAGE = "request has been rejected"

RESPONSE_REQUEST_ENDPOINT = 'request_bp.response_request_wrapper'

ADD_POST_ENDPOINT = 'post_bp.post_wrapper'
SAVE_POST_ENDPOINT = 'post_bp.save_post_wrapper'
POST_UPLOADED_MESSAGE = "Post has been uploaded sucessfully"
POST_SAVED_MESSAGE = "Post has been saved sucessfully"


COMMENT_ENDPOINT = 'comment_bp.comment_wrapper'
ADD_COMMENTID_ENDPOINT = 'comment_bp.add_commentId_wrapper'
COMMENT_REQUIRED = "comment field should not be empty"
PARENT_COMMENTID_MISSING_ERROR = 'parent_commentId field should not be empty'
COMMENT_POSTED_MESSAGE = "comment has been posted successfully"
COMMENTID_MISSING_ERROR = 'commentId field should not be empty'

ADDED_COMMENTID_MESSAGE = "commentId has been added successfully"

ROOM_ENDPOINT = 'rooms_bp.create_room_wrapper'
ROOM_NAME_REQUIRED = 'roomname field should not be empty'
ROOM_ID_MISSING_ERROR = 'roomId field should not be empty'
ROOM_CREATED_MESSAGE = 'room has been created successfully'
ROOM_MEMBER_ADDED_MESSAGE = 'member has been added successfully'
ROOM_FETCHED_MESSAGE = 'rooms has been fetched successfully'
ROOM_EXISTS_ERROR = 'room already exists, please enter a unique roomname'
ADD_MEMBER_ENDPOINT = 'rooms_bp.add_member_wrapper'

MESSAGE_ENDPOINT = 'message_bp.send_message_wrapper'
MESSAGE_TEXT_REQUIRED = 'message text field should not be empty'
MESSAGE_SENT = 'message has been sent successfully'  
MESSAGE_DELETED = 'message has been deleted successfully'