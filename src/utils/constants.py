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
ADD_POSTID_ENDPOINT = 'post_bp.add_postId_wrapper'
POST_UPLOADED_MESSAGE = "Post has been uploaded sucessfully"


COMMENT_ENDPOINT = 'comment_bp.comment_wrapper'
REPLY_COMMENT_ENDPOINT = 'comment_bp.reply_comment_wrapper'
COMMENT_REQUIRED = "comment field should not be empty"
PARENT_COMMENTID_MISSING_ERROR = 'parent_commentId field should not be empty'
COMMENT_POSTED_MESSAGE = "comment has been posted successfully"
COMMENTID_MISSING_ERROR = 'commentId field should not be empty'